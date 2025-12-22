---
tags:
  - xss-execution
  - user-interaction
  - javascript
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
  - '[[tools/Mozilla-Firefox]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:25.404Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: ffbb18ca-bc7b-4a87-8f15-9448d09cd0b5
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger XSS Execution via Copy Button

## Summary

This procedure simulates victim interaction to trigger the reflected XSS, executing the injected JavaScript in the page context upon clicking a 'copy' button that processes the malicious 'promo_code'.

## Description

After delivering the malicious URL, the victim loads the page, which decodes the JSON and renders the content. Scrolling to the bottom and clicking the 'copy' button (likely for sharing the promo code) evaluates the javascript: URL, running arbitrary code like alerting the domain or stealing data.

## Requirements

1. Victim to visit the crafted URL
2. Browser supporting javascript: navigation
3. No server-side changes needed

## Defense

Defensive measures and detection strategies:

- Sanitize hyperlink href attributes to prevent javascript: execution
- Avoid using user-controlled data in clipboard or link operations
- Monitor for anomalous JS alerts or network requests from client-side

## Objectives

1. Confirm payload execution in target domain context
2. Demonstrate potential for data exfiltration
3. Validate impact on authenticated sessions

## Instructions

### Step 1: Deliver and Load URL

**Context**: Ensure victim accesses the page with malicious 'q' parameter.

Share the URL: https://growth.grab.com/valentine/active/my.html?q=eyJuYW1lIjogIlRlc3QgSGFja2VyT25lIiwgInN0YXJ0X2RhdGUiOiAiMDEuMDEuMjAxOCIsICJsZWFucGx1bV9pZCI6ICJ0ZXN0IiwgInJpZGVzIjogIjIwMCIsICJwbGFjZXMiOiAiMjAiLCAiZGlzdGFuY2UiOiA1MDAsICJjYW5jZWxfdGltZXMiOiAiMCIsICJkYXlzIjogIjEwMCIsICJwcm9tb19jb2RlIjogImphdmFzY3JpcHQ6Ly9yLmdyYWIuY29tL3Rlc3QlMGFhbGVydChkb2N1bWVudC5kb21haW4pIiwgInByZl9yZXdhcmQiOiAiMTAifQ==.

> Load in [[tools/Google-Chrome]] (v63.0.3239.140) or [[tools/Mozilla-Firefox]] (v59.0b7) to verify.

### Step 2: Interact to Trigger Execution

**Context**: Simulate user action that processes the payload.

Scroll down the page and click the bottommost 'copy' button.

> Expected: Alert with 'growth.grab.com' pops up, confirming JS execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome]]
- [[tools/Mozilla-Firefox]]

## Tags

- [[xss-execution]]
- [[user-interaction]]
