# System Checker - First Release

> **Status: Work in Progress**  
> Core functionality stable. GUI enhancements and feature expansion ongoing.

This project is a **cross-platform system utility** built in Python. It provides detailed information about the host environment, housing a responsive Graphical User Interface (GUI) built with **wxPython**. It intelligently separates presentation from logic using a declarative design approach.

## Features

- **Cross-Platform Interface**: Uses **wxPython** to ensure a native look and feel on Windows, Linux, and macOS. 
- **Declarative Design**: The UI layout is defined in an external `.fbp` file, decoupling design from code.
- **Logic Abstraction**: Cleanly separates the GUI implementation (`GUI.py`) from the core application logic (`Main.py`).
- **Dynamic Data Grid**: Utilizes `wxGrid` to efficiently display and update rows of system information.
- **Deep System Analysis**: Leverages the **WMI** library to fetch detailed process and hardware statistics.
- **Menu-Driven Filtering**: Includes a "Filter" menu to instantly switch between Hardware, Windows, and Software views.

## Setup and Installation

### 1. Prerequisites

- **Python 3.x**

### 2. Clone the Repository

```bash
git clone https://github.com/Tr4p-kun/System-checker.git
cd System-checker
```
### 3. Install Dependencies
Install the required Python packages (wxPython and WMI):

```
pip install wxPython WMI
```

### 4. Review Project Files
You should verify that the three core files are present in the root directory.

**Main.py**: The entry point.

**GUI.py**: The auto-generated interface file.

**System-checker-GUI.fbp**: The design project file.

## Usage
Running the utility is straightforward. Ensure you are in the root directory of the project.

### Step 1: Launch the Application
Execute the main script to start the GUI.

```
python Main.py
```

### Step 2: Navigate the Interface
The application will launch with a default view. Use the Filter menu in the top bar to toggle between different data sets.
