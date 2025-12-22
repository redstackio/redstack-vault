---
data: 'puts cookies[:cookie]'
tags:
  - rails
  - output
type: command
executor: ruby
platforms:
  - Linux
id: e3d0056b-5428-4b10-ae9b-28d212b4a8a8
created_at: '2025-12-11T03:47:59.176Z'
updated_at: '2025-12-11T03:47:59.176Z'
verified: false
validated: true
submitted: true
---
# puts-cookie

## Command

```ruby
puts cookies[:cookie]
```

## Description

Prints the generated signed cookie value, which is base64-encoded for use in HTTP requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | N/A | No |

## Examples

### Basic Usage

```ruby
puts cookies[:cookie]
```

## Expected Output

Base64-encoded marshalled payload string.

## Related

- [[commands/cookies-sign]]
- [[procedures/Extract-Secrets-and-Generate-Marshalled-Payload]]
