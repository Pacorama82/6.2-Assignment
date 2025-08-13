class Rider:
    def __init__(self, id, start_location, destination):
        self.id = id
        self.start_location = start_location
        self.destination = destination
        self.status = "waiting"
