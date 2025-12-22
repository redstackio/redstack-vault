---
id: proc-exness-squid-disclosure
tags:
  - ssrf
  - information-disclosure
  - rebinding
type: procedure
tools:
  - '[[tools/localtest-me]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/get-check-localtest-me]]'
verified: false
platforms:
  - Web
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T03:46:14.639Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---
# Disclose-Squid-Proxy-Details-via-Local-Rebinding

## Summary

This procedure leverages localhost rebinding with localtest.me to force SSRF requests through the Squid proxy, leaking version, pod name, and generation details in error responses.

## Description

The backend routes SSRF via Squid/5.6 in a Kubernetes pod; rebinding exposes proxy headers. Targets proxied SSRF setups, disclosing infrastructure without direct access.

## Requirements

1. SSRF access
2. localtest.me for rebinding
3. curl

## Defense

Defensive measures and detection strategies:

- Isolate proxy from user-facing errors
- Sanitize error messages to remove versions/pod names
- Block rebinding domains in DNS filters

## Objectives

1. Leak Squid version and pod info
2. Fingerprint proxy configuration
3. Identify Kubernetes deployment

## Instructions

### Step 1: Initiate Rebinding Request

**Context**: Use localtest.me to rebind to localhost:80, triggering proxy error.

**Command** ([[commands/get-check-localtest-me]]):

```bash
curl -X GET "https://my.exnessaffiliates.com/api/partner_integrations/template/check/?url=http://localtest.me:80"
```

> Error includes 'Generated ... by partner-integrations-squid-6b99c4777d-vwkcn (squid/5.6)'.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Information Repositories]] Data from Information Repositories

### Sub-Techniques


## Commands Used

- [[commands/get-check-localtest-me]]

## Tools Used

- [[tools/localtest-me]]

## Tags

- ssrf
- information-disclosure
- rebinding
- squid
