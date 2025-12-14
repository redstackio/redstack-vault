---
tags:
  - nextcloud
  - email-bomb
  - dos
  - abuse-functionality
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Chrome-Developer-Tools]]'
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Set-Personal-Email-to-Target-in-Nextcloud]]'
  - '[[procedures/Send-Test-Email-from-Admin-Settings-in-Nextcloud]]'
  - '[[procedures/Replay-API-Request-for-Email-Flood-Using-Browser-DevTools]]'
step_count: 3
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:01.538Z'
description: >-
  An attack chain exploiting Nextcloud's unrestricted email testing API to
  perform email bombing, allowing an administrator to flood any target email
  address with unlimited test emails, resulting in a denial-of-service on the
  victim's inbox.
skill_level: intermediate
impact_level: medium
id: 601d1186-b20d-4cf2-bd93-cff47cc6578e
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Nextcloud Admin Email Bombing via Unrestricted Test API

Multi-stage attack chain demonstrating how an administrator can abuse Nextcloud's email testing functionality to send unlimited test emails to any target address, enabling email bombing and denial-of-service on the victim's inbox. The attack leverages the admin interface and API replay without rate limiting, though Nextcloud considers admins trusted, rating it low severity. Discovered in a HackerOne report, this can overwhelm email services with thousands of messages.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Set Target Email Address] --> B[Send Initial Test Email]
    B --> C[Replay API for Email Flood]
    C --> D[DoS on Victim Inbox]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Chrome-Developer-Tools]]

### Target Environment

- Nextcloud instance (web application)
- Administrator access to Nextcloud
- Email server configured in Nextcloud
- Network access to the Nextcloud admin interface

### Initial Access Requirements

- Valid admin credentials for Nextcloud
- Browser access to the Nextcloud URL (e.g., https://target.nextcloud.com)
- No prior compromise needed beyond admin privileges

## Detailed Attack Procedures

### Step 1: Set Target Email Address
procedure: [[procedures/Set-Personal-Email-to-Target-in-Nextcloud]]

**Objective**: Configure the attacker's personal email setting in Nextcloud to the victim's email address, directing all test emails to the target.

**Instructions**: Log in to Nextcloud as an administrator and navigate to the personal settings page. Update the email field with the victim's address. Save the changes to apply the configuration.

**Expected Output**: The personal email setting is updated, and any subsequent test emails will be sent to the specified victim address.

**Success Indicators**:
- Email field shows the victim's address in personal settings
- No validation errors on save

### Step 2: Send Initial Test Email
procedure: [[procedures/Send-Test-Email-from-Admin-Settings-in-Nextcloud]]

**Objective**: Trigger the email testing API to send a single test email to the configured target address, verifying the setup and demonstrating the functionality.

**Instructions**: From the admin settings, navigate to the additional settings section. Locate and click the 'Send test mail' button, which invokes the mailtest API endpoint.

**Expected Output**: A test email is sent to the victim's address, confirming delivery via the email server.

**Success Indicators**:
- Success message in the UI after clicking send
- Victim receives the initial test email

### Step 3: Replay API for Email Flood
procedure: [[procedures/Replay-API-Request-for-Email-Flood-Using-Browser-DevTools]]

**Objective**: Capture and repeatedly replay the API request to the mailtest endpoint, flooding the victim's inbox with thousands of emails for a DoS attack.

**Instructions**: Open the browser's developer tools, navigate to the network panel, and perform the test email send to capture the XHR request to /settings/admin/mailtest. Replay the request multiple times manually or via console scripting to send continuous emails.

**Expected Output**: Multiple API calls succeed, resulting in a flood of emails to the target address.

**Success Indicators**:
- Network panel shows repeated successful requests to mailtest API
- Victim's inbox overwhelmed with duplicate test emails

## Attack Chain Summary

### Key Achievements

1. Redirected email testing to arbitrary victim address without validation
2. Verified API functionality with initial send
3. Achieved scalable DoS by replaying requests unlimited times

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Impact]]

---
*Last updated: 2023-10-01T00:00:00Z*
