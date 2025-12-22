---
tags:
  - rce
  - execution
  - webshell
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:54.426Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[JavaScript]]'
id: 9694f08b-2276-4c2b-9308-0552f377acbf
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Trigger RCE by Accessing Uploaded File

## Summary

This procedure activates the uploaded malicious webshell by accessing its URL in a browser, triggering remote code execution on the server and allowing arbitrary command issuance.

## Description

With the webshell uploaded to a web-accessible path, navigating to its URL with parameters executes server-side code. Browser-specific behavior (e.g., execution in Firefox, plain text in Chrome) arises from MIME type handling. This targets the vulnerable web server, assuming PHP processing; outcomes include command output in the response, confirming RCE. Challenges include path discovery via brute-force or leaks.

## Requirements

1. Known path to the uploaded file
2. Browser access (Firefox preferred)
3. No additional tools needed beyond HTTP client

## Defense

Defensive measures and detection strategies:

- Disable script execution in upload directories via .htaccess or server config
- Monitor access logs for suspicious URL parameters (e.g., ?cmd=)
- Implement runtime application self-protection (RASP) to block shell execution

## Objectives

1. Execute the uploaded code remotely
2. Validate RCE with command output
3. Escalate if initial execution succeeds

## Instructions

### Step 1: Locate File Path

**Context**: Determine the exact URL of the uploaded shell.

Use upload response or test common paths like /uploads/, /files/, or /tmp/.

### Step 2: Access in Browser

**Context**: Trigger execution by loading the URL with a command parameter.

In Firefox, navigate to: http://target.com/uploads/shell.php?cmd=whoami

> Expected: Server username or process output. In Chrome, it may show source; switch browsers if needed.

### Step 3: Test Further Commands

**Context**: Issue additional commands to confirm control.

Append ?cmd=id or ?cmd=ls to verify full RCE capabilities.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques

- [[JavaScript]]

## Commands Used


## Tools Used


## Tags

- [[rce]]
- [[Execution]]
