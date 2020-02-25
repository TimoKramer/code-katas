class Lift():

    def __init__(self, current_floor):
        self.current_floor = current_floor

    def get_current_floor(self):
        return self.current_floor

    def deliver_to_floor(self, floor):
        return "ok"

    def call_lift(self, source_floor, direction):
        return "ok"



if __name__ == '__main__':
    print(call_lift(3, "down"))
