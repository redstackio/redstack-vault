---
id: cmd-uuid-4
data: 'Socket.getaddrinfo(hostname, nil).sample[3]'
tags:
  - ruby
  - mitigation
  - dns
type: command
output: IP address string
executor: ruby
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.129Z'
verified: false
validated: true
submitted: true
---
# ruby-socket-getaddrinfo

## Command

```ruby
Socket.getaddrinfo(hostname, nil).sample[3]
```

## Description

Resolves a user-supplied hostname to an IP address using Socket.getaddrinfo, sampling the address field for reliable SSRF private IP checking as an alternative to Resolv.getaddresses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| hostname | User-supplied hostname to resolve | Yes |
| nil | Service parameter (nil for any) | Yes |
| sample[3] | Extracts the IP address from the result array | Yes |

## Examples

### Basic Usage

```ruby
Socket.getaddrinfo('127.0.0.1', nil).sample[3]
```

### Advanced Usage

Replace Resolv in filtering: ip = Socket.getaddrinfo(host, nil).sample[3]; then check if private.

## Expected Output

String like "127.0.0.1" or equivalent resolved IP.

## Related

- [[commands/ruby-require-socket]]
