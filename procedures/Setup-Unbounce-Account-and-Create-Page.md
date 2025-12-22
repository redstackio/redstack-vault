---
id: proc-unbounce-setup-001
tags:
  - unbounce
  - account-setup
  - web-app
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:38:49.870Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup Unbounce Account and Create Page

## Summary

This procedure establishes a legitimate Unbounce account and creates a basic landing page, serving as the foundation for exploiting API vulnerabilities in subsequent steps of a subdomain takeover attack.

## Description

Unbounce is a web service for creating landing pages. Attackers can sign up for free and create pages to interact with the API. This step prepares the environment by creating a page whose URL can be manipulated via API calls, targeting the domain validation flaw. Prerequisites include internet access and a browser; no special credentials are needed beyond email signup.

## Requirements

1. Internet access to app.unbounce.com
2. Valid email for account registration
3. Browser for navigation (e.g., Chrome with proxy if preparing for interception)

## Defense

Defensive measures and detection strategies:

- Monitor for unusual signup patterns from suspicious IPs
- Implement rate limiting on account creation
- Log API interactions for anomaly detection

## Objectives

1. Gain access to Unbounce platform
2. Create a manipulable page resource
3. Prepare for URL change API exploitation

## Instructions

### Step 1: Register Unbounce Account

**Context**: Create a new account to access page creation features.

No command required; navigate to app.unbounce.com and complete the signup form with email and password.

> Expected: Confirmation email and login success.

### Step 2: Create New Page

**Context**: Build a basic page to obtain a page ID for API manipulation.

Navigate to /pages/new in the dashboard, add minimal content (e.g., text or blank), and save.

> Expected: Page saved with ID visible in URL or dashboard.

### Step 3: Initial URL Configuration

**Context**: Set a custom path to prepare for domain change.

Use the 'CHANGE URL' option, enter path like /blank-page-123133617adasdasdsa, and select default domain unbouncepages.com.

> Expected: URL assigned as https://unbouncepages.com/blank-page-123133617adasdasdsa/.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- unbounce
- account-setup
