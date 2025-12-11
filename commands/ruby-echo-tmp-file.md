---
id: d09fdb54-2a72-44f3-adb6-dd2a5f9eafce
name: ruby-echo-tmp-file
type: command
executor: bash
data: '`echo vakzz was here > /tmp/vakzz`'
output: null
created_at: '2025-12-11T06:10:13.244Z'
updated_at: '2025-12-11T06:10:13.244Z'
platforms:
  - Linux
tags:
  - ruby
  - file-write
verified: false
validated: true
submitted: true
---

# ruby-echo-tmp-file

## Command

```bash
`echo vakzz was here > /tmp/vakzz`
```

## Description

Executes a shell command from Ruby to write to a file in /tmp for proof of execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| echo vakzz was here > /tmp/vakzz | Shell command | Yes |

## Examples

### Basic Usage

```bash
`echo vakzz was here > /tmp/vakzz`
```

## Expected Output

Creates /tmp/vakzz with content 'vakzz was here'

## Related

- [[commands/ruby-puts-hello]]
- [[procedures/Upload-Ruby-Payload-via-GitLab-Snippet]]
