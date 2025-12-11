---
data: echo unused > /tmp/lala.txt
tags:
  - file-creation
type: command
executor: bash
platforms:
  - Linux
id: 31b8ee7c-4246-4d99-b017-ed8afd3b55ba
created_at: '2025-12-11T06:10:15.397Z'
updated_at: '2025-12-11T06:10:15.397Z'
verified: false
validated: true
submitted: true
---
# create-dummy-file-unused

## Command

```bash
echo unused > /tmp/lala.txt
```

## Description

Creates a dummy upload file with 'unused' content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo unused > /tmp/lala.txt` | Writes content | Yes |

## Examples

### Basic Usage

```bash
echo unused > /tmp/lala.txt
```

## Expected Output

File created.

## Related

- [[procedures/Prepare-GitLab-Server-Test-Files]]
