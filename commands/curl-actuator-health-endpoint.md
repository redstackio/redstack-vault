---
id: 1d39c7b8-732c-4c78-b47f-7ce50a4a4aa8
name: curl-actuator-health-endpoint
type: command
executor: bash
data: curl -X GET "$_TARGET_URL/health"
output: null
created_at: '2023-04-06T03:55:59.624892+00:00'
updated_at: '2023-04-10T20:22:29.430463+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - reconnaissance
  - web
verified: true
validated: true
---

# curl-actuator-health-endpoint

## Command

```bash
curl -X GET "$_TARGET_URL/health"
```

## Description

This command sends an HTTP GET request to the Spring Boot Actuator /health endpoint to retrieve the application's health status. Use it during reconnaissance to check if the endpoint is exposed and to gather information on application components like databases or caches.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Base URL of the target application (e.g., http://example.com:8080) | Yes |
| -X GET | Specifies the HTTP method as GET | Built-in |

## Examples

### Basic Usage

```bash
curl -X GET "http://target-app:8080/health"
```

### Advanced Usage (with verbose output)

```bash
curl -v -X GET "$_TARGET_URL/health"
```

## Expected Output

Successful execution returns a JSON object indicating health status:

```json
{"status":"UP","components":{"db":{"status":"UP","details":{"database":"PostgreSQL","hello":"1"}},"diskSpace":{"status":"UP","details":{"path":"/","free":12345678,"threshold":10485760}}}}
```

Look for "UP" or "DOWN" status and component details. Errors like 404 indicate the endpoint is not exposed, while 401/403 suggest authentication is required.

## Related

- [[procedures/Exploit-Spring-Boot-Actuator-Insecure-Endpoints]]
- [[commands/curl-actuator-info-endpoint]]
