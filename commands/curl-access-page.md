---
data: >-
  curl
  "https://target-dod-subdomain.com/path/user/NextRequestAccount.action?militarybranch=test"
tags:
  - web
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:53.491Z'
id: 13f34c7a-e373-441f-bd66-850f1de5a125
verified: false
validated: true
submitted: true
---
# curl-access-page

## Command

```bash
curl "https://target-dod-subdomain.com/path/user/NextRequestAccount.action?militarybranch=test"
```

## Description

This command uses curl to perform a GET request to the DoD registration page with a test value in the militarybranch parameter, allowing inspection of the response for reflection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Full target URL with query parameters | Yes |

## Examples

### Basic Usage

```bash
curl "https://target-dod-subdomain.com/path/user/NextRequestAccount.action?militarybranch=test"
```

### Advanced Usage

```bash
curl -v "https://target-dod-subdomain.com/path/user/NextRequestAccount.action?militarybranch=test" -o response.html
```

## Expected Output

HTML response from the server, including the reflected 'test' value in the page body without encoding.

## Related

- [[commands/curl-send-xss-payload]]
