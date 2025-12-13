---
tags:
  - monitoring
  - verification
type: procedure
tools:
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 4cc8748c-d9aa-40c1-a563-d86e7f882c47
created_at: '2025-12-13T09:01:17.564Z'
updated_at: '2025-12-13T09:01:17.564Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe Smuggled Request Effects

## Summary

This procedure monitors the outcomes of smuggled requests using Burp Collaborator to detect redirects and interactions from the target.

## Description

After sending the smuggling payload, observe logs for evidence of successful exploitation, such as redirects to Collaborator domains. This confirms the vulnerability in a sandbox environment without full compromise.

## Requirements

1. Burp Collaborator configured with a custom domain
2. Prior smuggling payload sent
3. Access to Burp Suite interface

## Defense

Defensive measures and detection strategies:

- Monitor outbound requests to unknown domains
- Implement rate limiting on suspicious paths

## Objectives

1. Log interactions from smuggled requests
2. Confirm redirect behavior
3. Validate exploitation success

## Instructions

### Step 1: Monitor Collaborator Logs

**Context**: Check for incoming requests indicating smuggling success.

> Open Burp Collaborator and review logs for HTTP or DNS interactions from the target, showing redirects to the specified domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Collaborator]]

## Tags

- [[monitoring]]
- [[verification]]
