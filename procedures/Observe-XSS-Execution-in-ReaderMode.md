---
tags:
  - xss-execution
  - data-theft
  - uuidkey
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - iOS
  - WebView
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.811Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 2d3e7a6f-aad9-4d1c-877e-7145036d9482
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Observe-XSS-Execution-in-ReaderMode

## Summary

This procedure confirms the success of the XSS by observing the execution of the injected JavaScript on the ReaderMode localhost page, capturing sensitive details like the uuidkey for further exploitation.

## Description

Once ReaderMode is active, the script with the valid nonce executes in the context of http://localhost:6571, bypassing same-origin restrictions. This allows arbitrary JS, such as alerting document.location to reveal the full URL with uuidkey, or more advanced payloads for stealing cross-origin content via iframes or accessing Brave's internal privileged pages. The impact includes potential data exfiltration and unauthorized access.

## Requirements

1. ReaderMode activated on malicious page
2. Payload designed to execute visibly (e.g., alert)
3. Ability to interact with the iOS device

## Defense

Defensive measures and detection strategies:

- Implement strict HTML escaping in all template placeholders
- Revoke or monitor uuidkey usage in ReaderMode URLs
- Use WebView sandboxing to limit localhost access

## Objectives

1. Verify script execution via observable effects
2. Capture uuidkey for privilege escalation
3. Demonstrate potential for data theft

## Instructions

### Step 1: Monitor for Execution

**Context**: Watch for immediate JS effects post-activation.

Upon ReaderMode load, observe for pop-ups or console errors.

> The alert(document.location) should display the localhost URL, confirming execution.

### Step 2: Capture Output

**Context**: Extract sensitive information from the execution.

Note the uuidkey from the alert or extend the payload to exfiltrate data (e.g., via fetch to attacker server).

> Successful capture enables access to http://localhost:6571 with the key for further attacks.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-execution
- data-theft
- uuidkey
