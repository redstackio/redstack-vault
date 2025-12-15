---
data: 'secret_key_base = Digest::MD5.hexdigest(VerifierRce::Application.name)'
tags:
  - payload
  - secret
  - ruby
type: command
output: '"7e485df67863e85e584b3feecb22276d"'
executor: ruby
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.292Z'
id: dc1f9058-e2f9-4cbe-990a-726646fe4c9b
verified: false
validated: true
submitted: true
---
# derive-secret-key-base

## Command

```ruby
secret_key_base = Digest::MD5.hexdigest(VerifierRce::Application.name)
```

## Description

Emulate development secret_key_base by MD5 hashing the app name.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| VerifierRce::Application.name | Input string to hash | Yes |

## Examples

### Basic Usage

```ruby
secret_key_base = Digest::MD5.hexdigest(VerifierRce::Application.name)
```

## Expected Output

"7e485df67863e85e584b3feecb22276d"

## Related

- [[commands/get-app-class-name]]
