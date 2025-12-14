---
tags:
  - oauth
  - login
  - authentication
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
updated_at: '2025-12-14T17:32:58.380Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: f418924d-ad94-45f0-8f53-e30b655b6f8f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Perform Google OAuth Login on Reddit

## Summary

This procedure authenticates a user via Google OAuth 2.0 on Reddit's accounts portal, creating or linking an account to a specific email address, setting up the foundation for exploiting email uniqueness issues.

## Description

The procedure targets https://accounts.reddit.com/ and uses Google's OAuth 2.0 flow to log in, which associates the provided email with a Reddit account. This is the initial step in demonstrating the misconfiguration where subsequent direct registrations ignore this association. No special tools are required; a standard web browser suffices. Expected outcome is a successfully linked account that can later be duplicated.

## Requirements

1. Access to a Google account with a unique email
2. Web browser with JavaScript enabled
3. Internet connectivity to reach Reddit and Google services

## Defense

Defensive measures and detection strategies:

- Implement strict email uniqueness checks across all authentication flows (OAuth and direct)
- Monitor for rapid login/logout cycles followed by registrations with the same email
- Use rate limiting on authentication endpoints to prevent abuse

## Objectives

1. Associate an email with a Reddit account via OAuth
2. Establish a baseline for duplicate creation testing
3. Gain initial access to demonstrate vulnerability

## Instructions

### Step 1: Navigate to Login Page

**Context**: Access the Reddit accounts portal to initiate the login process.

Open a web browser and go to https://accounts.reddit.com/.

> This loads the login interface where authentication options are presented.

### Step 2: Select Google Login

**Context**: Choose the OAuth option to leverage Google authentication.

Click the "Log in with Google" button to redirect to Google's OAuth consent screen.

> Expected output: Prompt for Google account selection and permissions.

### Step 3: Authenticate with Google

**Context**: Complete the OAuth flow to link the account.

Select your Google account, grant permissions to Reddit, and confirm.

> Expected output: Redirect back to Reddit with a successful login, possibly creating a new account if none exists.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- oauth
- google-auth
- login
