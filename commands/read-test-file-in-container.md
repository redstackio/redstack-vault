---
id: cmd-cat-pwned
data: cat /home/itszn/pwned
tags:
  - rce-demo
  - file-read
type: command
output: Hello from snap code exec
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:23.797Z'
verified: false
validated: true
submitted: true
---
# read-test-file-in-container

## Command

```bash
cat /home/itszn/pwned
```

## Description

Read the test file content to verify write access inside the snap container.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /home/itszn/pwned | Target file path | Yes |

## Examples

### Basic Usage

```bash
cat /home/itszn/pwned
```

### Advanced Usage

```bash
cat /home/itszn/pwned | grep Hello
```

## Expected Output

Hello from snap code exec.

## Related

- [[commands/write-test-file-in-container]]
- [[procedures/Trigger-RCE-in-Snap-Application]]
