---
tags:
  - access
  - login
  - yelp
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
updated_at: '2025-12-14T17:30:35.266Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 0359d792-9417-454a-84e7-3f0d25f796b9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-as-Non-Owner-Business-User

## Summary

This procedure establishes initial access to the Yelp Business account interface using a restricted non-owner user role, setting the stage for exploiting improper access controls in subsequent steps.

## Description

In the context of Yelp's business account system, non-owner users are intended to have limited permissions, excluding user management. However, this procedure leverages existing valid credentials to log in and access the dashboard, confirming the restricted role while preparing for privilege escalation tests. The target environment is the web-based Yelp Business portal, and success relies on having legitimate but limited account access.

## Requirements

1. Valid email and password for a non-owner business user account
2. Web browser with cookies enabled for session management
3. Internet access to reach business.yelp.com

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) audits to ensure login restrictions are enforced
- Monitor login events for unusual user role activities in business accounts
- Use multi-factor authentication (MFA) to prevent unauthorized credential use

## Objectives

1. Gain authenticated access to the business dashboard as a restricted user
2. Verify that user management permissions are absent
3. Prepare for testing invite functionality without owner privileges

## Instructions

### Step 1: Navigate to Login Page

**Context**: Access the Yelp Business login interface to initiate the session.

No command required; manually open a web browser and go to https://biz.yelp.com/login. Enter the non-owner user's email and password, then submit the form.

> Upon successful login, the browser redirects to the business dashboard. Check the URL and interface for confirmation of the restricted role (e.g., no admin menus visible).

### Step 2: Confirm Restricted Access

**Context**: Validate that the login succeeds but user management is inaccessible, indicating the proper restricted role.

No command required; explore the dashboard. Attempt to access 'User Management' or similar sections; they should be hidden or return permission errors.

> Expected behavior: Dashboard loads with standard features like profile viewing/editing available, but team/user controls are restricted.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[login]]
- [[access-control]]
- [[web]]
