---
data: 'request = ActionDispatch::Request.new(Rails.application.env_config)'
tags:
  - rails
  - payload-generation
type: command
executor: ruby
platforms:
  - Linux
id: dd2592ac-9bd6-481f-99e5-29e4a82fef7e
created_at: '2025-12-11T06:10:40.429Z'
updated_at: '2025-12-11T06:10:40.429Z'
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

Creates a new ActionDispatch::Request object using the Rails application environment configuration for simulating requests in console.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Rails.application.env_config` | Provides the Rails environment config | Yes |

## Examples

### Basic Usage

```ruby
request = ActionDispatch::Request.new(Rails.application.env_config)
```

## Expected Output

A request object instance.

## Related

- [[commands/rails-set-serializer]]
- [[procedures/Generate-and-Deliver-Deserialization-Payload-for-RCE]]
