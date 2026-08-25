import sys
from pathlib import Path

# Allow the test file to import files from the src folder
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from models import Volunteer, FoodPickup
from csp_solver import CSPSolver


def test_normal_scheduling():
    """Test that valid pickups are assigned to suitable volunteers."""

    volunteers = [
        Volunteer("Aisha", "5PM", 20),
        Volunteer("Amirul", "5PM", 30),
        Volunteer("Lee Jung", "6PM", 15)
    ]

    pickups = [
        FoodPickup("Ice Cream Cafe", 15, "5PM", "7PM"),
        FoodPickup("Fung Chui Restaurant", 25, "5PM", "7PM"),
        FoodPickup("Charlotte Bakery", 8, "6PM", "8PM")
    ]

    solver = CSPSolver(volunteers, pickups)

    result = solver.solve()

    assert result is True

    assert solver.solution["Ice Cream Cafe"] == "Aisha"
    assert solver.solution["Fung Chui Restaurant"] == "Amirul"
    assert solver.solution["Charlotte Bakery"] == "Lee Jung"


def test_vehicle_capacity_limitation():
    """Test that no schedule is found when food is too heavy."""

    volunteers = [
        Volunteer("Aisha", "5PM", 20),
        Volunteer("Amirul", "5PM", 30)
    ]

    pickups = [
        FoodPickup("Heavy Food Restaurant", 40, "5PM", "7PM")
    ]

    solver = CSPSolver(volunteers, pickups)

    result = solver.solve()

    assert result is False
    assert solver.solution == {}


def test_volunteer_availability_conflict():
    """Test that no schedule is found when no volunteer is available."""

    volunteers = [
        Volunteer("Aisha", "5PM", 20),
        Volunteer("Amirul", "5PM", 30)
    ]

    pickups = [
        FoodPickup("Late Restaurant", 10, "7PM", "9PM")
    ]

    solver = CSPSolver(volunteers, pickups)

    result = solver.solve()

    assert result is False
    assert solver.solution == {}


    