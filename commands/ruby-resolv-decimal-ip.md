---
id: cmd-uuid-3
data: require 'resolv'; Resolv.getaddress "2130706433"
tags:
  - ssrf-test
  - decimal-ip
type: command
output: 'Resolv::ResolvError: no address for 2130706433'
executor: ruby
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.671Z'
verified: false
validated: true
submitted: true
---
# ruby-resolv-decimal-ip

## Command

```ruby
require 'resolv'; Resolv.getaddress "2130706433"
```

## Description

Attempts resolution of decimal IP for localhost using Ruby Resolv, showing failure for SSRF bypass validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| "2130706433" | Decimal for 127.0.0.1 | Yes |

## Examples

### Basic Usage

```ruby
require 'resolv'; Resolv.getaddress "2130706433"
```

## Expected Output

Resolv::ResolvError: no address for 2130706433

## Related

- [[commands/ruby-resolv-hex-ip]]
- [[procedures/Bypass-SSRF-Filters-with-Hex-and-Decimal-IPs]]
