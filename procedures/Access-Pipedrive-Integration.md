---
id: proc-dropcontact-integration-access-001
tags:
  - integration
  - crm
  - pipedrive
  - dropcontact
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
updated_at: '2025-12-14T17:32:01.870Z'
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
# Access-Pipedrive-Integration

## Summary

This procedure navigates to the Pipedrive CRM integration setup within an authenticated Dropcontact session, preparing for API key input.

## Description

Once logged in, this step involves browsing to the integrations section to load the Pipedrive configuration form. The target environment is the Dropcontact web app, and the outcome is visibility of the API key input field without triggering any pre-authorization checks. Prerequisites include a valid session from the login procedure.

## Requirements

1. Active Dropcontact session
2. Web browser navigation capabilities
3. Knowledge of the integration menu location (typically under Settings > Integrations)

## Defense

Defensive measures and detection strategies:

- Log access to sensitive integration pages
- Require role-based access control (RBAC) for integration features
- Alert on repeated access to CRM setup from low-privilege accounts

## Objectives

1. Load the Pipedrive integration interface
2. Identify input fields for API configuration
3. Prepare for unauthorized key submission

## Instructions

### Step 1: Navigate to Settings

**Context**: From the dashboard, access the configuration area.

Click on the user menu or sidebar and select 'Settings' or 'Integrations'.

### Step 2: Select Pipedrive

**Context**: Choose the specific CRM integration to load its setup form.

In the integrations list, click on 'Pipedrive' to open the setup or modification page.

> The page should display fields for API key entry and connection options.

### Step 3: Confirm Form Availability

**Context**: Verify the interface is ready for input.

Check for the API key input box and any trial or connect buttons.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web-navigation]]
- [[integration-setup]]
- [[pipedrive]]
