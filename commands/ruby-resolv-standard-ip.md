---
id: cmd-uuid-5
data: require 'resolv'; Resolv.getaddresses("127.0.0.1")
tags:
  - baseline-test
  - resolv
type: command
output: '["127.0.0.1"]'
executor: ruby
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.660Z'
verified: false
validated: true
submitted: true
---
# ruby-resolv-standard-ip

## Command

```ruby
require 'resolv'; Resolv.getaddresses("127.0.0.1")
```

## Description

Baseline test resolving standard localhost IP with Ruby Resolv to contrast with malformed notations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| "127.0.0.1" | Standard localhost IP | Yes |

## Examples

### Basic Usage

```ruby
require 'resolv'; Resolv.getaddresses("127.0.0.1")
```

## Expected Output

["127.0.0.1"]

## Related

- [[commands/ruby-resolv-octal-ip]]
- [[procedures/Analyze-Cloning-Error-to-Confirm-SSRF]]
