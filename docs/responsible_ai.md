# Responsible AI
# Responsible AI 
## Overview

RescueSlot is an AI-based food rescue pickup scheduler that uses Constraint Satisfaction Problem (CSP) techniques to assign volunteers to food pickup tasks. The system is designed to support better organisation of food donation activities while considering important scheduling constraints.


## Fairness

The system assigns volunteers based on available information such as pickup time and vehicle capacity. It does not make decisions based on personal characteristics such as age, gender, ethnicity, or background.

However, fairness depends on the accuracy and completeness of the information provided by users.


## Transparency

The system uses CSP Backtracking Search with MRV heuristic. The assignment process is based on clear rules and constraints, making the decision process understandable.

Users can understand why a volunteer is assigned or rejected based on:
- Availability mismatch
- Insufficient vehicle capacity
- Pickup requirements


## Privacy

The prototype does not collect or store sensitive personal information.

Only basic volunteer information required for scheduling is used, such as:
- Volunteer name
- Available time
- Vehicle capacity


## Limitations

The current system has several limitations:

- It uses simulated data instead of real-time restaurant and volunteer information.
- It does not consider geographical distance or travel time.
- It does not include emergency changes such as volunteer cancellation.
- Testing was conducted using a limited number of pickup requests.


## Future Improvements

Future versions could include:

- Real-time volunteer availability updates.
- Route optimisation using location data.
- A larger dataset from actual food rescue organisations.
- Additional constraints such as volunteer preference and pickup priority.
Discuss fairness, privacy, safety, security, transparency, accessibility and sustainability where relevant, together with practical mitigation.


