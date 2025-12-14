---
id: cmd-uuid-2
data: Resolv.getaddresses('127.000.000.1')
tags:
  - ruby
  - ssrf
  - bug-test
type: command
output: '[] or ["127.0.0.1"]'
executor: ruby
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.140Z'
verified: false
validated: true
submitted: true
---
# ruby-resolv-getaddresses-127-000-000-1

## Command

```ruby
Resolv.getaddresses('127.000.000.1')
```

## Description

Resolves the encoded hostname '127.000.000.1' (octal form of localhost) to IP addresses using Ruby's Resolv library, revealing platform bugs where it returns an empty array instead of the expected IP.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| hostname | The hostname to resolve, e.g., '127.000.000.1' | Yes |

## Examples

### Basic Usage

```ruby
Resolv.getaddresses('127.000.000.1')
```

### Advanced Usage

Test variants: Resolv.getaddresses('0177.1') or Resolv.getaddresses('0x7f.1').

## Expected Output

[] (empty array on buggy Linux systems) or ["127.0.0.1"] (normal resolution).

## Related

- [[commands/ruby-require-resolv]]
