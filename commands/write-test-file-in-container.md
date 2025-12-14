---
id: cmd-echo-pwned-write
data: echo 'Hello from snap code exec' > /home/itszn/pwned
tags:
  - rce-demo
  - file-write
type: command
output: Creates file with content 'Hello from snap code exec'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:23.800Z'
verified: false
validated: true
submitted: true
---
# write-test-file-in-container

## Command

```bash
echo 'Hello from snap code exec' > /home/itszn/pwned
```

## Description

Write a test file to user home directory inside snap to demonstrate RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| > /home/itszn/pwned | Redirect output to file | Yes |

## Examples

### Basic Usage

```bash
echo 'Hello from snap code exec' > /home/itszn/pwned
```

### Advanced Usage

```bash
echo 'Test' > /tmp/test
```

## Expected Output

Creates file with content 'Hello from snap code exec'.

## Related

- [[commands/read-test-file-in-container]]
- [[procedures/Trigger-RCE-in-Snap-Application]]
