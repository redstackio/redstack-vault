---
tags:
  - xss
  - url-crafting
  - payload-injection
type: procedure
tools:
  - '[[tools/Firefox-Browser]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 3aa7de53-4739-40ad-abc2-26840aea287a
created_at: '2025-12-13T23:52:49.406Z'
updated_at: '2025-12-13T23:52:49.406Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-URL-for-Slack-Emoji-XSS

## Summary

This procedure involves constructing a malicious URL targeting the reflected XSS vulnerability in Slack's custom emoji page, where the 'name' parameter is injected into a flash message without sanitization, allowing JavaScript execution in teams with many emojis.

## Description

The vulnerability occurs because the 'name' parameter in `/customize/emoji?added=1&name=` is reflected into the message 'Here's what it looks like :name: in a sentence.' In large teams (e.g., 1600+ emojis), existence checks are skipped for performance, enabling breakout from the emoji syntax with payloads like `"><script>alert(0);</script>`. This procedure focuses on crafting and testing such URLs for reliable exploitation.

## Requirements

1. Knowledge of target Slack team name (guessable, e.g., company.slack.com)
2. Browser without XSS protections (e.g., Firefox)
3. Internet access to Slack

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to block inline scripts
- Sanitize all reflected parameters server-side
- Enable browser XSS auditors (e.g., in Chrome)

## Objectives

1. Create a functional XSS payload URL
2. Verify execution in a test environment
3. Prepare for delivery to victims

## Instructions

### Step 1: Identify Target Team

**Context**: Select or guess a Slack workspace URL, as team names are often predictable based on company names.

No command required; manually construct base URL: `https://{team}.slack.com/customize/emoji`.

> Expected: Valid Slack workspace accessible.

### Step 2: Build Payload

**Context**: Append query parameters to inject the payload, breaking out of the colon-delimited emoji syntax.

Manually craft: `?added=1&name=vuln"><script>alert(0);</script>`.

> Full URL example: `https://exampleteam.slack.com/customize/emoji?added=1&name=vuln%22%3E%3Cscript%3Ealert(0)%3B%3C/script%3E`. URL-encode the payload for transmission.

### Step 3: Test in Browser

**Context**: Visit the URL in a compatible browser to confirm reflection and execution.

Use [[tools/Firefox-Browser]] to load the URL.

> Expected: Alert dialog pops up, confirming XSS trigger in the flash message.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox-Browser]]

## Tags

- [[xss]]
- [[payload-injection]]
