---
id: 9a6fc951-29ca-4a8e-9fe8-20b372fd58cb
name: Escalate-User-Role-via-Profile-Update-Parameter-Tampering
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T18:35:39.509371+00:00'
updated_at: '2023-05-26T01:36:23.761397+00:00'
tactics:
  - '[[Privilege-Escalation-via-Direct-URL-Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - access-control
  - web-applications
  - parameter-tampering
  - role-escalation
  - authorization-bypass
commands:
  - '[[commands/curl-authenticate-user-login]]'
  - '[[commands/curl-perform-profile-update]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Escalate-User-Role-via-Profile-Update-Parameter-Tampering

## Summary

This procedure exploits poor server-side authorization in web applications by tampering with the 'roleid' parameter during a user profile update request. An authenticated user can modify their role to a higher privilege level, such as admin, gaining unauthorized access to restricted features like the admin panel. This targets applications that include role information in client-side requests without proper validation.

## Description

Many web applications allow users to update their profiles via API endpoints that accept JSON payloads containing user details like email. Due to flawed design, these endpoints may echo back or accept modifications to sensitive fields like 'roleid' without verifying the user's authorization to change it. An attacker, already authenticated with a low-privilege account, can intercept the update request using a proxy tool, modify the 'roleid' to an administrative value (e.g., 2 for admin), and resubmit it. Upon success, the server updates the role, allowing access to privileged areas. This technique relies on the assumption that role IDs are predictable or discoverable from initial responses. It is commonly found in custom web apps with inadequate input sanitization and is a classic example of broken access control.

## Requirements

1. Valid low-privilege user credentials for the target web application.
2. Access to a proxy tool like [[tools/Burp-Suite]] to intercept and modify HTTP requests, or equivalent CLI tools like curl for direct manipulation.
3. Knowledge of the application's profile update endpoint URL and login endpoint.
4. Network access to the target web application (e.g., via browser or direct HTTP).
5. Ability to identify administrative role IDs, often through trial (e.g., 1=user, 2=admin) or from initial response observation.

## Defense

Defensive measures and detection strategies:

- Implement server-side authorization checks to ensure users can only modify their own non-sensitive fields; reject or ignore unauthorized parameters like 'roleid'.
- Use role-based access control (RBAC) frameworks that enforce privileges at the server level, logging all role changes for auditing.
- Validate and sanitize all incoming JSON payloads, stripping or validating sensitive fields against user permissions.
- Monitor for anomalous role escalations via application logs or SIEM, alerting on unexpected privilege changes.
- Employ web application firewalls (WAFs) to detect parameter tampering patterns in profile update requests.

## Objectives

1. Authenticate as a legitimate user to establish a session.
2. Identify the current user role ID from a legitimate profile update response.
3. Tamper with the 'roleid' parameter to escalate privileges to admin level.
4. Verify escalation by accessing restricted admin functionality.

## Instructions

### Step 1: Authenticate to the Application

**Context**: Log in to the web application to obtain a valid session cookie, which is required for subsequent authenticated requests. This step establishes the attacker's legitimate session.

**Command** ([[commands/curl-authenticate-user-login]]):
```bash
curl -X POST -c cookies.txt -d "email=$_EMAIL&password=$_PASSWORD" $_LOGIN_URL
```

> This command sends a POST request to the login endpoint, storing the session cookie in 'cookies.txt'. Replace $_EMAIL and $_PASSWORD with valid low-privilege credentials, and $_LOGIN_URL with the actual login path (e.g., https://target.com/api/login). Expected output is a 200 OK response with a success message or redirect, confirming authentication. Verify the cookie file contains a session token (e.g., 'session=abc123').

### Step 2: Perform Legitimate Profile Update to Observe Role ID

**Context**: Submit a benign profile update (e.g., changing email) to capture the request and response, revealing the current 'roleid' in the JSON payload or response. This helps identify the structure and current role value without raising suspicion.

**Command** ([[commands/curl-perform-profile-update]]):
```bash
curl -X POST -b cookies.txt -H "Content-Type: application/json" -d '{"email":"$_NEW_EMAIL"}' $_PROFILE_URL
```

> Use the session cookie from Step 1. This sends a legitimate update without tampering. Observe the request body and response JSON for the 'roleid' field (e.g., {"roleid":1}). If using [[tools/Burp-Suite]], intercept the request via proxy to inspect easily. Expected output: 200 OK with updated profile confirmation, including the echoed 'roleid'. Note the current roleid (typically 1 for user) to contrast with the target admin roleid (e.g., 2).

### Step 3: Tamper with Role ID in Profile Update Request

**Context**: Modify the captured profile update request by injecting or altering the 'roleid' to an administrative value, then resubmit to escalate privileges. This exploits the lack of server-side validation.

**Command** ([[commands/curl-perform-profile-update]]):
```bash
curl -X POST -b cookies.txt -H "Content-Type: application/json" -d '{"email":"$_NEW_EMAIL","roleid":$_TARGET_ROLE_ID}' $_PROFILE_URL
```

> Build on the legitimate request from Step 2, adding or changing '"roleid":$_TARGET_ROLE_ID' (e.g., 2 for admin). If using [[tools/Burp-Suite]], send the modified request via Repeater. Expected output: 200 OK response confirming the update, with the JSON echoing the new 'roleid':2. If the server accepts it without error, the escalation succeeded.

### Step 4: Verify Privilege Escalation

**Context**: Test access to admin-only features to confirm the role change took effect. This validates the attack's success.

**Instructions**: Navigate to the admin panel URL (e.g., https://target.com/admin) in a browser using the same session, or use a GET request with the cookie:
```bash
curl -b cookies.txt $_ADMIN_URL
```
> Expected output: Access granted without authentication errors, displaying admin dashboard or features. If denied, try logging out and back in to refresh the session, or identify the correct admin roleid by testing values (e.g., 0, 2, 99).

### Step 5: Clean Up (Optional)

**Context**: Revert changes to avoid detection, if persistence is not desired.

**Instructions**: Repeat Step 3 with the original roleid to downgrade, or delete the account if possible.
