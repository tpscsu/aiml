class PotholeTrackingSystem:
    def __init__(self):
        self.actors = {
            "Citizen": ["Report Pothole", "Submit Claim", "Check Status"],
            "Public Works Admin": ["Assign Work Orders", "Track Repairs"],
            "Repair Crew": ["Update Repair Status", "Log Materials Used"]
        }

    def display_actors(self):
        print("Actors and Their Use Cases:")
        for actor, use_cases in self.actors.items():
            print(f"- {actor}:")
            for use_case in use_cases:
                print(f"  - {use_case}")


if __name__ == "__main__":
    system = PotholeTrackingSystem()
    system.display_actors()
