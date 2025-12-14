---
id: proc-firefox-whitespace-bypass
tags:
  - firefox
  - whitespace
  - cookie-injection
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Python-http-cookies]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/simplecookie-load-tab-delimiter]]'
  - '[[commands/simplecookie-load-vertical-tab-delimiter]]'
  - '[[commands/simplecookie-load-form-feed-delimiter]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:27:57.507Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Steal Web Session Cookie]]'
---
# Firefox-Whitespace-Bypass-for-Cookie-Injection

## Summary

This procedure provides an alternative CSRF injection method in Firefox using whitespace or control characters (tab, vertical tab, form feed) as delimiters in UTM parameters for __utmz cookie splitting.

## Description

Firefox allows whitespace in cookie values, enabling injection via UTM like utm_content=5%09csrftoken=x (%09=tab). SimpleCookie parses these as separators. Complements bracket delimiter for Chrome.

## Requirements

1. Firefox browser
2. Malicious URL with encoded whitespace
3. Python for testing

## Defense

Defensive measures and detection strategies:

- Filter control characters in GA UTM parameters
- Browser-specific cookie handling policies
- Monitor for unusual __utmz values

## Objectives

1. Inject via whitespace delimiter
2. Parse in SimpleCookie
3. Bypass in Firefox

## Instructions

### Step 1: Craft Firefox-Specific URL

**Context**: Use tab or space in UTM for injection.

URL: `https://instagram.com/?utm_source=1&utm_medium=2&utm_campaign=3&utm_term=4&utm_content=5%09csrftoken=x`

> Expected: __utmz set with \x09 separator.

### Step 2: Test Parsing

**Context**: Verify with Python commands.

Execute [[commands/simplecookie-load-tab-delimiter]]:

```python
from http import cookies
C = cookies.SimpleCookie()
C.load('__utmz=blah\x09csrftoken=x')
print(C)
```

> Expected: Separate cookies.

Repeat for vertical tab [[commands/simplecookie-load-vertical-tab-delimiter]] and form feed [[commands/simplecookie-load-form-feed-delimiter]].

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used

- [[commands/simplecookie-load-tab-delimiter]]
- [[commands/simplecookie-load-vertical-tab-delimiter]]
- [[commands/simplecookie-load-form-feed-delimiter]]

## Tools Used

- [[tools/Firefox]]
- [[tools/Python-http-cookies]]

## Tags

- [[tools/Firefox]]
- [[whitespace]]
- [[cookie-injection]]
