---
data: secret = key_generator.generate_key('ActiveStorage')
tags:
  - payload
  - secret
  - ruby
type: command
output: Binary secret string
executor: ruby
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.273Z'
id: 774cd037-3f54-44f6-a601-a535ffbc27cb
verified: false
validated: true
submitted: true
---
# generate-activestorage-secret

## Command

```ruby
secret = key_generator.generate_key('ActiveStorage')
```

## Description

Generate a specific key for ActiveStorage using the key generator.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ActiveStorage | Key name | Yes |

## Examples

### Basic Usage

```ruby
secret = key_generator.generate_key('ActiveStorage')
```

## Expected Output

Binary secret string

## Related

- [[commands/create-key-generator]]
