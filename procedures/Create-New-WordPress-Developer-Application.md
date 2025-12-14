---
id: proc-wordpress-create-app-001
tags:
  - wordpress
  - app-creation
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:37.253Z'
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
# Create-New-WordPress-Developer-Application

## Summary

This procedure outlines the initial step to access the WordPress Developer platform's app creation form, setting the stage for injecting malicious payloads into application metadata fields.

## Description

In the context of exploiting stored XSS vulnerabilities, this procedure involves navigating to the developer dashboard and initiating a new application. It requires a valid WordPress.com account and targets the public-facing https://developer.wordpress.com/apps/ endpoint. Successful execution provides access to fields vulnerable to injection, with outcomes including the ability to store unsanitized content server-side.

## Requirements

1. Valid WordPress.com developer account
2. Web browser with session cookies for authentication
3. Internet access to developer.wordpress.com

## Defense

Defensive measures and detection strategies:

- Implement account access logging for developer portal
- Require CAPTCHA or additional verification for app creation
- Monitor for unusual app creation patterns from single IPs

## Objectives

1. Gain access to the app creation interface
2. Prepare for payload injection in subsequent steps
3. Establish a stored malicious app for reflection

## Instructions

### Step 1: Navigate to My Apps Page

**Context**: Access the developer dashboard to locate the app creation option.

No command required; manually visit https://developer.wordpress.com/apps/ in your browser and ensure you are logged in. Click on "Create New Application".

> This loads the form for entering app details. Expected output: A web form with fields for Name, Website URL, Redirect URL, and Description.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[wordpress]]
- [[app-creation]]
