---
id: proc-auth-zomato-app
tags:
  - authentication
  - android
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:47.073Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-to-Zomato-Android-App

## Summary

This procedure authenticates a user to the Zomato Android app using valid credentials, establishing a session necessary for interacting with app features that trigger vulnerable POST requests to the backend API.

## Description

In the context of exploiting a Blind XSS in Zomato's admin dashboard, authentication provides the legitimate user context required to submit data via the app. The procedure involves installing the app, entering credentials, and navigating to a user input function. No special privileges are needed beyond standard user access, but credentials must be valid to avoid rate-limiting or blocks. Expected outcome is a logged-in session allowing POST requests to api.zomato.com endpoints.

## Requirements

1. Zomato Android app installed on a device or emulator (version compatible with the vulnerability era, e.g., pre-2019)
2. Valid user credentials (email/phone and password; redacted in reports as ██████)
3. Internet connectivity for app-server communication

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for app logins to prevent credential abuse
- Monitor for unusual login patterns from proxy-routed IPs
- Use certificate pinning in the app to detect and block proxy interceptions

## Objectives

1. Establish authenticated session in the Zomato Android app
2. Enable access to features submitting user input to backend
3. Prepare for request interception without session invalidation

## Instructions

### Step 1: Install and Launch App

**Context**: Set up the environment to run the Zomato Android app.

Install the Zomato app from Google Play or sideload an APK. Launch the app and proceed to the login screen.

### Step 2: Enter Credentials and Authenticate

**Context**: Use provided credentials to gain access.

Enter email/phone (e.g., ██████) and password, then tap 'Login'. The app sends an authentication request to api.zomato.com, establishing a session token in headers like X-Access-Token.

**Expected Output**: App navigates to the main dashboard; no error messages.

### Step 3: Navigate to Vulnerable Function

**Context**: Position the app to trigger the POST request.

Browse to the specific feature (redacted, likely a report or feedback function) that submits POST data to the vulnerable endpoint.

**Expected Output**: Form or input field ready for submission.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authentication]]
- [[android]]
- [[initial-access]]
