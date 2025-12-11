---
data: 'echo hello > /tmp/ggg; sudo chown root:root /tmp/ggg'
tags:
  - file-creation
type: command
executor: bash
platforms:
  - Linux
id: fad17425-caeb-42f0-9db0-12d6cfbb5b2b
created_at: '2025-12-11T06:10:15.410Z'
updated_at: '2025-12-11T06:10:15.410Z'
verified: false
validated: true
submitted: true
---
# create-test-file-root-owned

## Command

```bash
echo hello > /tmp/ggg; sudo chown root:root /tmp/ggg
```

## Description

Creates a test file in /tmp with 'hello' content and changes ownership to root:root.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo hello > /tmp/ggg` | Writes content | Yes |
| `sudo chown root:root /tmp/ggg` | Changes ownership | Yes |

## Examples

### Basic Usage

```bash
echo hello > /tmp/ggg; sudo chown root:root /tmp/ggg
```

## Expected Output

Creates /tmp/ggg owned by root:root.

## Related

- [[commands/create-test-file-git-owned]]
- [[procedures/Prepare-GitLab-Server-Test-Files]]
