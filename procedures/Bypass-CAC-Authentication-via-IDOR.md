---
tags:
  - auth-bypass
  - cac
  - idor
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:30.780Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: c01e7a9a-5167-47cf-853b-103083b792c7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass-CAC-Authentication-via-IDOR

## Summary

This procedure bypasses Common Access Card (CAC) authentication on protected file downloads by exploiting IDOR in the download form, using a password from a non-CAC file to access restricted content.

## Description

The file download endpoint at █████/███?id= lacks validation between the entered password and the target ID, allowing parameter swapping. An attacker uses a regular file's password on a CAC-protected ID, evading DoD's authentication requirements in the ASP.NET platform.

## Requirements

1. Password from a non-CAC file (obtained via prior recipient addition)
2. Target CAC-protected file ID (e.g., 15745307)
3. Burp Suite for form interception
4. Access to download pages

## Defense

Defensive measures and detection strategies:

- Enforce CAC validation on all protected downloads regardless of password
- Validate password-ID pairs server-side with cryptographic binding
- Monitor for parameter tampering in download POSTs and log CAC bypass attempts

## Objectives

1. Access CAC-protected files without authentication
2. Download sensitive protected documents
3. Demonstrate full auth bypass in the sharing workflow

## Instructions

### Step 1: Access Download Form

**Context**: Load a generic download page to prepare the form submission.

Navigate to █████/███?id=15745307 (or any arbitrary ID) in a browser. The form for password entry will appear.

> The page prompts for a password without initial CAC check.

### Step 2: Enter Mismatched Password

**Context**: Use a password from an unauthorized non-CAC file to initiate the request.

Input the password obtained from a regular package email into the form and submit. Intercept the POST request with Burp Suite.

> The request includes the original ID and entered password.

### Step 3: Swap ID and Submit

**Context**: Modify to target a CAC file while retaining the valid password.

In Burp Suite, replace the 'id' parameter in the POST with a CAC-protected file's ID (e.g., change to actual protected ID).

> Forward the request; the server accepts it due to missing validation.

### Step 4: Download Protected File

**Context**: Confirm bypass by retrieving the file.

After forwarding, the file details display, allowing direct download without CAC.

> Success grants access to classified or protected content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[auth-bypass]]
- [[cac]]
- [[idor]]
