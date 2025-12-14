---
id: cmd-curl-fetch-response
data: 'curl http://localhost:9999'
tags:
  - dos
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:37.272Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-malicious-response

## Command

```bash
curl http://localhost:9999
```

## Description

This command uses curl to request an HTTP response from a local server, processing malicious headers that cause memory exhaustion due to repeated compression directives.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `http://localhost:9999` | Target URL of the malicious server | Yes |

## Examples

### Basic Usage

```bash
curl http://localhost:9999
```

### Advanced Usage

Add verbose output for monitoring: curl -v http://localhost:9999

```bash
curl -v http://localhost:9999
```

## Expected Output

No content retrieved; process hangs or exits with code 137 (OOM) on Unix; potential system crash on Windows.

## Related

- [[commands/check-exit-status]]
- [[procedures/Trigger-curl-Memory-Exhaustion-with-Malicious-Response]]
