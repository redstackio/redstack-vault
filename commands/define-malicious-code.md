---
data: code = '`touch /tmp/rce`'
tags:
  - payload
  - rce
  - ruby
type: command
output: '"`touch /tmp/rce`"'
executor: ruby
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.256Z'
id: f5275b32-b04d-420c-9fa0-5f7d27de7134
verified: false
validated: true
submitted: true
---
# define-malicious-code

## Command

```ruby
code = '`touch /tmp/rce`'
```

## Description

Prepare shell command for ERB payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Code string | No |

## Examples

### Basic Usage

```ruby
code = '`touch /tmp/rce`'
```

## Expected Output

"`touch /tmp/rce`"

## Related

- [[commands/create-message-verifier]]
