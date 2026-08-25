# Responsible AI

## Overview

RescueSlot is an AI-based food rescue pickup scheduler that uses Constraint Satisfaction Problem (CSP) with Backtracking Search and Minimum Remaining Values (MRV) heuristic to assign volunteers to food pickup tasks.

Since the system supports decision-making in volunteer assignment, responsible AI considerations are important to ensure that generated schedules are fair, transparent, secure, reliable and beneficial for food rescue activities.

---

## Fairness

### Risk in RescueSlot

The volunteer assignment decision depends on operational information such as volunteer availability time, vehicle capacity and pickup requirements.

If the information provided to the system is incomplete or outdated, some volunteers may receive fewer assignment opportunities unintentionally.

For example, if a volunteer updates their availability for evening pickups but the system still contains outdated information, the volunteer may not be considered for suitable pickup tasks.

### Mitigation

To improve fairness in RescueSlot:

- Volunteer availability information should be updated regularly before generating a schedule.
- The system should only use relevant operational factors for assignment decisions, including:
  - volunteer availability
  - vehicle capacity
  - pickup requirements
- The system should not use unrelated personal characteristics such as age, gender, ethnicity or personal background when assigning volunteers.
- Assignment decisions should be reviewed by food rescue coordinators to ensure that the generated schedule is reasonable.


---

## Privacy

### Risk in RescueSlot

A real-world implementation of RescueSlot may require storing volunteer and restaurant information.

The current prototype only uses minimum scheduling information:

- Volunteer name
- Available pickup time
- Vehicle capacity
- Food pickup requirements

However, a deployed system may involve additional information such as volunteer profiles, restaurant donation records and pickup schedules.

### Mitigation

For volunteer information:

- Only authorised food rescue coordinators should be allowed to view or modify volunteer availability and vehicle information.
- Volunteers should only access their own assigned pickup tasks rather than all volunteer records.
- The system should avoid collecting unnecessary personal information such as home address, identification documents or private background information.

For restaurant and donation information:

- Restaurant donation details should only be accessible to authorised users.
- Information such as donation quantity, pickup timing and donor details should not be publicly displayed.
- Only information required for scheduling should be stored and processed.


---

## Transparency and Explainability

### Risk in RescueSlot

Users may question why a particular volunteer was assigned to a pickup task while another volunteer was rejected.

If the system only provides the final schedule without explanation, users may not understand or trust the AI decision.

### Mitigation

RescueSlot should provide clear explanations for assignment decisions.

Example:

Assigned volunteer:

**Amirul**

Reason:

- Available at the required pickup time (5 PM)
- Vehicle capacity (30 kg) is sufficient for food weight (25 kg)
- Pickup time is before food expiry


Rejected volunteer:

**Aisha**

Reason:

- Vehicle capacity (20 kg) is insufficient for food weight (25 kg)


This allows coordinators to understand that assignments are generated based on CSP constraints rather than random decisions.


---

## Safety and Reliability

### Risk in RescueSlot

The quality of the generated schedule depends on the accuracy of input information.

Incorrect information may affect the success of food rescue operations.

Examples:

- Incorrect vehicle capacity information may assign unsuitable volunteers.
- Incorrect food expiry information may result in delayed collection.
- Incorrect volunteer availability information may create failed pickup attempts.

### Mitigation

Before generating a schedule:

- Validate food weight and expiry information.
- Confirm volunteer availability before assignment.
- Ensure vehicle capacity information is accurate.
- Allow food rescue coordinators to review the generated schedule before confirming pickups.

The AI system should support human decision-making rather than completely replace human judgement.


---

## Security

### Risk in RescueSlot

Unauthorised changes to volunteer or pickup information may affect the generated schedule.

Examples:

- Changing volunteer availability may cause incorrect assignments.
- Changing food weight information may assign volunteers with unsuitable vehicle capacity.

### Mitigation

A deployed RescueSlot system should:

- Restrict editing access to authorised food rescue coordinators.
- Maintain records of changes made to volunteer and pickup information.
- Protect scheduling data from unauthorised modification.
- Apply user authentication before accessing volunteer and donation information.


---

## Accessibility

### Risk in RescueSlot

Different users, including restaurants, volunteers and coordinators, may have different levels of technical knowledge.

A complex system interface may make it difficult for users to understand pickup assignments.

### Mitigation

Future versions of RescueSlot should provide:

- Simple volunteer assignment views.
- Clear pickup instructions.
- Easy-to-understand assignment explanations.
- User-friendly notifications.

For example, volunteers should receive essential information such as:

- Pickup location
- Pickup time
- Food quantity

instead of complex CSP technical details.


---

## Sustainability

### Contribution of RescueSlot

RescueSlot supports sustainability by improving coordination between food donors and volunteers.

By generating suitable volunteer assignments, the system helps reduce missed pickups and improves the possibility that surplus food is collected before expiry.

### Mitigation and Future Improvement

Future improvements should focus on:

- Improving volunteer utilisation.
- Reducing failed pickup attempts.
- Adding route optimisation to reduce unnecessary travel distance.
- Integrating real-time availability updates to improve scheduling efficiency.


---

## Limitations

The current prototype has several limitations:

- It uses simulated volunteer and restaurant data instead of real-time operational data.
- It does not consider geographical distance or route optimisation.
- It does not include emergency situations such as volunteer cancellation.
- It is tested using a limited number of pickup requests and volunteers.

Future versions could integrate:

- Real-time volunteer availability.
- Location-based optimisation.
- Larger datasets from real food rescue organisations.
- Additional scheduling constraints such as volunteer preferences and pickup priority.


