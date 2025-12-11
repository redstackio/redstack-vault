---
id: 3bb2a31b-ecff-45e9-8b11-7293a17c49a4
name: cat-tmp-vakzz
type: command
executor: bash
data: cat /tmp/vakzz
output: null
created_at: '2025-12-11T06:10:13.242Z'
updated_at: '2025-12-11T06:10:13.242Z'
platforms:
  - Linux
tags:
  - verification
  - file-read
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

Reads the content of /tmp/vakzz to verify payload execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|


## Examples

### Basic Usage

```bash
cat /tmp/vakzz
```

## Expected Output

vakzz was here

## Related

- [[commands/ruby-echo-tmp-file]]
- [[procedures/Verify-Payload-Execution-and-RCE]]
