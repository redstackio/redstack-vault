---
tags:
  - authentication
  - lms
  - dod
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:08.187Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: ca0125aa-633e-4801-b8b8-ed09ba7f5970
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-and-Navigate-to-DoD-LMS-Reports

## Summary

This procedure establishes an authenticated session in the U.S. Department of Defense's Learning Management System (LMS) and navigates to the reports section, setting the stage for exploiting the export functionality.

## Description

The DoD LMS requires valid credentials for access. Once logged in, users can reach the reports area where the vulnerable export feature resides. This step assumes possession of legitimate credentials and direct network access to the LMS application, typically hosted on a Windows/IIS server with ASP.NET.

## Requirements

1. Valid DoD LMS username and password
2. Web browser with proxy support for later interception
3. Network connectivity to the LMS URL (e.g., https://lms.dod.mil)

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for LMS logins
- Monitor login attempts and session durations via web application firewall (WAF) logs
- Rate-limit report generation to prevent abuse

## Objectives

1. Achieve authenticated access to the LMS dashboard
2. Locate and access the reports module
3. Generate a sample report to trigger the export process

## Instructions

### Step 1: Authenticate to LMS

**Context**: Visit the login page and enter credentials to establish a session.

No specific command; use browser to navigate to the LMS URL and login with redacted credentials (e.g., username: █████, password: █████).

> Successful login redirects to the dashboard.

### Step 2: Navigate to Reports

**Context**: Access the reports section and select a report.

No specific command; click on 'Reports' in the navigation menu, scroll to a report, and click 'Run Report'. Confirm in the pop-up dialog.

> Page loads with report results; wait for generation if redirected (e.g., to ?rdNoShowWait=True).

### Step 3: Prepare for Export

**Context**: Position for the export action that will be intercepted.

Click 'Export to Excel' in the upper right to initiate the vulnerable POST request.

> This triggers the request to /RServer/rdPage.aspx, ready for interception.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- lms
- dod
