---
id: c9a8a7bf-fcf7-4d06-a167-8c7eb1e8c72a
name: Bypass-Referer-Based-Access-Control
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T13:49:03.134743+00:00'
updated_at: '2023-05-26T18:38:38.980522+00:00'
tactics:
  - '[[Privilege-Escalation-via-Direct-URL-Access]]'
techniques:
  - '[[Account Manipulation]]'
sub_techniques: []
tags:
  - access-control
  - web-applications
  - authorization-bypass
commands:
  - '[[commands/curl-admin-role-upgrade-with-custom-referer]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Bypass-Referer-Based-Access-Control

## Summary

This procedure exploits web applications that enforce access controls based on the HTTP Referer header, allowing an attacker to bypass restrictions and perform unauthorized actions such as promoting a non-admin user to admin privileges by spoofing the Referer header while using a legitimate session cookie.

## Description

Referer-based access controls are a flawed security mechanism where the server checks the Referer header to ensure requests originate from authorized pages (e.g., an admin panel). Since clients control this header, attackers can manipulate it to mimic legitimate requests. This technique is common in legacy or poorly designed web apps and can lead to privilege escalation. The procedure assumes a target like a user management system with endpoints like /admin-roles for role changes, requiring both admin and non-admin accounts for demonstration.

## Requirements

1. Valid admin and non-admin credentials for the target web application.
2. Burp Suite (or equivalent proxy) configured to intercept and modify HTTP requests.
3. Browser access to the application, with proxy settings enabled for interception.
4. Knowledge of the admin panel URL and the role upgrade endpoint (e.g., /admin-roles?username=TARGET&action=upgrade).

## Defense

Defensive measures and detection strategies:

- Implement server-side authorization checks based on user roles and sessions, ignoring client-supplied headers like Referer.
- Use strict CSP headers to control referer policies, though this primarily prevents leaks rather than spoofing.
- Log and monitor HTTP requests for mismatched Referer headers or anomalous role change attempts from non-admin sessions.
- Enforce multi-factor checks for sensitive actions, such as role promotions.

## Objectives

1. Identify and capture a legitimate Referer header from an admin action.
2. Use a non-admin session to attempt unauthorized access, confirming the referer check.
3. Spoof the Referer header to bypass controls and escalate privileges for a target user.
4. Verify success through redirection or role change confirmation.

## Instructions

### Step 1: Login as Admin and Capture Legitimate Request

**Context**: Authenticate as an admin to access the restricted functionality and intercept the request containing the valid Referer header for later spoofing. This establishes the baseline for legitimate traffic.

**Instructions**: Configure your browser to route traffic through Burp Suite proxy. Log in to the application using admin credentials (e.g., wiener:peter). Navigate to the admin panel and attempt to promote a test user (e.g., carlos) by submitting a request to the role upgrade endpoint. Intercept the outgoing request in Burp, note the Referer header (e.g., https://target.com/admin), and forward it to Repeater for modification later.

**Expected Output**: Successful promotion for the test user if not intercepted; captured request shows Referer: https://target.com/admin and session cookie for admin.

### Step 2: Login as Non-Admin and Obtain Session Cookie

**Context**: Create a session for a low-privilege user to simulate an unauthorized attempt, confirming the access control relies on Referer matching the admin origin.

**Instructions**: Open an incognito/private browser window to avoid session conflicts. Log in using non-admin credentials (e.g., carlos:carlos). Inspect the browser's developer tools (Network tab) or use Burp to capture the login response, then copy the session cookie value (e.g., session=abc123).

**Expected Output**: Successful login confirmation; session cookie visible in response headers or application storage.

### Step 3: Test Unauthorized Access with Non-Admin Session

**Context**: Verify the access control by attempting the privileged action with the non-admin session, which should fail due to mismatched Referer.

**Instructions**: In Burp Repeater, paste the captured admin request from Step 1. Replace the session cookie with the non-admin value from Step 2. Set the URL to /admin-roles?username=carlos&action=upgrade. Forward the request without modifying Referer.

**Expected Output**: HTTP 403 Forbidden or unauthorized error, indicating the Referer check blocks the action.

**Success Indicators**:
- Request rejected due to invalid origin (Referer mismatch).
- No role change occurs for the user.

### Step 4: Spoof Referer Header to Bypass Control

**Context**: Modify the Referer to mimic a legitimate admin request while retaining the non-admin session, allowing the server to process the action as authorized.

**Instructions**: In Burp Repeater, update the request from Step 3: Set Referer header to the admin value (e.g., https://target.com/admin), change username=weiner (or target user), and ensure the non-admin session cookie is set. Forward the request. Alternatively, simulate via command line for automation.

**Command** ([[commands/curl-admin-role-upgrade-with-custom-referer]]):
```bash
curl -X GET "https://$_TARGET_URL/admin-roles?username=$_TARGET_USERNAME&action=upgrade" \
  -H "Cookie: session=$_SESSION_COOKIE" \
  -H "Referer: $_ADMIN_REFERER" \
  -v
```

> This command sends the role upgrade request with spoofed Referer. If successful, the server processes it without checking the session's privilege level beyond the header.

**Expected Output**: HTTP 302 Found redirect to a success page or dashboard, indicating the role upgrade succeeded.

**Success Indicators**:
- 302 redirect or success response.
- Target user (e.g., weiner) promoted to admin upon verification.
