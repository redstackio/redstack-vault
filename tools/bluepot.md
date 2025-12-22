---
id: 55445aca-16d8-4ad6-9550-875c7843b43b
type: tool
verified: true
created_at: '2019-08-28T21:17:35.632918+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - bluetooth
  - honeypot
  - java
  - monitoring
url: 'https://github.com/example/bluepot'
validated: true
---

# bluepot

**Status**: Unverified

## Overview

Bluepot is a Java-based Bluetooth honeypot designed for Linux systems. It simulates vulnerable Bluetooth services to attract and interact with attackers performing common Bluetooth exploits like BlueBugging and BlueSnarfing. Primarily developed as a university project, it helps in studying and logging Bluetooth attack patterns.

## Description

Bluepot accepts incoming Bluetooth connections via hardware dongles, stores any malware or payloads sent to it, and responds to attack attempts to encourage further interaction. It includes a graphical user interface (GUI) for real-time monitoring, featuring dashboards, graphs, lists of events, and detailed log analysis. This tool is useful in red team exercises for testing Bluetooth attack tools or in defensive setups to gather intelligence on Bluetooth threats.

## Features

- Feature 1: Simulates vulnerable Bluetooth services to lure attackers
- Feature 2: Captures and stores malware payloads sent over Bluetooth
- Feature 3: Interacts with attacks like BlueBugging (unauthorized access) and BlueSnarfing (data theft)
- Feature 4: GUI-based monitoring with graphs, event lists, and log parsing
- Feature 5: Supports multiple Bluetooth dongles for extended coverage

## Installation

### Requirements

- Java 8 or higher
- Maven build tool
- Linux kernel with Bluetooth support (e.g., bluez package)
- Bluetooth hardware dongle

### Install Commands

Use [[commands/bluepot-clone-and-build]] to download and build:

```bash
git clone https://github.com/example/bluepot.git && cd bluepot && mvn clean install
```

For Kali Linux:

```bash
apt update && apt install default-jdk maven bluez
```

## Basic Usage

```bash
java -jar target/bluepot-1.0.jar --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-i, --interface` | Specify Bluetooth interface (e.g., hci0) |
| `-v, --verbose` | Enable verbose logging |
| `-g, --gui` | Launch GUI alongside server |

## Examples

### Example 1: Basic Usage

Start the honeypot on default interface:

```bash
java -jar target/bluepot-1.0.jar hci0
```

### Example 2: Advanced Usage

Run with GUI and verbose output:

```bash
java -jar target/bluepot-1.0.jar -i hci0 -v -g
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Archive Collected Data]] Archive Collected Data (for storing captured malware)
- [[Standard Application Layer Protocol]] Application Layer Protocol (Bluetooth protocol interactions)

### Tactics

- [[Collection]] Collection (gathering attack data)
- [[Resource Development]] Resource Development (tool for attack simulation)

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for Java processes binding to Bluetooth interfaces (e.g., ps aux | grep bluepot)
- Detection method 2: Unusual Bluetooth traffic logs in bluez or system journals
- Detection method 3: Presence of Bluepot JAR files or Maven build artifacts

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/BlueZ]]
- [[tools/Wireshark]]

## References

- Official GitHub repository: https://github.com/example/bluepot
- Bluetooth Security Documentation: https://www.bluetooth.com/security/
