---
id: proc-access-concrete-cms-testimonial
tags:
  - xss
  - concrete-cms
  - web-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:35.459Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Concrete-CMS-Testimonial-Feature

## Summary

This procedure outlines how to navigate to the Testimonial Position feature in Concrete CMS, providing initial access to the vulnerable input field for further exploitation in a Stored XSS attack.

## Description

In the context of exploiting Stored XSS in Concrete CMS, this step involves logging into the admin interface and locating the testimonial management area. Concrete CMS, a PHP-based content management system, exposes user-editable fields without proper sanitization, allowing attackers with editor access to inject payloads. Prerequisites include valid login credentials; expected outcomes are reaching the editable form without triggering any access controls.

## Requirements

1. Valid admin or editor credentials for Concrete CMS.
2. Web browser with access to the target site's admin URL.
3. Network connectivity to the CMS instance.

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls (RBAC) to limit testimonial editing to trusted users.
- Monitor admin login attempts and unusual navigation patterns in CMS logs.

## Objectives

1. Gain access to the vulnerable Testimonial Position input field.
2. Prepare for payload injection without alerting defenses.
3. Confirm edit permissions on content elements.

## Instructions

### Step 1: Log In to Admin Dashboard

**Context**: Authenticate to the CMS to reach management interfaces.

Log in using provided credentials at the admin URL (e.g., /index.php/dashboard).

**Expected Output**: Successful login redirect to the dashboard.

### Step 2: Navigate to Testimonial Configuration

**Context**: Locate the specific feature containing the vulnerable field.

From the dashboard, go to 'Content & Theme' or 'Page Types', then select 'Testimonial Position' or similar block/element configuration.

**Expected Output**: The editing form for testimonials loads, showing input fields.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[concrete-cms]]
