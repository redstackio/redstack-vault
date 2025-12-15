---
data: cat /tmp/RCE_VIA_ENGINE
tags:
  - verification
  - cat
type: command
executor: bash
platforms:
  - Linux
  - POSIX
id: 9dbdccd0-1905-421c-b21e-33c9070adb74
created_at: '2025-12-14T17:23:31.186Z'
updated_at: '2025-12-14T17:23:31.186Z'
verified: false
validated: true
submitted: true
---
# cat-rce-proof

## Command

```bash
cat /tmp/RCE_VIA_ENGINE
```

## Description

Displays the proof file contents to verify RCE success from the executed system command.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/tmp/RCE_VIA_ENGINE` | File path | Yes |

## Examples

### Basic Usage

```bash
cat /tmp/RCE_VIA_ENGINE
```

### Advanced Usage

cat /tmp/RCE_VIA_ENGINE | grep uid

## Expected Output

Output of the 'id' command, e.g., 'uid=1000(Dr4g0n) gid=1000(Dr4g0n) groups=... confirming RCE

## Related

- [[procedures/Verify-Code-Execution-via-Proof-File]]
