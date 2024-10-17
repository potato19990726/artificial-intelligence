# Artificial Intelligence Course Code Demonstration

This repository contains example code used in the Artificial Intelligence course.

## Contents

This repository mainly includes the following:

1. Fuzzy Logic Control System (hw3.py)

   - An autonomous driving speed control system implemented using the skfuzzy library
   - Considers multiple input variables such as traffic congestion, road conditions, visibility, etc.
   - Derives recommended speed through fuzzy rule inference

2. Fuzzy Set Visualization (fuzz_plot.py)

   - Demonstrates various commonly used fuzzy membership functions
   - Includes Gaussian functions, S-shaped functions, triangular functions, and more

3. Expert System (hw2.py)

   - Implements a basic expert system with rules and facts
   - Uses logical operators to evaluate conditions and derive actions

4. Environment Setup (.gitignore, requirements.txt)
   - Provides necessary files to set up the development environment
   - Includes a .gitignore file to exclude unnecessary files from version control
   - Lists required dependencies in requirements.txt for easy installation

## Usage

1. Clone this repository:
   `git clone <repository_url>`
2. Install the required dependencies:
   `pip install -r requirements.txt`
3. Run the respective Python scripts, such as:
   `python hw3.py`
   `python fuzz_plot.py`
   `python hw2.py`

## Contribution

We welcome questions or suggestions for improvements. If you have any questions, please open an issue for discussion.

## Additional Information

### Fuzzy Logic Control System

The fuzzy logic control system in `hw3.py` is designed to simulate an autonomous driving scenario. It takes into account various factors that affect driving speed and uses fuzzy logic to determine the optimal speed. The system is highly adaptable and can be extended to include more input variables or different fuzzy rules.

### Fuzzy Set Visualization

The `fuzz_plot.py` script provides visualizations of different fuzzy membership functions. These visualizations help in understanding how fuzzy sets work and how they can be applied in real-world scenarios. The script includes a variety of membership functions, each with its unique characteristics and applications.

### Expert System

The expert system in `hw2.py` demonstrates the use of rules and facts to derive actions based on logical conditions. It includes basic logical operators such as AND, OR, and NOT, and allows for the creation of complex conditions and actions.

### Getting Started

To get started with the code, make sure you have Python installed on your system. Clone the repository and install the dependencies as mentioned above. You can then run the scripts to see the fuzzy logic control system in action, visualize the fuzzy sets, and explore the expert system.

### Contact

For any further information or queries, feel free to contact the repository maintainers. We are here to help you understand and implement fuzzy logic systems and expert systems in your projects.
