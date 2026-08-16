# Problem Formulation

## AI Problem Type
The RescueSlot system is formulated as a Constraint Satisfaction Problem (CSP).

A CSP consists of variables, domains and constraints. The objective is to find a valid assignment of volunteers to food rescue pickups while satisfying all given constraints.


# Variables
The variables represent food pickup tasks that require volunteer assignment.

Example:
- Pickup_A
- Pickup_B
- Pickup_C

Each pickup task must be assigned to one suitable volunteer.

# Domains
The domain represents the possible values that each variable can take.

Example:

Pickup_A:

{Volunteer_1, Volunteer_2, Volunteer_3}


Pickup_B:

{Volunteer_1, Volunteer_2}

The AI agent searches through possible volunteer assignments to find a valid schedule.

# Constraints
The generated schedule must satisfy the following constraints:

## 1. Volunteer Availability Constraint
A volunteer can only be assigned when they are available during the required pickup time.

Example:
Volunteer_1:
Available:
5 PM - 7 PM
Cannot be assigned to a pickup at 9 PM.


## 2. Vehicle Capacity Constraint
The assigned volunteer's vehicle capacity must be sufficient for the food quantity.


Example:
Food donation:
30 kg
Vehicle capacity:
20 kg
Assignment is not allowed.


## 3. Food Expiry Constraint
Food must be collected before the expiry deadline.
Example:
Food expiry:
6 PM
Pickup after 6 PM is invalid.


## 4. Scheduling Conflict Constraint
A volunteer cannot perform multiple pickups at the same time.

Example:
Volunteer_1:
5 PM:
Restaurant A
5 PM:
Restaurant B
This assignment is invalid.


# Initial State
The initial state contains:
- Available volunteers
- Food donation requests
- Pickup time requirements
- Vehicle capacities

# State Representation
A state represents the current assignment status of all food pickup tasks.

Example:

Initial state:

- All food pickups are unassigned.
- Volunteer availability and vehicle capacity information are available.

Intermediate state:

- Some pickup tasks have been assigned to volunteers.
- Remaining tasks are still waiting for assignment.

Final state:

- All pickup tasks are assigned successfully.
- All constraints are satisfied.

# Actions
The AI agent performs the following actions:
1. Select an unassigned food pickup task.
2. Select possible volunteers from the available domain.
3. Check all constraints.
4. Assign a volunteer if constraints are satisfied.
5. Backtrack and try another option if the assignment fails.


# Goal Test
The goal is achieved when:
- All food pickups have been assigned.
- All constraints are satisfied.
- No invalid assignments exist.

# Solution Approach
A baseline backtracking search algorithm will be implemented.

An improved approach using the Minimum Remaining Values (MRV) heuristic will be added to reduce unnecessary searching by selecting the most constrained pickup task first.

# Algorithm Comparison

## Baseline Approach

The baseline method uses standard backtracking search. The algorithm explores possible volunteer assignments and backtracks when a constraint violation occurs.


## Improved Approach

The improved method applies the Minimum Remaining Values (MRV) heuristic. Instead of selecting pickup tasks randomly, the algorithm chooses the task with the fewest available volunteer options first. This reduces unnecessary searching and improves efficiency.