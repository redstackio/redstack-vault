---
id: uuid-induce-user-visit
tags:
  - phishing
  - user-inducement
  - open-redirect
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
  - '[[Phishing]]'
updated_at: '2025-12-14T17:24:26.386Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Induce-User-to-Visit-Malicious-URL

## Summary

This procedure involves social engineering to get a victim to access the crafted OAuth authorization URL, resulting in an automatic redirect to the attacker's site due to the invalid scope error, bypassing consent screens.

## Description

When the victim visits the URL, the server validates parameters per RFC6749 and detects the invalid scope, triggering an error redirect to the specified redirect_uri without showing a consent or error page to the user. This can lead to phishing (e.g., fake login on attacker.com) or chaining with referrer leaks for token theft. Targets users of the OAuth provider. Expected outcome: Seamless redirect to attacker-controlled domain.

## Requirements

1. Crafted URL from previous procedure
2. Social engineering vector (e.g., email, link in chat)
3. Attacker server hosting phishing content at redirect_uri

## Defense

Defensive measures and detection strategies:

- User education on suspicious OAuth links
- Server-side: Block redirects on errors or require user confirmation
- Monitor access logs for error patterns with external redirect_uris

## Objectives

1. Get victim to load the malicious URL
2. Trigger server error and automatic redirect
3. Deliver victim to phishing site for further exploitation

## Instructions

### Step 1: Distribute the URL

**Context**: Use phishing techniques to send the crafted URL to the target user.

Embed in an email or message: "Click here to authorize access: [crafted URL]"

> Expected output: User clicks and navigates to the /authorize endpoint.

### Step 2: Observe Redirect Behavior

**Context**: Monitor the attacker's server for incoming traffic from the redirect.

When user visits (e.g., http://victim.com/authorize?response_type=code&client_id=bc88FitX1298KPj2WS259BBMa9_KCfL3&scope=WRONG_SCOPE&redirect_uri=http://attacker.com), server redirects to http://attacker.com without prompt.

> Expected output: HTTP 302 redirect to attacker.com; no consent screen shown.

### Step 3: Validate Exploitation

**Context**: Confirm the redirect evades user interaction.

Test in a controlled browser; check network tab for redirect chain.

> Expected output: Direct jump to attacker site on error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Phishing]] Phishing

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[Phishing]]
- [[user-inducement]]
- [[open-redirect]]
