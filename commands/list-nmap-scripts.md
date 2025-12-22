---
id: 9561c925-2875-4e3b-b2a6-350e07228dfd
name: list-nmap-scripts
type: command
executor: bash
data: ls /usr/share/nmap/scripts/
output: null
created_at: '2023-04-06T03:56:22.058774+00:00'
updated_at: '2023-04-10T20:25:05.094903+00:00'
platforms:
  - Linux
tags:
  - nmap
  - recon
verified: true
validated: true
---

# list-nmap-scripts

## Command

```bash
ls /usr/share/nmap/scripts/
```

## Description

This command lists all available Nmap Scripting Engine (NSE) scripts in the default installation directory, helping users identify scripts for discovery tasks like service enumeration or vulnerability scanning.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; lists contents of the scripts directory | No |

## Examples

### Basic Usage

```bash
ls /usr/share/nmap/scripts/
```

### Advanced Usage

```bash
ls /usr/share/nmap/scripts/ | grep http
```

> Filters for HTTP-related scripts.

## Expected Output

A directory listing of .nse files, e.g.:

http-enum.nse  smb-enum-users.nse  ...

## Related

- [[procedures/Network-Discovery-with-Nmap-Scripting-Engine]]
- [[tools/Nmap]]
