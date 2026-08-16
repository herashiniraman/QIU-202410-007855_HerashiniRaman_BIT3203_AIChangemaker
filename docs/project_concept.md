# Project Concept

## Project Title
RescueSlot: Intelligent Food Rescue Pickup Scheduler

## Project Overview
Food waste remains a significant issue in many communities, where restaurants and cafes may have surplus food at the end of the day while charities and community organisations need food resources. However, organising food rescue activities can be challenging due to limited volunteer availability, transportation capacity and collection deadlines.

This project proposes an intelligent food rescue pickup scheduler that automatically assigns available volunteers to food donation pickups. The system will use a Constraint Satisfaction Problem (CSP) approach to generate suitable assignments while considering important real-world constraints.


## Problem Statement
Many restaurants and cafes have leftover food that could potentially be donated instead of discarded. However, food rescue organisations often face difficulties coordinating volunteers efficiently because each volunteer has different availability, vehicle capacity and pickup limitations.

Without an effective scheduling approach, some food donations may not be collected on time, resulting in unnecessary food waste. Therefore, an intelligent scheduling agent is needed to help assign volunteers to food pickups while satisfying multiple constraints.


## Target Users
### 1. Charity and Community Organisations
These organisations can use the system to manage food collection activities and assign suitable volunteers efficiently.

### 2. Volunteers
Volunteers can receive pickup tasks that match their available time and transportation capacity.

### 3. Restaurants and Cafes
Food donors can benefit from a more reliable collection process to ensure surplus food is collected before expiry.

## Proposed AI Method
The project will implement a Constraint Satisfaction Problem (CSP) approach.

The CSP agent will consider:
- Volunteer availability
- Vehicle capacity
- Food pickup deadlines
- Pickup schedule conflicts
- Food quantity requirements

The system will use backtracking search with a heuristic improvement to find valid volunteer assignments.

## Project Objectives
The objectives of this project are:
1. To develop an intelligent scheduling agent that assigns food rescue pickups to suitable volunteers.

2. To apply a Constraint Satisfaction Problem (CSP) approach to handle scheduling constraints such as availability, capacity and pickup deadlines.

3. To evaluate the effectiveness of the proposed approach using different test scenarios.
