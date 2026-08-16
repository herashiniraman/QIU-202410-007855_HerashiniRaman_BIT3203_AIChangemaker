class Volunteer:
    def __init__(self, name, available_time, vehicle_capacity):
        self.name = name
        self.available_time = available_time
        self.vehicle_capacity = vehicle_capacity


class FoodPickup:
    def __init__(self, restaurant, food_weight, pickup_time, expiry_time):
        self.restaurant = restaurant
        self.food_weight = food_weight
        self.pickup_time = pickup_time
        self.expiry_time = expiry_time

        