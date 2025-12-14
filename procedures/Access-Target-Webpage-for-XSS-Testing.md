---
id: proc-uuid-1
tags:
  - xss
  - web-access
  - recon
type: procedure
tools:
  - '[[tools/Chrome]]'
  - '[[tools/Firefox]]'
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
updated_at: '2025-12-13T23:55:20.489Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Target-Webpage-for-XSS-Testing

## Summary

This procedure involves navigating to the MTN Investor website's search page using a web browser to establish initial access for testing reflected XSS vulnerabilities.

## Description

In the context of web vulnerability assessment, accessing the target webpage is the first step to identify and interact with potentially vulnerable components like search inputs. The MTN Investor site at https://mtn-investor.com/mtn-cmd/index.php hosts a PHP-based search functionality that reflects user input without proper encoding, making it susceptible to XSS. This step requires no authentication and can be performed from any network position with internet access. Expected outcomes include loading the page and confirming the presence of the search interface.

## Requirements

1. Web browser such as Chrome or Firefox installed
2. Internet connectivity to reach https://mtn-investor.com
3. JavaScript enabled in the browser for payload execution testing

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAF) to block access to known vulnerable endpoints
- Monitor access logs for unusual patterns from reconnaissance tools or manual browsing
- Use content security policy (CSP) headers to restrict page navigation

## Objectives

1. Gain initial access to the public-facing web application
2. Verify the availability of the search functionality
3. Prepare for subsequent payload injection

## Instructions

### Step 1: Launch Browser and Navigate

**Context**: Open the browser and directly access the target URL to load the vulnerable page.

No command required; perform manually:

In Chrome or Firefox, enter the URL `https://mtn-investor.com/mtn-cmd/index.php` in the address bar and press Enter.

> This loads the main page with the search input. Expected output: The page renders fully, displaying the search form without errors.

### Step 2: Confirm Page Elements

**Context**: Inspect the page to ensure the search input is present and interactive.

Use browser developer tools (F12) to inspect the DOM for the search field.

> Look for elements like input fields or forms handling `zoom_query`. Success confirms readiness for injection.

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
- [[web]]
- [[recon]]
