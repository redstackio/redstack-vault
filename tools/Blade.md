---
id: c1ee019c-45b9-4a84-b7d5-f1c0992c3760
type: tool
verified: true
created_at: '2019-08-28T21:17:23.677931+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - webshell
  - post-exploitation
  - console-tool
url: ''
commands:
  - '[[commands/blade-connect-webshell]]'
  - '[[commands/blade-execute-command]]'
  - '[[commands/blade-upload-file]]'
  - '[[commands/blade-download-file]]'
validated: true
---

# Blade

**Status**: Unverified

## Overview

Blade is a console-based webshell connection tool designed for managing and interacting with deployed webshells during penetration testing and red team operations. It provides a command-line interface for tasks such as connecting to webshells, executing remote commands, and transferring files. Currently under development, it aims to serve as a lightweight alternative to tools like China Chopper, focusing on simplicity and stealth in post-exploitation scenarios.

## Description

Blade facilitates interaction with webshells by establishing encrypted or obfuscated connections to web servers where a webshell has been uploaded. It supports common webshell types (e.g., PHP, ASP) and allows operators to send commands, upload payloads, and exfiltrate data without relying on graphical interfaces. Key use cases include maintaining access after initial exploitation, lateral movement in web environments, and data collection from compromised servers. As an open-source project in active development, it emphasizes modularity for custom protocol support and evasion techniques.

## Features

- Feature 1: Console-based interaction for stealthy webshell management
- Feature 2: Support for multiple webshell protocols (HTTP/HTTPS, custom encodings)
- Feature 3: File transfer capabilities (upload/download) with progress indicators
- Feature 4: Command execution with output parsing and session persistence
- Feature 5: Basic evasion options like user-agent rotation and proxy support

## Installation

### Requirements

- Python 3.6+ (for core scripting)
- Requests library: `pip install requests`
- Optional: Cryptography library for encrypted sessions: `pip install cryptography`

### Install Commands

```bash
# Clone the repository (assuming GitHub hosting)
git clone https://github.com/example/blade.git
cd blade
pip install -r requirements.txt
```

For Kali Linux/Ubuntu:

```bash
sudo apt update
sudo apt install python3-pip git
# Then run the clone and pip install as above
```

For Windows (using Chocolatey):

```powershell
choco install python git
# Then clone and pip install
```

## Basic Usage

```bash
blade --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage |
| `-v, --verbose` | Enable verbose logging for debugging |
| `--proxy` | Specify proxy server for connections (e.g., http://127.0.0.1:8080) |
| `--ua` | Custom user-agent string for HTTP requests |

## Examples

### Example 1: Basic Usage

Connect to a webshell and list directory contents:

```bash
blade connect --url http://target.com/shell.php --pass mypass
blade execute "ls -la"
```

### Example 2: Advanced Usage

Upload a file via proxy with custom user-agent:

```bash
blade connect --url https://target.com/admin.aspx --pass secret --proxy http://127.0.0.1:8080 --ua "Mozilla/5.0"
blade upload localfile.txt /remote/path/file.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Web Shell]] Web Shell
- [[Web Protocols]] Web Protocols
- [[Remote File Copy]] Ingress Tool Transfer

### Tactics

- [[Persistence]] Persistence
- [[Command and Control]] Command and Control
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual HTTP POST requests to web directories with base64-encoded payloads
- Detection method 2: Console processes spawning Python scripts with network activity to internal web servers
- Detection method 3: File uploads to web roots with timestamps matching tool execution
- Detection method 4: Network logs showing repeated connections from the same IP to shell endpoints

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/China-Chopper]]
- [[tools/AntSword]]
- [[tools/Cobalt-Strike]]

## References

- Official repository (under development)
- Webshell management best practices in red teaming
