---
id: proc-intercept-profile-001
tags:
  - interception
  - analysis
  - burp
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Foxy-Proxy]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-profile-update-attacker]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:06.655Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Analyze-Profile-Update-Request

## Summary

This procedure involves logging in as the attacker, navigating to profile editing, and using proxy tools to intercept the POST request to /EditUserProfile/Save, revealing the static userId parameter critical for IDOR exploitation.

## Description

The target ASP.NET Core application fails to validate the userId against the authenticated session, allowing manipulation. By updating the attacker's profile and intercepting the request, the procedure identifies the userId (e.g., 123464) and confirms it does not change with input modifications, indicating the IDOR flaw.

## Requirements

1. Attacker account credentials
2. Burp Suite configured as proxy
3. Foxy Proxy enabled in browser
4. Access to My Account page

## Defense

Defensive measures and detection strategies:

- Implement server-side authorization checks for userId
- Log and monitor anomalous profile update requests
- Use WAF rules to detect parameter tampering

## Objectives

1. Capture the profile update request structure
2. Identify and note the attacker's userId
3. Verify userId static nature for IDOR confirmation

## Instructions

### Step 1: Login and Navigate to Profile

**Context**: Authenticate as attacker and access the edit profile page.

Login at https://target.com/login with attacker credentials, then go to My Account > Edit Profile.

> Redirect to /EditUserProfile page.

### Step 2: Perform Profile Update and Intercept

**Context**: Update a field like email and intercept the submission.

Enable Foxy Proxy, update Email to a test value, submit, and intercept in Burp Suite using [[commands/curl-profile-update-attacker]] equivalent or direct proxy capture.

**Command** ([[commands/curl-profile-update-attacker]]):
```bash
curl -X POST https://target.com/EditUserProfile/Save \
  -H "Cookie: .AspNetCore.Antiforgery.w=...; TS014b77bb=..." \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "Email=attacker@gmail.com&userId=123464&__RequestVerificationToken=...&Title=Pentester&FirstName=attacking&LastName=wearehackerone&passChange=true&CitizenshipId=101&PositionTitleIds=10&PersonProfileId=0"
```

> Intercepted request shows userId=123464; response is success (200 OK).

### Step 3: Analyze for Static userId

**Context**: Modify email in the form and re-intercept to confirm userId unchanged.

Repeat update with new email (e.g., test@gmail.com) and check userId remains 123464.

> Confirms IDOR potential as parameter is not session-bound.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-profile-update-attacker]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Foxy-Proxy]]

## Tags

- interception
- analysis
- burp
