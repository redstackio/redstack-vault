---
tags:
  - verification
  - oob-interaction
type: procedure
tools:
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: bf7607be-5a36-41b4-bf69-39d817ae9cb1
created_at: '2025-12-13T09:01:17.701Z'
updated_at: '2025-12-13T09:01:17.701Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Monitor Burp Collaborator for Redirects

## Summary

This procedure monitors Burp Collaborator for out-of-band interactions to confirm successful HTTP Request Smuggling and arbitrary redirects.

## Description

After executing the attack, check for incoming HTTP requests to the Collaborator domain, verifying that the smuggled request caused redirects to the malicious Host.

## Requirements

1. Burp Collaborator client running
2. Unique subdomain in payload
3. Post-attack monitoring time

## Defense

Defensive measures and detection strategies:

- Restrict outbound connections from servers
- Monitor DNS and HTTP logs for unknown domains

## Objectives

1. Confirm exploitation via OOB requests
2. Validate redirect impact
3. Document proof of concept

## Instructions

### Step 1: Open Collaborator Client

**Context**: Access the Burp Collaborator interface.

> Navigate to the Collaborator tab in Burp Suite.

### Step 2: Check for Interactions

**Context**: Look for polled interactions matching the attack time.

> Filter by domain and request type.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Collaborator]]

## Tags

- [[verification]]
- [[oob-interaction]]
