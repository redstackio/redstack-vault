---
tags:
  - authentication
  - admin-access
  - helium
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
updated_at: '2025-12-14T03:46:09.132Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: 4bbdf92a-fe64-41d8-aa1e-0085ed0c7c5f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate as Admin to Helium Console

## Summary

This procedure establishes authenticated access to the Helium Console as an administrator user within an active organization, enabling access to features like custom integrations required for SSRF exploitation.

## Description

The Helium Console is a web-based platform for managing LoRaWAN devices and integrations. Authentication as an admin allows navigation to sensitive configuration areas. This step assumes possession of valid credentials and targets organizations with connected devices. Successful authentication grants a session token for subsequent actions, setting the stage for vulnerability exploitation without requiring advanced technical skills.

## Requirements

1. Valid admin credentials (username/email and password) for a Helium organization
2. Web browser with cookies enabled (e.g., Chrome, Firefox)
3. Internet access to https://console.helium.com
4. Organization must have at least one active LoRaWAN device

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for admin accounts to prevent credential compromise
- Monitor login attempts from unusual IP addresses or locations using SIEM tools
- Enforce least-privilege access, limiting admin roles to necessary users

## Objectives

1. Gain session access to the organization dashboard
2. Verify presence of devices for integration association
3. Prepare for integration configuration without triggering alerts

## Instructions

### Step 1: Navigate to Login Page

**Context**: Access the public-facing login endpoint to initiate authentication.

Open a web browser and go to https://console.helium.com.

> The login form will appear, prompting for credentials.

### Step 2: Enter Credentials

**Context**: Submit admin credentials to authenticate and establish a session.

Enter the admin email/username and password, then click 'Log In'.

> Upon success, the browser redirects to the organization dashboard, displaying tabs like 'Devices' and 'Integrations'. Check for session persistence by refreshing the page.

### Step 3: Verify Access

**Context**: Confirm admin privileges and organization setup.

From the dashboard, navigate to 'Devices' to ensure at least one LoRaWAN device is listed and active.

> Expected: Device list visible; if no devices, the attack cannot proceed to association.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- admin-access
- helium
