class Car:
    def __init__(self, id, location):
        self.id = id
        self.location = location
        self.status = "available"
        self.assigned_rider = None
