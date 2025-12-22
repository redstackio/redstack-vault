---
id: d439f5e7-f206-4345-aad6-a1ad0ded7252
type: tool
verified: true
created_at: '2019-08-28T21:17:20.149663+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - oracle
  - tns
  - reconnaissance
  - database
url: 'https://www.kali.org/tools/tnscmd10g/'
validated: true
---

# tnscmd10g

**Status**: Unverified

## Overview

tnscmd10g is a command-line tool designed for interacting with Oracle TNS (Transparent Network Substrate) listeners, typically running on TCP port 1521. It allows security testers to send basic commands such as pings, version queries, and status requests to enumerate and assess Oracle database services during reconnaissance phases.

## Description

tnscmd10g enables simple communication with Oracle TNS listeners without requiring full Oracle client installation. It is particularly useful in penetration testing for discovering Oracle database infrastructure, verifying listener responsiveness, and gathering version information that can reveal potential vulnerabilities. The tool sends raw TNS packets to elicit responses from the listener, making it a lightweight alternative to more complex Oracle tools.

## Features

- Feature 1: Send ping commands to test TNS listener connectivity and response time.
- Feature 2: Query listener version to identify Oracle software versions and patch levels.
- Feature 3: Retrieve status information including active services, instances, and endpoints.

## Installation

### Requirements

- Perl (version 5 or higher)
- Network access to target TNS port (default 1521)

### Install Commands

```bash
# On Kali Linux (pre-installed)
# No action needed

# On Ubuntu/Debian
sudo apt update
sudo apt install tnscmd10g

# Manual installation from source (if available)
git clone https://github.com/kali-tools/tnscmd10g.git
cd tnscmd10g
make install
```

## Basic Usage

```bash
tnscmd10g --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --host | Specify the target hostname or IP |
| -p, --port | Specify the TNS port (default 1521) |
| -v, --version | Query listener version |
| -s, --status | Retrieve listener status |
| --ping | Send a ping to the listener |

## Examples

### Example 1: Basic Usage

```bash
tnscmd10g version -h 192.168.1.100
```

### Example 2: Advanced Usage

```bash
tnscmd10g status -h oracle.example.com -p 1521
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Network traffic monitoring for unusual TCP connections to port 1521 with TNS packet signatures.
- Detection method 2: Host-based logging of tnscmd10g process execution or Perl scripts accessing Oracle ports.
- Detection method 3: IDS/IPS rules for TNS protocol probes (e.g., version or status requests).

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]]
- [[Oracle SQL*Plus]]

## References

- Official Kali documentation: https://www.kali.org/tools/tnscmd10g/
- Oracle TNS Protocol: https://docs.oracle.com/en/database/oracle/oracle-database/19/netrf/tns-overview.html

## Related Commands

- [[commands/tnscmd10g-version-query]]
- [[commands/tnscmd10g-status-query]]
- [[commands/tnscmd10g-ping]]
