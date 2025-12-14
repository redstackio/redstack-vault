---
tags:
  - shopify
  - login
  - privileged-access
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Mobile
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:09.580Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: 4ac10eef-a5b3-4823-878d-95b4c0da2d8f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-Shopify-with-Privileged-Account

## Summary

This procedure authenticates a full-access Shopify administrator account in the mobile app to initiate the device registration process, setting up for request interception.

## Description

In the context of exploiting Shopify's mobile device API, logging in with a privileged account triggers the automatic registration of the device's APNS token. This step requires a Shopify admin account with full permissions, including 'Settings', and is performed via the official Shopify mobile app on iOS or Android. The outcome is an authenticated session that sends the initial POST request to the vulnerable endpoint.

## Requirements

1. Valid Shopify admin credentials with full permissions
2. Shopify mobile app installed on a device
3. Proxy tool (e.g., Burp Suite) configured for traffic interception

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) for all admin logins
- Monitor login events for unusual device registrations from privileged accounts

## Objectives

1. Establish an authenticated session with full permissions
2. Trigger the mobile device registration API call
3. Prepare for request capture

## Instructions

### Step 1: Install and Configure Proxy

**Context**: Set up traffic interception to monitor the login-induced API call.

Configure Burp Suite as a proxy on the mobile device (e.g., via Wi-Fi proxy settings or app-specific configuration). Install the Burp CA certificate on the device to handle HTTPS traffic.

### Step 2: Perform Login

**Context**: Authenticate to generate the registration request.

Open the Shopify mobile app, enter the privileged admin credentials, and complete the login process. The app will automatically attempt to register the device by sending a POST to `/admin/mobile_devices.json`.

**Expected Output**: Successful app login and observable API request in the proxy.

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

- shopify
- login
- api-trigger
