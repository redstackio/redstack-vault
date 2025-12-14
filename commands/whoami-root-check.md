---
data: whoami
tags:
  - enumeration
  - privilege-check
type: command
output: root
executor: bash
platforms:
  - Linux
created_at: '2024-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:24.837Z'
id: aaa59084-fea4-4c08-b109-eee1f0e995b4
verified: false
validated: true
submitted: true
---
# whoami-root-check

## Command

```bash
whoami
```

## Description

Displays the effective username of the current process, used here by the malicious plugin to verify root privileges post-RCE in the exploited Crowd instance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | No parameters; prints current user | No |

## Examples

### Basic Usage

```bash
whoami
```

## Expected Output

'root' indicating execution as the root user on the Linux server.

## Related

- [[Related Procedure: Invoke-Malicious-Plugin-for-RCE]]
