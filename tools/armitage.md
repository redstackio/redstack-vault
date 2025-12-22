---
id: bb0fb10b-06b6-4995-b131-9d12ec504ed1
type: tool
verified: true
description: >-
  Armitage is a scriptable red team collaboration tool for Metasploit that
  visualizes targets, recommends exploits, and exposes advanced
  post-exploitation features in the framework.
url: 'http://armitage.fastandfurioushacker.com/'
created_at: '2019-08-28T21:17:38.323986+00:00'
updated_at: '2024-01-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
tags:
  - red-team
  - collaboration
  - metasploit
  - gui
  - exploitation
validated: true
---

# armitage

**Status**: Verified

## Overview

Armitage is a graphical cyber attack management tool designed for the Metasploit Framework. It provides a user-friendly interface for red team operations, allowing teams to visualize networks, select exploits, manage sessions, and collaborate in real-time. Commonly used for penetration testing, it simplifies complex Metasploit workflows.

## Description

Armitage enhances Metasploit by offering a visual representation of targets and attacks. Through a single Metasploit instance, teams can share sessions, hosts, captured data, and downloaded files while communicating via a shared event log. It supports running bots for automation and is particularly useful for coordinated red team exercises. Armitage acts as a force multiplier by streamlining exploit selection, payload management, and post-exploitation tasks.

## Features

- **Target Visualization**: Graphical display of scanned networks, hosts, and services.
- **Exploit Recommendations**: Suggests relevant exploits based on target information.
- **Session Management**: Handles multiple shells and meterspreter sessions collaboratively.
- **Team Collaboration**: Shared event logs and data syncing across team members.
- **Scripting Support**: Integrates with Metasploit's Ruby-based scripting for automation.
- **Post-Exploitation Tools**: Exposes advanced features like keylogging, pivoting, and credential harvesting.

## Installation

### Requirements

- Java Runtime Environment (JRE) 7 or higher.
- Metasploit Framework installed.
- Network access for team server (if using collaboration features).

### Install Commands

On Kali Linux (pre-installed with Metasploit):

```bash
# Update Metasploit to ensure latest Armitage
msfupdate

# Armitage is located in /opt/metasploit-framework
cd /opt/metasploit-framework
```

On Ubuntu:

```bash
# Install Metasploit (includes Armitage)
sudo apt update
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall
```

On Windows:

Download and install the Metasploit installer from Rapid7, which includes Armitage. Launch via the Start menu or run `armitage.bat` from the installation directory.

## Basic Usage

```bash
armitage
```

This opens the GUI. For secure mode (if certificates are set up):

```bash
armitage -https
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Display help and usage information |
| `-https` | Use HTTPS for team server connections |
| `-c <config>` | Load a specific configuration file |

## Examples

### Example 1: Basic Usage

```bash
armitage
```

Launches the standalone Armitage instance connected to a local Metasploit console.

### Example 2: Advanced Usage

First, start the team server on a host:

```bash
cd /opt/metasploit-framework
./msfvenom --list payloads  # Optional: Verify payloads
./teamserver 192.168.1.100 team123
```

Then connect clients:

```bash
armitage -server 192.168.1.100 -user hacker -pass team123
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter (via Metasploit payloads)
- [[Remote Services]] Remote Services (pivoting and session management)
- [[Third-party Software]] Software Deployment Tools (exploit delivery)

### Tactics

- [[Execution]] Execution
- [[Lateral Movement]] Lateral Movement
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- **Process Monitoring**: Look for `java.exe` or `armitage` processes with high CPU/network activity.
- **Network Traffic**: Unusual outbound connections to team servers on ports like 55553 (default).
- **File Artifacts**: Presence of Armitage logs in Metasploit directories (`~/.msf4/logs/`).
- **Registry/Logs**: Windows event logs showing Java launches or Metasploit module executions.
- **Behavioral**: Correlated Metasploit sessions with graphical tool signatures in IDS/EDR.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/metasploit-framework]]
- [[tools/cobalt-strike]]

## References

- Official Armitage Documentation: http://armitage.fastandfurioushacker.com/
- Metasploit Integration Guide: https://docs.metasploit.com/docs/using-metasploit/basics/using-armitage-with-metasploit.html
- GitHub Repository (Legacy): https://github.com/rsmudge/armitage-wiki
