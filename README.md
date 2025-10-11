# Humanoid Classroom Robot System

**Author:** Lauren Pechey  
**Module:** Object-Oriented Programming – University of Essex Online  

---

## 1. Introduction

This project implements the **Humanoid Classroom Robot System**, designed to support classroom operations such as object delivery, task scheduling, and interaction with teachers and students. The implementation is based on the UML diagrams (Class, Sequence, Activity, and State Transition) developed during the design stage in Unit 7. The system demonstrates the application of core object-oriented programming (OOP) principles including encapsulation, inheritance, and polymorphism. It has been implemented and tested using Python in accordance with the PEP-8 Style Guide to ensure clarity, structure, and maintainability.

---

## 2. System Overview

The system simulates a classroom robot capable of receiving and executing delivery tasks while maintaining interaction with its environment.  

### Key Classes:
- **RobotController:** Manages robot states (IDLE, EXECUTING, COMPLETED) and coordinates operations.  
- **TaskManager:** Handles task creation, queuing, and dispatch to the robot.  
- **DeliveryTask:** Defines a single delivery operation with attributes such as sender, recipient, and object details.  
- **SensorModule:** Simulates environmental awareness and obstacle detection.  
- **InteractionModule:** Facilitates communication between the robot and classroom users, ensuring simulated dialogue.  

These components are designed to reflect the modular structure and flow identified in the UML diagrams, ensuring a strong correspondence between design and implementation.

---
