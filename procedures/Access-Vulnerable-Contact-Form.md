---
tags:
  - recon
  - web
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
updated_at: '2025-12-13T23:52:24.360Z'
sub_techniques: []
id: 0275bd5b-7d15-47c3-aaa8-6d2e04abd92d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access Vulnerable Contact Form

## Summary

This procedure involves navigating to a public web contact form to assess for injection vulnerabilities, specifically targeting the Acronis Czech site's form at https://www.acronis.cz/poptavka-acronis/ as an entry point for XSS testing.

## Description

Accessing the target form is the initial step in vulnerability assessment. The page is publicly available without login, allowing direct inspection of form handling. Use browser tools to examine how inputs are processed and reflected, setting up for payload injection. This step confirms reachability and form structure before exploitation.

## Requirements

1. Standard web browser
2. Internet connection
3. No special permissions needed

## Defense

Defensive measures and detection strategies:

- Rate-limit form submissions to prevent automated probing
- Log all form accesses and flag unusual user agents
- Use HTTPS and monitor for direct URL access patterns

## Objectives

1. Confirm form accessibility
2. Identify input fields for injection
3. Prepare for subsequent payload testing

## Instructions

### Step 1: Navigate to Target URL

**Context**: Directly load the contact form page.

Open your browser and enter https://www.acronis.cz/poptavka-acronis/. Wait for the page to fully load.

### Step 2: Inspect Form Elements

**Context**: Use developer tools to analyze form structure.

Press F12 to open dev tools, navigate to the Elements tab, and locate <form> tags and input fields. Note any attributes like name or id that might influence reflection.

> Look for fields without visible sanitization indicators.

### Step 3: Basic Input Test

**Context**: Submit neutral data to observe reflection behavior.

Enter simple text like "test" in fields and submit. View the response source (Ctrl+U) to see if input is echoed verbatim.

> Verbatim reflection indicates potential for injection attacks.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[web-access]]
