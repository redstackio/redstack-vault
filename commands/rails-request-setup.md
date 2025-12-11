---
data: 'request = ActionDispatch::Request.new(Rails.application.env_config)'
tags:
  - rails
  - payload
type: command
executor: ruby
platforms:
  - Linux
id: 11c76531-7166-4348-89ba-3b7589e4993b
created_at: '2025-12-11T03:47:59.303Z'
updated_at: '2025-12-11T03:47:59.303Z'
verified: false
validated: true
submitted: true
---
# rails-request-setup

## Command

```ruby
request = ActionDispatch::Request.new(Rails.application.env_config)
```

## Description

Creates a new request object in the Rails environment for setting up cookie serialization in payload generation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Rails.application.env_config` | Application's environment configuration | Yes |

## Examples

### Basic Usage

```ruby
request = ActionDispatch::Request.new(Rails.application.env_config)
```

## Expected Output

A Request object instance.

## Related

- [[commands/rails-set-serializer]]
- [[procedures/Extract-Secrets-and-Generate-Marshalled-Payload]]
