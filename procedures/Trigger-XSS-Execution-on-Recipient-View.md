---
tags:
  - xss
  - execution-trigger
  - session-hijacking
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: d24122d3-fbe9-4352-8c8a-118afadc70a0
created_at: '2025-12-13T23:52:39.453Z'
updated_at: '2025-12-13T23:52:39.453Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-on-Recipient-View

## Summary

This procedure triggers the execution of the stored XSS payload when a recipient views the shared video on TikTok, leading to JavaScript running in their browser context for attacks like session theft.

## Description

Once the payload is stored via video sharing, it renders in the recipient's view of the message text without proper escaping, executing JavaScript client-side. This can hijack sessions by exfiltrating cookies or tokens, impersonate users, or perform other attacks. Targets web browsers on TikTok's platform. Prerequisites: Payload already injected and shared to a target. Outcomes include payload execution, data exfiltration to attacker, and potential account compromise.

## Requirements

1. Recipient TikTok account targeted via shared video
2. Attacker monitoring server for exfiltrated data
3. Standard internet access for recipient to view content

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP headers to block unauthorized script sources
- Sanitize all rendered user content on client-side display
- Log and alert on suspicious client-side network outflows (e.g., beaconing to external domains)

## Objectives

1. Induce recipient to view the shared video
2. Execute the stored JavaScript payload in victim context
3. Achieve session hijacking or data collection

## Instructions

### Step 1: Deliver Shared Video to Recipient

**Context**: Ensure the target receives and is prompted to view the video containing the payload.

Send the video via TikTok's friend messaging or feed; use social engineering if needed to encourage viewing (e.g., "Check out this funny video!")

### Step 2: Recipient Views Video

**Context**: When the recipient opens the message and views the video, the message text renders, executing the payload.

The unsanitized text field displays the JavaScript, which runs automatically in the browser. For example, a cookie-stealing payload sends data to the attacker's server.

> Monitor your server logs for incoming requests from the victim's IP/session.

### Step 3: Validate Execution and Impact

**Context**: Confirm payload fired and assess compromise.

Check attacker server for received data (e.g., cookies). Test with alert payload first to verify execution without harm.

> Expected: Network request or alert in victim's browser; stolen session allows attacker login as victim.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[client-side]]
- [[hijacking]]
