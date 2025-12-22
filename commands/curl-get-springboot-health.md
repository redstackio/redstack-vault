---
type: command
executor: bash
data: 'curl -X GET http://$_TARGET:$_PORT/health -v'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - web-recon
  - http-request
verified: true
validated: true
---

# curl-get-springboot-health

## Command

```bash
curl -X GET http://$_TARGET:$_PORT/health -v
```

## Description

This command sends an HTTP GET request to the Spring Boot Actuator /health endpoint to retrieve the application's health status. It is used during reconnaissance to check if the endpoint is exposed and to gather details about the application's components, such as database connectivity or disk usage, without requiring authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET | The IP address or hostname of the target Spring Boot application | Yes |
| $_PORT | The port on which the application is listening (default: 8080) | Yes |
| -X GET | Specifies the HTTP method as GET | Built-in |
| -v | Enables verbose mode to show request/response headers | No |

## Examples

### Basic Usage

```bash
curl -X GET http://192.168.1.100:8080/health -v
```

### Advanced Usage

```bash
curl -X GET http://example-app.com/health -H "User-Agent: Mozilla/5.0" -v
```

## Expected Output

A successful response will return HTTP 200 OK with a JSON body indicating the health status:

```
* Connected to 192.168.1.100 (192.168.1.100) port 8080
> GET /health HTTP/1.1
> Host: 192.168.1.100:8080
< HTTP/1.1 200 OK
< Content-Type: application/vnd.spring-boot.actuator.v2+json
{
  "status": "UP",
  "components": {
    "db": {
      "status": "UP",
      "details": {...}
    },
    "diskSpace": {
      "status": "UP",
      "details": {...}
    }
  }
}
```

If the endpoint is not exposed or secured, expect 404 Not Found or 401 Unauthorized.

## Related

- [[procedures/Enumerate-Spring-Boot-Actuator-Health-Endpoint]]
