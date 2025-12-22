---
id: proc-semrush-idor-intercept
tags:
  - idor
  - intercept
  - modification
  - web
  - semrush
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:34.086Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Modify-Enrollment-Request-for-IDOR

## Summary

This procedure uses Burp Suite to intercept, modify, and forward the Semrush Academy course enrollment POST request, exploiting an IDOR vulnerability by changing the userId parameter to impersonate any user and gain unauthorized access to their enrollment data.

## Description

The Semrush Academy enrollment endpoint at POST https://www.semrush.com/academy/courses/userEnroll lacks proper authorization checks on the userId parameter, allowing attackers to reference any user's ID. By intercepting the request during a legitimate enrollment attempt, modifying the userId to a victim's (e.g., from 5410425 to 5407773), and forwarding it, the attacker can enroll the victim in arbitrary courses and retrieve sensitive details like creationDate, engagement, status, and userEngagement. This affects all users and enables broad account manipulation and data exposure. Prerequisites include an active session and Burp Suite proxy setup.

## Requirements

1. Active authenticated session from Semrush Academy
2. Burp Suite running with proxy interception enabled
3. Knowledge of a target victim's userId (e.g., via prior enumeration)
4. Browser proxied through Burp Suite

## Defense

Defensive measures and detection strategies:

- Enforce server-side validation of userId against the authenticated session's user identity
- Log and monitor all enrollment requests for userId mismatches
- Implement rate limiting on enrollment endpoints and alert on proxy-detected traffic (e.g., via User-Agent or headers)

## Objectives

1. Capture the enrollment request for analysis and modification
2. Exploit IDOR by impersonating a victim user
3. Achieve unauthorized enrollment and data access

## Instructions

### Step 1: Enable Interception and Trigger Enrollment

**Context**: Start capturing traffic and initiate the request to be intercepted.

In Burp Suite Proxy > Intercept, ensure 'Intercept is on'. In the browser, select a course and click 'Enroll for free' to send the POST request.

**Expected Output**: Request held in Burp, showing body with userId and courseId.

### Step 2: Forward Non-Target Requests

**Context**: Isolate the enrollment POST by forwarding unrelated traffic.

Click 'Forward' in Burp for any incidental requests until the target POST to /academy/courses/userEnroll is displayed.

**Expected Output**: Clean view of the enrollment request parameters.

### Step 3: Modify the userId Parameter

**Context**: Change the userId to the victim's to bypass authorization.

Edit the request body (e.g., JSON: change "userId": "5410425" to "userId": "5407773"). Preserve other fields like courseId.

**Expected Output**: Updated request body reflecting the victim's userId.

### Step 4: Forward the Modified Request

**Context**: Submit the tampered request to exploit the vulnerability.

Click 'Forward' to send the request to the server.

**Expected Output**: Server processes the request, returning 200 OK with victim's enrollment data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor]]
- [[intercept]]
- [[modification]]
- [[web]]
- [[semrush]]
