---
tags:
  - endpoint-access
  - authentication
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
updated_at: '2025-12-14T17:26:00.626Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 8f9bb7a4-1ff7-4fb9-8cbd-73cf6d733a57
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-My-Cabins-Endpoint

## Summary

This procedure describes logging into the Airship CMS and navigating to the /my/cabins endpoint, a user management page that serves as the trigger point for path disclosure.

## Description

After account registration, authentication is required to access user-specific features. This step involves logging in and directly targeting the cabins endpoint, which is part of the application's internal functionality. The target is a PHP-based web app, and the outcome is reaching a page that may error out due to unhandled exceptions, exposing server details.

## Requirements

1. Valid user credentials from prior registration
2. Web browser session
3. HTTPS access to airship.paragonie.com

## Defense

Defensive measures and detection strategies:

- Enforce proper session management and log access to sensitive endpoints
- Use web application firewalls to monitor unusual navigation patterns

## Objectives

1. Establish authenticated session
2. Reach the vulnerable endpoint
3. Prepare for error induction

## Instructions

### Step 1: Log In to Application

**Context**: Use credentials to authenticate and gain session access.

**Instructions**: On the login page, enter the username/email and password, then submit.

> Successful login redirects to the dashboard or user area.

### Step 2: Navigate to Endpoint

**Context**: Directly access the cabins management URL to load the vulnerable page.

**Instructions**: In the browser, enter or click to https://airship.paragonie.com/my/cabins.

> The page should attempt to load, potentially triggering an error immediately.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[endpoint-access]]
- [[web]]

