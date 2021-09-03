class ServoAndPosition(Exception):

    def __init__(self):
        self.message = "Number of servos and positions are not the same"
        super().__init__(self.message)