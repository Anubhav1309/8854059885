from object import Object, Color
from enum import Enum

class Bin:
    def __init__(self, bin_id, capacity):
        self.bin_id = bin_id
        self.capacity = capacity
        self.objects = []

    def add_object(self, object):
        # Implement logic to add an object to this bin
        if self.capacity >= object.size:
            self.objects.append(object)

    def remove_object(self, object_id):
        # Implement logic to remove an object by ID
        for obj in self.objects:
            if obj.id == object.id:
                self.objects.remove(obj.id)
                break
