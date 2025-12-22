---
id: 57774da4-1dd1-4c0a-a982-bc32aee33d02
type: code
language: url-payload
verified: true
created_at: '2023-04-06T03:56:31.798229+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - redirect-bypass
  - whitelist
validated: true
---

# Whitelisted-Domain-Subdomain-Bypass

## Code

```url-payload
www.whitelisted.com.evil.com
```

## Description

This payload appends a malicious domain as a subdomain to a whitelisted base domain, tricking filters that validate only the root domain into allowing the redirect.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| whitelisted.com | Known whitelisted domain | example.com |
| evil.com | Attacker's malicious domain | attacker-phish.com |

## Usage

Insert into redirect parameter: http://target.com/redirect?url=http://www.whitelisted.com.evil.com. Use in phishing links to redirect victims seamlessly.

## Detection

- Monitor for subdomains resolving to external IPs not matching whitelist owners.
- Log DNS queries for unusual subdomain patterns.
- WAF rules for appended domains in redirect params.

## Related

- [[procedures/Bypass-Open-URL-Redirection-Filters]]
