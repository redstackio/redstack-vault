---
data: cat /tmp/vakzz
tags:
  - verification
type: command
executor: bash
platforms:
  - Linux
id: cf25c267-5444-430f-b5ec-d545476c66d5
created_at: '2025-12-11T03:47:59.062Z'
updated_at: '2025-12-11T03:47:59.062Z'
verified: false
validated: true
submitted: true
---
# cat-verify-file

## Command

```bash
cat /tmp/vakzz
```

## Description

Displays the content of a file created by RCE to verify successful command execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/tmp/vakzz` | File path | Yes |

## Examples

### Basic Usage

```bash
cat /tmp/vakzz
```

## Expected Output

vakzz was here

## Related

- [[commands/curl-malicious-cookie]]
- [[procedures/Send-Malicious-Cookie-for-RCE]]
