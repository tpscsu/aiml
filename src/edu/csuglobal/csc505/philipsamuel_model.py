class PhilipSamuel:
    def __init__(self):
        self.stages = []
        self.improvements = {}

    def input_stages(self):
        print("Enter the stages of your modified Waterfall Model (type 'done' to finish):")
        while True:
            stage = input("Stage: ")
            if stage.lower() == 'done':
                break
            self.stages.append(stage)

    def input_improvements(self):
        print("\nEnter the improvements for each stage:")
        for stage in self.stages:
            improvement = input(f"Improvement for {stage}: ")
            self.improvements[stage] = improvement

    def display_model(self):
        print("\nPhilipSamuel Model:")
        for stage in self.stages:
            print(f"{stage}: {self.improvements.get(stage, 'No improvements specified')}")


if __name__ == "__main__":
    model = PhilipSamuel()
    model.input_stages()
    model.input_improvements()
    model.display_model()
