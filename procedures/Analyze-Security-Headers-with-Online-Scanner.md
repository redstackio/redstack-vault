---
tags:
  - reconnaissance
  - web
  - security-headers
  - scanning
type: procedure
tools:
  - '[[tools/securityheaders-io]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
techniques:
  - '[[Active Scanning]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: ee79f75d-ab65-4c42-9a10-810f21434fe5
created_at: '2025-12-14T03:16:20.580Z'
updated_at: '2025-12-14T03:16:20.580Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Analyze-Security-Headers-with-Online-Scanner

## Summary

This procedure uses an online scanning tool to automatically analyze a website's HTTP security headers, identifying misconfigurations such as the incorrect 'DENY' value in X-XSS-Protection that fails to enable proper XSS protection.

## Description

Online header scanners provide a quick, no-install method to evaluate web application security postures by simulating browser requests and grading headers against best practices. For https://www.sfl-tap.army.mil/, the scan reveals the X-XSS-Protection header mis-set to 'DENY' (intended for X-Frame-Options), resulting in no effective XSS filtering and a low-severity vulnerability. The tool suggests remediation to '1; mode=block' to activate blocking mode. This is ideal for initial reconnaissance in bug bounty programs or compliance audits, requiring only a web browser and the target URL.

## Requirements

1. Web browser with internet access
2. Publicly accessible target URL
3. No credentials or special permissions needed

## Defense

Defensive measures and detection strategies:

- Block or rate-limit requests to scanning services from unknown IPs
- Use Content Security Policy (CSP) headers as a stronger alternative to X-XSS-Protection
- Monitor server logs for patterns matching known scanner user-agents

## Objectives

1. Submit target URL to an automated header scanner
2. Receive detailed report on misconfigurations and severity
3. Validate findings for XSS-related risks

## Instructions

### Step 1: Access the Scanning Tool

**Context**: Navigate to the securityheaders.io website to initiate the scan interface.

**Command** (Browser-based; no CLI):

> Open https://securityheaders.com/ in a browser and enter the target URL in the scan field.

### Step 2: Submit and Review Scan Results

**Context**: Run the scan and analyze the output for X-XSS-Protection issues, noting recommendations and overall security score.

**Command** (Browser-based):

> Click 'Scan' and wait for results. Expected output includes a grade (e.g., C or lower) and specifics: "X-XSS-Protection header is set to 'DENY', which is invalid; use '1; mode=block' instead."

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/securityheaders-io]]

## Tags

- [[Reconnaissance]]
- [[web]]
- [[security-headers]]
- [[scanning]]
