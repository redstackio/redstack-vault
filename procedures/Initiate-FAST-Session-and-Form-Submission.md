---
id: proc-uuid-1
name: Initiate FAST Session and Form Submission
tags:
  - ssrf
  - web
  - setup
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:28:28.650Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate FAST Session and Form Submission

## Summary

This procedure sets up a new session in the Functional Administrative Support Tool (FAST) v1.0, completes initial form fields, and triggers the PDF generation process while preparing for traffic interception. It establishes the groundwork for exploiting the SSRF vulnerability during subsequent payload injection.

## Description

The FAST application is a web-based tool for administrative workflows. Starting a session involves navigating to the login or entry point, entering basic details like an MCC code, selecting a process, and providing dummy data such as an EDIPI code. This leads to the PDF generation stage where the vulnerable /api/save/ endpoint is called. Burp Suite must be configured as a proxy to capture traffic. Prerequisites include external access to the application and no authentication barriers.

## Requirements

1. Network access to the target FAST web application (HTTPS)
2. Burp Suite installed and configured as browser proxy
3. Basic knowledge of web form interactions

## Defense

Defensive measures and detection strategies:

- Implement web application firewall (WAF) rules to block anomalous form submissions
- Monitor for unusual PDF generation requests or spikes in internal metadata service calls
- Sanitize all user inputs in JSON payloads before processing

## Objectives

1. Create a valid session and reach the PDF generation step
2. Ensure all requests are interceptable for modification
3. Generate an initial PDF URL for later exploitation

## Instructions

### Step 1: Start New Session

**Context**: Access the application and initiate a workflow session to bypass any entry checks.

No specific command; perform via browser:

Navigate to https://target.example.com/, click 'BEGIN NEW SESSION', enter MCC code 'h99', and submit.

> This advances to the process selection page.

### Step 2: Complete Form Fields

**Context**: Fill required fields to progress to PDF stage while proxying through Burp Suite.

Select a process, enter EDIPI '0123456789', add random data, and click CONTINUE.

> Burp Suite captures the submission request.

### Step 3: Generate Initial PDF

**Context**: Trigger PDF to identify the session ID and endpoint.

Click PRINT (VIEW PDF) in 'Get Action Items'.

> PDF opens at /print/checklist/fast_session_XXXXXX.pdf; note the session ID.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

-

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- ssrf
- web
- setup
