---
tags:
  - csrf
  - intercept
  - openid
  - weblate
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:33:06.240Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 1886049a-0434-49e1-a9f2-757687f53619
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Prepare Attacker Account and Intercept Auth Request

## Summary

This procedure sets up the attacker's Weblate account for Ubuntu One association and intercepts the vulnerable authentication completion request using a proxy tool, capturing OpenID parameters for later CSRF exploitation.

## Description

In the context of Weblate's third-party authentication via Python Social Auth, this step prepares the groundwork by logging into the attacker's account, initiating the Ubuntu One login flow, and proxying the request to extract sensitive OpenID response data. The vulnerability arises from the lack of CSRF tokens or proper nonce validation in the /accounts/complete/ubuntu/ endpoint, allowing the request to be replayed cross-site. Prerequisites include a valid Weblate account for the attacker and Burp Suite configured as a proxy. Expected outcome is the full capture of parameters like identity, email, nonce, and signature for crafting a CSRF payload.

## Requirements

1. Valid attacker credentials for Weblate (e.g., demo.weblate.org)
2. Burp Suite installed and browser proxy configured to intercept HTTPS traffic
3. Access to Ubuntu One login (login.ubuntu.com)
4. Victim's Weblate session active (for later steps)

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens or state parameters in all POST endpoints handling authentication
- Enforce same-site cookie policies (Lax/Strict) and validate referer/origin headers
- Monitor for anomalous authentication associations from third-party providers

## Objectives

1. Establish attacker's control over Ubuntu One identity
2. Extract OpenID response without completing legitimate association
3. Prepare data for cross-site replay to victim's session

## Instructions

### Step 1: Log In to Attacker's Weblate Account

**Context**: Authenticate to gain access to profile settings where third-party associations are managed.

No specific command; manually access https://demo.weblate.org/accounts/login/ and enter credentials.

> Successful login redirects to the dashboard; verify by checking user profile.

### Step 2: Navigate to Profile Authentication Section

**Context**: Reach the area for adding third-party auth providers.

Manually go to https://demo.weblate.org/accounts/profile/#auth.

> Page loads with 'Add new association' options including Ubuntu One.

### Step 3: Select and Initiate Ubuntu One Association

**Context**: Start the auth flow to trigger the vulnerable endpoint.

Choose 'Ubuntu' in the association section, which redirects to login.ubuntu.com for OAuth/OpenID.

> Enter Ubuntu credentials but do not confirm 'Yes log me in' yet.

### Step 4: Intercept the Completion Request

**Context**: Capture the POST before it reaches Weblate to prevent legitimate linking.

Configure Burp Suite to intercept; drop the request to /accounts/complete/ubuntu/ containing parameters like openid.identity, openid.ax.value.email.1, janrain_nonce, and openid.sig.

> Intercepted request shows no CSRF token; parameters ready for extraction.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- csrf-prep
- auth-intercept
- openid-capture
