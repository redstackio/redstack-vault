---
tags:
  - ssrf-detection
  - oob-interaction
type: procedure
tools:
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:55.203Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 4abb1212-d980-4a48-b22f-fe3c4cf6250a
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe-SSRF-Interaction

## Summary

This procedure monitors for out-of-band HTTP interactions to validate SSRF exploitation, confirming the server's unauthorized request to the attacker's controlled domain.

## Description

After injecting the URL, the procedure involves polling the monitoring service to capture details like request headers, IP source, and timing, providing evidence of the vulnerability and insights into the server's configuration.

## Requirements

1. Active Burp Collaborator session
2. Payload already injected
3. Knowledge of HTTP request analysis

## Defense

Defensive measures and detection strategies:

- Implement network segmentation to limit web server outbound access
- Use intrusion detection systems (IDS) to flag unusual DNS/HTTP patterns
- Regularly audit server logs for SSRF indicators

## Objectives

1. Capture proof of SSRF execution
2. Analyze interaction details for further reconnaissance
3. Validate vulnerability impact

## Instructions

### Step 1: Poll for Interactions

**Context**: Check the Collaborator client for incoming requests post-injection.

In Burp Suite, navigate to Collaborator and poll for new interactions.

> Look for HTTP GET/POST requests originating from the target's IP.

### Step 2: Analyze Request Data

**Context**: Review captured data to confirm SSRF and extract useful information.

Examine headers, user-agent, and any forwarded data in the interaction log.

> Successful analysis shows server-initiated contact, confirming exploitation.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Collaborator]]

## Tags

- [[ssrf-detection]]
- [[oob-interaction]]
