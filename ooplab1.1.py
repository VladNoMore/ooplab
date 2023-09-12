class GameObject:
    def __init__(self, name, is_moving, speed, color):
        self.name = name
        self.is_moving = is_moving
        self.speed = speed
        self.color = color

    def display_state(self):
        state = f"{self.name} is currently "
        if self.is_moving:
            state += f"moving at a speed of {self.speed} units per second and is colored {self.color}."
        else:
            state += f"standing still and is colored {self.color}."
        print(state)

    def move(self, new_speed):
        if new_speed > 0:
            self.is_moving = True
            self.speed = new_speed
        else:
            self.is_moving = False
            self.speed = 0

    def change_color(self, new_color):
        self.color = new_color

# Example usage:
if __name__ == "__main__":
    obj1 = GameObject("Object1", True, 10, "red")
    obj2 = GameObject("Object2", False, 0, "blue")

    obj1.display_state()  # Output: Object1 is currently moving at a speed of 10 units per second and is colored red.
    obj2.display_state()  # Output: Object2 is currently standing still and is colored blue.

    obj1.move(20)  # Object1 starts moving at a speed of 20 units per second.
    obj2.change_color("green")  # Object2 changes color to green.

    obj1.display_state()  # Output: Object1 is currently moving at a speed of 20 units per second and is colored red.
    obj2.display_state()  # Output: Object2 is currently standing still and is colored green.
