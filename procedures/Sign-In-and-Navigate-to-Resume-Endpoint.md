---
tags:
  - initial-access
  - web
type: procedure
tools:
  - '[[Burp Suite]]'
  - '[[curl]]'
tactics:
  - '[[TA0001]]'
commands:
  - '[[curl-execute-dir-command]]'
  - '[[curl-execute-type-command]]'
platforms:
  - Web
techniques:
  - '[[T1190]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 5f313c07-41ad-41f8-b3c9-f6784250fc62
created_at: '2025-12-11T06:04:35.089Z'
updated_at: '2025-12-11T06:04:35.089Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Sign In and Navigate to Resume Endpoint

## Summary

This procedure involves authenticating to the target website and navigating to the resume upload feature to access the vulnerable avatar upload endpoint.

## Description

The attack begins with standard user authentication on the Starbucks recruitment site. After logging in, the user navigates to the resume management section where avatar uploads are handled. This sets the stage for exploiting the file upload vulnerability. The target is a web application on Windows with ASP.NET, and no special tools are needed for this step.

## Requirements

1. Valid user credentials for ecjobs.starbucks.com.cn
2. Web browser or HTTP client
3. Network access to the site

## Defense

Defensive measures and detection strategies:

- Implement strong authentication and session management
- Monitor login attempts and unusual navigation patterns

## Objectives

1. Obtain authenticated session
2. Reach the avatar upload functionality
3. Prepare for upload interception

## Instructions

### Step 1: Access and Login

**Context**: Visit the site and sign in with valid credentials.

Access the URL https://ecjobs.starbucks.com.cn and log in to reach the resume upload feature.

> Upon success, you should see the resume management interface.

### Step 2: Navigate to Upload

**Context**: Proceed to the avatar upload section within the resume endpoint.

Locate and access the avatar upload form.

> This positions you to initiate the upload request.

## MITRE ATT&CK Mapping

### Tactics

- [[TA0001]]

### Techniques

- [[T1190]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[initial-access]]
- [[web]]
