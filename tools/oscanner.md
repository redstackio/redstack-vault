---
id: fbb75aff-bd61-4fc4-93a9-23b5cf5f23cf
type: tool
verified: true
created_at: '2019-08-28T21:17:27.046192+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - oracle
  - database
  - enumeration
  - credential-access
url: ''
commands:
  - '[[commands/oscanner-enumerate-sid]]'
  - '[[commands/oscanner-enumerate-version]]'
  - '[[commands/oscanner-brute-passwords]]'
validated: true
---

# oscanner

**Status**: Unverified

## Overview

Oscanner is a Java-based Oracle assessment framework designed for security testing of Oracle databases. It features a plugin-based architecture that enables enumeration of various database elements, such as SIDs, versions, accounts, privileges, and more. Commonly used in penetration testing for discovering weak configurations, default credentials, and sensitive information in Oracle environments.

## Description

Oscanner allows testers to perform remote assessments against Oracle database servers without requiring direct authentication in many cases. Its plugins target common enumeration tasks, making it valuable for initial reconnaissance and credential gathering phases. The tool outputs results in a graphical Java tree interface for easy navigation and analysis. It supports both common password testing and dictionary-based brute-forcing, along with enumeration of roles, privileges, hashes, audit info, policies, and database links.

## Features

- **SID Enumeration**: Discovers Oracle System Identifiers on target hosts.
- **Password Testing**: Checks for common and dictionary-based passwords.
- **Version Enumeration**: Identifies Oracle database version and patch levels.
- **Account Enumeration**: Lists roles, privileges, and associated accounts.
- **Hash Extraction**: Retrieves password hashes for offline cracking.
- **Policy and Link Enumeration**: Gathers database policies and inter-database links.
- **Graphical Output**: Results displayed in an interactive Java tree view.

## Installation

### Requirements

- Java Runtime Environment (JRE) 8 or higher.
- Access to the oscanner JAR file (download from official repository or source).

### Install Commands

```bash
# Download the JAR file (replace with actual source URL)
wget https://example.com/oscanner.jar

# Verify Java is installed
java -version
```

On Windows, use a browser to download the JAR and ensure Java is in PATH. No compilation required as it's pre-built.

## Basic Usage

```bash
java -jar oscanner.jar --help
```

This displays available options, plugins, and usage syntax.

### Common Options

| Option | Description |
|--------|-------------|
| `-server` | Target Oracle server in format IP:PORT (default port 1521) |
| `-plugins` | Comma-separated list of plugins to run (e.g., sid,version,passwords) |
| `-username` | Username for authenticated enumeration (optional) |
| `-password` | Password for authenticated sessions (optional) |
| `-wordlist` | Path to dictionary file for password testing |
| `-v` | Verbose output mode |

## Examples

### Example 1: Basic Usage

```bash
java -jar oscanner.jar -server 192.168.1.100:1521 -plugins sid,version
```

This enumerates SIDs and versions on the target Oracle server.

### Example 2: Advanced Usage

```bash
java -jar oscanner.jar -server 192.168.1.100:1521 -username scott -wordlist /usr/share/wordlists/rockyou.txt -plugins passwords,privileges
```

Performs password brute-forcing and privilege enumeration using provided credentials and wordlist.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Account Discovery]] Account Discovery
- [[System Information Discovery]] System Information Discovery
- [[Brute Force]] Brute Force

### Tactics

- [[Discovery]] Discovery
- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to Oracle ports (default 1521) with enumeration patterns (e.g., multiple TNS connection attempts).
- Java process spawning with oscanner.jar on assessment machines.
- Logs showing failed authentication attempts or SID probes in Oracle listener logs.
- Unusual queries for version, roles, or privileges from external IPs.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/sqlmap]]
- [[oraclescan]]

## References

- Official repository or source (if available)
- Oracle security documentation for listener protection
