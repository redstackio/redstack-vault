---
tags:
  - css-escape
  - proxy-bypass
  - injection
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: df05464f-7e2c-4bd3-9294-825ec2a0c9b9
created_at: '2025-12-13T23:52:20.794Z'
updated_at: '2025-12-13T23:52:20.794Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject Escaped CSS URL into Profile Bio

## Summary

This procedure injects HTML with CSS escape sequences into Chaturbate profile bio fields to obfuscate URLs, bypassing the Camo image proxy and allowing direct external image loads.

## Description

In the context of Chaturbate's user profiles, the backend sanitization fails to decode CSS escapes like `\72` for 'r' in 'url'. By injecting `<span style="background:u\72l(http://foo.com/bar)">XX</span>`, the URL evades proxying, resulting in browsers loading external resources directly when viewing the profile. This can enable IP logging or tracking, though CSP mitigates in modern browsers. Prerequisites include a room owner account for bio editing.

## Requirements

1. Authenticated Chaturbate room owner account
2. Browser access to profile edit page
3. Knowledge of target external URL for testing (e.g., a controlled image server)

## Defense

Defensive measures and detection strategies:

- Implement CSS escape decoding in sanitization pipelines
- Enforce strict CSP to block external resource loads
- Monitor profile fields for suspicious HTML patterns like escaped sequences

## Objectives

1. Obfuscate URL to bypass proxy detection
2. Persist malicious HTML in profile
3. Enable direct external requests from viewers

## Instructions

### Step 1: Prepare Malicious HTML

**Context**: Craft the injection payload using CSS escapes to hide the URL from the parser.

No command required; manually enter in the bio field:

```html
<span style="background:u\72l(http://foo.com/bar)">XX</span>
```

> This sets a background image with an escaped 'url' that unescapes in the browser to load http://foo.com/bar directly.

### Step 2: Insert and Save

**Context**: Add the payload to the bio and submit to persist it.

Navigate to profile edit (About Me or Wish List), paste the HTML, and submit the form.

> Backend accepts without proxying due to failure to handle escapes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[css-escape]]
- [[proxy-bypass]]
