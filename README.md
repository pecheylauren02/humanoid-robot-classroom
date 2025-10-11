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

## 3. Object-Oriented Design and Data Structures

The program applies object-oriented design techniques and uses data structures effectively to manage operational data.

### Object-Oriented Features:
- **Encapsulation:** Each class maintains its own internal data and exposes methods for controlled access.
- **Inheritance:** Shared behaviours are structured in base classes, allowing specialized extensions in subclasses.
- **Polymorphism:** Common methods such as `execute()` are overridden by different task types to achieve unique actions.
- **Abstraction:** The main control logic is separated from task definitions, improving modularity and code reuse.

### Data Structures:
- **Lists (Queues):** Used to manage pending tasks efficiently.  
- **Dictionaries:** Store and manage attributes of delivery tasks (sender, receiver, and item).  
- **Strings and UUIDs:** Used to generate unique task identifiers for logging and tracking.  

---

## 4. Implementation and Execution

### Running the Code
1. Clone the repository:
   git clone https://github.com/pecheylauren02/humanoid-robot-classroom

2. Open the folder in your Python IDE (e.g., Visual Studio Code or PyCharm).

3. Run the program: 
    python main.py

4. Enter a sample command such as:
    deliver book from teacher to student

The robot will interpret this command, enqueue the delivery task, and execute it sequentially, providing console feedback at each stage.