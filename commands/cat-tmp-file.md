---
id: 85a393f6-9373-4c70-ad95-7558de3a6e20
name: cat-tmp-file
type: command
executor: bash
data: cat /tmp/vakzz
output: null
created_at: '2025-12-09T00:20:45.025Z'
updated_at: '2025-12-09T00:20:45.025Z'
platforms:
  - Linux
tags:
  - verification
verified: false
validated: true
submitted: true
---

# cat-tmp-file

## Command

```bash
cat /tmp/vakzz
```

## Description

Displays the contents of a temporary file for verification.

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

- [[Verify Exploitation and Execute Reverse Shell]]
