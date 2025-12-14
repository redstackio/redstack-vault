---
tags:
  - web-access
  - reconnaissance
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:12.875Z'
sub_techniques: []
id: 5169dab3-5362-467d-98d0-5b5999558baf
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Access-MTN-Vulnerable-Web-Pages

## Summary

This procedure involves navigating to specific public-facing web pages in MTN Group's application that serve as entry points for triggering vulnerable API calls, allowing attackers to begin the information disclosure process without authentication.

## Description

In the context of MTN Group's web services, such as Virtual Top-Up (VTU), certain pages provide interfaces for phone number inputs that lead to unauthenticated API queries. Accessing these pages is the initial step in discovering and exploiting the information disclosure vulnerability. The target environment is MTN's web platform running on WildFly/10 and Undertow/1. Expected outcomes include loading the interface ready for input, setting the stage for request interception.

## Requirements

1. Web browser with proxy support (e.g., Firefox or Chrome)
2. Internet access to MTN's public web services
3. Burp Suite configured as a proxy (optional for this step but recommended for chaining)

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on web page access to prevent automated scanning
- Monitor access logs for unusual patterns to public service pages
- Use web application firewalls (WAF) to block suspicious browsing behavior

## Objectives

1. Gain access to the vulnerable interface without authentication
2. Identify input fields for phone numbers
3. Prepare for subsequent request interception

## Instructions

### Step 1: Launch Web Browser and Navigate to Target Pages

**Context**: Open a browser and direct it to the redacted MTN service pages to load the vulnerable interface.

No specific command; use browser navigation:

Visit URLs such as 'https://redacted.mtn.com/vtu' or 'https://redacted.mtn.com/service' which are part of the VTU or similar features.

> This loads the page with phone number input fields. Ensure proxy is set to localhost:8080 if using Burp Suite.

### Step 2: Verify Page Accessibility

**Context**: Confirm the page is public and functional without login prompts.

Inspect the page source or interact with elements to ensure no auth barriers.

> Expected: Page renders fully, input form visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[web-access]]
- [[Reconnaissance]]
