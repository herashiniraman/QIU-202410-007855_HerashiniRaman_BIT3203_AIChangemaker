from models import Volunteer, FoodPickup


def convert_time(time):
    """
    Convert time format such as 5PM into 24-hour integer format.
    Example:
    5PM -> 17
    8PM -> 20
    """

    hour = int(time[:-2])
    period = time[-2:]

    if period == "PM" and hour != 12:
        hour += 12

    elif period == "AM" and hour == 12:
        hour = 0

    return hour



class CSPSolver:

    def __init__(self, volunteers, pickups):

        self.volunteers = volunteers
        self.pickups = pickups
        self.solution = {}


    def check_constraints(self, volunteer, pickup):

        # Constraint 1:
        # Vehicle capacity must be sufficient
        if volunteer.vehicle_capacity < pickup.food_weight:
            return False


        # Constraint 2:
        # Volunteer must be available during pickup time
        if volunteer.available_time != pickup.pickup_time:
            return False


        # Constraint 3:
        # Pickup must happen before food expiry
        if convert_time(pickup.pickup_time) >= convert_time(pickup.expiry_time):
            return False


        return True



    # MRV heuristic
    def select_mrv_order(self):

        pickup_options = []

        for pickup in self.pickups:

            options = []

            for volunteer in self.volunteers:

                if self.check_constraints(volunteer, pickup):
                    options.append(volunteer)


            pickup_options.append(
                (pickup, options)
            )


        # Select the pickup with the fewest available volunteers first
        pickup_options.sort(
            key=lambda x: len(x[1])
        )


        return [
            item[0] for item in pickup_options
        ]



    # Backtracking search
    def backtrack(self, index):

        if index == len(self.pickups):
            return True


        pickup = self.pickups[index]


        for volunteer in self.volunteers:

            if volunteer.name not in self.solution.values():

                if self.check_constraints(volunteer, pickup):

                    self.solution[pickup.restaurant] = volunteer.name


                    if self.backtrack(index + 1):
                        return True


                    del self.solution[pickup.restaurant]


        return False



    def solve(self):

        self.pickups = self.select_mrv_order()

        success = self.backtrack(0)

        return success

    