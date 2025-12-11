---
data: ls -asl /tmp
tags:
  - verification
type: command
executor: bash
platforms:
  - Linux
id: 9600e608-d141-4842-a71e-b5230a36d5e2
created_at: '2025-12-11T03:48:05.984Z'
updated_at: '2025-12-11T03:48:05.984Z'
verified: false
validated: true
submitted: true
---
# ls-asl

## Command

```bash
ls -asl /tmp
```

## Description

Lists directory contents with details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-asl` | Options | Yes |

## Examples

### Basic Usage

```bash
ls -asl /path
```

## Expected Output

Directory listing

## Related

- [[procedures/Bypass-Feature-Flag-and-Verify-RCE]]
