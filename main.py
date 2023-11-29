class TrafficLight:
    def __init__(self):
        self.state = "red"

    def change_state(self):
        if self.state == "red":
            self.state = "green"
        elif self.state == "green":
            self.state = "yellow"
        elif self.state == "yellow":
            self.state = "red"

    def display_state(self):
        print(f"The traffic light is {self.state}")


# Instantiate the TrafficLight class
traffic_light = TrafficLight()

# Display initial state
traffic_light.display_state()

# Simulate state changes
for i in range(5):
    traffic_light.change_state()
    traffic_light.display_state()

