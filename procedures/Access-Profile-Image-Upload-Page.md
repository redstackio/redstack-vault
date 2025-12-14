---
tags:
  - web
  - access
  - upload
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
updated_at: '2025-12-14T05:32:10.242Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 584e169b-752d-49c9-a5a8-4131d6017f52
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Profile-Image-Upload-Page

## Summary

This procedure involves navigating to the profile image upload page in the target web application, setting the stage for intercepting and exploiting the IDOR vulnerability during the upload process.

## Description

In the context of a U.S. Department of Defense web application, this step requires an authenticated user to access the specific URL for profile editing. The vulnerability lies in the subsequent upload request, but this initial access ensures the attacker can trigger the vulnerable functionality. Expected outcomes include loading the upload interface without issues, confirming the environment is ready for proxy interception.

## Requirements

1. Valid credentials for the target web application
2. Web browser with proxy support (e.g., configured to route through Burp Suite)
3. Knowledge of the base URL: https://██████████/███████ID/#Common/EditOne/Person/{account_id}

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) to restrict profile editing to authorized users only
- Monitor access logs for unusual navigation patterns to profile edit pages

## Objectives

1. Gain access to the upload interface
2. Prepare for request interception
3. Confirm authenticated session validity

## Instructions

### Step 1: Authenticate and Navigate

**Context**: Log in to the application and directly access the profile upload page to initiate the attack surface exposure.

No specific command; use browser navigation:

Navigate to: `https://██████████/███████ID/#Common/EditOne/Person/{account_id}`

> Replace `{account_id}` with your own account ID. Click the upload button and select a test image to prepare for interception. Expected output: Upload interface loads successfully.

### Step 2: Verify Interface

**Context**: Ensure the upload functionality is available and no client-side restrictions are evident.

Inspect the page source or interact with the upload button.

> Expected output: Image selection dialog opens upon clicking upload.

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

- [[web]]
- [[upload]]
- [[access]]
