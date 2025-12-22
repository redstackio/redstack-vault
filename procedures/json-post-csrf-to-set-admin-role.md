---
id: 4d2d8318-d150-4734-b8ab-6c7d7baafcd4
type: procedure
name: json-post-csrf-to-set-admin-role
verified: true
submitted: false
created_at: '2023-04-06T03:55:55.551063+00:00'
updated_at: '2023-04-06T03:55:55.562794+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Command and Scripting Interpreter/T1059.007 -
    JavaScript|T1059.007 - JavaScript]]
sub_techniques: []
tags:
  - '[[tags/Cross-Site Request Forgery]]'
  - '[[tags/JSON POST - Complex Request]]'
  - '[[tags/Payloads]]'
commands: []
platforms:
  - Web
tools: []
validated: true
---

# json-post-csrf-to-set-admin-role

## Summary

This procedure outlines a Cross-Site Request Forgery (CSRF) attack leveraging a JSON POST request to escalate a user's role to admin on a vulnerable web application. By tricking an authenticated victim into visiting a malicious site, the attack forges a request using the victim's session credentials to modify their account privileges without their knowledge.

## Description

In this CSRF attack, the target application lacks proper CSRF protections like tokens or SameSite cookies, allowing forged requests from external sites. The procedure uses JavaScript within an HTML page to create an XMLHttpRequest that sends a POST to the application's API endpoint (/api/setrole) with a JSON payload setting the role to 'admin'. The withCredentials flag ensures the victim's cookies are included, authenticating the request. This is effective against applications that process JSON POSTs without validating the origin. The attack assumes the victim is logged in and visits the attacker's controlled page, such as via phishing or a malicious link. Success grants the attacker indirect admin access through the victim's elevated session, enabling further actions like data access or modification.

## Requirements

1. Victim must be authenticated (logged in) to the target web application with a session cookie.
2. Attacker must control a malicious website or page that the victim can be induced to visit.
3. Target application must expose an API endpoint (e.g., /api/setrole) that accepts JSON POSTs for role changes without CSRF protection.
4. Browser must support XMLHttpRequest and allow cross-origin requests with credentials (no strict CORS blocking credentials).

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing forms and API endpoints to validate request authenticity.
- Set SameSite=Strict or SameSite=Lax on session cookies to prevent cross-site inclusion.
- Enforce CORS policies that restrict credentialed requests to trusted origins only.
- Monitor for anomalous role changes or unexpected API calls from unusual referers.
- Educate users on phishing risks and verifying links before clicking.

## Objectives

1. Forge a state-changing request using the victim's authenticated session to elevate their role to admin.
2. Achieve privilege escalation without direct credential theft or victim interaction beyond page visit.
3. Enable subsequent unauthorized access to admin functions on the target application.

## Instructions

### Step 1: Identify Target Endpoint and Payload Structure

**Context**: Determine the API endpoint responsible for role updates and confirm it accepts JSON without CSRF checks. This step involves reconnaissance to understand the application's structure.

Inspect the application's network traffic during a legitimate role change (if possible) or review documentation/source code. Verify the endpoint (e.g., http://www.example.com/api/setrole) processes {"role":"admin"} payloads.

### Step 2: Create Malicious HTML Page with CSRF Payload

**Context**: Develop the attack page that embeds the JavaScript payload to automatically send the forged request upon loading.

Create an HTML file hosted on an attacker-controlled server (e.g., via GitHub Pages or a simple web host). Embed the payload code [[codes/html-csrf-json-post-payload]] within a <script> tag. Disguise the page as legitimate content (e.g., a fake news article or image) to lure the victim.

Example hosting: Upload to a domain like attacker-site.com and ensure it's publicly accessible.

### Step 3: Lure Victim to Malicious Page

**Context**: Trick the authenticated victim into loading the page, triggering the automatic request.

Send a phishing email, SMS, or social engineering link pointing to the malicious page. Ensure the victim is logged into the target site beforehand (e.g., via a prior legitimate visit).

### Step 4: Verify Role Escalation

**Context**: Confirm the attack succeeded by checking the victim's account status or observing admin access.

After the victim visits the page, monitor the target application for role changes. If possible, use a secondary account or logs to verify the payload was processed. Test admin functions with the victim's session if captured.

**Expected Output**: The XMLHttpRequest completes silently; on success, the API responds with a 200 OK or updated user object showing "role": "admin". No visible feedback to the victim.

**Success Indicators**:
- Victim's account role updated to admin in application database or UI.
- No errors in browser console (e.g., CORS or credential issues).
- Subsequent requests from victim's session grant admin privileges.
