---
data: 'hash[''my_key'']'
tags:
  - ruby
  - hash
type: command
executor: ruby
platforms:
  - Web
id: 74f96d50-e199-4fd1-ae78-93bf027c15db
created_at: '2025-12-11T06:10:28.438Z'
updated_at: '2025-12-11T06:10:28.438Z'
verified: false
validated: true
submitted: true
---
# hash-string-key-access

## Command

```ruby
hash['my_key']
```

## Description

Accesses the value associated with the string key 'my_key' in a Ruby hash, showing distinct treatment from symbol keys.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `'my_key'` | String key in the hash | Yes |

## Examples

### Basic Usage

```ruby
hash = { :my_key => 'my_value', 'my_key' => 'my_other_value' }
hash['my_key']
```

## Expected Output

'my_other_value'

## Related

- [[commands/hash-symbol-key-access]]
- [[commands/hash-to-json]]
