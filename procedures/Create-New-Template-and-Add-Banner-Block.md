---
tags:
  - xss
  - web
  - template-creation
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
updated_at: '2025-12-13T23:52:24.139Z'
sub_techniques: []
id: 229aa14d-54f5-4f73-abf1-b728a2046142
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Create-New-Template-and-Add-Banner-Block

## Summary

This procedure outlines the initial setup in Stripo's email template editor by creating a new template and adding a banner block, establishing the foundation for injecting a stored XSS payload into the description field.

## Description

In the context of exploiting a stored XSS vulnerability in Stripo Inc's web-based email template editor, this step involves accessing the authenticated user interface to create a blank template and inserting a banner block component. The banner block includes a description field that lacks proper sanitization, making it vulnerable to malicious input storage. This procedure requires an active user session and is typically performed in a modern web browser. Expected outcomes include a ready template canvas with the banner block positioned for further manipulation.

## Requirements

1. Authenticated access to Stripo email template editor
2. Web browser with JavaScript enabled
3. No special permissions beyond standard user account

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls to limit template creation to trusted users
- Monitor for unusual template modifications via audit logs
- Use client-side validation to flag suspicious inputs during block addition

## Objectives

1. Establish a new email template for payload injection
2. Position a vulnerable banner block component
3. Prepare the environment for XSS exploitation without triggering alerts

## Instructions

### Step 1: Log In and Access Template Creation

**Context**: Authenticate to the platform and navigate to the template builder to start a new project.

Open your web browser and navigate to the Stripo login page. Enter credentials to access the dashboard, then click on "Create New Template" to open the editor interface.

> Upon successful login, the dashboard loads, and the new template canvas appears empty.

### Step 2: Add Banner Block to Template

**Context**: Insert the banner block, which contains the exploitable description field.

In the template editor sidebar, locate the "Blocks" section, search for or select the "Banner" block type, and drag it onto the canvas. Position it as needed.

> The banner block renders on the canvas with editable fields, including the description area ready for input.

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
- [[web]]
- [[template-creation]]
