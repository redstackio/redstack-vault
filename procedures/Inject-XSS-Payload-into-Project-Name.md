---
id: proc-uuid-2
name: Inject XSS Payload into Project Name
tags:
  - xss
  - injection
  - weblate
type: procedure
tools:
  - '[[tools/Docker]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:37.347Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload into Project Name

## Summary

This procedure exploits the lack of input validation in Weblate's project name field by injecting a stored XSS payload, which is persisted in the database and rendered unsanitized on user profile pages.

## Description

Weblate's project settings allow authorized users to edit the project name via the Manage -> Settings interface. Due to insufficient sanitization in the Django backend, HTML and JavaScript payloads like <svg/onload=alert(document.domain)> are stored and executed when the project name is displayed on the /accounts/profile/ page for any user. This affects all users, including admins and public viewers, enabling session hijacking, data theft, or further attacks. Testing requires a local Docker instance from Weblate's GitHub repo.

## Requirements

1. User account with project management permissions
2. Access to the project's settings page
3. Running Weblate instance
4. Basic knowledge of XSS payloads

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs in project metadata using HTML escaping (e.g., Django's mark_safe)
- Implement Content Security Policy (CSP) to block inline scripts
- Log and alert on suspicious changes to project names containing script tags

## Objectives

1. Store malicious payload in project name
2. Ensure payload persists without detection
3. Prepare for execution on victim pages

## Instructions

### Step 1: Navigate to Watched Projects

**Context**: Log in as the authorized user and access the list of projects they can manage.

Go to the watched projects dashboard in Weblate.

> Select the target project from the list.

### Step 2: Access Project Settings

**Context**: Enter the management interface to edit project details.

Click 'Manage' -> 'Settings'.

> Locate the 'Project Name' field.

### Step 3: Inject and Save Payload

**Context**: Enter the XSS payload and submit to store it.

Input the payload `<svg/onload=alert(document.domain)>` into the Project Name field and click 'Save'.

> Verify no errors occur; the form should submit successfully, updating the project name.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Docker]]

## Tags

- xss
- injection
- weblate
