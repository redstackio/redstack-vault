---
data: 'hash[:my_key]'
tags:
  - ruby
  - hash
type: command
executor: ruby
platforms:
  - Web
id: f97c85fd-4353-4ff0-af3d-d70de990e4bd
created_at: '2025-12-11T06:10:28.440Z'
updated_at: '2025-12-11T06:10:28.440Z'
verified: false
validated: true
submitted: true
---
# hash-symbol-key-access

## Command

```ruby
hash[:my_key]
```

## Description

Accesses the value associated with the symbol key :my_key in a Ruby hash, demonstrating key handling differences.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `:my_key` | Symbol key in the hash | Yes |

## Examples

### Basic Usage

```ruby
hash = { :my_key => 'my_value', 'my_key' => 'my_other_value' }
hash[:my_key]
```

## Expected Output

'my_value'

## Related

- [[commands/hash-string-key-access]]
- [[commands/hash-to-json]]
