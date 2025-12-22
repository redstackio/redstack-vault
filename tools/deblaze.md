---
id: 9a267596-2634-4447-afe9-0619dba43566
name: deblaze
type: tool
verified: true
created_at: '2019-08-28T21:17:22.477206+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - reconnaissance
  - flash-remoting
  - bruteforce
  - web-application
url: 'https://github.com/SpiderLabs/deblaze'
validated: true
---

# deblaze

**Status**: Unverified

## Overview

Deblaze is a Python-based tool designed for security testing of Adobe Flash Remoting endpoints. It enables penetration testers to enumerate and interrogate services and methods exposed via Flash Remoting, which is commonly used in legacy Flex and ActionScript applications for remote procedure calls. The tool is particularly useful for identifying misconfigurations or vulnerabilities in Flash-based web applications by brute-forcing names and fingerprinting the technology stack.

## Description

Flash Remoting allows Flash applications to invoke server-side functions directly, such as database queries or business logic operations. While this facilitates dynamic content loading, it expands the attack surface if not properly secured. Deblaze addresses this by providing capabilities to probe endpoints without relying on the Flash client, making it easier to discover hidden services and methods. It exploits the often case-insensitive naming in Flash Remoting implementations and can operate stealthily since POST requests may not be logged on poorly monitored systems. Developed during security assessments of Flash-heavy sites, deblaze helps uncover potential security holes like unauthorized method access or information disclosure.

## Features

- Brute Force Service and Method Names: Enumerate exposed services and methods using wordlists.
- Method Interrogation: Probe specific methods to understand parameters, responses, and behaviors.
- Flex Technology Fingerprinting: Identify versions and configurations of Flex/BlazeDS backends.
- Stealthy Operation: Uses HTTP POST requests that may evade basic logging.
- Multi-threaded Support: Accelerate brute-forcing with configurable threads.

## Installation

### Requirements

- Python 2.7 or 3.x
- Requests library: `pip install requests`
- Wordlists for brute-forcing (e.g., common service/method names)

### Install Commands

```bash
# Clone the repository (assuming it's available on GitHub or similar)
git clone https://github.com/SpiderLabs/deblaze.git
cd deblaze

# Install dependencies
pip install -r requirements.txt
```

For Kali Linux, it may be available via apt or manual download; otherwise, use the git clone method. On Windows, ensure Python is in PATH.

## Basic Usage

```bash
python deblaze.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -u, --url | Target Flash Remoting URL |
| -v, --verbose | Enable verbose output for debugging |
| -t, --threads | Number of threads for brute-forcing (default: 1) |

## Examples

### Example 1: Basic Usage (Fingerprinting)

```bash
python deblaze.py -u http://target.com/gateway -f
```

This fingerprints the Flex technology at the endpoint.

### Example 2: Advanced Usage (Brute-Force Services)

```bash
python deblaze.py -u http://target.com/gateway -b services -w services_wordlist.txt -t 10
```

This brute-forces service names using 10 threads.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning: Network Service Scanning (for endpoint probing)
- [[Gather Victim Host Information]] Gather Victim Host Information: Software (for fingerprinting Flex versions)

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual POST requests to /messagebroker/amf or similar Flash Remoting paths with rapid, patterned payloads.
- High volume of 404/Method not found responses from the application server.
- Network logs showing requests from security testing IPs or tools like Python Requests User-Agent.
- Enable AMF request logging on servers like BlazeDS or ColdFusion to monitor for brute-force patterns.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Burp Suite]] (for intercepting and modifying AMF requests)
- [[tools/sqlmap]] (if SQL injection is found in enumerated methods)

## References

- Original tool: https://github.com/SpiderLabs/deblaze
- Adobe Flash Remoting Documentation: https://helpx.adobe.com/flash-player/kb/flash-remoting.html
- OWASP Testing Guide for Flash Applications
