# Problem Formulation


## AI Problem Type

The RescueSlot system is formulated as a Constraint Satisfaction Problem (CSP).

A CSP consists of three main components: variables, domains and constraints. The objective is to find a valid assignment of volunteers to food rescue pickup tasks while satisfying all given constraints.


# Formal CSP Representation

The RescueSlot scheduling problem can be formally represented as:

CSP = (X, D, C)

where:


## Variables (X)

The variables represent food pickup tasks that require volunteer assignment.

Example:

X = {Pickup_A, Pickup_B, Pickup_C}

Each variable represents one food rescue pickup request that must be assigned to a suitable volunteer.


## Domains (D)

The domain represents the possible volunteers that can be assigned to each pickup task.

Example:

D(Pickup_A) = {Aisha, Amirul, Lee Jung}

The possible domain values are reduced after checking constraints such as volunteer availability, vehicle capacity and food expiry.


## Constraints (C)

The constraints define the rules that must be satisfied before a volunteer can be assigned.

C = {C1, C2, C3, C4}


### C1: Volunteer Availability Constraint

The volunteer must be available during the required pickup time.

Example:

A volunteer available at 5 PM cannot be assigned to a pickup scheduled at 9 PM.


### C2: Vehicle Capacity Constraint

The volunteer's vehicle capacity must be greater than or equal to the food weight.

Example:

Food donation weight: 30 kg

Vehicle capacity: 20 kg

Assignment is not allowed.


### C3: Food Expiry Constraint

The pickup must be completed before the food expiry deadline.

Example:

Food expiry: 6 PM

Pickup after 6 PM is invalid.


### C4: Scheduling Conflict Constraint

A volunteer cannot handle multiple pickup tasks occurring at the same time.

Example:

Volunteer A:

5 PM - Restaurant A

5 PM - Restaurant B

This assignment is invalid.


The goal of the CSP solver is to find a valid assignment of volunteers to all pickup tasks while satisfying all constraints.


# Initial State

The initial state contains:

- Available volunteers
- Food donation requests
- Pickup time requirements
- Vehicle capacities


# State Representation

A state represents the current assignment status of all food pickup tasks.

Example:


Initial State:

- All food pickups are unassigned.
- Volunteer availability and vehicle capacity information are available.


Intermediate State:

- Some pickup tasks have been assigned to volunteers.
- Remaining tasks are waiting for assignment.


Final State:

- All pickup tasks are assigned successfully.
- All constraints are satisfied.


# Actions

The AI agent performs the following actions:

1. Select an unassigned food pickup task.

2. Select possible volunteers from the available domain.

3. Check all constraints.

4. Assign a volunteer if all constraints are satisfied.

5. Backtrack and try another assignment if a constraint violation occurs.


# Goal Test

The goal is achieved when:

- All food pickup tasks have been assigned.
- All constraints are satisfied.
- No invalid assignments exist.


# Solution Approach

A baseline backtracking search algorithm is implemented.

An improved approach using the Minimum Remaining Values (MRV) heuristic is applied to reduce unnecessary searching by selecting the most constrained pickup task first.


# Algorithm Comparison


## Baseline Approach: Backtracking Search

The baseline approach uses standard backtracking search.

The algorithm explores possible volunteer assignments sequentially and backtracks when a constraint violation occurs.

Advantages:

- Complete search method that can find a valid solution.
- Simple implementation.

Limitations:

- May explore unnecessary combinations.
- Searching efficiency decreases when the number of pickup tasks increases.


## Alternative Approach: Greedy Assignment

A greedy approach assigns the first suitable volunteer available for each pickup task without considering future assignments.

Advantages:

- Simple and fast implementation.
- Requires less computational effort.

Limitations:

- Does not reconsider previous decisions.
- May fail when future constraints cannot be satisfied.
- Can produce invalid or suboptimal schedules.


## Selected Approach: CSP Backtracking with MRV Heuristic

The RescueSlot system uses CSP backtracking combined with the Minimum Remaining Values (MRV) heuristic.

The MRV heuristic selects the pickup task with the fewest possible volunteer choices first. This allows the system to solve the most constrained tasks earlier and reduce unnecessary searching.

Advantages:

- Handles multiple constraints simultaneously.
- Can recover from incorrect assignments using backtracking.
- Produces a valid schedule that satisfies all constraints.


## Reason for Selecting CSP with MRV

Food rescue scheduling involves multiple interacting constraints such as volunteer availability, vehicle capacity, food expiry and scheduling conflicts.

Therefore, CSP with MRV is selected because it provides a more reliable and systematic solution compared with a simple greedy assignment approach.


