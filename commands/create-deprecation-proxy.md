---
data: >-
  dump_target = ActiveSupport::Deprecation::DeprecatedInstanceVariableProxy.new
  erb, :result
tags:
  - payload
  - proxy
  - ruby
type: command
output: Proxy object
executor: ruby
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.214Z'
id: b0dc7368-c42a-4192-bc2b-b86e3bbcd400
verified: false
validated: true
submitted: true
---
# create-deprecation-proxy

## Command

```ruby
dump_target = ActiveSupport::Deprecation::DeprecatedInstanceVariableProxy.new erb, :result
```

## Description

Wrap the ERB in a proxy that triggers :result method on deserialization, executing the ERB.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| erb | ERB object | Yes |
| :result | Method to proxy | Yes |

## Examples

### Basic Usage

```ruby
dump_target = ActiveSupport::Deprecation::DeprecatedInstanceVariableProxy.new erb, :result
```

## Expected Output

Proxy object

## Related

- [[commands/set-erb-lineno]]
