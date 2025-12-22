---
data: 'echo hello > /tmp/ggg; sudo chown git:git /tmp/ggg'
tags:
  - file-creation
type: command
executor: bash
platforms:
  - Linux
id: d783ea7d-3144-420c-9b97-cb2bb964b319
created_at: '2025-12-11T06:10:15.414Z'
updated_at: '2025-12-11T06:10:15.414Z'
verified: false
validated: true
submitted: true
---
# create-test-file-git-owned

## Command

```bash
echo hello > /tmp/ggg; sudo chown git:git /tmp/ggg
```

## Description

Creates a test file in /tmp with 'hello' content and changes ownership to git:git for GitLab exploit testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo hello > /tmp/ggg` | Writes content to file | Yes |
| `sudo chown git:git /tmp/ggg` | Changes ownership | Yes |

## Examples

### Basic Usage

```bash
echo hello > /tmp/ggg; sudo chown git:git /tmp/ggg
```

## Expected Output

Creates /tmp/ggg owned by git:git, no output if successful.

## Related

- [[commands/create-test-file-root-owned]]
- [[procedures/Prepare-GitLab-Server-Test-Files]]
