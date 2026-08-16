# Development Log

## 24 July 2026 — Project Concept and Planning

- Selected the problem area of food rescue management because restaurants and cafes often have surplus food while organisations may require food support.
- Identified the main challenge as matching food pickup requests with suitable volunteers while considering different constraints.
- Defined the target users as restaurants, food rescue organisations, and volunteers.
- Selected Constraint Satisfaction Problem (CSP) as the AI approach because the problem involves multiple requirements that must be satisfied before making assignments.
- Defined the initial constraints:
  - Volunteer availability time
  - Vehicle carrying capacity
  - Food pickup requirements


## 30 July 2026 — Problem Formulation and Prototype Design

- Designed the system structure using Python classes:
  - Volunteer class to store volunteer information.
  - FoodPickup class to store restaurant pickup information.
  - CSPSolver class to handle assignment decisions.
- Implemented the initial CSP solver using constraint checking.
- Developed the assignment logic to verify:
  - Whether volunteer capacity is sufficient.
  - Whether volunteer availability matches pickup time.
- Tested the initial prototype and identified issues related to unsuccessful assignments.


## 4 August 2026 — Algorithm Improvement

- Improved the scheduling approach by implementing CSP Backtracking Search.
- Added Minimum Remaining Values (MRV) heuristic to improve the search process.
- Updated the solver to explore possible assignments instead of assigning volunteers sequentially only.
- Improved the reliability of finding valid schedules when multiple constraints exist.


## 6 August 2026 — Testing and Evaluation

- Conducted testing using different scheduling scenarios.
- Created three test cases:
  1. Normal scheduling scenario where all constraints are satisfied.
  2. Vehicle capacity constraint where food weight exceeds volunteer capacity.
  3. Volunteer availability conflict where no volunteer is available at the required time.
- Recorded testing outputs and screenshots in the `results/` folder.
- Verified that the system can generate valid schedules and reject invalid assignments.


## Final Reflection

- The project successfully demonstrates how AI-based constraint solving can support food rescue coordination.
- The current prototype focuses on assignment scheduling and does not include real-time location tracking or route optimisation.
- Future improvements could include integrating maps, travel distance calculation, and real-time volunteer availability.

