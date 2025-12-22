---
data: set payload 5
tags:
  - metasploit
type: command
executor: bash
platforms:
  - Linux
id: dd15a405-21a8-4b20-92a9-571db334fcf1
created_at: '2025-12-11T03:47:47.774Z'
updated_at: '2025-12-11T03:47:47.774Z'
verified: false
validated: true
submitted: true
---
# msf-set-payload

## Command

```bash
set payload 5
```

## Description

Sets the payload for the exploit in Metasploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `payload 5` | Payload index | Yes |

## Examples

### Basic Usage

```bash
set payload 5
```

## Expected Output

Configures the payload.

## Related

- [[procedures/Configure-Metasploit-and-Trigger-Reporting-Job-for-Reverse-Shell]]
- [[commands/msf-set-uripath]]
