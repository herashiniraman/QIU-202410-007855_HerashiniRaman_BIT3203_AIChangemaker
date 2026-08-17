class CSPSolver:

    def __init__(self, volunteers, pickups):

        self.volunteers = volunteers
        self.pickups = pickups
        self.solution = {}


    def check_constraints(self, volunteer, pickup):

        # Vehicle capacity constraint
        if volunteer.vehicle_capacity < pickup.food_weight:
            return False


        # Volunteer availability constraint
        if volunteer.available_time != pickup.pickup_time:
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


        # Sort by least available volunteers first
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


    