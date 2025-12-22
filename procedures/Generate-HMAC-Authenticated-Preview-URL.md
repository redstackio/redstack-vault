---
tags:
  - hmac
  - auth-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/hmac-generation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-13T23:52:44.196Z'
sub_techniques: []
id: db287202-fc29-43a6-af01-bbc579d4eaf7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Generate-HMAC-Authenticated-Preview-URL

## Summary

Create a time-bound URL using HMAC authentication to force a victim to log in as the attacker and preview the malicious template, triggering XSS.

## Description

Judge.me uses HMAC-signed URLs for passwordless access to shop resources. With the attacker's API token as the key, generate a URL that authenticates the victim to the attacker's session, enabling preview execution.

## Requirements

1. Shop's API private token
2. Victim's shop domain
3. PHP environment for hash_hmac

## Defense

- Rotate API tokens regularly
- Add expiration and IP checks to HMAC URLs
- Educate users on phishing HMAC links

## Objectives

1. Produce valid signed URL
2. Ensure victim authentication
3. Lead to XSS trigger

## Instructions

### Step 1: Compute HMAC

**Context**: Use PHP to hash query parameters with the token.

**Command** ([[commands/hmac-generation]]):
```php
$hmac = hash_hmac('sha256', "no_iframe=1&platform=woocommerce&shop_domain={$domain}", $token, false);
```

> Replace $domain with victim's domain and $token with API key. Output is hex HMAC.

### Step 2: Construct URL

**Context**: Append HMAC to base URL.

```url
https://www.judge.me/shop/emails/2243518/edit?no_iframe=1&shop_domain=wordpress.caueo.me&platform=woocommerce&hmac=[HMAC]
```

> Send this URL to victim via email or chat.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/hmac-generation]]

## Tools Used


## Tags

- [[hmac]]
- [[auth-bypass]]
