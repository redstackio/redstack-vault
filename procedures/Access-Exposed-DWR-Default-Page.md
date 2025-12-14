---
tags:
  - information-disclosure
  - dwr
  - reconnaissance
type: procedure
tools:
  - '[[tools/Firefox-Web-Browser]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:28:52.011Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6ab50658-27f1-409f-822c-695e89815dd6
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Access-Exposed-DWR-Default-Page

## Summary

This procedure involves directly accessing the default installation page of the Direct Web Remoting (DWR) engine, which is often left exposed in misconfigured web applications, leading to immediate disclosure of internal classes and methods without authentication.

## Description

In vulnerable web applications using DWR for AJAX-style remote method invocation, the default /dwr/index.html page may remain accessible in production environments. This page serves as an interface for testing and configuration, listing all registered Java classes and their public methods. Attackers can discover this endpoint through directory enumeration or direct URL guessing, especially if the application path is predictable (e.g., /app/dwr/index.html). Upon access, the page reveals sensitive details like admin and test functions, which can be executed directly, bypassing intended access controls. This reconnaissance step sets the stage for abusing insecure methods that may harbor SQL injection or XSS flaws, potentially resulting in data breaches or unauthorized system access. Prerequisites include network reachability to the target and a standard web browser; no special tools or credentials are required.

## Requirements

1. Network access to the target web application (HTTP/HTTPS)
2. Knowledge of the application base path to construct the DWR URL (e.g., https://target.com/path/dwr/index.html)
3. Web browser for manual navigation

## Defense

Defensive measures and detection strategies:

- Remove or restrict access to /dwr/index.html in production by configuring web server rules (e.g., Apache mod_rewrite or Nginx location blocks) to deny public access.
- Implement authentication wrappers around DWR endpoints using application-level checks or reverse proxies like Apache mod_auth.
- Monitor web server logs for accesses to /dwr/* paths and alert on suspicious patterns, such as repeated method executions from unknown IPs.

## Objectives

1. Confirm the presence of the exposed DWR default page.
2. Gather initial intelligence on available classes and methods.
3. Establish a foothold for further method execution and vulnerability identification.

## Instructions

### Step 1: Navigate to Suspected DWR Endpoint

**Context**: Directly visit the URL to check for exposure, assuming the application structure is known or guessed.

Use a web browser to access the target URL.

> No specific command is needed; perform this via browser address bar. For automation in testing, a simple curl request can verify accessibility:
>
> ```bash
> curl -i https://target.com/path/dwr/index.html
> ```
>
> Expected output: HTTP 200 response with HTML content containing DWR interface elements, such as script tags referencing dwr-engine.js and a list of classes.

### Step 2: Verify Page Content

**Context**: Inspect the loaded page to confirm disclosure of sensitive information.

Load the page in the browser and review the interface.

> Look for a table or list enumerating classes (e.g., AdminClass, TestUtil) and their methods (e.g., executeQuery, renderHTML). If present, the exposure is confirmed.
>
> Expected output: Visible listing of internal Java classes and methods, including non-public admin/test functions.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Firefox-Web-Browser]]

## Tags

- information-disclosure
- dwr
- web-recon
