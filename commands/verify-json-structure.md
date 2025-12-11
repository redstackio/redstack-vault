---
data: 'verify(format: :json) { subject.body }'
tags:
  - ruby
  - testing
type: command
executor: ruby
platforms:
  - Web
id: eabeed3f-ec14-4bae-8e04-597330cbc74f
created_at: '2025-12-11T06:10:28.422Z'
updated_at: '2025-12-11T06:10:28.422Z'
verified: false
validated: true
submitted: true
---
# verify-json-structure

## Command

```ruby
verify(format: :json) { subject.body }
```

## Description

Verifies the JSON structure using the approvals gem in automated tests, but may miss duplicate keys due to parsing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `format: :json` | Specifies JSON format | Yes |
| `{ subject.body }` | Block providing JSON body | Yes |

## Examples

### Basic Usage

```ruby
verify(format: :json) { subject.body }
```

## Expected Output

Normalized JSON for test comparison.

## Related

- [[tools/approvals-gem]]
- [[procedures/Exploit-Information-Disclosure-in-HackerOne-Report-JSON-Endpoint]]
