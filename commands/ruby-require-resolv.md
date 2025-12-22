---
id: cmd-uuid-1
data: require 'resolv'
tags:
  - ruby
  - dns
type: command
output: null
executor: ruby
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.143Z'
verified: false
validated: true
submitted: true
---
# ruby-require-resolv

## Command

```ruby
require 'resolv'
```

## Description

Loads the Resolv library in a Ruby environment (e.g., IRB) to enable DNS resolution functions like getaddresses, used for testing hostname-to-IP mapping in SSRF scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | No parameters; standard require statement | Yes |

## Examples

### Basic Usage

```ruby
require 'resolv'
```

### Advanced Usage

In IRB: Start IRB, then run the require to prepare for subsequent resolution tests.

## Expected Output

No output; silently loads the module if successful, or raises LoadError if unavailable.

## Related

- [[commands/ruby-resolv-getaddresses-127-000-000-1]]
