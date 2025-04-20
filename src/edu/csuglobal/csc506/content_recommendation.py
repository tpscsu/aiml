class ContentRecommendationSystem:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]  # Chaining via lists

    def _hash(self, user_id):
        return hash(user_id) % self.size

    def add_user_preferences(self, user_id, preferences):
        index = self._hash(user_id)
        # Replace existing if user_id already exists
        for pair in self.table[index]:
            if pair[0] == user_id:
                pair[1] = preferences
                return
        self.table[index].append([user_id, preferences])

    def get_recommendations(self, user_id):
        index = self._hash(user_id)
        for pair in self.table[index]:
            if pair[0] == user_id:
                return pair[1]
        return []

    def display_all(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Index {i}: {bucket}")

if __name__ == "__main__":
    system = ContentRecommendationSystem()

    system.add_user_preferences("user123", ["Tech", "Gaming", "Science"])
    system.add_user_preferences("user456", ["Cooking", "Travel", "Fitness"])
    system.add_user_preferences("user789", ["Music", "Podcasts"])

    print("Recommendations for user456:", system.get_recommendations("user456"))
    print("Recommendations for user999 (non-existent):", system.get_recommendations("user999"))

    print("\nHash Table Content Snapshot:")
    system.display_all()