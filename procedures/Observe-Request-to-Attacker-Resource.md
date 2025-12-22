---
tags:
  - xxe
  - blind-xxe
  - dos
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 0cdb0f7f-d5b1-424e-acc9-85705b588485
created_at: '2025-12-13T09:00:33.801Z'
updated_at: '2025-12-13T09:00:33.801Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe Request to Attacker Resource

## Summary

This procedure confirms the success of the blind XXE by monitoring requests to the attacker-controlled resource referenced in the XML entity.

## Description

After triggering the XXE, the DuckDuckGo server requests the entity URL, which can be logged for verification. This demonstrates DoS potential and blind injection.

## Requirements

1. Server logging enabled
2. Prior steps completed
3. Monitoring tools for requests

## Defense

Defensive measures and detection strategies:

- Block external entity inclusions
- Monitor for unexpected outbound traffic

## Objectives

1. Verify entity expansion
2. Log incoming requests
3. Confirm vulnerability exploitation

## Instructions

### Step 1: Monitor Server Logs

**Context**: Check for requests from DuckDuckGo.

Monitor access logs for GET requests to /Blind_xxe.

> Look for IP addresses associated with DuckDuckGo.

### Step 2: Validate Impact

**Context**: Assess DoS or injection success.

If requests are observed, the blind XXE is confirmed.

> Multiple triggers could amplify DoS effects.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[xxe]]
- [[blind-xxe]]
- [[dos]]
