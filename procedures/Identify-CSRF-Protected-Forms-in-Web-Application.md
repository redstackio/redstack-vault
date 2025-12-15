---
tags:
  - csrf
  - recon
  - web
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
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:36.115Z'
sub_techniques: []
id: 35a72696-cdd9-4463-a8df-94545cc70b21
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-CSRF-Protected-Forms-in-Web-Application

## Summary

This procedure involves inspecting web application forms to detect CSRF protection mechanisms, such as token fields, in features like messaging on sites like Reverb.com.

## Description

In the context of testing Reverb.com's sandbox environment, this step focuses on the reply message and send message features. By examining the form HTML, attackers can confirm the use of CSRF tokens for validation. This reconnaissance is crucial for identifying potential bypass opportunities in web applications where token enforcement might be weak.

## Requirements

1. Access to the target web application with an authenticated session.
2. Browser with developer tools enabled or a web proxy tool.
3. Basic knowledge of HTML form inspection.

## Defense

Defensive measures and detection strategies:

- Implement strict CSRF token validation on all state-changing forms.
- Monitor for anomalous form submissions lacking tokens via web application firewall (WAF).

## Objectives

1. Confirm presence of CSRF tokens in target forms.
2. Map protected endpoints for messaging actions.
3. Prepare for validation testing.

## Instructions

### Step 1: Navigate to Target Features

**Context**: Access the messaging interface to load the relevant forms.

Log in to the Reverb.com sandbox and go to the reply or send message sections.

### Step 2: Inspect Form Elements

**Context**: Use developer tools to examine the form structure for CSRF tokens.

Right-click on the form and select "Inspect Element". Look for input fields with names like `csrf_token` or `_token` hidden within the form.

> Expected output: Visible CSRF token field in the HTML source, confirming protection is in place.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web-recon]]
