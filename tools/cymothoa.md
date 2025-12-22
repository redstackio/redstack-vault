---
id: 83185736-42de-4d1f-8467-108da5cbead6
type: tool
verified: true
created_at: '2019-08-28T21:17:39.851762+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - backdoor
  - process-injection
  - post-exploitation
url: 'https://github.com/cymothoa/cymothoa'
validated: true
---

# cymothoa

**Status**: Unverified

## Overview

Cymothoa is a stealthy backdooring tool designed for Unix-like systems. It injects shellcode into existing processes using the ptrace system call, allowing attackers to establish persistent access without creating new processes or leaving obvious artifacts.

## Description

Cymothoa manipulates running processes to inject modular shellcode, such as bind shells, reverse shells, or file read/write capabilities. It leverages ptrace to attach to a target process, overwrite its memory with backdoor code, and detach seamlessly. This makes it ideal for post-exploitation scenarios where process creation is monitored. The tool supports various modules for different backdoor types and is lightweight, compiling to a small binary.

## Features

- Feature 1: Process injection via ptrace without forking new processes
- Feature 2: Multiple shellcode modules (bind/reverse shells, file I/O, application spawners)
- Feature 3: Interactive shell support for direct command execution
- Feature 4: No shell dependency for some modules (e.g., direct execve)
- Feature 5: UDP-based shells for evading some firewalls

## Installation

### Requirements

- Linux system with ptrace support (most distributions)
- GCC compiler
- Git

### Install Commands

```bash
# Clone the repository
git clone https://github.com/cymothoa/cymothoa.git
cd cymothoa

# Compile
make

# Install to /usr/local/bin (optional)
sudo make install
```

On Kali Linux, it may be available via apt:

```bash
sudo apt update && sudo apt install cymothoa
```

## Basic Usage

```bash
cymothoa --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -p PID | Target process ID |
| -m NUMBER | Module to inject (0-12) |
| -s IP:PORT | Reverse shell callback |
| -b PORT | Bind shell port |
| -i | Interactive mode |
| -w | Spawn wget backdoor |

## Examples

### Example 1: Basic Usage

List modules:

```bash
[[commands/cymothoa-list-modules]]
```

### Example 2: Advanced Usage

Inject reverse shell:

```bash
[[commands/cymothoa-inject-reverse-shell]]
```

Inject bind shell:

```bash
[[commands/cymothoa-inject-bind-shell]]
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Dynamic-link Library Injection]] Dynamic-link Library Injection (process hollowing via shellcode)
- [[Windows Service]] Create or Modify System Process (process injection)
- [[Web Protocols]] Application Layer Protocol: Web Protocols (for wget module)

### Tactics

- [[Privilege Escalation]] Privilege Escalation
- [[Command and Control]] Command and Control
- [[Persistence]] Persistence

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor ptrace system calls (e.g., via auditd or sysdig) for unexpected process attachments
- Detection method 2: Anomalous network connections from legitimate processes (e.g., httpd connecting outbound)
- Detection method 3: Memory forensics showing injected shellcode in process address space
- Detection method 4: Strace or ltrace on suspicious processes to detect ptrace manipulation
- Detection method 5: Host-based IDS rules for cymothoa binary signatures or compilation artifacts

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[metasploit]] (for similar payload injection)
- [[procinject]] (alternative process injector)

## References

- Official GitHub: https://github.com/cymothoa/cymothoa
- Blog post on usage: https://null-byte.wonderhowto.com/how-to/use-cymothoa-inject-shells-into-ram-stealth-backdoors-0160000
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1055/
