---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - xss
  - oauth
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:39.233Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-and-Visit-Malicious-OAuth-Redirect-URL

## Summary

This procedure crafts a malicious URL exploiting the unsanitized 'redirect_to' parameter in Mattermost's OAuth mobile login endpoint to inject HTML and JavaScript, enabling reflected XSS for session hijacking.

## Description

In Mattermost Server, the OAuth flow in web/oauth.go (line 284) assigns the 'redirect_to' query parameter to redirectURL without sanitization. This value is passed to utils/api.go's RenderMobileError, which concatenates it into an HTML anchor tag via RenderMobileMessage without escaping. An attacker can close the href attribute with a payload like ">%3Cimg src="" onerror="alert('XSS')"%3E, injecting executable script when a victim visits the crafted URL during authentication. This leads to arbitrary JS execution in the browser, allowing cookie theft for regular users (chat access) or privilege escalation for admins (add admins, modify settings).

## Requirements

1. Publicly accessible Mattermost Server URL with OAuth enabled
2. Knowledge of the OAuth provider (e.g., 'shielder')
3. Ability to socially engineer victim to click the link (no direct access needed)
4. Web browser for testing

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs in HTML contexts (e.g., use HTML entities or templating engines like Go's html/template)
- Implement Content Security Policy (CSP) to block inline scripts and unsafe eval
- Monitor for anomalous OAuth redirects or unusual alert popups in logs
- Use WAF rules to detect common XSS payloads in query parameters

## Objectives

1. Inject malicious HTML/JS into the OAuth response
2. Trigger execution upon page render
3. Enable session hijacking or data exfiltration

## Instructions

### Step 1: Construct the Malicious URL

**Context**: Build the URL by URL-encoding a payload that breaks out of the href and injects an <img> tag with onerror JS.

No command required; manually construct:

```url
https://<mattermost_url>/oauth/shielder/mobile_login?redirect_to=%22%3E%3Cimg%20src=%22%22%20onerror=%22alert(%27zi0Black%20@%20Shielder%27)%22%3E
```

> The payload %22%3E closes the quote and >, then injects <img src="" onerror="alert('zi0Black @ Shielder')">. Expected: Valid URL ready for distribution.

### Step 2: Distribute and Visit the URL

**Context**: Trick the victim into navigating to the URL, initiating the OAuth flow and triggering the reflection.

Open a browser and visit the constructed URL (or send via phishing).

> Browser loads the page, reflects the payload in the HTML anchor, rendering the injected tag. Expected: Page displays with potential visual anomalies if alert fires.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[oauth]]
- [[payload-injection]]
