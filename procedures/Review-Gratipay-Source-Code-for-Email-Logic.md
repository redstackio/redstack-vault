---
id: proc-gratipay-code-review
tags:
  - recon
  - source-code-review
  - gratipay
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:32:57.828Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Review-Gratipay-Source-Code-for-Email-Logic

## Summary

This procedure involves analyzing the open-source code of Gratipay to identify business logic flaws in the email addition feature, specifically the lack of whitespace trimming in uniqueness checks.

## Description

In the context of vulnerability research on web applications like Gratipay (a Python-based platform), reviewing source code on GitHub reveals flaws such as improper handling of URL-encoded spaces in email parameters. This allows planning exploits where appended %20 evades database checks but is ignored during email sending, enabling duplicate email additions across accounts. Prerequisites include basic Python knowledge and access to the repository.

## Requirements

1. Internet access to GitHub
2. Text editor or browser for code review
3. Understanding of Python and web application logic

## Defense

Defensive measures and detection strategies:

- Implement code reviews and static analysis tools like Bandit for Python apps
- Monitor GitHub repository access logs for suspicious patterns
- Enforce input validation and trimming in all user-submitted fields

## Objectives

1. Identify the email uniqueness check flaw at line 123 in email.py
2. Confirm lack of URL-decoding or trimming
3. Plan bypass using %20 appended to emails

## Instructions

### Step 1: Access Repository

**Context**: Locate and clone or browse the Gratipay source code to examine relevant files.

Navigate to the Gratipay GitHub repository and search for the models/participant/email.py file.

### Step 2: Analyze Key Lines

**Context**: Focus on the uniqueness check and email sending logic to spot the vulnerability.

Examine line 123 for the database existence check, which compares emails without trimming. Check line 131 for email sending, which normalizes the address by ignoring trailing spaces.

### Step 3: Document Flaw

**Context**: Note how %20 (URL-encoded space) allows bypass since it's treated differently in checks vs. sending.

Record that line 314 updates the primary email without re-verification, enabling duplicates.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- recon
- source-code
- python
