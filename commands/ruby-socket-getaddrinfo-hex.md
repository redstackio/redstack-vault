---
id: cmd-uuid-7
data: 'require ''socket''; Socket.getaddrinfo("0x7f.1", nil)'
tags:
  - fix-test
  - socket
type: command
output: >-
  [["AF_INET", 0, "127.0.0.1", "127.0.0.1", 2, 1, 6], ["AF_INET", 0,
  "127.0.0.1", "127.0.0.1", 2, 2, 17], ["AF_INET", 0, "127.0.0.1", "127.0.0.1",
  2, 3, 0]]
executor: ruby
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.650Z'
verified: false
validated: true
submitted: true
---
# ruby-socket-getaddrinfo-hex

## Command

```ruby
require 'socket'; Socket.getaddrinfo("0x7f.1", nil)
```

## Description

Uses Ruby Socket to get OS-level address info for hex IP, recommended for fixing SSRF by catching malformed resolutions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| "0x7f.1" | Hex IP | Yes |
| nil | Default port | Yes |

## Examples

### Basic Usage

```ruby
require 'socket'; Socket.getaddrinfo("0x7f.1", nil)
```

## Expected Output

[["AF_INET", 0, "127.0.0.1", "127.0.0.1", 2, 1, 6], ["AF_INET", 0, "127.0.0.1", "127.0.0.1", 2, 2, 17], ["AF_INET", 0, "127.0.0.1", "127.0.0.1", 2, 3, 0]]

## Related

- [[commands/ruby-resolv-hex-ip]]
- [[procedures/Bypass-SSRF-Filters-with-Hex-and-Decimal-IPs]]
