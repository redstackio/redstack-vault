---
tags:
  - dom-xss
  - privilege-escalation
  - parameter-tampering
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:32:58.226Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 39ec62f3-0d95-49b9-be6b-333540fb2323
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Privilege-Escalation-to-Admin-via-CSS-and-Array-Injection

## Summary

This procedure logs in as staff, injects CSS classes into the profile to set up hash-based auto-clicks, and uses array parameter tampering to load multiple templates, triggering JavaScript for admin upgrade.

## Description

Staff login at https://staff.bountypay.h1ctf.com/. JS in /js/website.js auto-clicks on location hash. Inject 'upgradeToAdmin tab2' class into avatar. Tamper ?template[] to load login and ticket templates with username and #tab2, reported to admins to execute JS upgrade.

## Requirements

1. Staff credentials
2. Browser dev tools or Burp for manipulation
3. Access to report ticket feature

## Defense

- Sanitize CSS classes in profile fields
- Validate array parameters in PHP to prevent multiple loads
- Avoid client-side privilege changes; use server-side auth

## Objectives

1. Prepare DOM for auto-execution
2. Inject parameters for template chaining
3. Trigger admin escalation

## Instructions

### Step 1: Staff Login and JS Inspection

**Context**: Login and review JS for auto-click behavior.

Login at https://staff.bountypay.h1ctf.com/ with sandra.allison creds. Inspect /js/website.js.

> Reveals hash-based clicks.

### Step 2: CSS Class Injection

**Context**: Update profile to inject class.

Use dev tools to set avatar class='upgradeToAdmin tab2'.

> Sets up for hash trigger.

### Step 3: Array Parameter Tampering

**Context**: Manipulate URL to load templates and trigger.

Construct ?template[]=login&template[]=ticket&ticket_id=3582&username=sandra.allison#tab2 on staff subdomain. Report ticket to admins with this URL.

> JS executes upgrade on admin view.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

- None

## Commands Used

None

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[dom-xss]]
- [[privilege-escalation]]
- [[parameter-tampering]]
