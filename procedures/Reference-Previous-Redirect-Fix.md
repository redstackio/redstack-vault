---
tags:
  - recon
  - vulnerability-research
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Vulnerability Scanning]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 56c2fc11-62ad-43aa-b01f-1554c08215e6
created_at: '2025-12-14T03:47:12.607Z'
updated_at: '2025-12-14T03:47:12.607Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Reference-Previous-Redirect-Fix

## Summary

This procedure involves reviewing prior vulnerability reports to understand fixes applied to a target endpoint, enabling identification of potential bypass opportunities in web applications like Semrush's redirect functionality.

## Description

In the context of security research, referencing previous reports (e.g., HackerOne #311330 marked as duplicate) reveals that the /redirect?url= endpoint was patched for URL validation. This step sets the stage for re-testing to find weaknesses, such as incomplete sanitization of javascript: schemes. Prerequisites include access to public bug bounty platforms and basic knowledge of web vulnerabilities. Expected outcomes: Awareness of the fix and targeted testing plan.

## Requirements

1. Access to HackerOne or similar platforms
2. Knowledge of the target application (Semrush)
3. Web browser for endpoint verification

## Defense

Defensive measures and detection strategies:

- Regularly review and triage duplicate reports to ensure comprehensive fixes
- Implement logging for endpoint access to detect research patterns
- Use WAF rules to block repeated probing of fixed endpoints

## Objectives

1. Understand the scope of previous fixes
2. Identify endpoints for bypass testing
3. Plan subsequent exploitation steps

## Instructions

### Step 1: Access Prior Report

**Context**: Locate and read the details of the previous vulnerability report to note the fix applied.

No command required; manually navigate to https://hackerone.com/reports/311330 and review the duplicate status and fix description for the redirection URL.

> Expected: Confirmation that basic javascript: payloads were blocked post-fix.

### Step 2: Verify Endpoint Status

**Context**: Confirm the target endpoint is live and accessible.

Visit https://www.semrush.com/redirect?url=https://example.com in a browser to ensure the redirect works for valid URLs.

> Expected: Successful redirect without errors, indicating the endpoint is operational.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[web-vuln]]
