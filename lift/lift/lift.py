class Lift():


    def __init__(self):
        self.current_floor = 0
        self.current_direction = None
        self.queue = []

    def departing_to_floor(self, floor):
        self.current_direction = "up" if self.current_floor < floor else "down"
        return "ok", self.current_floor

    def arriving_at_floor(self, floor):
        self.current_floor = floor
        self.current_direction = None
        self.queue = [f for f in self.queue if f != floor]
        return "ok", self.current_floor

    def call_lift(self, source_floor, direction):
        self.queue.append(source_floor)
        return "ok", self.current_floor

    def send_lift(self, destination_floor):
        self.queue.append(destination_floor)
        return "ok", self.current_floor



if __name__ == '__main__':
    print(call_lift(3, "down"))
