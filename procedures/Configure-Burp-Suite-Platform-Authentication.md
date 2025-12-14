---
id: proc-burp-auth-config-001
tags:
  - authentication
  - configuration
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Desktop Application
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:19.392Z'
sub_techniques:
  - '[[Domain Accounts]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Configure-Burp-Suite-Platform-Authentication

## Summary

This procedure configures HTTP Basic authentication credentials in Burp Suite's Platform Authentication settings for a specific domain, which are then used in requests and can be leaked during cross-domain redirections.

## Description

Burp Suite's Platform Authentication feature allows global configuration of authentication for targeted hosts, injecting an Authorization header with base64-encoded credentials into relevant requests. For this attack, credentials (e.g., user:pass) are set for example.com. This simulates a security tester's environment where sensitive creds are stored for legitimate testing but get exposed via tool flaws. The process involves GUI navigation in Burp; prerequisites include Burp Suite running. Expected outcome: Requests to the domain include the auth header, verifiable in Repeater or Proxy logs.

## Requirements

1. Burp Suite Professional or Community edition installed
2. Target domain (e.g., example.com) defined in scope
3. Basic knowledge of HTTP authentication mechanisms

## Defense

Defensive measures and detection strategies:

- Avoid storing real credentials in tools; use temporary or dummy values
- Regularly audit tool configurations for stored secrets
- Enable logging in Burp to detect unexpected header forwarding

## Objectives

1. Apply authentication to requests for the controlled domain
2. Ensure credentials are base64-encoded in Authorization headers
3. Prepare for testing redirection behaviors

## Instructions

### Step 1: Access Platform Authentication Settings

**Context**: Navigate to Burp's global authentication configuration.

No command (GUI). In Burp Suite, go to User options > Platform Authentication.

> This opens the settings panel. Click Add to create a new entry.

### Step 2: Add HTTP Basic Auth for Domain

**Context**: Specify the domain and credentials to inject the header.

No command (GUI). Set Host/IP: example.com, Authentication type: HTTP Basic, Username: user, Password: pass.

> Save the configuration. Test by sending a request to example.com in Repeater; inspect the raw request for Authorization: Basic dXNlcjpwYXNz.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- [[Domain Accounts]] Domain Accounts

## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- authentication
- configuration
