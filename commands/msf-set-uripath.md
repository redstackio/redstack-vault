---
data: set uripath /
tags:
  - metasploit
type: command
executor: bash
platforms:
  - Linux
id: 8520bfa8-66f4-4c70-95ce-09d2bf1a3488
created_at: '2025-12-11T03:47:47.771Z'
updated_at: '2025-12-11T03:47:47.771Z'
verified: false
validated: true
submitted: true
---
# msf-set-uripath

## Command

```bash
set uripath /
```

## Description

Sets the URI path for the exploit server in Metasploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `uripath /` | URI path | Yes |

## Examples

### Basic Usage

```bash
set uripath /
```

## Expected Output

Configures the URI path.

## Related

- [[procedures/Configure-Metasploit-and-Trigger-Reporting-Job-for-Reverse-Shell]]
- [[commands/msf-set-lhost]]
