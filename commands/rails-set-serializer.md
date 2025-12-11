---
data: 'request.env["action_dispatch.cookies_serializer"]=:marshal'
tags:
  - rails
  - deserialization
type: command
executor: ruby
platforms:
  - Linux
id: 6a657f26-7f7e-4a6a-9525-0fcb36ee90a8
created_at: '2025-12-11T06:10:40.426Z'
updated_at: '2025-12-11T06:10:40.426Z'
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

Sets the cookie serializer to marshal to enable insecure deserialization in Rails.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `action_dispatch.cookies_serializer` | Set to :marshal | Yes |

## Examples

### Basic Usage

```ruby
request.env["action_dispatch.cookies_serializer"]=:marshal
```

## Expected Output

None (sets environment variable).

## Related

- [[commands/rails-request-setup]]
- [[procedures/Generate-and-Deliver-Deserialization-Payload-for-RCE]]
