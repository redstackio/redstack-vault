---
id: proc-uuid-1
tags:
  - recon
  - web
  - csrf
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:27:22.838Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Capture-Login-Request-with-Browser-Dev-Tools

## Summary

This procedure involves using browser developer tools to intercept and capture a legitimate POST request to the login endpoint, identifying key parameters like authenticity_token for subsequent CSRF testing.

## Description

In a Login CSRF attack scenario, the first step is to understand the normal authentication flow. By capturing a real login request from the Mavenlink application (or similar Rails-based web app), the attacker can examine the request structure, including headers and form data. This reveals if CSRF protections like authenticity_token are present and enforceable. The target environment is a web application with a POST /login endpoint. Prerequisites include browser access to the login page and valid test credentials. Expected outcome: Detailed request log for modification in the next step.

## Requirements

1. Modern web browser (e.g., Chrome, Firefox) with developer tools enabled
2. Valid login credentials for the target application
3. Network access to the web application

## Defense

Defensive measures and detection strategies:

- Enable comprehensive web application firewall (WAF) rules to log anomalous request patterns
- Implement strict CSRF token validation on all state-changing endpoints
- Monitor for unusual login attempts from non-standard referers

## Objectives

1. Obtain the exact structure of a legitimate login request
2. Identify CSRF protection parameters for vulnerability assessment
3. Prepare data for forging requests in cross-site contexts

## Instructions

### Step 1: Access Login Page and Open Dev Tools

**Context**: Navigate to the target's login page and prepare to monitor network traffic.

Open the login form in your browser. Press F12 (or right-click > Inspect) to open developer tools, then switch to the Network tab. Ensure "Preserve log" is checked to capture requests across navigations.

### Step 2: Submit Login and Capture Request

**Context**: Perform a normal login to intercept the POST request.

Enter valid credentials (e.g., email and password) and submit the form. In the Network tab, locate the POST request to /login. Click it to view details: Headers (e.g., User-Agent: Mozilla/5.0..., Accept: text/html..., Cookie: session_id=...), and Request Payload (utf8=✓, authenticity_token=abc123..., login[email_address]=user@example.com, login[password]=pass123, login[open_id]=, from=).

**Expected Output**: Full request breakdown, confirming successful login (status 200 or 302 redirect).

### Step 3: Export or Note Request Details

**Context**: Document the request for replication without protections.

Copy the request as cURL (right-click > Copy > Copy as cURL) or manually note parameters. Focus on the authenticity_token for removal in testing.

**Expected Output**: Saved request template ready for modification.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[recon]]
- [[web]]
- [[csrf]]
