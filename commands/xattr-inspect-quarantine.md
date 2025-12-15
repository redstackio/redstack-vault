---
id: cmd-uuid-1
data: xattr -l filename.terminal
tags:
  - inspection
  - quarantine
type: command
output: >-
  No output if no attributes; lists xattrs if present (e.g.,
  com.apple.quarantine: ...)
executor: bash
platforms:
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:24:08.099Z'
verified: false
validated: true
submitted: true
---
# xattr-inspect-quarantine

## Command

```bash
xattr -l filename.terminal
```

## Description

This command lists all extended attributes on a file, used to verify if the com.apple.quarantine attribute is missing, confirming the bypass in the Slack download process.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-l` | List all extended attributes in long format | Yes |
| `filename.terminal` | Path to the target file | Yes |

## Examples

### Basic Usage

```bash
xattr -l downloaded.terminal
```

### Advanced Usage

```bash
xattr -l -p com.apple.quarantine downloaded.terminal
```

> Checks specifically for quarantine attribute.

## Expected Output

If bypassed: No output or empty. If quarantined: com.apple.quarantine: 0081;... (base64 data).

## Related

- [[Related Procedure: Bypass-macOS-Gatekeeper-and-Quarantine-Checks]]
