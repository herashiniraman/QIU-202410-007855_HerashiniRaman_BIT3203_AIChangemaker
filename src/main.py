from models import Volunteer, FoodPickup
from csp_solver import CSPSolver


def main():

    volunteers = [

        Volunteer(
            "Aisha",
            "5PM",
            20
        ),

        Volunteer(
            "Amirul",
            "5PM",
            30
        ),

        Volunteer(
            "Lee Jung",
            "6PM",
            15
        )

    ]


    pickups = [

        FoodPickup(
            "Ice Cream Cafe",
            15,
            "5PM",
            "7PM"
        ),

        FoodPickup(
            "Fung Chui Restaurant",
            25,
            "5PM",
            "6PM"
        ),

        FoodPickup(
            "Charlotte Bakery",
            8,
            "6PM",
            "8PM"
        )

    ]


    solver = CSPSolver(volunteers, pickups)

    success = solver.solve()


    print("Food Rescue Pickup Schedule")
    print("--------------------------")


    if success:

        for restaurant, volunteer in solver.solution.items():

            print(
                restaurant,
                "→",
                volunteer
            )

        print("\nScheduling completed successfully.")
        print("Algorithm used: CSP Backtracking with MRV Heuristic")


    else:

        print("No valid schedule found")



if __name__ == "__main__":
    main()

    