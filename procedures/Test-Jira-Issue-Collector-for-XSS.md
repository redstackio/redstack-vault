---
id: proc-uuid-3
tags:
  - xss-testing
  - injection-testing
  - jira
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
updated_at: '2025-12-13T23:52:49.314Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Jira-Issue-Collector-for-XSS

## Summary

This procedure tests the Jira issue collector for reflected XSS vulnerabilities by probing input fields in search interfaces for injection points.

## Description

Targeting endpoints like https://jira.roblox.com/issues/?filter=-8, this involves navigating to search forms and identifying fields such as 'Updated Date' that reflect user input. The goal is to find unsanitized areas exploitable per CVE-2018-5230. Requires browser access; outcomes include confirmation of injectable points.

## Requirements

1. Access to the vulnerable Jira instance.
2. Web browser for manual testing.
3. Awareness of basic XSS payloads.

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs in search forms with proper encoding.
- Deploy XSS filters or CSP headers to block script execution.

## Objectives

1. Locate specific input fields vulnerable to XSS.
2. Verify reflection without execution.
3. Prepare for payload injection.

## Instructions

### Step 1: Navigate to Search Endpoints

**Context**: Access potential injection interfaces.

Go to https://jira.roblox.com/issues/?filter=-8 and open the advanced search or issue collector.

> Expected output: Form fields like 'Updated Date' visible.

### Step 2: Probe Input Fields

**Context**: Test for reflection by entering benign inputs.

Enter test strings like 'test' into fields such as 'More than [] minutes ago' and submit to check if they appear in the response.

> Expected output: Input reflected in the page HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-testing]]
- [[injection-testing]]
