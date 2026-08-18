# RescueSlot: Intelligent Food Rescue Pickup Scheduler

This repository is for the individual assignment in **BCS2143/BIT3203 Artificial Intelligence**, Study Intake 202607.

## Student information

- Student name: Herashini Raman
- Student ID: QIU-202410-007855
- Programme: BIT
- Course code: BIT3203
- GitHub username: herashiniraman

## Project title

RescueSlot

## Problem summary

Food waste is a common problem where restaurants and cafes may have extra food at the end of the day, while some communities and organisations still need food support. However, arranging food pickups can be difficult because volunteers have different available times, vehicle limitations, and pickup schedules.

The target users of this project are restaurants, cafes, food rescue organisations, and volunteers who participate in food donation activities.

RescueSlot helps organise food pickup assignments by finding suitable volunteers based on different constraints.The project aims to reduce food wastage and make the food rescue process easier to manage.

## AI method

The main AI method used in this project is a Constraint Satisfaction Problem (CSP).

The system uses CSP with Backtracking Search and Minimum Remaining Values (MRV) heuristic to assign volunteers to food pickup tasks. The algorithm considers constraints such as volunteer availability, vehicle capacity, and pickup requirements to find a suitable schedule.

## PEAS

- Performance measure:
  Successfully create a valid food pickup schedule while satisfying all given constraints.

- Environment:
  A food rescue environment involving restaurants, food donations, volunteers, and vehicle resources.

- Actuators:
  Assign available volunteers to different food pickup tasks.

- Sensors:
  Information about volunteer availability, vehicle capacity, food weight, pickup time, and expiry time.

## Installation

```powershell
py -V:3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```


## Running the prototype

Run the following command from the project folder:

```bash
python3 src/main.py

The program uses CSP Backtracking Search with MRV heuristic to generate volunteer assignments while checking availability and vehicle capacity constraints.


## Testing

The system was tested using three different scenarios:

1. Successful scheduling when volunteer availability and vehicle capacity satisfy requirements.
2. Vehicle capacity constraint where no volunteer can handle the food weight.
3. Volunteer availability conflict where no suitable volunteer is available.

The testing results, test case descriptions, and evidence screenshots are recorded in the `results/` folder.

## Repository structure

- `src/` — Python source code
- `tests/` — test cases
- `results/` — outputs and testing evidence
- `docs/` — project documentation
- `presentation/` — presentation materials


## Known limitations

- The system currently uses simulated volunteer and food pickup data instead of real-time data from restaurants or organisations.
- The scheduling process does not include real-time location tracking or route optimisation for volunteers.
- The accuracy of the generated schedule depends on the correctness of volunteer availability and vehicle information provided.
- The current prototype is tested on a small number of pickup requests and volunteers, so larger-scale deployment may require further improvements.

## Submission

Final deadline: **6 August 2026, 5:00 pm**.

Submit the private repository URL, final commit SHA and repository ZIP through eQIU. The written report is submitted through Turnitin.
