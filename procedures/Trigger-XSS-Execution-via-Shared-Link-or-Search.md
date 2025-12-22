---
tags:
  - xss-trigger
  - reflected-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:16:07.921Z'
sub_techniques: []
id: 5354f0a0-27c3-4f2c-bcb1-e64489023716
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Trigger-XSS-Execution-via-Shared-Link-or-Search

## Summary

This procedure activates the stored XSS by accessing the shared template URL or exploits reflected XSS via the search parameter, leading to JavaScript execution in the victim's browser.

## Description

Viewing the public form renders the unsanitized field name, executing the onload JS. For reflected XSS, encoded payloads in the query parameter trigger on events like mouseover. If the victim is logged in, redirects to user subdomains enable session-targeted attacks, such as cookie theft.

## Requirements

1. Public URL from shared template
2. Victim browser (or self for testing)
3. Optional: Logged-in session for subdomain redirect testing

## Defense

Defensive measures and detection strategies:

- Output encoding for all dynamic content in forms and search results
- HttpOnly and Secure flags on cookies to mitigate theft
- Client-side event monitoring for suspicious JS execution

## Objectives

1. Execute arbitrary JS in victim context
2. Demonstrate impact like domain alerting or data exfiltration
3. Leverage redirects for account-specific exploitation

## Instructions

### Step 1: Access Shared Template URL

**Context**: Load the public form to trigger stored XSS.

Paste the shared URL (e.g., https://www.drchrono.com/medical-forms/1460752/aaabbbcccdddeee) into a browser.

> Observe the alert popping up with document.domain on page load.

### Step 2: Test Reflected XSS via Search

**Context**: Exploit the unsanitized query parameter for immediate execution.

Navigate to https://www.drchrono.com/medical-forms/?query=aaa%22bbb%27ccc%3Cddd%3Eeee.

> Hover or interact to trigger mouseover-based JS; check console for execution.

### Step 3: Simulate Logged-In Victim Redirect

**Context**: Target session if victim is authenticated.

Log in as a test user, then visit the URL to force redirect to https://%user%.drchrono.com/medical-forms/....

> Verify JS executes in the subdomain context, potentially accessing user-specific data.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-execution
- subdomain-redirect
