---
id: 8998e334-be27-45f2-a630-7bfd4d0ab332
name: curl-actuator-info-endpoint
type: command
executor: bash
data: curl -X GET "$_TARGET_URL/info"
output: null
created_at: '2023-04-06T03:56:19.601066+00:00'
updated_at: '2023-04-10T20:34:25.407905+00:00'
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

# curl-actuator-info-endpoint

## Command

```bash
curl -X GET "$_TARGET_URL/info"
```

## Description

This command queries the Spring Boot Actuator /info endpoint to obtain application metadata, such as build details, environment variables, and configuration properties. It is useful for discovering sensitive information during the discovery phase of an engagement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Base URL of the target application (e.g., http://example.com:8080) | Yes |
| -X GET | Specifies the HTTP method as GET | Built-in |

## Examples

### Basic Usage

```bash
curl -X GET "http://target-app:8080/info"
```

### Advanced Usage (with headers for simulation)

```bash
curl -H "User-Agent: Mozilla/5.0" -X GET "$_TARGET_URL/info"
```

## Expected Output

A successful response is typically JSON with application info:

```json
{"build":{"name":"my-app","version":"1.0.0","time":"2023-01-01T00:00:00Z"},"git":{"commit":{"id":"abc123"}},"info":{"env":"prod","databaseUrl":"jdbc:postgresql://dbhost:5432/mydb"}}
```

Parse for version numbers, environment details, or credentials. Empty JSON or 404 errors mean the endpoint is disabled or secured.

## Related

- [[procedures/Exploit-Spring-Boot-Actuator-Insecure-Endpoints]]
- [[commands/curl-actuator-health-endpoint]]
