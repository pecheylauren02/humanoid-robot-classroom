# Humanoid Classroom Robot System

**Author:** Lauren Pechey  
**Module:** Object-Oriented Programming – University of Essex Online  

---

## 1. Project Overview & Introduction

The Humanoid Classroom Robot System is a Python-based implementation designed to simulate a humanoid robot operating in a classroom environment. Its core functionalities include:

- Delivering objects to specified locations

- Scheduling and managing tasks

- Interacting with teachers and students

Handling errors such as failed deliveries or sensor anomalies

This implementation is based on UML diagrams (Class, Sequence, Activity, and State Transition) prepared in Unit 7. Any modifications from the original design were made to improve system efficiency and incorporate feedback received during the design phase.

---

## 2. System Overview

The system simulates a classroom robot capable of receiving and executing delivery tasks while maintaining interaction with its environment.  

### Key Classes:

- **RobotController:** Manages robot states (IDLE, EXECUTING, COMPLETED) and coordinates operations.  
- **TaskManager:** Handles task creation, queuing, and dispatch to the robot.  
- **DeliveryTask:** Defines a single delivery operation with attributes such as sender, recipient, and object details.  
- **SensorModule:** Simulates environmental awareness and obstacle detection.  
- **InteractionModule:** Facilitates communication between the robot and classroom users, ensuring simulated dialogue.  

These components are designed to reflect the modular structure and flow identified in the UML diagrams, ensuring a strong correspondence between design and implementation (Bennett et al., 2021).

---

## 3. Object-Oriented Design and Data Structures

The program applies object-oriented design techniques and uses data structures effectively to manage operational data.

### Object-Oriented Features:

Software engineering highlights that applying core object-oriented principles improves maintainability, scalability, and reduces the risk of errors in complex systems.

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

This section describes how to set up, run, and interact with the Humanoid Classroom Robot System, including the steps for executing the main program and running automated tests to verify functionality.

### Running the Code:

1. Clone the repository:
    git clone https://github.com/pecheylauren02/humanoid-robot-classroom.git

2. Open the folder in your Python IDE (e.g., Visual Studio Code or PyCharm).
    cd humanoid-robot-classroom

3. Create virtual environment
    python -m venv .venv
    source .venv/bin/activate  # Mac/Linux
    .venv\Scripts\activate     # Windows

4. Install dependencies (if any)
    pip install -r requirements.txt

5. Run the program: 
    python3 -m src.cli

6. Enter a sample command such as:
    deliver book from teacher to student

The robot will interpret this command, enqueue the delivery task, and execute it sequentially, providing console feedback at each stage.

## 5. Commentary on Development Process and Approach (600 words)

### 5.1 Project Objectives and Alignment with Design

The implementation of the Humanoid Classroom Robot System reflects both the UML diagrams developed in Unit 7 and the iterative development process I followed during coding and testing. The primary objective was to translate the class, sequence, activity, and state transition diagrams into a functional Python program that simulates a classroom robot capable of receiving, queuing, and executing delivery tasks while interacting with teachers and students. The implementation also considered feedback received on the original design, leading to minor adjustments in task handling and interaction features (Lott & Phillips, 2021).

### 5.2 Modular Design and Class Responsibilities

From the outset, a modular architecture was deliberately adopted to ensure that each class adhered to a well-defined, single responsibility (Lott & Phillips, 2021). The RobotController is responsible for managing the robot’s operational states and coordinating overall system behaviour, whereas the TaskManager oversees task creation, queuing, and dispatch. The DeliveryTask class encapsulates the attributes of individual delivery operations, including sender, recipient, and item details. Additionally, the SensorModule and InteractionModule simulate environmental perception and classroom communication, respectively. This clear separation of concerns facilitated more efficient debugging and targeted testing, as faults could be systematically traced to discrete components rather than the system in its entirety (Mishra et al., 2021).

### 5.3 Application of Object-Oriented Principles

The development process was guided by foundational object-oriented programming (OOP) principles (Rumbaugh et al., 1999). Encapsulation ensured that each class maintained its own internal state while providing controlled access through well-defined methods (Singh et al., 2021). Inheritance facilitated the organization of shared behaviours within base classes, which could be extended by subclasses to provide specialized functionality (Singh et al., 2021). Polymorphism was employed in task execution, whereby methods such as execute() were overridden by different task types to perform distinct operations (Mishra et al., 2021). Abstraction was used to separate the system’s control logic from task definitions, thereby enhancing modularity, promoting code reuse, and supporting maintainability (Rumbaugh et al., 1999). Collectively, these principles ensured that the implementation remained faithful to the original design while preserving flexibility for future extension and adaptation.

### 5.4 Data Structures and Task Management

Efficient data management was integral to the system’s overall functionality. Queues were implemented using Python lists to manage pending tasks in a sequential, first-in-first-out manner, ensuring orderly execution. Dictionaries were employed to store task attributes, including sender, recipient, and item type, thereby enabling rapid access and processing. Unique task identifiers were generated using UUIDs to facilitate precise logging and tracking of operations. Collectively, these data structures enabled the robot to manage multiple concurrent tasks without conflicts or errors, effectively simulating the operational dynamics of a real-world classroom environment (Ackerman, 2023).

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

Several challenges were encountered during the development process. Translating abstract UML diagrams into concrete Python classes necessitated meticulous planning to ensure that inter-class interactions were accurately represented (Singh et al., 2021). The design of the interaction module, intended to simulate realistic classroom dialogue without introducing unnecessary complexity, required careful consideration of both functionality and maintainability. These challenges provided valuable learning opportunities, highlighting the importance of modularity, systematic planning, and iterative refinement (Mishra et al., 2021). Overall, the project substantially enhanced my understanding of object-oriented programming, Python development, and principles of effective software design.

### 5.7 Future Enhancements

Future improvements could include adding additional task types, incorporating more advanced sensor simulations, or developing a graphical interface for more intuitive user interaction. These enhancements would increase the system’s realism and functionality while continuing to adhere to OOP principles (Ackerman, 2023).

### 5.8 Conclusion

This project successfully demonstrates the integration of theoretical design with practical Python programming. It highlights modular software design, effective use of data structures, and systematic testing, while providing a working simulation of a humanoid classroom robot. The development process offered opportunities for reflection and learning, documented here to provide insight into the approach and challenges encountered during implementation.

### 6. References

- Bennett, S., McRobb, S., & Farmer, R. (2021) Object-Oriented Systems Analysis and
Design Using UML. London: McGraw-Hill Higher Education.
- Lott, S., & Phillips, D. (2021) Python Object-Oriented Programming: Build Robust and
Maintainable Object-Oriented Python Applications and Libraries. 4th ed. Birmingham,
UK: Packt Publishing.
- Mishra, D., Parish, K., Lugo, R., & Wang, H. (2021) A framework for using humanoid
robots in the school learning environment. Electronics 10(6): 1-12. DOI: https://
doi.org/10.3390/electronics10060756
- Rumbaugh, J., Jacobson, I., & Booch, G. (1999) The Unified Modeling Language
Reference Manual. 2nd ed. Addison-Wesley.
- Singh, N., Chouhan, S. S., & Verma, K. (2021). Object oriented programming: Concepts,
limitations and application trends. 2021 5th International Conference on Information
Systems and Computer Networks (ISCON), Mathura, India, 1-4. DOI: https://doi.org/
10.1109/ISCON52037.2021.9702463