---
data: 'cookies.signed[:cookie]= depr'
tags:
  - rails
  - cookie
type: command
executor: ruby
platforms:
  - Linux
id: d058c401-84ef-4728-a663-87d0f9fd63b6
created_at: '2025-12-11T06:10:40.412Z'
updated_at: '2025-12-11T06:10:40.412Z'
verified: false
validated: true
submitted: true
---
# rails-set-signed-cookie

## Command

```ruby
cookies.signed[:cookie]= depr
```

## Description

Signs and sets the cookie with the deprecated proxy object using the secret key.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `depr` | Proxy object | Yes |
| `:cookie` | Cookie name | Yes |

## Examples

### Basic Usage

```ruby
cookies.signed[:cookie]= depr
```

## Expected Output

Signed cookie set.

## Related

- [[commands/rails-deprecated-proxy]]
- [[procedures/Generate-and-Deliver-Deserialization-Payload-for-RCE]]
