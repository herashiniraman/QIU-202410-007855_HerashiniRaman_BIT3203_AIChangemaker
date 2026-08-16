# Testing Results

The developed AI food rescue pickup scheduler was tested using different scenarios to evaluate whether the system can generate valid assignments and handle constraint violations.

---

## Test Case 1: Normal Scheduling Scenario

### Purpose
To verify that the system can assign food pickup tasks when volunteer availability and vehicle capacity satisfy the pickup requirements.

### Result

The system successfully generated a pickup schedule:

- Ice Cream Cafe → Aisha
- Fung Chui Restaurant → Amirul
- Charlotte Bakery → Lee Jung

### Outcome
Successful scheduling was achieved.

---

## Test Case 2: Vehicle Capacity Constraint

### Purpose
To test whether the system can detect situations where the food weight exceeds volunteer vehicle capacity.

### Result

The system displayed:
No valid schedule found


### Outcome
The system correctly prevented invalid assignments when vehicle capacity requirements were not satisfied.

---

## Test Case 3: Volunteer Availability Conflict

### Purpose
To evaluate whether the system checks volunteer availability before assigning pickup tasks.

### Result

The system displayed:
No valid schedule found


### Outcome
The system successfully identified that no suitable volunteer was available for the requested pickup time.

