---
tags:
  - xss
  - browser-setup
  - web-testing
type: procedure
tools:
  - '[[tools/Chrome]]'
  - '[[tools/Firefox]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:55:06.893Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 8334893f-9ca0-4472-a7cf-c57d1426af12
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare-Web-Browser-for-XSS-Testing

## Summary

This procedure sets up a web browser environment to safely test and exploit XSS vulnerabilities without interference from security extensions or cached data, ensuring reliable payload delivery and execution.

## Description

In the context of exploiting reflected XSS on web applications like the Starbucks login page, preparing the browser involves launching a clean instance of Chrome or Firefox. This step is crucial to avoid false negatives from ad blockers or script blockers that might prevent JavaScript execution. The target environment is any modern web browser accessing public-facing HTTPS sites, with expected outcomes including a ready-to-use session for URL navigation and interaction. Prerequisites include having Chrome or Firefox installed on the attacker's machine.

## Requirements

1. Chrome or Firefox installed (latest stable version)
2. Internet access to reach the target site
3. No administrative privileges needed

## Defense

Defensive measures and detection strategies:

- Use browser extensions like uBlock Origin or NoScript to block suspicious scripts
- Implement Content Security Policy (CSP) on web apps to restrict inline event handlers
- Monitor for anomalous JavaScript execution via browser developer tools or endpoint detection tools

## Objectives

1. Establish a controlled browser session for vulnerability testing
2. Verify no interfering extensions are active
3. Prepare for payload delivery and execution

## Instructions

### Step 1: Launch Browser in Incognito Mode

**Context**: Starting in incognito mode ensures a clean slate without cookies or extensions impacting the test.

No specific command; manually launch Chrome via `chrome://newtab/` or Firefox equivalent.

> Expected output: New incognito window opens.

### Step 2: Disable Interfering Extensions

**Context**: Temporarily disable any security extensions to allow XSS payload execution.

Navigate to browser settings > Extensions and toggle off blockers.

> Expected output: Extensions list shows disabled status.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome]]
- [[tools/Firefox]]

## Tags

- [[xss]]
- [[browser-setup]]
