---
tags:
  - account-creation
  - web-access
  - file-upload
type: procedure
tools:
  - '[[tools/Burp-Suite-Pro]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 5399af45-db35-4ae6-8bc6-5098ae3d7b7b
created_at: '2025-12-14T05:32:10.177Z'
updated_at: '2025-12-14T05:32:10.177Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-LISTSERV-Account-and-Initiate-Upload

## Summary

This procedure sets up a user account on a LISTSERV 16.0 instance and navigates to the logo upload interface to prepare for request interception, enabling subsequent exploitation of upload restrictions.

## Description

LISTSERV 16.0 allows public registration and profile customization, including logo uploads limited to 10 slots client-side. This step establishes authenticated access and triggers the initial upload request, which can then be captured for tampering. The target environment is a web-based CGI application; prerequisites include internet access to the target URL. Expected outcome: Authenticated session with form ready for proxy interception, setting the stage for bypass without alerting defenses.

## Requirements

1. Web browser (e.g., Firefox or Chrome) with proxy support
2. Valid email for account registration (to receive confirmation if required)
3. Network access to the LISTSERV instance (no firewall blocks on port 80/443)

## Defense

Defensive measures and detection strategies:

- Require CAPTCHA or email verification on registration to slow automated account creation
- Monitor for rapid profile updates or unusual user agents indicating proxy use
- Log all registration and preference access events for anomaly detection

## Objectives

1. Establish persistent access to the upload endpoint
2. Generate a capturable POST request for the logo form
3. Avoid triggering any rate limits during setup

## Instructions

### Step 1: Access Target and Register Account

**Context**: Begin by reaching the LISTSERV homepage to initiate registration.

No command; manual browser action:

Access http://█████████ and click the registration link. Fill in username, password, and email, then submit.

> Expected output: Confirmation email or immediate login page. Success if account is created without errors.

### Step 2: Log In and Navigate to Preferences

**Context**: Authenticate to access user-specific features.

No command; manual navigation:

Enter credentials at the login form. After login, select 'Preferences' > 'Newsletter Profile' tab.

> Expected output: Profile page loads. Success if logos section is visible.

### Step 3: Select Slot and Image File

**Context**: Prepare the upload to mimic legitimate behavior.

No command; form interaction:

Choose 'Slot 1', browse and select a test image (e.g., 100x100 PNG).

> Expected output: File selected. Success if form shows the file path.

### Step 4: Submit Form for Capture

**Context**: Trigger the request for proxy interception.

No command; submit form:

Click 'Update' to send POST.

> Expected output: Request intercepted if Burp is configured. Success if no client errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Pro]]

## Tags

- [[account-creation]]
- [[web-access]]
