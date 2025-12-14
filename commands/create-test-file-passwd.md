---
id: cmd-echo-secret-passwd
name: create-test-file-passwd
type: command
executor: bash
data: echo 'secret' > /tmp/passwd
output: File created with the specified content
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.217Z'
platforms:
  - Linux
tags:
  - testing
  - file-creation
verified: false
validated: true
submitted: true
---

# create-test-file-passwd

## Command

```bash
echo 'secret' > /tmp/passwd
```

## Description

Creates a test file /tmp/passwd with content 'secret' for simulating sensitive file exposure in symlink attacks during GitLab import testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| content | String to write ('secret') | Yes |
| file | Output file path (/tmp/passwd) | Yes |

## Examples

### Basic Usage

```bash
echo 'secret' > /tmp/passwd
```

### Advanced Usage

```bash
echo 'sensitive data' > /tmp/custom_file
```

## Expected Output

No stdout; file /tmp/passwd created with content 'secret'. Verify with cat /tmp/passwd.

## Related

- [[Related Procedure]]
