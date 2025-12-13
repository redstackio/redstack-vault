---
tags:
  - xxe
  - ssrf
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands: []
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7c2ebf08-7700-4242-ab9f-865a90a0e39d
created_at: '2025-12-13T09:00:28.007Z'
updated_at: '2025-12-13T09:00:28.007Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger XXE for SSRF

## Summary

This procedure triggers an XML External Entity (XXE) vulnerability via a magic method on an injected object to perform Server-Side Request Forgery (SSRF) and access internal services.

## Description

By visiting /memes.php, the session array is echoed, invoking __toString() on the ConfigFile object, which calls parse() with malicious XML. This resolves external entities to internal URLs like http://localhost:1337/status, enabling SSRF.

## Requirements

1. Injected object in session
2. Access to /memes.php
3. Knowledge of internal service endpoints

## Defense

Defensive measures and detection strategies:

- Disable external entity resolution in XML parsers
- Monitor for anomalous internal requests in logs

## Objectives

1. Trigger XXE via magic method
2. Perform SSRF to internal ports
3. Probe for further vulnerabilities

## Instructions

### Step 1: Invoke Magic Method

**Context**: Load the page to trigger __toString().

Visit the URL:

```bash
curl http://target/memes.php
```

> This parses the malicious XML and performs SSRF.

### Step 2: Probe Internal Service

**Context**: Use SSRF to interact with endpoints.

Embed different URLs in the XXE payload and repeat to access /status and /update-status.

> Retrieve responses to identify pickle vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[xxe]]
- [[ssrf]]
