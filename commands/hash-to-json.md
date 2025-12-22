---
data: hash.to_json
tags:
  - ruby
  - json
type: command
executor: ruby
platforms:
  - Web
id: b10b5f85-f576-4891-a954-a014dc1abed0
created_at: '2025-12-11T06:10:28.432Z'
updated_at: '2025-12-11T06:10:28.433Z'
verified: false
validated: true
submitted: true
---
# hash-to-json

## Command

```ruby
hash.to_json
```

## Description

Serializes a Ruby hash to JSON, highlighting changes in behavior between Rails versions regarding duplicate keys.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | No parameters | No |

## Examples

### Basic Usage

```ruby
hash = { :my_key => 'my_value', 'my_key' => 'my_other_value' }
hash.to_json
```

## Expected Output

In Rails 6.1.7.9: {"my_key":"my_other_value"}; In Rails 7.1.5.1: {"my_key":"my_value","my_key":"my_other_value"}

## Related

- [[commands/json-parse-duplicate-keys]]
- [[procedures/Exploit-Information-Disclosure-in-HackerOne-Report-JSON-Endpoint]]
