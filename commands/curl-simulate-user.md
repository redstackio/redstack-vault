---
id: cmd-curl-user-sim
data: 'curl https://www.paypal.com/ -v'
tags:
  - web
  - http
  - dos
type: command
output: |-
  HTTP/1.1 200 OK
  ... (with potential JS 501 references)
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:02.968Z'
verified: false
validated: true
submitted: true
---
# curl-simulate-user

## Command

```bash
curl https://www.paypal.com/ -v
```

## Description

Simulates a standard user request to the target site to observe DoS effects from poisoned cache.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output for inspection | Yes |

## Examples

### Basic Usage

```bash
curl https://www.paypal.com/ -v
```

### Advanced Usage

```bash
curl https://www.paypal.com/signin -v --cookie "session=abc"
```

## Expected Output

200 OK for page, but logs or follow-up show JS failures.

## Related

- [[Related Procedure: Induce-Denial-of-Service-via-Poisoned-Cache]]
