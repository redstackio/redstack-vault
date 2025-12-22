---
data: 'puts cookies[:cookie]'
tags:
  - rails
  - output
type: command
executor: ruby
platforms:
  - Linux
id: bf2fc08a-1c73-4f98-a89c-fe644e21962b
created_at: '2025-12-11T06:10:40.408Z'
updated_at: '2025-12-11T06:10:40.408Z'
verified: false
validated: true
submitted: true
---
# rails-print-cookie

## Command

```ruby
puts cookies[:cookie]
```

## Description

Prints the value of the serialized and signed cookie for use in attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|


## Examples

### Basic Usage

```ruby
puts cookies[:cookie]
```

## Expected Output

The base64-encoded serialized payload.

## Related

- [[commands/rails-set-signed-cookie]]
- [[procedures/Generate-and-Deliver-Deserialization-Payload-for-RCE]]
