---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - concrete-cms
  - dashboard-access
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:15:35.336Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Blog-Page-Configuration-in-Concrete-CMS

## Summary

This procedure outlines how to log in to the Concrete CMS administrative dashboard and navigate to the blog page tile settings, providing access to the vulnerable Custom Title Text field for further exploitation.

## Description

In Concrete CMS, administrative users can edit page elements like blog tiles through the dashboard. This step assumes authenticated access and focuses on reaching the configuration interface where the unsanitized input field is exposed. It sets the stage for injecting malicious payloads in a stored XSS attack scenario targeting the web-based CMS environment.

## Requirements

1. Valid administrative credentials for the Concrete CMS instance.
2. Web browser with JavaScript enabled for dashboard functionality.
3. Network access to the CMS server (typically over HTTPS on port 443).

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) to limit dashboard access to trusted admins.
- Monitor login attempts and dashboard navigation for anomalous admin activity using web application firewalls (WAF).

## Objectives

1. Authenticate and access the CMS dashboard.
2. Locate and open the blog page tile editing interface.
3. Identify the Custom Title Text field for payload injection.

## Instructions

### Step 1: Authenticate to Dashboard

**Context**: Log in to gain administrative privileges required for editing page tiles.

Open a web browser and navigate to the Concrete CMS login page (e.g., `/index.php/login`). Enter admin credentials and submit the form.

> Upon successful login, the dashboard homepage loads, confirming access.

### Step 2: Navigate to Blog Page Settings

**Context**: Reach the specific configuration for the blog page tile to expose the vulnerable input field.

From the dashboard, go to "Pages & Themes" > Select the blog page > Edit the page layout > Click on the blog tile to open its settings. Locate the "Custom Title Text" field.

> The tile editing form appears, ready for input modifications.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[concrete-cms]]
- [[dashboard-access]]
