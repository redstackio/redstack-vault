---
data: 'JSON.parse(''{"my_key":"my_value","my_key":"my_other_value"}'')'
tags:
  - ruby
  - json
type: command
executor: ruby
platforms:
  - Web
id: 45c26c77-8155-4ea9-abab-dc79f8fea943
created_at: '2025-12-11T06:10:28.420Z'
updated_at: '2025-12-11T06:10:28.420Z'
verified: false
validated: true
submitted: true
---
# json-parse-duplicate-keys

## Command

```ruby
JSON.parse('{"my_key":"my_value","my_key":"my_other_value"}')
```

## Description

Parses a JSON string in Ruby, retaining only the last duplicate key, explaining why tests didn't detect the issue.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `'{"my_key":"my_value","my_key":"my_other_value"}'` | JSON string with duplicates | Yes |

## Examples

### Basic Usage

```ruby
JSON.parse('{"my_key":"my_value","my_key":"my_other_value"}')
```

## Expected Output

{"my_key"=>"my_other_value"}

## Related

- [[commands/hash-to-json]]
- [[procedures/Exploit-Information-Disclosure-in-HackerOne-Report-JSON-Endpoint]]
