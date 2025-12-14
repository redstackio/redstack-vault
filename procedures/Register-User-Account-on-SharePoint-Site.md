---
tags:
  - account-creation
  - initial-access
  - sharepoint
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 06fde832-6356-4cf5-98b4-c0f39e537e85
created_at: '2025-12-13T23:56:19.971Z'
updated_at: '2025-12-13T23:56:19.971Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Register-User-Account-on-SharePoint-Site

## Summary

This procedure outlines the registration process on a SharePoint-based website to obtain authenticated access for exploiting blog features, such as in vulnerability assessments targeting user-generated content areas.

## Description

In the context of testing for stored XSS in a DoD SharePoint site, registration provides the necessary user account to create blog posts and upload files. The process involves navigating to a public registration page and submitting standard form details. No advanced privileges are required, making it a low-barrier initial access step. Expected outcomes include a functional account that can access personal profile sections like the blog.

## Requirements

1. Access to a web browser
2. Valid email address for registration confirmation (if required)
3. Target site with open registration at /SitePages/Register.aspx

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA or email verification to prevent automated registrations
- Monitor for unusual registration spikes or patterns indicative of abuse
- Restrict blog access to verified users only

## Objectives

1. Establish authenticated session for blog interactions
2. Enable creation of user content for vulnerability testing
3. Confirm access to profile and blog endpoints

## Instructions

### Step 1: Navigate to Registration Page

**Context**: Access the public registration endpoint to begin account creation.

Open a web browser and go to https://██████████/SitePages/Register.aspx.

> Fill out the registration form with details such as username, email, and password. Submit the form to complete registration.

### Step 2: Verify Account Creation

**Context**: Confirm the account is active and log in to test access.

After submission, check for a confirmation message or email. Log in using the new credentials to ensure access to restricted areas like the profile blog.

> Successful login redirects to the dashboard or profile, indicating the account is ready for use.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[initial-access]]
- [[Sharepoint]]
