---
id: cmd-cat-tmp-vakzz
data: cat /tmp/vakzz
tags:
  - verification
  - file-read
type: command
output: vakzz was here
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:15.007Z'
verified: false
validated: true
submitted: true
---
# cat-tmp-vakzz

## Command

```bash
cat /tmp/vakzz
```

## Description

Displays the contents of /tmp/vakzz to verify Ruby payload execution post-RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /tmp/vakzz | Path to verification file | Yes |

## Examples

### Basic Usage

```bash
cat /tmp/vakzz
```

## Expected Output

vakzz was here

## Related

- [[procedures/Verify-Payload-Execution-and-Command-Injection]]
