---
tags:
  - template-injection
  - ssrf
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:57.967Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 85b3fadb-97ad-46ed-a2ed-48bbd044b763
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Escalate Privileges via Template Injection

## Summary

Inject PHP array parameters to chain templates, tricking admin into upgrading staff to admin via reported URL.

## Description

On staff.bountypay.h1ctf.com, use ?template[]=login&username=sandra.allison&template[]=ticket&ticket_id=3582#tab1 to inject, base64 encode malicious URL for /admin/report to trigger /admin/upgrade?username=sandra.allison.

## Requirements

1. Staff login
2. Base64 encoder
3. Access to report function

## Defense

Defensive measures: Sanitize array params, restrict template chaining; Detection: Validate report URLs, log injections.

## Objectives

1. Chain templates
2. Trigger admin action
3. Expected outcome: Admin privileges

## Instructions

### Step 1: Inject Template Chain

**Context**: Modify URL params.

Navigate to staff.bountypay.h1ctf.com?template[]=login&username=sandra.allison&template[]=ticket&ticket_id=3582#tab1.

> Expected output: Injected username in ticket.

### Step 2: Report Malicious URL

**Context**: Trick admin.

Base64 encode /admin/upgrade?username=sandra.allison, submit to /admin/report.

> Expected output: Admin upgrade executed.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used


## Tools Used


## Tags

- template-injection
- ssrf
