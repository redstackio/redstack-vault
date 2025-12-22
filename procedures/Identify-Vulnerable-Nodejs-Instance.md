---
tags:
  - recon
  - nodejs
  - vulnerability-scanning
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/scan-for-nodejs-version]]'
platforms:
  - Node.js
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: f45895b3-9b62-4945-8d60-0c9825dda7a0
created_at: '2025-12-13T09:01:17.722Z'
updated_at: '2025-12-13T09:01:17.722Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable Node.js Instance

## Summary

This procedure involves scanning a target web service to determine if it is running Node.js v18.7.0 with the vulnerable llhttp parser, setting the stage for HTTP Request Smuggling exploitation.

## Description

The procedure targets web applications built on Node.js, probing HTTP responses for version information. It is useful in reconnaissance phases to identify exploitable instances of the llhttp parsing vulnerability, which mishandles headers not terminated with CRLF.

## Requirements

1. Network access to the target HTTP service
2. curl installed for sending probes
3. Basic knowledge of HTTP headers

## Defense

Defensive measures and detection strategies:

- Update Node.js to patched versions beyond v18.7.0
- Monitor for anomalous HTTP requests with non-standard header formats

## Objectives

1. Confirm Node.js version
2. Identify presence of llhttp parser
3. Assess vulnerability to smuggling

## Instructions

### Step 1: Probe Target Headers

**Context**: Send a HEAD request to extract server headers.

**Command** ([[commands/scan-for-nodejs-version]]):

```bash
curl -I http://target.com -A "TestAgent"
```

> This command fetches headers; look for 'Server' field indicating Node.js v18.7.0.

### Step 2: Verify Vulnerability

**Context**: Analyze response for confirmation.

**Command** ([[commands/scan-for-nodejs-version]]):

```bash
curl -v http://target.com
```

> Verbose mode helps inspect full response for parsing indicators.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/scan-for-nodejs-version]]

## Tools Used

- [[tools/curl]]

## Tags

- [[recon]]
- [[nodejs]]
