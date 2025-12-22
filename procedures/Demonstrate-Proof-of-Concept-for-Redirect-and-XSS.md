---
id: proc-adobe-poc-demo
tags:
  - proof-of-concept
  - validation
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:15:52.940Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Demonstrate Proof-of-Concept for Redirect and XSS

## Summary

This procedure captures video evidence of the open redirect and reflected XSS exploits in the return_url parameter to validate the vulnerabilities and illustrate their impact for reporting or escalation.

## Description

Following identification and testing, record the full attack flow: victim receives crafted URL, authenticates, and triggers redirect to a fake site or XSS payload for session theft. Videos from the Adobe Youth Voices site demonstrate real-world execution, confirming lack of validation. This step aids in bug bounty submissions or internal assessments.

## Requirements

1. Screen recording software (e.g., OBS Studio).
2. Completed prior testing steps.
3. Controlled environment to avoid real harm.

## Defense

Defensive measures and detection strategies:

- Review PoC submissions in bug bounty programs promptly.
- Audit video-based reports for validation.
- Enhance logging to trace exploit attempts.

## Objectives

1. Visually confirm exploit triggers.
2. Document for impact assessment.
3. Support remediation efforts.

## Instructions

### Step 1: Record Open Redirect Flow

**Context**: Capture the phishing redirect in action.

Start recording, access http://youthvoices.adobe.com/community?return_url=//www.attacker.com/phish, log in, and show redirect to fake site.

> Expected: Video shows seamless external navigation post-auth.

### Step 2: Record XSS Execution

**Context**: Demonstrate script injection and data theft.

Record access to http://youthvoices.adobe.com/community?return_url=javascript:alert(document.cookie), authenticate, and capture alert with session data.

> Expected: Video evidences JavaScript execution and cookie exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[proof-of-concept]]
- [[validation]]
