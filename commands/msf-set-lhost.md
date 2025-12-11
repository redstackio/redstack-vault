---
data: 'set lhost [your public ip]'
tags:
  - metasploit
type: command
executor: bash
platforms:
  - Linux
id: c8620a19-22db-46ef-b707-50e505828936
created_at: '2025-12-11T03:47:47.767Z'
updated_at: '2025-12-11T03:47:47.767Z'
verified: false
validated: true
submitted: true
---
# msf-set-lhost

## Command

```bash
set lhost [your public ip]
```

## Description

Sets the local host IP for the listener in Metasploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `lhost [your public ip]` | Listener IP | Yes |

## Examples

### Basic Usage

```bash
set lhost 192.168.0.1
```

## Expected Output

Configures the listener host.

## Related

- [[procedures/Configure-Metasploit-and-Trigger-Reporting-Job-for-Reverse-Shell]]
- [[commands/msf-use-exploit]]
