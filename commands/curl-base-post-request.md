---
id: cmd-curl-base-post-001
data: 'curl ''https://target.gov/userops.aspx'' --data-raw ''sendingForm=userInfo'''
tags:
  - http
  - post
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:28.876Z'
verified: false
validated: true
submitted: true
---
# curl-base-post-request

## Command

```bash
curl 'https://target.gov/userops.aspx' --data-raw 'sendingForm=userInfo'
```

## Description

Sends a basic POST request to the user operations API endpoint with the 'sendingForm' parameter to test accessibility and confirm no authentication is required. This is the foundation for adding exploitable parameters like UID in IDOR scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL (positional) | Target API endpoint URL | Yes |
| --data-raw | Raw POST data string | Yes |
| sendingForm | Form type value (e.g., 'userInfo') | Yes |

## Examples

### Basic Usage

```bash
curl 'https://target.gov/userops.aspx' --data-raw 'sendingForm=userInfo'
```

### Advanced Usage

```bash
curl -v 'https://target.gov/userops.aspx' --data-raw 'sendingForm=userInfo' -o response.html
```

## Expected Output

HTTP 200 OK response with server output indicating successful processing, such as empty JSON {} or a form acknowledgment, without auth errors.

## Related

- [[commands/curl-idor-exploit]]
- [[procedures/Test-Endpoint-with-Base-POST-Request]]
