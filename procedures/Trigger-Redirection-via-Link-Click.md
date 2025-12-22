---
tags:
  - open-redirect
  - user-interaction
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-open-redirect]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: e81734d9-3863-44bb-9008-a33e56d45e23
created_at: '2025-12-13T09:01:26.456Z'
updated_at: '2025-12-13T09:01:26.456Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger Redirection via Link Click

## Summary

This procedure simulates user interaction by clicking a crafted link to trigger the open redirection vulnerability in the SSO-SAML endpoint.

## Description

After inserting the crafted URL, clicking it initiates the redirection. The double slash bypasses the warning, leading directly to the external site. This step is critical for demonstrating the exploit in a web environment with SSO-SAML. Expected outcome is successful redirection without alerts.

## Requirements

1. Access to the platform where the link was inserted
2. Web browser or HTTP client
3. The crafted link must be present

## Defense

Defensive measures and detection strategies:

- Add client-side checks for external redirects
- Log and alert on unexpected redirection patterns

## Objectives

1. Initiate the redirection through user action
2. Bypass the external link warning
3. Confirm exploit functionality

## Instructions

### Step 1: Locate and Click the Link

**Context**: Find the inserted link and click it to trigger.

**Command** ([[commands/curl-test-open-redirect]]):
```bash
curl -L 'https://hackerone.com/users//saml/sign_in?email=teste@snapchat.com&remember_me=true'
```

> This command follows the redirect to simulate the click.

### Step 2: Monitor Redirection Path

**Context**: Observe the browser or tool following the link.

> Expected: Redirection occurs immediately without warnings.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-test-open-redirect]]

## Tools Used



## Tags

- [[open-redirect]]
- [[user-interaction]]
