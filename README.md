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

## 5. Commentary on Development Process and Approach (600 words)

### 5.1 Project Objectives and Alignment with Design
The implementation of the Humanoid Classroom Robot System reflects both the UML diagrams developed in Unit 7 and the iterative development process I followed during coding and testing. The primary objective was to translate the class, sequence, activity, and state transition diagrams into a functional Python program that simulates a classroom robot capable of receiving, queuing, and executing delivery tasks while interacting with teachers and students. The implementation also considered feedback received on the original design, leading to minor adjustments in task handling and interaction features.

### 5.2 Modular Design and Class Responsibilities
From the outset, I prioritized a modular structure to ensure that each class had a clear, single responsibility. The `RobotController` manages robot states and orchestrates operations, while the `TaskManager` handles task creation, queuing, and dispatch. `DeliveryTask` defines the attributes of each delivery operation, including sender, recipient, and object. The `SensorModule` and `InteractionModule` simulate environmental awareness and classroom communication, respectively. This separation of concerns enabled easier debugging and more targeted testing, as errors could be traced to specific components rather than the system as a whole.

### 5.3 Application of Object-Oriented Principles
Object-oriented programming (OOP) principles guided the development process. Encapsulation ensured that each class maintained its own data and exposed controlled methods for access. Inheritance allowed shared behaviors to be structured in base classes and extended in subclasses for specialized functionality. Polymorphism was applied in task execution; for example, the `execute()` method is overridden by different task types to perform unique actions. Abstraction separated control logic from task definitions, improving modularity, code reuse, and maintainability. These principles ensured the code closely reflected the original design while remaining flexible for future enhancements.

### 5.4 Data Structures and Task Management
Efficient data management was central to the system’s functionality. Queues were implemented using Python lists to manage pending tasks sequentially, ensuring first-in-first-out execution. Dictionaries stored task attributes such as sender, recipient, and item type, allowing fast access during processing. Unique task identifiers were generated with UUIDs to support logging and tracking. These structures allowed the robot to handle multiple tasks without data conflicts or errors, simulating realistic classroom workflow.

### 5.5 Testing Strategy

Both Automated and Unit testing were carried out using Python’s built-in `unittest` framework, with fake classes used to simulate dependencies for deterministic and isolated testing. The tests cover:

- Task delivery (including success, failure, and forbidden items)  
- State transitions of the robot (IDLE, EXECUTING, COMPLETED, ERROR, RECOVERING)  
- Environment monitoring and anomaly detection  
- Student greeting and interaction logging  
- Status reporting and task queue management  

Automated tests and static code analysis were conducted to ensure both **functional correctness** and **code quality** of the Humanoid Classroom Robot System. Manual Testing was also conducted to ensure thorough analysis.

#### 5.5.1 Summary Table of Test and Analysis Results

| Feature / Tool                     | Description                                                      | Result |
|-----------------------------------|------------------------------------------------------------------|--------|
| Initial state verification         | Robot starts in IDLE state with empty logs and history           | ✅ Pass |
| Forbidden item delivery            | Robot rejects unsafe/too large items and logs rejection          | ✅ Pass |
| Normal delivery (success)          | Task executed successfully; correct state transitions            | ✅ Pass |
| Normal delivery (failure/recovery)| Task failure simulated; robot recovers to IDLE; logs updated     | ✅ Pass |
| Monitor environment                | Temperature readings and anomaly detection logged properly       | ✅ Pass |
| Greet student and log interaction  | Greeting messages generated; interaction logged; temp considered | ✅ Pass |
| Status report structure            | Status dictionary correctly includes state, history, queue, logs, temperature | ✅ Pass |
| **Pylint**                         | Checked coding standards, errors, and refactoring suggestions    | ✅ Pass |
| **Flake8**                         | Verified PEP-8 compliance and style issues                       | ✅ Pass |
| **Pycodestyle**                     | Confirmed consistent code formatting                              | ✅ Pass |
| **Pyflakes**                        | Static analysis for syntax and error detection                    | ✅ Pass |
| **Pydocstyle**                       | Verified proper docstring formatting                               | ✅ Pass |

#### 5.5.2 Test Result Screenshots

<details> <summary>Pylint Results</summary>

Screenshot: Console output of unit tests

</details>

<details> <summary>Unit Test Results</summary>

Screenshot: Console output of all unit tests

</details>

<details> <summary>Flake8 Results</summary>

Screenshot: Console output of flake8 before and after

</details>

<details> <summary>Pycodestyle Results</summary>

Screenshot: Console output of pycodestyle

</details>


### 5.6 Challenges and Lessons Learned
Several challenges emerged during development. Mapping abstract diagrams into concrete Python classes required careful planning to ensure interactions were accurately represented. Designing the interaction module to provide realistic dialogue without overcomplicating the logic also demanded thoughtful design choices. These challenges were valuable learning experiences, emphasizing modularity, planning, and iterative refinement. Overall, the project strengthened my understanding of OOP, Python programming, and effective software design.

### 5.7 Future Enhancements
Future improvements could include adding additional task types, incorporating more advanced sensor simulations, or developing a graphical interface for more intuitive user interaction. These enhancements would increase the system’s realism and functionality while continuing to adhere to OOP principles.

### 5.8 Conclusion
This project successfully demonstrates the integration of theoretical design with practical Python programming. It highlights modular software design, effective use of data structures, and systematic testing, while providing a working simulation of a humanoid classroom robot. The development process offered opportunities for reflection and learning, documented here to provide insight into the approach and challenges encountered during implementation.