---
id: cmd-uuid-005
data: 'curl -v localhost:8500/v1/config'
tags:
  - consul
  - ssrf
  - test
type: command
output: |-
  HTTP/1.1 405 Method Not Allowed
  method GET not allowed
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.518Z'
verified: false
validated: true
submitted: true
---
# curl-local-consul

## Command

```bash
curl -v localhost:8500/v1/config
```

## Description

Directly queries local Consul endpoint to simulate and compare SSRF response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose headers | No |
| `localhost:8500/v1/config` | Consul path | Yes |

## Examples

### Basic Usage

```bash
curl -v localhost:8500/v1/status/leader
```

## Expected Output

405 error with body 'method GET not allowed'.

## Related

- [[Related Procedure: Check-Import-Status-for-SSRF-Result]]
