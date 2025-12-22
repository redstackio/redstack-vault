---
tags:
  - recon
  - file-upload
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
updated_at: '2025-12-14T17:23:41.471Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 663517a3-5920-4eb1-9e8b-30ab1389bc19
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Repository-File-Upload-Endpoint

## Summary

This procedure involves navigating to a hidden file upload endpoint in a web repository application to identify and access the upload functionality, setting the stage for exploitation of unrestricted file upload vulnerabilities.

## Description

In vulnerable web repository applications running on IIS with Classic ASP, hidden endpoints like '/repo/orbital/repo.asp?fileToUpload=pizza.asp' may expose file upload capabilities without proper authentication. Fuzzing or manual navigation reveals these endpoints, allowing attackers to prepare for malicious uploads. The target environment is a public-facing Windows web server, and success enables subsequent steps in the attack chain.

## Requirements

1. Network access to the target web server (HTTPS port 443)
2. Browser or proxy tool like Burp Suite for inspection
3. No credentials; assumes unauthenticated access

## Defense

Defensive measures and detection strategies:

- Implement web application firewall (WAF) rules to block access to hidden or administrative endpoints
- Log all requests to ASP endpoints and monitor for fuzzing patterns (e.g., high volume of probes)
- Enforce authentication on all upload functionalities

## Objectives

1. Identify and access the file upload interface
2. Confirm multipart/form-data support for file submissions
3. Prepare for malicious payload delivery

## Instructions

### Step 1: Navigate to Endpoint

**Context**: Directly access the repository endpoint to load the upload form.

No specific command; use a browser to visit 'https://target.com/repo/orbital/repo.asp?fileToUpload=pizza.asp'.

> The page should load without errors, displaying or implying file upload fields. Inspect the HTML for form action pointing to the POST endpoint.

### Step 2: Inspect with Proxy

**Context**: Use Burp Suite to capture and analyze the request structure.

Configure browser proxy to Burp and refresh the endpoint.

> Expected output: Intercepted GET request showing parameters like 'fileToUpload'. Confirm the endpoint supports POST for uploads.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[recon]]
- [[file-upload]]
