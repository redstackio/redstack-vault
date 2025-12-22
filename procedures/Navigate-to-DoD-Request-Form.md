---
tags:
  - web-access
  - initial-access
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:10.273Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 218c382f-393c-49a5-9265-28b06660a49f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Navigate to DoD Request Form

## Summary

This procedure accesses the public new request page on the U.S. Department of Defense's website, serving as the entry point for exploiting the unrestricted file upload vulnerability.

## Description

The DoD's request submission system is publicly accessible via a ColdFusion-based web application. Navigating to the form allows unauthenticated users to create support requests, where the upload flaw resides. This step requires no special tools, only a standard web browser, and assumes the target URL is known (e.g., redacted public site).

## Requirements

1. Web browser with internet access
2. Knowledge of the public request form URL
3. No authentication or prior access needed

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on form access to prevent abuse
- Log all form page visits and monitor for anomalous patterns
- Use web application firewall (WAF) to inspect incoming requests

## Objectives

1. Load the request creation interface
2. Identify the form structure for subsequent steps
3. Establish initial foothold without triggering alerts

## Instructions

### Step 1: Open Browser and Navigate

**Context**: Directly access the public endpoint to begin the process.

Browse to `██████PublicSite/index.cfm?fwa=newreq` using a web browser.

> This loads the initial request page. Expected output: Page renders with a 'Create a New Request' button.

### Step 2: Initiate Request Creation

**Context**: Click to enter the form workflow.

Click the 'Create a New Request' button.

> This transitions to the email entry field. Expected output: Form input appears without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web]]
- [[initial-access]]
