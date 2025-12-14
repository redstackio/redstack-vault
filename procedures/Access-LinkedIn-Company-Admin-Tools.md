---
id: proc-uuid-001
tags:
  - initial-access
  - linkedin
  - admin-tools
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:07.506Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-LinkedIn-Company-Admin-Tools

## Summary

This procedure outlines logging into LinkedIn and navigating to a company's admin tools to trigger the vulnerable API endpoint for employee verification, setting the stage for privilege escalation testing.

## Description

In the context of testing LinkedIn's Voyager API, this step involves authenticating with a valid account and accessing the company management interface. It triggers the initial API call to /voyager/api/voyagerOrganizationDashEmailDomainMappings, which can then be intercepted. Prerequisites include a LinkedIn account affiliated with the target company. Expected outcome is visibility into admin tools without errors, preparing for request interception.

## Requirements

1. Valid LinkedIn credentials with company access
2. Browser configured for proxy interception (e.g., Burp Suite)
3. Internet access to www.linkedin.com

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls (RBAC) on UI navigation
- Monitor login patterns for unusual company admin access
- Log API triggers from admin tools for anomaly detection

## Objectives

1. Establish authenticated session to company page
2. Trigger vulnerable API without higher privileges
3. Prepare for request modification

## Instructions

### Step 1: Login to LinkedIn

**Context**: Authenticate to gain session cookies needed for subsequent requests.

No specific command; use browser to visit https://www.linkedin.com/ and log in with test account credentials.

> Expected output: Successful login, redirect to profile or dashboard.

### Step 2: Navigate to Company Admin Tools

**Context**: Access the management section to reach Employee Verification, which issues the API request.

No specific command; from the profile ('Me' icon), select 'Manage' > company, then 'Admin Tools' > 'Employee Verification'.

> Expected output: Admin Tools page loads, API request sent in background.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- initial-access
- linkedin
- admin-tools
