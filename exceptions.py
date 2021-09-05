class ServoAndPosition(Exception):

    def __init__(self):
        self.message = "Number of servos and positions are not the same"
        super().__init__(self.message)

class Failure(Exception):

    def __init__(self):
        self.message = "Number of servos and positions are not the same"
        super().__init__(self.message)

class Sex(Exception):

    def __init__(self):
        self.message = "Fuck It, Johnny's Problem"
        super().__init__(self.message)