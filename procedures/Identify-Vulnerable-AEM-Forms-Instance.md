---
tags:
  - xxe
  - aem
  - recon
type: procedure
tools:
  - '[[tools/Curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-scan-for-aem-endpoint]]'
platforms:
  - Web
  - Cloud
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 52b9040f-dcce-463c-aeb9-bed84748e19d
created_at: '2025-12-13T09:00:27.617Z'
updated_at: '2025-12-13T09:00:27.617Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable AEM Forms Instance

## Summary

This procedure involves scanning and identifying vulnerable instances of Adobe Experience Manager (AEM) Forms that are susceptible to XXE injection, focusing on Cloud Service and versions 6.5.10.0 and below.

## Description

The procedure targets web-based AEM Forms deployments to confirm vulnerability presence. It uses HTTP requests to probe endpoints, checking for AEM-specific indicators. This is a reconnaissance step to ensure the target is exploitable before attempting XXE injection for RCE. Expected outcomes include confirmation of the service and version.

## Requirements
1. Network access to the target domain or IP
2. Tool: Curl for sending HTTP requests
3. Knowledge of potential AEM endpoints (e.g., /forms)

## Defense

Defensive measures and detection strategies:
- Monitor for unusual HTTP requests to AEM endpoints
- Implement web application firewalls (WAF) to block suspicious User-Agent strings or probes

## Objectives
1. Confirm presence of AEM Forms
2. Verify vulnerable version
3. Prepare for exploitation

## Instructions

### Step 1: Probe for AEM Endpoint

**Context**: Send a HEAD request to check for AEM Forms presence.

**Command** ([[commands/curl-scan-for-aem-endpoint]]):
```bash
curl -I https://target.example.com/forms -A "Mozilla/5.0"
```

> This command checks response headers for AEM indicators without downloading full content.

### Step 2: Verify Version

**Context**: If possible, access metadata or banners to confirm version <= 6.5.10.0.

**Command** ([[commands/curl-scan-for-aem-endpoint]]):
```bash
curl https://target.example.com/forms/metadata -A "Mozilla/5.0"
```

> Look for version information in the response body.

## MITRE ATT&CK Mapping

### Tactics
- [[Initial Access]]

### Techniques
- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used
- [[commands/curl-scan-for-aem-endpoint]]

## Tools Used
- [[tools/Curl]]

## Tags
- [[xxe]]
- [[aem]]
- [[recon]]
