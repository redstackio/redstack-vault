---
data: >-
  key_generator =
  ActiveSupport::CachingKeyGenerator.new(ActiveSupport::KeyGenerator.new(secret_key_base,
  iterations: 1000))
tags:
  - payload
  - keygen
  - ruby
type: command
output: KeyGenerator object
executor: ruby
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.280Z'
id: 8543141d-ad0a-4855-ae52-11799affecf1
verified: false
validated: true
submitted: true
---
# create-key-generator

## Command

```ruby
key_generator = ActiveSupport::CachingKeyGenerator.new(ActiveSupport::KeyGenerator.new(secret_key_base, iterations: 1000))
```

## Description

Create a key generator instance using the secret_key_base for ActiveStorage secret.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| iterations | 1000 | Yes |
| secret_key_base | Base secret | Yes |

## Examples

### Basic Usage

```ruby
key_generator = ActiveSupport::CachingKeyGenerator.new(ActiveSupport::KeyGenerator.new(secret_key_base, iterations: 1000))
```

## Expected Output

KeyGenerator object

## Related

- [[commands/derive-secret-key-base]]
