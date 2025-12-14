---
id: proc-verify-multi-domain-uber
tags:
  - open-redirect
  - multi-domain-test
  - uber
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-multi-domain-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Phishing]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:26.904Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Redirect-on-Multiple-Domains

## Summary

This procedure confirms the open redirection vulnerability works across various external domains like HackerOne, Facebook, and Yahoo by testing similar URL patterns on Uber.com.

## Description

After initial success, broaden testing to urls like https://www.uber.com//hackerone.com/rohk to ensure consistency. This validates the root cause (improper path validation) for widespread phishing use. Web-only; no special access required.

## Requirements

1. List of target domains/IPs
2. Curl or browser
3. Logging for response comparison

## Defense

Defensive measures and detection strategies:

- Path normalization to strip double slashes globally
- Rate-limit suspicious URL accesses
- Audit redirects in server logs for external hosts

## Objectives

1. Confirm exploit reliability across sites
2. Assess broader impact potential
3. Collect evidence for vulnerability report

## Instructions

### Step 1: Test Additional Domains

**Context**: Replace target with other sites to check universal applicability.

**Command** ([[commands/curl-multi-domain-test]]):
```bash
curl -L -I "https://www.uber.com//hackerone.com/rohk"
```

> Expects successful redirect to HackerOne, similar for Facebook.com and Yahoo.com.

### Step 2: Document Responses

**Context**: Note any variations in behavior.

Manually test in browser and log outcomes.

> All should redirect without errors, confirming the vuln.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Phishing]] Phishing
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-multi-domain-test]]

## Tools Used


## Tags

- open-redirect
- multi-domain-test
