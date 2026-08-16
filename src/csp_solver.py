from models import Volunteer, FoodPickup


class CSPSolver:

    def __init__(self, volunteers, pickups):
        self.volunteers = volunteers
        self.pickups = pickups
        self.solution = {}


    def check_constraints(self, volunteer, pickup):

        # Check vehicle capacity
        if volunteer.vehicle_capacity < pickup.food_weight:
            return False


        # Check availability
        if volunteer.available_time != pickup.pickup_time:
            return False


        # Check assignment conflict
        if volunteer.name in self.solution.values():
            return False


        return True


    def solve(self):

        return self.backtrack(0)


    def backtrack(self, pickup_index):

        # Goal test:
        # All pickups assigned
        if pickup_index == len(self.pickups):
            return True


        pickup = self.pickups[pickup_index]


        for volunteer in self.volunteers:

            if self.check_constraints(volunteer, pickup):

                # Assign volunteer
                self.solution[pickup.restaurant] = volunteer.name


                # Continue searching
                if self.backtrack(pickup_index + 1):
                    return True


                # Backtrack
                del self.solution[pickup.restaurant]


        return False
    