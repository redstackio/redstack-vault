---
id: 6eca01c2-8d08-451f-9a3a-52fbfbec529d
type: tool
verified: true
created_at: '2019-08-28T21:17:42.694506+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
tags:
  - ics
  - scada
  - smart-meter
  - protocol-testing
url: 'https://github.com/planb-net/termineter'
commands:
  - '[[commands/termineter-initialize-connection]]'
  - '[[commands/termineter-read-table]]'
  - '[[commands/termineter-execute-procedure]]'
validated: true
---

# termineter

**Status**: Unverified

## Overview

Termineter is a Python-based framework designed for security testing of smart meters. It facilitates communication using the ANSI C12.18 and C12.19 protocols, enabling penetration testers to interact with utility meters in controlled environments. Commonly used in ICS/SCADA assessments to identify vulnerabilities in meter firmware, authentication, and data access.

## Description

Termineter provides a platform for enumerating, reading, and manipulating data on smart meters that support C12.19 with 7-bit character sets. It connects via serial interfaces, typically using an ANSI type-2 optical probe, allowing testers to simulate attacker interactions such as unauthorized data extraction or configuration changes. The tool is particularly useful for red team exercises targeting energy sector infrastructure.

## Features

- Feature 1: Protocol implementation for C12.18 (optical) and C12.19 (serial) communications
- Feature 2: Table enumeration and reading capabilities for meter data structures
- Feature 3: Procedure execution for testing meter responses and manipulations
- Feature 4: Support for 7-bit character sets in C12.19 meters
- Feature 5: Interactive shell for real-time command issuance

## Installation

### Requirements

- Python 2.7 or 3.x
- PySerial library for serial communication
- Access to a compatible serial probe (e.g., ANSI type-2 optical probe)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/planb-net/termineter.git
cd termineter

# Install dependencies
pip install -r requirements.txt

# For Kali/Ubuntu
sudo apt update
sudo apt install python3-pip python3-serial
pip3 install pyserial
```

## Basic Usage

```bash
termineter --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and exit |
| -p PORT | Specify serial port (e.g., /dev/ttyUSB0) |
| -b BAUD | Set baud rate (default: 9600) |
| -v, --verbose | Enable verbose output for debugging |

## Examples

### Example 1: Basic Usage

Connect to a meter and enter interactive mode:

```bash
termineter -p /dev/ttyUSB0
```

### Example 2: Advanced Usage

Read a specific table non-interactively:

```bash
termineter -p /dev/ttyUSB0 -t 0 -r
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T0836]] Drive-by Compromise (for initial meter access simulation)
- [[T0807]] Manipulate Device Identification (meter enumeration)
- [[T0855]] Unauthorized Command Message (procedure execution)

### Tactics

- [[TA0107]] Inhibit Response Function
- [[TA0109]] Collect Data from Information Repositories

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor serial port activity on systems with optical probes attached
- Detection method 2: Log anomalous C12.19 protocol traffic in ICS networks
- Detection method 3: Presence of Termineter binaries or Python processes accessing /dev/tty devices
- Detection method 4: Unexpected meter table reads or procedure executions in audit logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/metasploit]] (for broader ICS exploitation)
- [[tools/scapy]] (for protocol crafting)

## References

- Official GitHub: https://github.com/planb-net/termineter
- ANSI C12.19 Standard Documentation
- ICS Security Testing Guidelines (NIST SP 800-82)
