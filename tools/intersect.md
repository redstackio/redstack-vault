---
id: b232fdfa-89dc-420c-8a94-2c6acdea88aa
name: intersect
type: tool
verified: true
created_at: '2019-08-28T21:17:29.297766+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
  - Windows
tags:
  - post-exploitation
  - red-team
  - script-generation
  - payload-creation
url: 'https://github.com/byt3bl33d3r/Intersect'
commands:
  - '[[commands/intersect-create-custom-script]]'
  - '[[commands/intersect-execute-generated-script]]'
validated: true
---

# intersect

**Status**: Unverified

## Overview

Intersect is a post-exploitation framework designed for red team operations, allowing users to create highly customized scripts by selecting modular features such as keyloggers, screen captures, persistence mechanisms, and more. Version 2.5 emphasizes user control, enabling the import of custom modules and generation of tailored scripts via a menu-driven interface. It is commonly used in advanced persistent threat simulations to build flexible payloads for Windows environments.

## Description

Intersect 2.5 represents a significant evolution from prior versions, shifting focus to modular architecture. Users interact with the Create.py application, a guided menu system that lets them choose from pre-built modules or import their own. This results in a bespoke Python script that can be executed to generate payloads in various formats (e.g., .exe, .py, .dll). The tool supports features like credential harvesting, system enumeration, and C2 communication, making it ideal for post-compromise scenarios in red team engagements. It requires Python 2.7 or 3.x and is primarily targeted at Windows for payload execution, though the framework runs on Linux for generation.

## Features

- **Modular Selection**: Choose from core modules including keylogging (T1056), screen capture (T1113), boot persistence (T1547), and mic recording.
- **Custom Module Import**: Easily add user-defined features to extend functionality.
- **Payload Generation**: Output payloads in multiple formats with obfuscation options.
- **C2 Integration**: Built-in support for TCP-based command and control.
- **Cross-Platform Generation**: Scripts generated on Linux/macOS for Windows targets.

## Installation

### Requirements

- Python 2.7 or 3.x
- Git
- pip for dependencies (e.g., pynput, pillow for certain modules)

### Install Commands

```bash
# Clone the repository
sudo apt update && sudo apt install git python3 python3-pip -y  # On Ubuntu/Kali
git clone https://github.com/byt3bl33d3r/Intersect.git
cd Intersect

# Install dependencies
pip3 install -r requirements.txt

# For Kali Linux (pre-requisites often met)
# No additional steps needed beyond clone if Python is set up
```

On Windows, use git bash or PowerShell for cloning, and ensure Python is in PATH.

## Basic Usage

```bash
python Create.py
```

This starts the interactive menu for script creation. After generation, execute the script with connection details.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help for intersect.py |
| --obfuscate | Apply basic obfuscation to generated payloads |
| -f, --file | Specify the custom script file to execute |

## Examples

### Example 1: Basic Usage

Create a simple script with keylogger and persistence:

```bash
python Create.py
# Select: Keylogger, Persistence
# Generate: basic_intersect.py

# Execute to generate payload
python intersect.py basic_intersect.py -i 10.0.0.1 -p 8080 --payload-type exe
```

### Example 2: Advanced Usage

Build a full-featured script and generate an obfuscated DLL:

```bash
python Create.py
# Select all modules + import custom module
# Generate: advanced_intersect.py

python intersect.py advanced_intersect.py -i 10.0.0.1 -p 8080 --payload-type dll --obfuscate
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Input Capture]] Input Capture (keylogging modules)
- [[Screen Capture]] Screen Capture
- [[Boot or Logon Autostart Execution]] Boot or Logon Autostart Execution (persistence)
- [[Remote Services]] Remote Services (C2 communication)

### Tactics

- [[Persistence]] Persistence
- [[Command and Control]] Command and Control
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of Intersect-generated executables with unusual imports (e.g., pynput, socket for C2).
- Network traffic to non-standard ports from generated payloads.
- File creation patterns: Custom .py scripts in temp directories or unusual .exe with embedded Python.
- Process monitoring for python.exe spawning child processes with keylogging behavior.
- EDR signatures for known Intersect modules like screen grabs or mic access.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Empire]] (Alternative C2 framework)
- [[tools/Covenant]] (.NET-based post-exploitation)

## References

- Official GitHub: https://github.com/byt3bl33d3r/Intersect
- Documentation: README.md in the repository
- Blog Post: Original release notes on medium.com or author's site
