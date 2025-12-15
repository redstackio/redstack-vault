---
data: rm -f /tmp/RCE_VIA_ENGINE
tags:
  - cleanup
  - rm
type: command
executor: bash
platforms:
  - Linux
  - POSIX
id: 86814e52-799a-4cb8-906f-d1539faf3b2a
created_at: '2025-12-14T17:23:31.190Z'
updated_at: '2025-12-14T17:23:31.190Z'
verified: false
validated: true
submitted: true
---
# rm-rce-proof-file

## Command

```bash
rm -f /tmp/RCE_VIA_ENGINE
```

## Description

Removes the RCE proof file to prepare for clean verification in exploitation tests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-f` | Force removal without confirmation | Yes |
| `/tmp/RCE_VIA_ENGINE` | Target file path | Yes |

## Examples

### Basic Usage

```bash
rm -f /tmp/RCE_VIA_ENGINE
```

### Advanced Usage

rm -f /tmp/RCE_VIA_ENGINE /tmp/other_proof

## Expected Output

No output if file doesn't exist or is removed

## Related

- [[procedures/Clean-Verification-Proof-File]]
