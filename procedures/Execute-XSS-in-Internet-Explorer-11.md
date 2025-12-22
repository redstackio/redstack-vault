---
tags:
  - xss
  - execution
  - ie11
  - csp-bypass
type: procedure
tools:
  - '[[tools/Internet-Explorer-11]]'
  - '[[tools/Inspect-Element]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.105Z'
sub_techniques: []
id: 78e4717d-fa52-496a-9a89-59e2fe2c8e56
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute-XSS-in-Internet-Explorer-11

## Summary

This procedure triggers the stored XSS by viewing the profile in Internet Explorer 11, where the lack of CSP enforcement allows the payload to execute, demonstrating the vulnerability's impact.

## Description

Modern browsers block the inline script due to CSP, but IE11 does not support or enforce it, allowing the Twig-rendered payload to run. Use developer tools to inspect the DOM and confirm unsanitized output. Impact is primarily self-XSS, but could facilitate phishing or takeover if combined with account access.

## Requirements

1. Payload stored from previous steps
2. Internet Explorer 11 installed and accessible
3. Target page reloaded in the vulnerable browser

## Defense

Defensive measures and detection strategies:

- Deploy CSP headers with 'script-src' restrictions
- Encourage browser updates and deprecate IE11 usage
- Monitor for JavaScript errors or alerts in client logs

## Objectives

1. Render the profile to execute the stored script
2. Verify execution only in vulnerable environments
3. Assess potential for data exfiltration or takeover

## Instructions

### Step 1: Switch to IE11

**Context**: Use the legacy browser to bypass CSP.

Open Internet Explorer 11 and navigate to https://bridge.cspr.ng/my/account.

> The page loads with the profile, including the display name.

### Step 2: Trigger and Inspect

**Context**: Observe execution and verify in DOM.

Use [[tools/Inspect-Element]] (F12) to check the display name element; the alert should pop up.

> Alert 'xss' executes; DOM shows unescaped <script> tag.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Internet-Explorer-11]]
- [[tools/Inspect-Element]]

## Tags

- xss
- execution
- browser-exploit
