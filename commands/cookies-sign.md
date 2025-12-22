---
data: 'cookies.signed[:cookie]= depr'
tags:
  - rails
  - cookie
type: command
executor: ruby
platforms:
  - Linux
id: ad005726-f577-47ed-b791-4e94ffa2e3ea
created_at: '2025-12-11T03:47:59.208Z'
updated_at: '2025-12-11T03:47:59.208Z'
verified: false
validated: true
submitted: true
---
# cookies-sign

## Command

```ruby
cookies.signed[:cookie]= depr
```

## Description

Signs and sets the deprecated proxy object in the cookie jar using the secret_key_base.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `:cookie` | Cookie key | Yes |
| `depr` | Object to sign | Yes |

## Examples

### Basic Usage

```ruby
cookies.signed[:cookie]= depr
```

## Expected Output

Signed cookie set.

## Related

- [[commands/deprecation-proxy-create]]
- [[procedures/Extract-Secrets-and-Generate-Marshalled-Payload]]
