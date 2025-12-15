---
tags:
  - reconnaissance
  - jenkins
  - exposure
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-check-jenkins-url]]'
platforms:
  - Web
techniques:
  - '[[Gather Victim Host Information]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 843a9b79-5f92-4a86-b4be-782c81a2a7f7
created_at: '2025-12-14T17:23:28.141Z'
updated_at: '2025-12-14T17:23:28.141Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Discover-Exposed-Jenkins-Instance

## Summary

This procedure involves guessing and verifying the accessibility of a Jenkins CI instance using predictable URL patterns, such as ci.domain.com, to identify publicly exposed servers without firewall protections.

## Description

In scenarios where organizations use standard naming conventions for CI/CD tools, attackers can enumerate potential Jenkins instances by trying common subdomains. This targets environments like ownCloud's ci.owncloud.com, which was linked from public GitHub pages and running on a public IP. The procedure confirms exposure by checking HTTP responses for Jenkins-specific indicators, enabling further exploitation without prior access.

## Requirements

1. Internet access to the target domain
2. Knowledge of the organization's domain and common CI naming (e.g., ci., build.)
3. HTTP client like curl for verification

## Defense

Defensive measures and detection strategies:

- Implement firewall rules to restrict Jenkins access to internal networks only
- Use non-predictable URLs or path obfuscation for CI instances
- Monitor access logs for anomalous probes to common CI paths

## Objectives

1. Identify exposed Jenkins servers
2. Confirm public accessibility without authentication
3. Map the attack surface for CI environments

## Instructions

### Step 1: Guess Potential URLs

**Context**: Based on the target domain, hypothesize CI URLs like http://ci.target.com or http://ci.target.org.

**Command** ([[commands/curl-check-jenkins-url]]):
```bash
curl -I http://ci.owncloud.com/
```

> This HEAD request checks for HTTP 200 and Jenkins headers (e.g., X-Jenkins: 1.0). Expected output includes server details confirming exposure.

### Step 2: Verify Jenkins Presence

**Context**: Inspect the response for Jenkins login page or API endpoints to confirm the service.

No specific command; parse the curl output for keywords like "Jenkins" or dashboard elements.

> Successful verification shows the instance is running and publicly reachable.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-check-jenkins-url]]

## Tools Used

- None

## Tags

- [[Reconnaissance]]
- [[jenkins]]
- [[exposure]]
