---
id: 56476382-bd3f-43ec-b15a-ff8e1d18918c
name: shell-echo-to-file
type: command
executor: bash
data: '`echo vakzz was here > /tmp/vakzz`'
output: null
created_at: '2025-12-09T00:20:45.042Z'
updated_at: '2025-12-09T00:20:45.042Z'
platforms:
  - Linux
tags:
  - shell
  - payload
verified: false
validated: true
submitted: true
---

# shell-echo-to-file

## Command

```bash
`echo vakzz was here > /tmp/vakzz`
```

## Description

Executes a shell command to write to a file, used in Ruby payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo vakzz was here > /tmp/vakzz` | Shell command | Yes |

## Examples

### Basic Usage

```bash
`echo vakzz was here > /tmp/vakzz`
```

## Expected Output

Creates /tmp/vakzz with content.

## Related

- [[Upload Payload Snippet in GitLab]]
