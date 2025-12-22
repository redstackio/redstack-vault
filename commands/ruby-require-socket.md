---
id: cmd-uuid-3
data: require 'socket'
tags:
  - ruby
  - mitigation
type: command
output: null
executor: ruby
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.134Z'
verified: false
validated: true
submitted: true
---
# ruby-require-socket

## Command

```ruby
require 'socket'
```

## Description

Loads the Socket library in Ruby for alternative address resolution using getaddrinfo, recommended as a mitigation for Resolv.getaddresses inconsistencies in SSRF filtering.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Standard require | Yes |

## Examples

### Basic Usage

```ruby
require 'socket'
```

## Expected Output

No output; loads the module.

## Related

- [[commands/ruby-socket-getaddrinfo]]
