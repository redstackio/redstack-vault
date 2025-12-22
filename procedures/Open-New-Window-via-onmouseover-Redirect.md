---
tags:
  - xss
  - html-injection
  - open-redirect
type: procedure
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:41.689Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: b247ec4f-797b-44e0-84d1-560c184b867a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Open-New-Window-via-onmouseover-Redirect

## Summary

This procedure uses HTML injection to create a link that opens an arbitrary external window via JavaScript on mouseover, demonstrating open redirect capabilities for phishing or malware delivery.

## Description

The vulnerability allows unrestricted href attributes and JS methods like window.open(), enabling attackers to force navigation to attacker-controlled sites. Combined with social engineering, this can bypass some redirect protections and facilitate drive-by downloads or credential harvesting.

## Requirements

1. JavaScript-enabled browser
2. Access to https://[redacted]/help-leave/help/index.htm?ux=search
3. Encoding for URL-safe payload transmission

## Defense

Defensive measures and detection strategies:

- Validate and whitelist allowed protocols in href attributes (e.g., block javascript: or data:)
- Implement popup blockers and monitor window.open() calls via CSP
- Use browser security features like Safe Browsing to flag suspicious redirects

## Objectives

1. Inject interactive redirect-capable elements
2. Trigger external site access without user intent
3. Enable phishing or exfiltration vectors

## Instructions

### Step 1: Craft Redirect Payload

**Context**: Encode a <marquee> with <a> tag using window.open() on onmouseover for forced navigation.

Encoded: `%3Cmarquee%3E%3Ca%20href=%22http://google.com%22%20onmouseover=window.open(%22https://www.google.com%22)%3Etest%20for%20hackerone%3C/marquee%3E`

Full URL:

```url
https://[redacted]/help-leave/help/index.htm#rhsearch=%3Cmarquee%3E%3Ca%20href=%22http://google.com%22%20onmouseover=window.open(%22https://www.google.com%22)%3Etest%20for%20hackerone%3C/marquee%3E&ux=search
```

> On hover, opens https://www.google.com in a new window, ignoring the href unless clicked.

### Step 2: Execute and Observe

**Context**: Visit and hover to confirm redirect behavior.

Load the URL, find the injected link in the marquee, and hover.

> Expected: New window/tab opens to the target site. Verify no blocking occurs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[html-injection]]
- [[open-redirect]]
