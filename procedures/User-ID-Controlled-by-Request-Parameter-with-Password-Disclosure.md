---
id: 7ccbbbf5-d9e9-401b-b794-05d64fa545b0
name: User-ID-Controlled-by-Request-Parameter-with-Password-Disclosure
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T09:56:01.762495+00:00'
updated_at: '2023-05-26T18:48:57.606718+00:00'
platforms:
  - Web
tags:
  - access-control
  - web-applications
tactics:
  - '[[Discovery]]'
  - '[[Credential Access]]'
techniques:
  - '[[Account Discovery]]'
  - '[[Unsecured Credentials]]'
sub_techniques: []
commands: []
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# User-ID-Controlled-by-Request-Parameter-with-Password-Disclosure

## Summary

This procedure exploits a logical flaw in web applications where unauthorized access to a user's account page triggers a redirection to the home page, but the redirect response inadvertently leaks the target user's password, such as an administrator's. By intercepting and modifying the user ID parameter in the request, an attacker with low-privileged credentials can disclose sensitive password information, enabling account takeover.

## Description

Web applications often enforce access controls by checking authentication and authorization before serving sensitive pages like account management or password update forms. If a user attempts to access another user's resource without permission, the application typically redirects to a safe page, such as the home page. However, due to improper handling of sensitive data during this process, the redirect response may include leaked information like the current password of the targeted user. This vulnerability combines insecure direct object references (IDOR) with improper error handling, allowing an authenticated low-privilege user to enumerate and extract credentials for higher-privilege accounts. It is commonly found in legacy or poorly coded applications lacking proper input validation and output encoding. The target environment is a web application with session-based authentication, and success relies on the application's failure to sanitize responses during authorization failures.

## Requirements

- Valid low-privilege user credentials (e.g., a standard user account) to authenticate and establish a session.
- Network access to the web application, including the ability to reach endpoints like login, my account, and password update pages.
- A web proxy tool like [[tools/Burp-Suite]] configured to intercept and modify HTTP requests.
- Basic knowledge of HTTP requests, parameters, and session cookies.

## Defense

- Implement strict authorization checks on all user-specific endpoints to prevent IDOR, ensuring the requested user ID matches the authenticated session.
- Avoid including sensitive data (e.g., passwords) in redirect responses or error messages; use server-side logging instead of client-visible leaks.
- Employ content security policies (CSP) and output encoding to sanitize all responses.
- Monitor for anomalous requests modifying user IDs and enable web application firewall (WAF) rules to detect parameter tampering.
- Use multi-factor authentication (MFA) to mitigate credential theft impacts.

## Objectives

- Authenticate as a low-privilege user and access the account management page to capture the baseline request structure.
- Modify the user ID parameter to target a privileged account (e.g., administrator) and trigger the vulnerable redirect.
- Extract the leaked password from the redirect response and use it to authenticate as the target user.
- Achieve unauthorized access to the privileged account for further exploitation.

## Instructions

### Step 1: Authenticate and Access the Account Page

**Context**: Log in to the application with valid low-privilege credentials and navigate to the 'My Account' or password update page. This establishes a valid session and allows interception of the request that loads the form, which may pre-populate or reference the current password (often masked in the UI but visible in requests/responses).

Configure [[tools/Burp-Suite]] as your browser proxy to intercept traffic. Use the Proxy tab to capture the request to the account endpoint (e.g., GET /myaccount or POST /change-password). Forward the request and observe the response or form data for any pre-filled password fields.

> This step verifies session establishment and identifies the request format, including the 'id' parameter set to your user ID.

### Step 2: Intercept and Analyze the Password Update Request

**Context**: With the session active, submit or load the password update form to capture the full request. The request will include the 'id' parameter tied to your account and may contain the current password in plain or masked form within the body or headers.

In [[tools/Burp-Suite]], switch to the Repeater tab with the intercepted request. Inspect the parameters: note the 'id' value (e.g., 'user123') and any password-related fields. Do not submit changes yet; document the structure for modification.

> Expected: The request body or query string shows the 'id' parameter and potentially the current password in a field like 'current_password'.

### Step 3: Modify the User ID Parameter to Target Administrator

**Context**: Alter the 'id' parameter to reference a privileged account (e.g., 'administrator') to simulate unauthorized access. This triggers the application's access denial and redirection, exploiting the flaw to leak the target user's password in the response.

In Burp Repeater, change the 'id' parameter value from your user ID to 'administrator' (or the known admin identifier). Ensure the session cookie remains valid. Send the modified request.

> The server detects the authorization failure, redirects to the home page (e.g., 302 to /home), but the response body or Location header inadvertently includes the administrator's current password.

### Step 4: Extract the Leaked Password from the Redirect Response

**Context**: Analyze the redirect response for the disclosed password, which appears due to improper sanitization during the error handling process.

Review the response in Burp: Look for the password in the HTML body, JavaScript variables, or even comments. Common leak patterns include error messages like 'Invalid access for administrator, current password: secretpass' or unmasked form data in the redirect page.

> Success is confirmed if the response contains readable password text for the targeted account.

### Step 5: Authenticate as the Administrator Using the Leaked Password

**Context**: Use the extracted password to log in as the administrator, verifying the vulnerability's impact and gaining elevated access.

Return to the login page (or use a new Burp tab). Submit credentials with username 'administrator' and the leaked password. Intercept if needed to confirm no anomalies.

> Expected: Successful authentication, redirect to the admin dashboard or account page.

### Step 6: Verify Elevated Access

**Context**: Confirm the account takeover by accessing privileged features only available to administrators.

Navigate to admin-only sections (e.g., /admin panel). If access is granted without errors, the exploitation is complete.

> This validates the password's validity and the potential for further attacks like data exfiltration or persistence.
