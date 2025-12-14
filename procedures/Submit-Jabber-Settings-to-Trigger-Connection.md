---
id: proc-phpbb-submit-jabber-001
tags:
  - ssrf
  - trigger
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:10.146Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Jabber-Settings-to-Trigger-Connection

## Summary

This procedure enables the Jabber feature and submits the form to force the phpBB server to attempt a connection to the specified localhost port, exploiting the SSRF vulnerability.

## Description

Upon submission, phpBB processes the 'jabber server' and port without validation, leading to a server-side connection attempt. This can reveal internal network details if successful. Targeted at phpBB 3.3.1, this step requires prior configuration of localhost parameters. No CLI tools needed; it's form-based. Outcomes: Server initiates outbound connection, potentially logging or erroring based on target.

## Requirements

1. Configured Jabber form with localhost and port
2. Admin session active
3. Server-side PHP environment vulnerable to SSRF

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all input parameters to block internal IPs
- Disable verbose error reporting in production
- Monitor outbound connections from the web server (e.g., via firewall logs)

## Objectives

1. Activate the feature to enable connection
2. Submit to execute SSRF
3. Initiate internal resource probe

## Instructions

### Step 1: Enable Jabber Feature

**Context**: Toggle the feature on to ensure connection attempt occurs.

Select the 'Enabled' radio button in the form.

> Expected output: Option selected; submit button active.

### Step 2: Submit the Form

**Context**: Trigger server-side processing.

Click the 'Submit' button.

> Expected output: Page reloads or redirects; server attempts connection to 127.0.0.1:port.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Service Scanning]] Network Service Scanning
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- trigger
