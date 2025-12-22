---
id: a227b838-ec26-4f0e-9dc6-971c91cbc6cf
name: msfrpc
type: tool
verified: true
created_at: '2019-08-28T21:17:17.793121+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - exploitation
  - rpc
  - api
  - metasploit
url: 'https://docs.rapid7.com/metasploit/msfrpc-api/'
validated: true
---

# msfrpc

**Status**: Unverified

## Overview

msfrpc is the Remote Procedure Call (RPC) interface for the Metasploit Framework, allowing programmatic control of Metasploit modules, sessions, and exploits over an HTTP-based API. It is commonly used for automating penetration testing tasks, integrating Metasploit with other tools, or building custom scripts for exploit execution and post-exploitation. The RPC server is loaded within msfconsole, and clients can interact via JSON-RPC calls.

## Description

The msfrpc API provides methods for authentication, module management, payload generation, exploit execution, and session handling. It enables remote control of Metasploit without needing to interact directly with the console, making it ideal for scripting complex attack chains or integrating with CI/CD pipelines for security testing. The API uses JSON over HTTP, with methods like `auth.login`, `module.execute`, and `session.list`. Security features include token-based authentication and SSL support for encrypted communications.

## Features

- Feature 1: Full access to Metasploit modules (exploits, auxiliaries, payloads) via RPC calls
- Feature 2: Session management for maintaining and interacting with compromised hosts
- Feature 3: Console interaction proxy for running commands remotely
- Feature 4: Job control for managing background tasks like port scans or brute-force attacks
- Feature 5: Support for custom plugins and extensions through the API

## Installation

### Requirements

- Metasploit Framework installed (version 5.x or later recommended)
- Ruby 2.7+ (bundled with Metasploit)
- Network access to the RPC port (default 55553)

### Install Commands

msfrpc is included with the Metasploit Framework. Install Metasploit on Kali Linux (pre-installed) or other platforms:

```bash
# On Ubuntu/Debian
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall

# On Windows/macOS, download from https://www.metasploit.com/download
```

After installation, verify with `msfconsole -v`.

## Basic Usage

```bash
msfconsole --help
```
Load the RPC server within msfconsole:

```bash
msfconsole -q -x "load msgrpc msgrpc_passwd=yourpassword msgrpc_host=0.0.0.0"
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help for msfconsole |
| `-q` | Quiet mode (suppress banner) |
| `-x` | Execute command non-interactively |
| `msgrpc_passwd` | Set RPC password |
| `msgrpc_host` | Bind RPC to specific host (default 127.0.0.1) |
| `msgrpc_port` | RPC port (default 55553) |

## Examples

### Example 1: Basic Usage

Start msfconsole and load the RPC module:

```bash
msfconsole -q -x "load msgrpc msgrpc_passwd=secret"
```
This starts the RPC server listening on localhost:55553.

### Example 2: Advanced Usage

Authenticate via curl (client interaction):

```bash
curl -H "Content-Type: application/json" -d '{"method":"auth.login","params":["msf","secret"],"id":1,"jsonrpc":"2.0"}' http://127.0.0.1:55553/api/2.0
```
This returns a token for further API calls.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[PowerShell]] Command and Scripting Interpreter: PowerShell (for Windows scripting via RPC)
- [[DLL Side-Loading]] Scheduled Task/Job: Job (for managing background jobs)
- [[Execution through API]] Native API (for interacting with system APIs through Metasploit modules)

### Tactics

- [[Execution]] Execution
- [[Lateral Movement]] Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for msfconsole processes or RPC traffic on port 55553 (e.g., via netstat or firewall logs)
- Detection method 2: Look for loaded modules like 'msgrpc' in Metasploit logs or process arguments
- Detection method 3: JSON-RPC HTTP requests with Metasploit-specific methods (e.g., 'auth.login') in web proxy logs
- Detection method 4: Unusual outbound connections from msfconsole to attacker-controlled RPC endpoints

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
- [[tools/armitage]]
- [[Cobalt-Strike]]

## References

- Official documentation: https://docs.rapid7.com/metasploit/msfrpc-api/
- GitHub repository: https://github.com/rapid7/metasploit-framework
- Related resources: Metasploit Unleashed (Offensive Security guide)
