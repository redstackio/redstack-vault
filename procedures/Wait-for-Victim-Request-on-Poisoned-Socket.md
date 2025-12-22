---
tags:
  - socket-poisoning
  - hijacking
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:34.493Z'
sub_techniques: []
id: 08c6c0ba-55e5-48b8-b9b1-03a768a461ce
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Wait-for-Victim-Request-on-Poisoned-Socket

## Summary

This passive procedure waits for a legitimate victim request to interact with the poisoned backend socket, causing the smuggled payload to execute and trigger a redirect with cookies.

## Description

Following payload sending, the desynchronized socket causes the backend to treat the smuggled GET as part of the victim's request, prompting slackb.com to redirect to the collaborator URL and include session cookies. No tools needed beyond prior setup; outcome is automatic hijacking upon victim traffic.

## Requirements

1. Poisoned socket from prior step
2. Active victim traffic to target
3. Monitoring in place

## Defense

Defensive measures and detection strategies:

- Reset connections after suspicious requests
- Use per-request socket handling
- Detect unexpected redirects in backend logs

## Objectives

1. Hijack incoming victim request
2. Force cookie-leaking redirect
3. Enable data capture

## Instructions

### Step 1: Monitor Socket State

**Context**: Passively observe for desync effects.

No command; wait for natural victim requests to hit the shared backend.

> The backend prepends the smuggled GET, altering the request to GET <collaborator_URL>, resulting in 301 with cookies.

### Step 2: Confirm Hijack

**Context**: Verify via downstream effects.

Check collaborator or logs for incoming redirect.

> Success if redirect includes victim details.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- desync
- redirect
