---
tags:
  - rce
  - webshell
type: procedure
tools:
  - Web browser
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - PHP
techniques:
  - '[[Python]]'
skill_level: basic
impact_level: high
detection_risk: high
sub_techniques: []
id: bae83d01-384f-46a0-92eb-0253369171a1
created_at: '2025-12-14T17:23:27.990Z'
updated_at: '2025-12-14T17:23:27.990Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Access-Uploaded-Webshell-for-RCE

## Summary

This procedure directly accesses the persisted PHP webshell in the temporary directory to execute arbitrary code, achieving remote code execution on the target server.

## Description

Once the temp directory is located, visiting the webshell URL triggers PHP execution. In the PoC, it runs phpinfo(), but can be extended for full RCE with admin privileges.

## Requirements

1. Known path to byc.php in temp directory
2. Web browser or HTTP client
3. No additional auth (as temp files are publicly accessible)

## Defense

Defensive measures and detection strategies:

- Serve temp directories with .htaccess denying PHP execution
- Auto-delete temps on timeout regardless
- WAF rules to block direct temp file access

## Objectives

1. Load and execute the webshell
2. Confirm RCE via output
3. Escalate to full server control

## Instructions

### Step 1: Construct Webshell URL

**Context**: Build the direct access path.

No command; e.g., http://target/application/files/volatile-0-[uniqid]/byc.php.

> URL ready for access.

### Step 2: Execute in Browser

**Context**: Visit the URL to trigger execution.

No command; open in web browser.

> Displays phpinfo() or custom output, confirming RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Python]]

### Sub-Techniques


## Commands Used


## Tools Used

- Web browser

## Tags

- [[rce]]
- [[webshell]]
