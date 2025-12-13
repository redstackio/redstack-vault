---
tags:
  - http-request-smuggling
  - xss
  - verification
type: procedure
tools:
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Adversary-in-the-Middle]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: fa801a17-531f-4d9c-9dee-2087f711dd29
created_at: '2025-12-13T09:01:22.501Z'
updated_at: '2025-12-13T09:01:22.501Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Observe Poisoned Request Interactions

## Summary

This procedure involves monitoring Burp Collaborator for interactions from poisoned requests and checking the target for reflections, confirming the success of the HTTP smuggling exploit.

## Description

After sending the desync request, observe responses for redirections to 404 pages and reflections of the attacker's domain in elements like script tags or links, verifying potential for stored XSS or cookie theft.

## Requirements

1. Burp Collaborator client running
2. Prior desync request sent
3. Access to target responses

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization
- Monitor outbound connections to unknown domains

## Objectives

1. Verify poisoning of victim requests
2. Confirm reflections and interactions
3. Assess impact like XSS or data theft

## Instructions

### Step 1: Check Burp Collaborator

**Context**: Poll Burp Collaborator for any DNS or HTTP interactions from the poisoned request.

> Look for logs showing requests to o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net.

### Step 2: Inspect Target Responses

**Context**: Examine subsequent requests to the target for poisoned elements.

> Check for 404 redirections and reflections in script tags, links, etc.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Adversary-in-the-Middle]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Collaborator]]

## Tags

- [[verification]]
- [[xss]]
