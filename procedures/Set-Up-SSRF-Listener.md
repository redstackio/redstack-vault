---
id: proc-setup-ssrf-listener
tags:
  - ssrf
  - listener
  - oob
type: procedure
tools:
  - '[[tools/interactsh]]'
  - '[[tools/Burp-Suite-Collaborator]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:08:46.021Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Set-Up-SSRF-Listener

## Summary

This procedure sets up an external listener server to detect blind SSRF callbacks by hosting a unique domain and monitoring for interactions from the target server, commonly used in out-of-band (OOB) testing for vulnerabilities like SSRF in web applications.

## Description

In a blind SSRF attack, the target server makes requests to an attacker-controlled URL without visible feedback. This procedure deploys tools like interact.sh or Burp Suite Collaborator to generate unique payloads (e.g., DNS or HTTP endpoints) and listen for callbacks, confirming exploitation. It targets environments with exposed web services like WordPress xmlrpc.php, where no direct response is returned but external interactions occur. Prerequisites include a VPS or local server for hosting the listener and basic networking knowledge.

## Requirements

1. VPS or local machine with public IP/DNS for hosting listener
2. Installed [[tools/interactsh]] or access to [[tools/Burp-Suite]]
3. Network access to generate and resolve unique domains

## Defense

Defensive measures and detection strategies:

- Implement outbound traffic filtering to block connections to unknown domains
- Monitor DNS queries and HTTP logs for anomalous external resolutions
- Disable unnecessary XML-RPC features in WordPress (e.g., pingbacks)

## Objectives

1. Establish a reliable OOB channel for blind vulnerability confirmation
2. Capture callback details like source IP and headers for further analysis
3. Validate SSRF without alerting the target

## Instructions

### Step 1: Install and Start interact.sh Server

**Context**: Deploy the interact.sh server to generate payloads and listen for interactions.

No specific command; follow tool installation. Run the server payload generator.

> Generate a unique payload URL like abc123.oast.fun and start polling for interactions.

### Step 2: Alternative - Use Burp Suite Collaborator

**Context**: Leverage Burp's built-in OOB tool for domain generation and monitoring.

No command; in Burp, navigate to Collaborator > Generate payload.

> Copy the generated URL (e.g., oast-xyz.burpcollaborator.net) for use in payloads. Poll the Collaborator client for callbacks.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/interactsh]]
- [[tools/Burp-Suite-Collaborator]]

## Tags

- [[ssrf]]
- [[oob]]
- [[listener]]
