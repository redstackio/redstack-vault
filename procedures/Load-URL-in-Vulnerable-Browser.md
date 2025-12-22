---
id: proc-uuid-3
tags:
  - xss
  - browser-exploitation
  - windows
type: procedure
tools:
  - '[[tools/Microsoft-Edge]]'
  - '[[tools/Internet-Explorer]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.721Z'
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
# Load-URL-in-Vulnerable-Browser

## Summary

This procedure loads the payload-injected URL into a vulnerable browser version to reflect the stored XSS without immediate execution, setting up the final trigger.

## Description

Vulnerability is browser-specific, affecting Microsoft Edge (v44.17763.1.0) and Internet Explorer on Windows 10 due to legacy handling of reflected content. The page loads normally, but the payload is injected into the DOM. This step confirms compatibility before triggering. Expected outcome: Page loads with payload in place, no alerts yet.

## Requirements

1. Prepared malicious URL from injection step
2. Windows 10 OS
3. Installed vulnerable browser versions

## Defense

Defensive measures and detection strategies:

- Patch browsers to latest versions
- Disable legacy browsers in enterprise environments
- Monitor for legacy browser usage in logs

## Objectives

1. Load the page in a context where XSS can execute
2. Verify no immediate breakage
3. Confirm environment vulnerability

## Instructions

### Step 1: Select and Open Browser

**Context**: Choose a vulnerable browser to ensure the reflection works as expected.

Launch Microsoft Edge version 44.17763.1.0 or Internet Explorer.

> Ensure the browser is running on Windows 10; verify version via about: page.

### Step 2: Navigate to Malicious URL

**Context**: Enter the URL to load the page with the injected payload.

Paste the full URL into the address bar and press Enter.

> The page should display content without errors, but inspect source to see payload reflection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Microsoft-Edge]]
- [[tools/Internet-Explorer]]

## Tags

- [[xss]]
- [[browser-exploitation]]
