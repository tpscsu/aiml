"""
Warehouse Inventory Reorder Predictor
Portfolio Project - Module 8
Author: Tigin Philip Samuel
"""

import pandas as pd
import numpy as np
from math import sqrt
from sklearn.linear_model import LinearRegression

# ===============================
# 1) Synthetic data generation
# ===============================
def generate_data(num_products=20, months=12, seed=42):
    rng = np.random.default_rng(seed)
    rows = []
    for pid in range(1, num_products + 1):
        product_id = f"P{pid:03d}"
        category = rng.choice(["Electronics", "Clothing", "Home", "Grocery"])
        lead_time = int(rng.integers(5, 21))  # days

        # Base demand profile with trend and seasonality
        base = int(rng.integers(20, 90))        # average level
        trend = rng.uniform(-2.0, 3.0)          # down to up trend
        amplitude = rng.uniform(5, 25)          # seasonality amplitude
        noise_sd = rng.uniform(3, 12)           # noise

        monthly = []
        for m in range(1, months + 1):
            seasonal = amplitude * np.sin(2 * np.pi * m / 12.0)
            val = base + trend * m + seasonal + rng.normal(0, noise_sd)
            monthly.append(max(0, int(round(val))))

        # Stock roughly around 1.2x average with noise so some will be under-stocked
        current_stock = int(max(10, rng.normal(loc=np.mean(monthly) * 1.2, scale=20)))

        rows.append([product_id, category, lead_time, current_stock] + monthly)

    cols = ["product_id", "category", "lead_time", "current_stock"] + [f"m{i}" for i in range(1, months + 1)]
    return pd.DataFrame(rows, columns=cols)

# ===============================
# 2) Forecasting (stable)
# ===============================
def forecast_demand(df):
    """
    Forecast next month's demand using simple linear regression over months 1..12.
    Works reliably with short series.
    """
    forecasts = {}
    X = np.arange(1, 13).reshape(-1, 1)
    for _, row in df.iterrows():
        y = row[[f"m{i}" for i in range(1, 13)]].values.astype(float)
        model = LinearRegression()
        model.fit(X, y)
        next_month = np.array([[13]])
        pred = model.predict(next_month)[0]
        forecasts[row["product_id"]] = max(0.0, float(pred))
    return forecasts

# ===============================
# 3) Classification
# ===============================
def classify_products(df):
    """
    Classify items by average monthly sales into Fast, Medium, Slow.
    """
    avg_sales = df[[f"m{i}" for i in range(1, 13)]].mean(axis=1)
    labels = []
    for val in avg_sales:
        if val >= 70:
            labels.append("Fast")
        elif val >= 30:
            labels.append("Medium")
        else:
            labels.append("Slow")
    df["class"] = labels
    return df

# ===============================
# 4) Inventory math and rules
# ===============================
def compute_inventory_metrics(row, forecast, z=1.28, review_days=7):
    """
    Compute standard inventory control quantities:
    - lead time demand (lt_demand) = forecast * (lead_time/30)
    - safety stock = z * std_monthly * sqrt(lead_time/30)
    - reorder point (ROP) = lt_demand + safety
    - target stock = ROP + forecast * (review_days/30)
    - order_qty = max(0, target_stock - current_stock)
    z=1.28 approximates 90% service level.
    """
    sales = row[[f"m{i}" for i in range(1, 13)]].values.astype(float)
    std = sales.std(ddof=1) if len(sales) > 1 else 0.0
    stock = float(row["current_stock"])
    lead = float(row["lead_time"])

    lt_factor = max(lead / 30.0, 0.1)
    rv_factor = max(review_days / 30.0, 0.1)

    lt_demand = forecast * lt_factor
    safety = z * std * sqrt(lt_factor)
    reorder_point = lt_demand + safety
    target_stock = reorder_point + forecast * rv_factor
    order_qty = max(0.0, target_stock - stock)

    return {
        "std": std,
        "lt_demand": lt_demand,
        "safety": safety,
        "reorder_point": reorder_point,
        "target_stock": target_stock,
        "order_qty": order_qty
    }

def apply_fol_rules(df, forecasts, z=1.28, review_days=7):
    """
    Explainable decisions using explicit rules:
    - If stock < lt_demand: "Reorder urgently"
    - Else if stock < ROP: "Reorder soon"
    - Else: "Stock sufficient"
    """
    outputs = []
    for _, row in df.iterrows():
        pid = row["product_id"]
        f = forecasts[pid]
        m = compute_inventory_metrics(row, f, z=z, review_days=review_days)
        stock = float(row["current_stock"])

        if stock < m["lt_demand"]:
            status = "Reorder urgently"
        elif stock < m["reorder_point"]:
            status = "Reorder soon"
        else:
            status = "Stock sufficient"

        outputs.append((pid, status))
    return outputs

# ===============================
# 5) Search: budget-aware greedy plan
# ===============================
def greedy_reorder(df, forecasts, budget=2500, unit_cost_by_class=None, z=1.28, review_days=7):
    """
    Choose items under a budget using a simple risk score:
    risk = max(0, ROP - stock) / unit_cost
    Then order up to target stock within the remaining budget.
    """
    if unit_cost_by_class is None:
        unit_cost_by_class = {"Fast": 15, "Medium": 10, "Slow": 6}

    candidates = []
    for _, row in df.iterrows():
        pid = row["product_id"]
        f = forecasts[pid]
        m = compute_inventory_metrics(row, f, z=z, review_days=review_days)
        stock = float(row["current_stock"])
        deficit_to_rop = max(0.0, m["reorder_point"] - stock)
        unit_cost = float(unit_cost_by_class.get(row["class"], 10.0))
        risk_score = deficit_to_rop / max(unit_cost, 1e-6)
        candidates.append((pid, row["class"], unit_cost, m, risk_score))

    # Highest risk first
    candidates.sort(key=lambda x: x[4], reverse=True)

    plan = []
    remaining = float(budget)
    for pid, cls, unit_cost, m, _ in candidates:
        if remaining <= 0:
            break
        qty_needed = int(round(max(0.0, m["target_stock"] - m["reorder_point"])))  # order up to target beyond ROP
        qty_alt = int(round(max(0.0, m["order_qty"])))  # or directly from computed order_qty
        qty = max(qty_needed, qty_alt)
        if qty <= 0:
            continue
        affordable_qty = min(qty, int(remaining // unit_cost))
        if affordable_qty > 0:
            cost = affordable_qty * unit_cost
            plan.append((pid, cls, affordable_qty, unit_cost, cost))
            remaining -= cost

    return plan


def print_metrics_preview(df, forecasts, n=5, z=1.28, review_days=7):
    print("\nMetrics preview:")
    for _, r in df.head(n).iterrows():
        pid = r["product_id"]
        m = compute_inventory_metrics(r, forecasts[pid], z=z, review_days=review_days)
        short = {k: round(v, 2) for k, v in m.items()}
        print(pid, short)

def main():
    # Generate data
    data = generate_data(num_products=20, months=12, seed=42)
    print("Sample Inventory Data:\n", data.head())

    # Forecast
    forecasted_demand = forecast_demand(data)
    print("\nForecasted Demand (next month, per product):")
    print({k: round(v, 2) for k, v in list(forecasted_demand.items())[:10]}, "...")

    # Classification
    classified_data = classify_products(data)
    print("\nClassified Products (first 10):")
    print(classified_data[["product_id", "class"]].head(10))

    # Preview metrics and plans
    print_metrics_preview(classified_data, forecasted_demand, n=5)
    reorder_suggestions = greedy_reorder(classified_data, forecasted_demand, budget=2500)
    print("\nReorder Suggestions (pid, class, qty, unit_cost, cost):")
    print(reorder_suggestions)

    logic_results = apply_fol_rules(classified_data, forecasted_demand)
    print("\nFirst-Order Logic Decisions (first 10):")
    print(logic_results[:10])

    # MENU
    while True:
        print("\n--- Warehouse Inventory Reorder Predictor ---")
        print("1. View Data (first 10)")
        print("2. View Forecasted Demand (all)")
        print("3. View Classification (all)")
        print("4. View Reorder Suggestions")
        print("5. View FOL Decisions (all)")
        print("6. Metrics Preview (first 10)")
        print("7. Exit")

        choice = input("\nEnter choice: ").strip()
        if choice == "1":
            print(classified_data.head(10))
        elif choice == "2":
            print({k: round(v, 2) for k, v in forecasted_demand.items()})
        elif choice == "3":
            print(classified_data[["product_id", "class"]])
        elif choice == "4":
            print(reorder_suggestions)
        elif choice == "5":
            print(logic_results)
        elif choice == "6":
            print_metrics_preview(classified_data, forecasted_demand, n=10)
        elif choice == "7":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
