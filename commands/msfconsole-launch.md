---
type: command
executor: bash
data: msfconsole
output: null
created_at: '2023-04-06T03:56:00.963888+00:00'
updated_at: '2023-04-06T03:56:00.972471+00:00'
platforms:
  - Linux
tags:
  - exploitation
  - metasploit
verified: true
validated: true
---

# msfconsole-launch

## Command

```bash
msfconsole
```

## Description

Launches the Metasploit Framework console, providing an interactive shell for loading exploits, payloads, and auxiliaries.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters needed; runs the console directly | No |

## Examples

### Basic Usage

```bash
msfconsole
```

### Advanced Usage

```bash
msfconsole -q
```
(Suppresses banner for quieter startup)

## Expected Output

msf6 > (interactive prompt ready for commands)

## Related

- [[commands/msfconsole-java-rmi-server-exploit]]
- [[procedures/Java-RMI-Server-RCE-using-Metasploit]]
