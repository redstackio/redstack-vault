---
id: proc-nextcloud-inject-xss-001
tags:
  - xss
  - injection
  - nextcloud
  - profile
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:02.382Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Inject-XSS-Payload-into-Nextcloud-User-Profile

## Summary

This procedure sets up a Nextcloud server instance and injects a malicious HTML payload into the user's Full Name and Status Message fields via the web profile interface, exploiting the lack of server-side sanitization for client rendering.

## Description

In the Nextcloud ecosystem, user profile fields like Full Name and Status Message are editable via the web UI and synced to clients. This procedure demonstrates injecting an HTML payload (e.g., an `<img>` tag) that will be treated as markup in the Desktop Client. The attack scenario involves an authenticated user (potentially malicious or compromised) setting these fields to arbitrary HTML, leading to client-side execution when viewed. Prerequisites include a running Nextcloud server and a user account. Expected outcomes: Payload stored on server, ready for client trigger, enabling resource loading or script execution in more advanced cases.

## Requirements

1. Nextcloud Server installed and accessible via web browser
2. Valid user credentials for login
3. Web browser for profile editing (no special tools needed)

## Defense

Defensive measures and detection strategies:

- Sanitize all user-input fields on server and client sides using HTML entity encoding
- Implement Content Security Policy (CSP) in the Desktop Client to restrict resource loading
- Monitor profile field changes for suspicious content (e.g., via logging anomalous HTML tags)

## Objectives

1. Inject executable HTML into profile fields without triggering server validation errors
2. Prepare for client-side exploitation by storing unsanitized data
3. Confirm payload persistence across server sync

## Instructions

### Step 1: Install and Start Nextcloud Server

**Context**: Set up the server environment to host Nextcloud, providing the foundation for profile manipulation.

No specific command; download and install Nextcloud Server from official sources, then start it (e.g., via Apache/Nginx on Linux or built-in setup).

> Expected output: Server running at http://localhost or configured domain, accessible via browser.

### Step 2: Log into Nextcloud Account

**Context**: Authenticate to gain access to user profile settings.

Navigate to the login page and enter credentials.

> Expected output: Successful login, dashboard displayed.

### Step 3: Navigate to Profile Page

**Context**: Access the user settings to edit profile fields.

Click on user avatar or settings menu, then select "Profile" or "Personal info".

> Expected output: Profile edit form loaded.

### Step 4: Inject Payload into Full Name Field

**Context**: Set the Full Name to a malicious HTML payload that will be rendered in the client.

Enter `<img src="https://avatars.githubusercontent.com/u/99037623">` in the Full Name field and save.

> Expected output: Field updated; payload stored as plain text on server.

### Step 5: Inject Payload into Status Message Field

**Context**: Repeat injection in the Status Message for broader impact.

Enter the same payload `<img src="https://avatars.githubusercontent.com/u/99037623">` in the Status Message and save.

> Expected output: Status updated; confirms multiple vectors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- injection
- nextcloud

---
