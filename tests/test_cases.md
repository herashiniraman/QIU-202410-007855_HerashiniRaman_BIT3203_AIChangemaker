# Testing Results

## Test Case 1: Normal Scheduling Scenario

### Test Description
This test checks whether the system can successfully assign food pickups to suitable volunteers when the volunteer availability and vehicle capacity meet the pickup requirements.

### Test Input
- Ice Cream Cafe requires 15kg pickup at 5PM.
- Fung Chui Restaurant requires 25kg pickup at 5PM.
- Charlotte Bakery requires 8kg pickup at 6PM.

### Test Output
Ice Cream Cafe → Aisha  
Fung Chui Restaurant → Amirul  
Charlotte Bakery → Lee Jung  

### Result
The system successfully generated a valid pickup schedule.


---

## Test Case 2: Vehicle Capacity Limitation

### Test Description
This test evaluates whether the system can identify situations where volunteers are unable to collect food due to insufficient vehicle capacity.

### Test Input
- Food pickup weight is higher than the available vehicle capacity of all volunteers.

### Test Output
No valid schedule found.

### Result
The system correctly prevented invalid assignments when vehicle capacity constraints were not satisfied.


---

## Test Case 3: Volunteer Availability Conflict

### Test Description
This test checks whether the system considers volunteer availability before assigning pickup tasks.

### Test Input
- The pickup time does not match any volunteer available time.

### Test Output
No valid schedule found.

### Result
The system successfully identified that no suitable volunteer was available for the pickup request.

