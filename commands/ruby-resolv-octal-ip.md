---
id: cmd-uuid-1
data: require "resolv"; Resolv.getaddress "0177.1"
tags:
  - ssrf-test
  - resolv
type: command
output: 'Resolv::ResolvError: no address for 0177.1'
executor: ruby
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.679Z'
verified: false
validated: true
submitted: true
---
# ruby-resolv-octal-ip

## Command

```ruby
require "resolv"; Resolv.getaddress "0177.1"
```

## Description

Tests Ruby's Resolv library resolution of octal IP notation for localhost, demonstrating failure that enables SSRF bypass in GitLab.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| "0177.1" | Octal representation of 127.0.0.1 | Yes |

## Examples

### Basic Usage

```ruby
require "resolv"; Resolv.getaddress "0177.1"
```

### Advanced Usage

Run in irb for interactive testing.

## Expected Output

Resolv::ResolvError: no address for 0177.1

## Related

- [[commands/ruby-resolv-hex-ip]]
- [[procedures/Import-Repository-with-Octal-Localhost-IP-for-SSRF]]
