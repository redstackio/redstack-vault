---
tags:
  - initial-access
  - editor-role
  - management-console
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:27.189Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: 48298fe7-7c63-4e8e-868a-f5673b2065e8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-GitHub-Enterprise-Management-Console-with-Editor-Role

## Summary

This procedure outlines logging into the GitHub Enterprise Server Management Console using editor-role credentials, providing the necessary access to configuration interfaces like SMTP settings for further exploitation.

## Description

The GitHub Enterprise Server appliance features a web-based Management Console for administrative tasks. Users with editor role can access non-sensitive configuration options, including SMTP setup, which is vulnerable to injection attacks. This step assumes possession of valid editor credentials, typically obtained through legitimate assignment or prior compromise. The procedure targets the web interface on the appliance's IP address and sets the stage for injecting payloads in subsequent steps.

## Requirements

1. Valid editor-role username and password for the Management Console
2. Web browser with network access to the GitHub Enterprise Server (e.g., https://<appliance-ip>/manage)
3. Target running GitHub Enterprise Server version prior to 3.12

## Defense

Defensive measures and detection strategies:

- Enforce least-privilege access: Limit editor roles to necessary users and audit credential usage
- Monitor Management Console logins: Log and alert on unusual IP addresses or failed attempts
- Enable multi-factor authentication (MFA) for console access

## Objectives

1. Authenticate and access the editor dashboard
2. Verify availability of SMTP configuration
3. Prepare for payload injection without triggering alerts

## Instructions

### Step 1: Navigate to Management Console

**Context**: Locate and access the web interface of the GitHub Enterprise Server Management Console.

Open a web browser and enter the URL: https://<appliance-ip>/manage. This loads the login page for the console.

> Ensure the connection is over HTTPS to avoid interception; successful load shows the GitHub login form.

### Step 2: Authenticate with Editor Credentials

**Context**: Log in using provided editor privileges to gain dashboard access.

Enter the editor username and password in the login fields, then submit. Upon success, the dashboard appears with configuration menus.

> Expected output: Redirect to /manage/dashboard with editor options visible; no admin-only features.

### Step 3: Verify SMTP Access

**Context**: Confirm editor role allows SMTP configuration to proceed to injection.

Navigate to Settings > SMTP in the console menu. If accessible, the form fields for server, port, etc., are available.

> Success: Form loads; failure indicates insufficient privileges.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- initial-access
- editor-role
- management-console
