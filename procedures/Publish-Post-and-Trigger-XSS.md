---
tags:
  - xss
  - trigger
  - cookie-theft
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
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
id: 67a42338-159a-46b1-80c9-bfb38515d9d9
created_at: '2025-12-13T23:52:49.671Z'
updated_at: '2025-12-13T23:52:49.671Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Publish-Post-and-Trigger-XSS

## Summary

This procedure publishes the WordPress post containing the malicious poll and triggers the stored XSS payload through victim interaction, executing JavaScript to steal cookies or perform other browser-based attacks.

## Description

Once embedded, publishing the post makes it accessible. Victims viewing the post see the poll; interacting (e.g., hovering over the green-bordered answer) triggers the onmouseover event, alerting document cookies. This can be extended to exfiltrate data to an attacker-controlled server. The procedure assumes the post is shared via links or social media; outcomes include session hijacking if cookies are captured.

## Requirements

1. Draft post with embedded malicious poll
2. Victim access (simulated by attacker or real lure)
3. Browser with JavaScript enabled

## Defense

Defensive measures and detection strategies:

- Enable browser sandboxing and XSS filters (e.g., via extensions)
- Monitor for anomalous JavaScript alerts or network requests from embeds
- Use web application firewalls to block known XSS patterns in embeds

## Objectives

1. Publish the post to expose the payload to victims
2. Trigger JavaScript execution on interaction
3. Collect sensitive data like session cookies

## Instructions

### Step 1: Publish the Post

**Context**: Make the post live for viewing.

In the WordPress editor, click 'Publish' to make the post public.

### Step 2: View and Interact with Poll

**Context**: Simulate or lure victim to trigger the payload.

Open the published post URL in a browser, locate the embedded poll, and click 'View Results'. Then hover over the malicious answer (the one with green border).

### Step 3: Observe Execution

**Context**: Verify XSS trigger and potential data theft.

The onmouseover event fires, displaying an alert with document.cookie contents. In a real attack, replace alert with fetch to exfiltrate data.

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
- [[trigger]]
- [[cookie-theft]]
- [[Execution]]
