---
id: proc-identify-faq-form
tags:
  - reconnaissance
  - web-form
  - xss-prep
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T03:47:12.999Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Identify FAQ Feedback Form

## Summary

This procedure involves locating and analyzing the FAQ helpfulness feedback form on a target website to identify potential injection points for XSS attacks, specifically the 'helpful' parameter in the POST request.

## Description

In the context of web vulnerability assessment, identifying user-input forms like FAQ feedback is crucial for discovering reflection vulnerabilities. On developers.mtn.com, the form submits to a PHP endpoint without proper sanitization, allowing reflected XSS. This step requires no special tools, just browser inspection, and sets up subsequent payload crafting.

## Requirements

1. Public access to the target website (https://developers.mtn.com)
2. Browser with developer tools (e.g., Chrome DevTools)
3. Basic knowledge of HTML forms and HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict inline scripts
- Log and monitor form submissions for anomalous payloads
- Use web application firewalls (WAF) to detect SVG or script patterns

## Objectives

1. Locate the feedback form and its endpoint
2. Confirm user-controlled parameters like 'helpful'
3. Prepare for payload injection testing

## Instructions

### Step 1: Navigate and Inspect the Site

**Context**: Access the developers portal and find FAQ sections to locate feedback mechanisms.

Browse to https://developers.mtn.com and search for FAQ articles. Right-click on any helpfulness feedback button and select "Inspect Element" to view the form HTML.

**Expected Output**: Form action points to /sites/all/themes/mtn/helpers/faq-helpful.php with method POST.

### Step 2: Analyze Form Parameters

**Context**: Examine inputs to identify injectable fields.

In DevTools, check the form fields; focus on hidden or visible inputs like 'helpful' which may be boolean but accepts strings.

**Expected Output**: Identification of 'helpful' as a reflected parameter in responses.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[web-form]]
