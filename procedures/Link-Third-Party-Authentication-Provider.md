---
tags:
  - oauth
  - authentication-setup
  - weblate
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
updated_at: '2025-12-14T17:31:10.930Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: d1d78fb9-925c-4b27-869f-63e945902ee0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Link-Third-Party-Authentication-Provider

## Summary

This procedure establishes a linkage between a Weblate user account and a third-party authentication provider like Google OAuth, serving as a prerequisite for exploiting session persistence vulnerabilities.

## Description

In the context of Weblate's authentication system, linking a third-party provider allows OAuth-based logins. This step is performed on an initial device to set up conditions for testing session invalidation flaws. The target environment is the Weblate web platform, requiring an authenticated session and access to profile settings. Expected outcome is a confirmed linkage, enabling subsequent logins via the provider without direct password use.

## Requirements

1. Valid Weblate account credentials for initial login
2. Access to a Google account for OAuth linkage
3. Two devices or incognito browser sessions for isolation
4. Network connectivity to https://hosted.weblate.org

## Defense

Defensive measures and detection strategies:

- Monitor for unusual OAuth linkage events in application logs
- Implement rate limiting on authentication profile changes
- Require re-authentication for sensitive profile modifications like linking providers

## Objectives

1. Securely link external identity provider to the account
2. Enable multi-factor or alternative login paths
3. Set up for vulnerability testing in session management

## Instructions

### Step 1: Access Profile Settings

**Context**: Log in to the target account and navigate to authentication management to initiate linkage.

Log in to https://hosted.weblate.org using existing credentials, then proceed to the profile section at https://hosted.weblate.org/accounts/profile/#auth.

> Locate the third-party authentication options and select Google to start the OAuth flow.

### Step 2: Complete OAuth Authorization

**Context**: Authorize the linkage using the external provider's credentials.

Follow the redirect to Google's authorization page, grant permissions for Weblate access, and confirm the linkage upon return.

> Verify the linkage in the profile by checking that Google is listed as connected.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[oauth]]
- [[weblate]]
