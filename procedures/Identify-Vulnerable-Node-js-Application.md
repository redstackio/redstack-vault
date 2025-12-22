---
tags:
  - recon
  - node-js
type: procedure
tools:
  - '[[tools/Curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-http-request]]'
platforms:
  - Web
  - Node.js
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: ada7cf16-0278-43d2-8f3f-c203cefe7544
created_at: '2025-12-13T09:01:17.294Z'
updated_at: '2025-12-13T09:01:17.294Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable Node.js Application

## Summary
This procedure involves scanning a web target to determine if it runs a vulnerable version of Node.js susceptible to CVE-2022-32215 HTTP Request Smuggling.

## Description
By probing HTTP headers and banners, identify Node.js presence and version. The vulnerability affects 14.x, 16.x, 18.x lines due to llhttp parser flaws in handling multi-line Transfer-Encoding.

## Requirements
1. Network access to the target URL
2. Curl installed
3. Basic knowledge of HTTP responses

## Defense
- Update Node.js to patched versions (llhttp v6.0.7 or v2.1.5)
- Monitor for anomalous multi-line headers in logs

## Objectives
1. Confirm Node.js usage
2. Verify vulnerable version
3. Prepare for exploitation

## Instructions

### Step 1: Probe Headers
**Context**: Send a HEAD request to retrieve server banners.

**Command** ([[commands/curl-http-request]]):
```bash
curl -I http://target.com
```

> This fetches headers; look for 'Server: Node.js' or similar.

### Step 2: Version Check
**Context**: If possible, access version info via endpoints.

**Command** ([[commands/curl-http-request]]):
```bash
curl http://target.com/version
```

> Check if response indicates vulnerable Node.js version.

## MITRE ATT&CK Mapping

### Tactics
- [[Initial Access]]

### Techniques
- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used
- [[commands/curl-http-request]]

## Tools Used
- [[tools/Curl]]

## Tags
- [[recon]]
- [[node-js]]
