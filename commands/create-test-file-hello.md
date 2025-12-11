---
data: echo hello > /tmp/ggg;
tags:
  - file-creation
type: command
executor: bash
platforms:
  - Linux
id: 552ef9da-d8e5-4532-80a3-27dc6d7d5c6a
created_at: '2025-12-11T06:10:15.399Z'
updated_at: '2025-12-11T06:10:15.399Z'
verified: false
validated: true
submitted: true
---
# create-test-file-hello

## Command

```bash
echo hello > /tmp/ggg;
```

## Description

Creates a simple test file with 'hello' in /tmp/ggg.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo hello > /tmp/ggg` | Writes content | Yes |

## Examples

### Basic Usage

```bash
echo hello > /tmp/ggg;
```

## Expected Output

File created.

## Related

- [[procedures/Prepare-GitLab-Server-Test-Files]]
