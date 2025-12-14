---
tags:
  - csrf
  - payload-delivery
  - phishing
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Account Manipulation]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 9266095f-8957-4768-9a1d-1260d29a26d9
created_at: '2025-12-14T17:33:24.590Z'
updated_at: '2025-12-14T17:33:24.590Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Craft-and-Deliver-CSRF-Payload

## Summary

This procedure crafts a CSRF payload from the captured callback request and delivers it to an authenticated victim, forcing their Discourse account to connect to the attacker's Yahoo credentials.

## Description

Exploiting the lack of CSRF protection, the attacker modifies the intercepted GET request into a victim-executable format, such as an HTML form auto-submitting the parameters or a direct malicious URL. Delivery occurs via social engineering (e.g., phishing email with link). When the victim, logged into Discourse, processes the payload, the connection completes without validation, linking accounts.

## Requirements

1. Captured callback request with auth token
2. Victim authenticated on the target Discourse site
3. Delivery vector (e.g., email, malicious site hosting form)

## Defense

Defensive measures and detection strategies:

- Require CSRF tokens for all auth callbacks
- SameSite cookie attributes to block cross-site requests
- User education on suspicious links during auth flows

## Objectives

1. Transform captured request into executable payload
2. Induce victim to submit the request
3. Achieve unauthorized account connection

## Instructions

### Step 1: Craft the Payload

**Context**: Convert the GET request to a deliverable format preserving parameters.

No command executed; create an HTML form like:

```html
<form action="https://try.discourse.org/auth/yahoo/callback" method="GET">
  <input type="hidden" name="openid.claimed_id" value="...">
  <input type="hidden" name="openid.ax.value.email" value="...">
  <!-- Include auth token param -->
  <input type="submit" value="Click to Connect">
</form>
<script>document.forms[0].submit();</script>
```

> Or use the full URL as a link for direct visit.

### Step 2: Deliver to Victim

**Context**: Trick the victim into visiting/submitting while authenticated.

No command executed; send the link or host the form on a controlled site and phishing-invite the victim.

> Victim must be logged in for the request to apply to their session.

### Step 3: Confirm Processing

**Context**: Observe the victim's side for completion.

No command executed; victim sees 'authentication complete' and redirect to https://try.discourse.org/?authComplete=true.

> Account linkage occurs silently.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[payload-delivery]]
