---
type: tool
description: >-
  The team server component of Armitage, a graphical cyber attack management
  tool for Metasploit that enables red team collaboration.
url: 'https://www.metasploit.com/'
verified: true
created_at: '2019-08-28T21:17:31.836044+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
tags:
  - collaboration
  - red-team
  - metasploit
  - c2
validated: true
---

# armitage-teamserver

**Status**: Unverified

## Overview

Armitage teamserver is the backend server for Armitage, a scriptable red team collaboration tool built on Metasploit. It visualizes targets, recommends exploits, and exposes advanced post-exploitation features. The teamserver allows multiple team members to share sessions, hosts, captured data, downloaded files, and communicate through a shared event log. It also supports running bots for task automation, making it a force multiplier for red team operations.

## Description

Armitage integrates with Metasploit to provide a user-friendly interface for managing attacks. The teamserver component runs a Metasploit RPC instance that multiple Armitage clients can connect to, enabling real-time collaboration. Teams can jointly control compromised hosts, share intelligence, and coordinate actions without needing separate Metasploit instances. This is particularly useful in large-scale red team engagements where synchronization is key. Note that Armitage is now integrated into the Metasploit Framework, but the teamserver functionality remains for multi-user setups.

## Features

- **Shared Sessions**: Multiple users control the same Metasploit sessions simultaneously.
- **Data Sharing**: Automatically shares hosts, screenshots, files, and loot across the team.
- **Event Log Communication**: Built-in chat-like log for team coordination.
- **Automation Bots**: Scriptable bots for repetitive tasks like alerting on new sessions.
- **Visualization**: Graphical interface for exploit recommendations and attack planning.
- **Post-Exploitation Focus**: Easy access to Metasploit's advanced modules for persistence and lateral movement.

## Installation

### Requirements

- Java Runtime Environment (JRE) 8 or later.
- Metasploit Framework installed.
- Network access for client connections (default RPC port 55553).

### Install Commands

Armitage and teamserver are included in Kali Linux Metasploit package:

```bash
# On Kali Linux (pre-installed with Metasploit)
sudo apt update && sudo apt install metasploit-framework

# Download standalone Armitage if needed (older versions)
wget https://www.forkbomb.org/release/armitage-3.1.4.tgz

tar xzf armitage-3.1.4.tgz
cd armitage-3.1.4
```

For Windows: Download the JAR files from the official Metasploit resources and ensure Java is installed.

## Basic Usage

```bash
./teamserver --help
```

Start the teamserver to allow clients to connect:

Use [[commands/start-armitage-teamserver]] for detailed syntax.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage. |
| `<bind_address>` | IP to bind (e.g., 0.0.0.0). |
| `<password>` | Authentication password for clients. |

## Examples

### Example 1: Basic Usage

Start teamserver bound to a specific IP:

```bash
./teamserver 192.168.1.100 teamPass123
```

Clients connect via Armitage GUI using this IP and password.

### Example 2: Advanced Usage

Bind to all interfaces for internal network access:

```bash
./teamserver 0.0.0.0 teamPass123
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Standard Application Layer Protocol]] Application Layer Protocol (for C2 over Metasploit payloads)
- [[Remote Services]] Remote Services (team collaboration via RPC)
- [[Encrypted Channel]] Encrypted Channel (if using HTTPS beacons)

### Tactics

- [[Command and Control]] Command and Control
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- **Network Traffic**: Unusual RPC traffic on port 55553 or Metasploit-related beacons.
- **Process Monitoring**: Java processes running teamserver.jar or msfrpcd.
- **File Artifacts**: Presence of armitage.jar, teamserver scripts, or Metasploit logs with shared session activity.
- **Behavioral**: Multiple connections to a single Metasploit instance from team IPs.
- **Logging**: Enable Metasploit RPC logging to capture authentication attempts.

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
- [[tools/armitage-client]]

## References

- Official Metasploit Documentation: https://docs.metasploit.com/
- Armitage Project (archived): https://www.forkbomb.org/
- Related resources: Cobalt Strike documentation for similar concepts (commercial alternative).
