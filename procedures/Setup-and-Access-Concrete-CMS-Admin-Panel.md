---
tags:
  - setup
  - concrete-cms
  - admin-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:16:26.150Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 16804734-01fd-4924-9b26-b17807732785
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Setup-and-Access-Concrete-CMS-Admin-Panel

## Summary

This procedure sets up a Concrete CMS 8.5.2 environment and gains administrative access to the dashboard, enabling navigation to vulnerable components like the file search filter.

## Description

In a controlled testing environment, download and install Concrete CMS version 8.5.2, which is vulnerable to stored XSS in its advanced file search functionality. Authenticate using administrator credentials to access the dashboard. This step assumes a fresh installation on a local or remote web server running PHP. The goal is to reach the file search interface without triggering any security measures, preparing for payload injection. Expected outcomes include full admin privileges and visibility of the search tools.

## Requirements

1. Web server with PHP (version 7.4 or compatible with Concrete CMS 8.5.2)
2. Download access to Concrete CMS 8.5.2 from official sources
3. Administrator credentials (default or custom during installation)
4. Web browser for interaction

## Defense

Defensive measures and detection strategies:

- Implement web application firewall (WAF) rules to monitor admin logins
- Use multi-factor authentication (MFA) for admin accounts
- Log all admin dashboard accesses and alert on unusual IP origins

## Objectives

1. Establish a vulnerable Concrete CMS instance for testing
2. Authenticate as admin to access privileged interfaces
3. Navigate to file management sections without restrictions

## Instructions

### Step 1: Download and Install Concrete CMS

**Context**: Obtain and set up the vulnerable version to replicate the target environment.

Download Concrete CMS 8.5.2 from the official website and follow the installation wizard, configuring database and admin credentials.

> During installation, note the admin username and password for later use. Successful installation results in a running web application at the configured URL (e.g., http://localhost/concrete).

### Step 2: Log In as Administrator

**Context**: Gain privileged access to the dashboard.

Navigate to the login page (typically /index.php/login) and enter admin credentials.

> Upon successful authentication, the dashboard loads, confirming access.

### Step 3: Navigate to File Search

**Context**: Reach the vulnerable search interface.

From the dashboard, go to Dashboard > Files > Search.

> The file search page appears, with a search bar and 'Advanced' option visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[concrete-cms]]
- [[admin-access]]
