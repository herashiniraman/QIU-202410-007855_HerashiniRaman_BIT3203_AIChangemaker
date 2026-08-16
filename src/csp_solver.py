class CSPSolver:

    def __init__(self, volunteers, pickups):

        self.volunteers = volunteers
        self.pickups = pickups
        self.solution = {}


    def check_constraints(self, volunteer, pickup):

        # Vehicle capacity constraint
        if volunteer.vehicle_capacity < pickup.food_weight:
            return False


        # Availability constraint
        if volunteer.available_time != pickup.pickup_time:
            return False


        # One volunteer cannot handle multiple pickups
        if volunteer.name in self.solution.values():
            return False


        return True



    # MRV Heuristic
    # Select pickup with the fewest possible volunteers first

    def select_mrv_order(self):

        pickup_options = []


        for pickup in self.pickups:

            possible_volunteers = []


            for volunteer in self.volunteers:

                if self.check_constraints(volunteer, pickup):

                    possible_volunteers.append(volunteer)


            pickup_options.append(
                (pickup, len(possible_volunteers))
            )


        pickup_options.sort(
            key=lambda x: x[1]
        )


        return [
            item[0]
            for item in pickup_options
        ]



    def solve(self):

        self.pickups = self.select_mrv_order()

        return self.backtrack(0)



    def backtrack(self, index):

        # Goal: all pickups assigned

        if index == len(self.pickups):

            return True


        pickup = self.pickups[index]


        for volunteer in self.volunteers:


            if self.check_constraints(volunteer, pickup):


                # Assign

                self.solution[pickup.restaurant] = volunteer.name



                # Continue searching

                if self.backtrack(index + 1):

                    return True



                # Undo assignment (backtracking)

                del self.solution[pickup.restaurant]



        return False

    