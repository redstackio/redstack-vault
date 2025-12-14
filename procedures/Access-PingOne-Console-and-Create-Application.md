---
id: proc-001
tags:
  - ping-identity
  - console-access
  - application-creation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-13T23:52:24.107Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Access-PingOne-Console-and-Create-Application

## Summary

This procedure outlines logging into the Ping Identity console, navigating to the Applications section, and creating a new application to prepare for vulnerability exploitation, such as stored XSS injection.

## Description

In the context of exploiting web application vulnerabilities in identity management platforms like PingOne, this procedure provides authenticated access and sets up a target application. It assumes the attacker has valid credentials and is performed in a staging environment (e.g., https://console-staging.pingone.com/). The outcome is a new application entry ready for modification, enabling subsequent payload injection. Prerequisites include browser access and proxy configuration for traffic interception.

## Requirements

1. Valid PingOne console credentials (username/password or SSO).
2. Network connectivity to the console URL (HTTPS on port 443).
3. Configured proxy tool like Burp Suite to monitor requests.

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for console access to prevent unauthorized logins.
- Monitor application creation logs for anomalous activity, such as rapid successive creations.
- Use web application firewalls (WAF) to scan for suspicious navigation patterns.

## Objectives

1. Establish authenticated session in the console.
2. Create a new Native App application for payload targeting.
3. Confirm application visibility in the list for exploitation setup.
4. Enable interception of save requests without alerting defenses.

## Instructions

### Step 1: Login and Navigate

**Context**: Authenticate and reach the Applications section to initiate setup.

No specific command; use browser to access https://console-staging.pingone.com/, log in, and click Connections > Applications.

> Expected output: Applications list loads, allowing new app creation.

### Step 2: Create Application

**Context**: Add a new entry to access the editable fields.

No specific command; select "Native App" type, name it (e.g., "VulnTestApp"), and save with defaults.

> Expected output: App appears in list; edit view accessible via pencil icon.

### Step 3: Verify List View

**Context**: Ensure the app is stored and viewable for triggering.

No specific command; refresh or return to Application List.

> Expected output: App listed without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[ping-identity]]
- [[web-access]]
