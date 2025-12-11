---
data: set target 0
tags:
  - metasploit
type: command
executor: bash
platforms:
  - Linux
id: 96eedf36-b4e0-4af0-8b82-0a2a11e7d2e6
created_at: '2025-12-11T03:47:47.777Z'
updated_at: '2025-12-11T03:47:47.777Z'
verified: false
validated: true
submitted: true
---
# msf-set-target

## Command

```bash
set target 0
```

## Description

Sets the target for the exploit in Metasploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `target 0` | Target index | Yes |

## Examples

### Basic Usage

```bash
set target 0
```

## Expected Output

Configures the target.

## Related

- [[procedures/Configure-Metasploit-and-Trigger-Reporting-Job-for-Reverse-Shell]]
- [[commands/msf-set-payload]]
