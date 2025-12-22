---
id: 05520c72-cc0c-4e64-b8f2-d8f6660910ea
type: tool
verified: true
created_at: '2019-08-28T21:17:29.828669Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - brute-force
  - web
  - fuzzing
  - discovery
url: 'https://sourceforge.net/projects/webslayer/'
validated: true
---

# webslayer

**Status**: Unverified

## Overview

Webslayer is a Java-based tool for brute forcing web applications, primarily used in penetration testing to discover hidden resources, brute force authentication forms, fuzz parameters for injections, and perform session-based attacks. It excels in automated discovery of unlinked directories, servlets, scripts, and files, making it ideal for reconnaissance and vulnerability identification in web environments.

## Description

Webslayer supports a variety of attack vectors including predictable resource location with recursion, login form brute forcing, session brute forcing, parameter brute forcing, and parameter fuzzing for issues like XSS or SQL injection. It also handles basic and NTLM authentication brute forcing. Key strengths include support for 15 encodings, proxy integration (with authentication), multithreading, live filters for cleaner results, and an integrated WebKit browser for manual verification. The tool includes a payload generator and results analyzer for efficient testing workflows.

## Features

- **Recursion and Extensions**: Supports recursive directory traversal and common file extensions for comprehensive discovery.
- **Encodings**: 15 encoding types to bypass filters and WAFs.
- **Authentication**: Brute forces Basic and NTLM auth, plus form-based logins.
- **Multiple Payloads**: Allows dual payloads for different attack vectors.
- **Proxy Support**: Integrates with proxies, including authenticated ones, and balances load across multiples.
- **Filters and Performance**: Live filters, multithreading, and time delays for optimized scanning.
- **Session Management**: Saves sessions for resuming attacks.
- **Non-Standard Detection**: Identifies resources based on unusual response codes.
- **Predefined Dictionaries**: Built-in wordlists for common web servers.

## Installation

### Requirements

- Java Runtime Environment (JRE) 1.6 or higher
- Access to download the JAR file

### Install Commands

```bash
# Download the latest WebSlayer JAR from SourceForge
wget https://sourceforge.net/projects/webslayer/files/webslayer.jar/download -O WebSlayer.jar

# On Kali Linux (may require manual download as not in repos)
# Or build from source if available: git clone [repo] && make

# For Ubuntu/Debian
sudo apt update
# Note: Not in standard repos; download JAR as above

# Windows/macOS: Download JAR and run with java -jar
```

Run with `java -jar WebSlayer.jar` to launch the GUI.

## Basic Usage

```bash
java -jar WebSlayer.jar
```

This opens the graphical interface where you select modes (e.g., PRL for discovery) and configure targets, wordlists, and options.

### Common Options

| Option | Description |
|--------|-------------|
| -u, --url | Specify target URL |
| -m, --mode | Attack mode (PRL, LFBF, PF, etc.) |
| -d, --dict | Path to dictionary/wordlist |
| -t, --threads | Number of threads for multithreading |
| -p, --proxy | Proxy server (e.g., 127.0.0.1:8080) |

## Examples

### Example 1: Basic Usage

Launch GUI and configure for directory discovery on a target.

```bash
java -jar WebSlayer.jar -u http://example.com -m PRL -d /path/to/wordlist.txt
```

### Example 2: Advanced Usage

Brute force a login form with proxy support.

```bash
java -jar WebSlayer.jar -u http://example.com/login -m LFBF -uf users.txt -pf passes.txt -p 127.0.0.1:8080
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Brute Force]] Brute Force
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual HTTP request patterns from a single source (high volume to common paths).
- Java process (java.exe or javaw.exe) with network activity to web targets.
- Proxy logs showing forwarded brute force traffic.
- Error logs from web servers indicating repeated 401/403 responses.
- Monitor for downloads of WebSlayer.jar or related artifacts.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/dirb]]
- [[tools/Gobuster]]
- [[tools/ffuf]]

## References

- Official SourceForge page: https://sourceforge.net/projects/webslayer/
- Related resources: OWASP Testing Guide for brute force techniques
