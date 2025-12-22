---
id: new-uuid-for-copy
name: copy-tickey-binary-to-tmp
type: command
executor: bash
data: cp tickey /tmp/tickey && chmod +x /tmp/tickey
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - setup
  - file-management
verified: true
validated: true
---

# Copy Tickey Binary to Tmp

## Command

```bash
cp tickey /tmp/tickey && chmod +x /tmp/tickey
```

## Description

Copies the compiled Tickey binary to the /tmp directory and sets executable permissions, allowing easy execution from a system-wide writable location.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| tickey | Source binary file in current directory | Yes |
| /tmp/tickey | Destination path in /tmp | Yes |
| +x | Execute permission flag | Yes |

## Examples

### Basic Usage

```bash
cp tickey /tmp/tickey && chmod +x /tmp/tickey
```

### With Verification

```bash
cp tickey /tmp/tickey && chmod +x /tmp/tickey && ls -l /tmp/tickey
```

## Expected Output

No output for cp/chmod; verification shows: -rwxr-xr-x 1 user user ... /tmp/tickey

## Related

- [[procedures/extract-ccache-tickets-from-linux-keyring-with-tickey]]
- [[tools/tickey]]
