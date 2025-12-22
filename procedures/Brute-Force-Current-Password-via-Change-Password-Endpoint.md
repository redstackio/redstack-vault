---
id: 9f07f4b3-a211-4856-86be-714da33f021b
name: Brute-Force-Current-Password-via-Change-Password-Endpoint
type: procedure
verified: true
submitted: true
created_at: '2020-09-02T13:43:58.812507+00:00'
updated_at: '2023-05-26T18:08:02.085621+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Brute Force]]'
sub_techniques:
  - '[[Password Guessing]]'
tags:
  - '[[tags/broken authentication]]'
  - '[[tags/Web Applications]]'
  - brute-force
  - credential-access
commands:
  - '[[commands/curl-password-change-post]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Brute-Force-Current-Password-via-Change-Password-Endpoint

## Summary

This procedure exploits weak protections in a web application's password change functionality to brute-force a user's current password. By submitting password change requests with intentionally mismatched new passwords and systematically varying the current password field using a tool like Burp Suite Intruder, an attacker can identify the correct password based on distinct server error responses: 'Current password is incorrect' for wrong attempts and 'New passwords do not match' for the correct current password.

## Description

Many web applications validate the current password during changes without sufficient rate limiting or additional authentication, allowing brute-force attacks. This technique assumes the attacker has a valid session (e.g., via another account or prior access) and can intercept/modify requests. It targets endpoints like /change-password that accept POST data for current_password, new_password1, and new_password2. The attack leverages response differentiation: incorrect current passwords trigger an early validation error, while correct ones proceed to new password matching checks. This is effective against applications lacking brute-force protections, such as account lockouts or CAPTCHA on changes. Primary use case: gaining unauthorized access to a target account in a multi-user web app.

## Requirements

- Valid session cookies or authentication token for the target application (e.g., logged in with another account if needed)
- Burp Suite or equivalent proxy tool configured to intercept and modify HTTP requests
- A wordlist of potential passwords (e.g., common passwords, leaked lists from sources like https://github.com/1N3/IntruderPayloads)
- Knowledge of the password change endpoint URL and parameter names (typically /account/change-password or similar)
- Network access to the target web application

## Defense

- Implement rate limiting on password change endpoints (e.g., max 5 attempts per minute per session/IP)
- Require multi-factor authentication (MFA) or secondary verification for password changes
- Use strong session management to invalidate sessions on suspicious activity
- Monitor for anomalous request patterns, such as high volumes of password change attempts from a single session
- Employ Web Application Firewalls (WAF) to detect and block brute-force patterns

## Objectives

1. Identify the target user's current password through response-based brute-forcing
2. Use the discovered password to log in and access the account
3. Demonstrate the lack of brute-force protections in the password change flow

## Instructions

### Step 1: Establish a Valid Session and Intercept Login

**Context**: Log in to the application to obtain a valid session, then configure interception to capture requests. This ensures you can modify subsequent requests without re-authenticating.

Use [[tools/Burp-Suite]] to proxy traffic and intercept the login POST request.

**Command** (example login request for reference):

The login request typically looks like a POST to /login with username and password parameters. After successful login, note the session cookie (e.g., JSESSIONID or auth_token).

> Expected: 200 OK response with session cookie in Set-Cookie header. Verify by accessing a protected page.

### Step 2: Access Password Change Form and Test Error Responses

**Context**: Navigate to the password change page to identify the request structure and baseline error messages. This step confirms the vulnerability by observing distinct responses for incorrect current passwords vs. mismatched new passwords.

In the browser (proxied through Burp), go to the account settings > change password. Submit with an obviously incorrect current password (e.g., 'wrong') and any new passwords. Intercept the POST request using [[tools/Burp-Suite]].

The request format is similar to:

**Command** ([[commands/curl-password-change-post]]):
```bash
curl -X POST -b "session_cookie=$_SESSION_COOKIE" \
  -d "current_password=wrong&new_password1=abc&new_password2=abc" \
  $_ENDPOINT_URL
```

> Expected: HTTP 200 or 400 response body containing "Current password is incorrect". Forward the request in Burp and confirm no change occurs.

Next, resubmit with a guessed correct current password but mismatched new passwords (e.g., new1='abc', new2='def').

> Expected: Response body containing "New passwords do not match". This confirms the server checks current password first, then new password matching.

### Step 3: Capture and Prepare the Password Change Request for Brute-Forcing

**Context**: From Burp's HTTP history, select a password change request with mismatched new passwords and send it to Intruder. This sets up the baseline for payload insertion on the current_password field.

In Burp Proxy > HTTP history, right-click the /change-password POST > Send to Intruder.

Ensure the request has fixed mismatched new passwords (e.g., new_password1=hacker888&new_password2=hacker999) to trigger the matching error only if current is correct.

> Expected: Intruder tab opens with the request loaded, payload positions cleared.

### Step 4: Configure Payload Positions and Wordlist

**Context**: Mark the current_password parameter as the payload position to brute-force it while keeping new passwords fixed and mismatched.

In Intruder > Positions tab, highlight the value of current_password (e.g., §oldpassword§) and click 'Add §' to set it as payload position 1. Clear other positions.

Switch to Payloads tab, select 'Simple list' as payload type. Paste or load a wordlist of passwords (obtain from https://github.com/1N3/IntruderPayloads or similar sources).

> Expected: Payload sets list populated (e.g., 1000+ common passwords). No errors in payload loading.

### Step 5: Set Up Response Analysis Rules

**Context**: Configure Intruder to flag responses containing the 'New passwords do not match' message, which indicates a correct current password.

In Intruder > Options tab, under Grep - Match, add a rule for 'New passwords do not match'. Set it to extract or highlight occurrences in responses.

Optionally, add another grep for 'Current password is incorrect' to differentiate failures.

> Expected: Rules added without syntax errors. Attack configuration ready.

### Step 6: Execute the Brute-Force Attack

**Context**: Launch the Intruder attack to test each password from the wordlist. Monitor for the distinguishing response.

Click 'Start attack' in Intruder. Let it run through the payload set (may take minutes depending on wordlist size and server response time).

> Expected: Results table showing request #, payload, status, length, and grep matches. Look for the entry where 'New passwords do not match' appears (this is the correct current password). Other entries should show 'Current password is incorrect' or no match.

### Step 7: Verify and Use the Discovered Password

**Context**: Once identified, test the password by logging in to confirm access.

Note the payload from the matching response. Log out if needed, then attempt login with the target username and discovered password.

Use [[commands/curl-password-change-post]] for a test change if desired, but primarily verify login.

> Expected: Successful login (200 OK, redirect to dashboard). Account access granted.
