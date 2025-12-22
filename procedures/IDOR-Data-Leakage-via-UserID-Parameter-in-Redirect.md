---
id: f6e00897-167f-491b-b25b-d4a60d76d664
name: IDOR-Data-Leakage-via-UserID-Parameter-in-Redirect
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T09:30:24.864782+00:00'
updated_at: '2023-05-26T18:50:52.607662+00:00'
platforms:
  - Web
tags:
  - '[[tags/access control]]'
  - '[[tags/Web Applications]]'
  - idor
  - data-leakage
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Account Discovery]]'
sub_techniques: []
commands:
  - '[[commands/curl-access-account-details]]'
  - '[[commands/curl-modify-userid-for-leakage]]'
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/cURL]]'
validated: true
---

# IDOR-Data-Leakage-via-UserID-Parameter-in-Redirect

## Summary

This procedure demonstrates how to exploit an Insecure Direct Object Reference (IDOR) vulnerability where the UserID parameter in a web request can be manipulated to access unauthorized data. By changing the UserID from the authenticated user's value to another user's (e.g., 'carlos'), the application redirects to the home page but leaks sensitive information, such as an API key, in the redirect response. This technique is useful for identifying access control weaknesses in web applications that fail to properly validate user parameters.

## Description

In web applications, IDOR vulnerabilities occur when user-supplied input directly references internal objects (like user IDs) without sufficient authorization checks. Here, after logging in as a low-privilege user (e.g., 'wiener'), accessing account details involves a request with a UserID parameter set to the current user's ID. Modifying this parameter to another valid UserID (e.g., 'carlos') bypasses access controls, causing the server to process the unauthorized request. Instead of denying access, the application redirects to the home page, but inadvertently includes sensitive data like an API key in the redirect URL or response headers/body. This leakage can lead to further compromise, such as unauthorized API access or token abuse. The procedure assumes a session-based authentication and uses tools like Burp Suite for interception or curl for direct requests. It maps to MITRE ATT&CK technique T1087 (Account Discovery) under the Discovery tactic, as it reveals information about other user accounts and associated secrets.

## Requirements

1. Valid credentials for a low-privilege account (e.g., username: wiener, password: provided in lab/context).
2. Network access to the target web application (e.g., via browser or proxy).
3. Tools: Burp Suite for request interception and manipulation, or curl for CLI-based testing.
4. Active session cookie or authentication token from login.
5. Knowledge of the target endpoint (e.g., /my-account) and parameter name (UserID).

## Defense

Defensive measures and detection strategies:

- Implement proper access controls by validating that the UserID parameter matches the authenticated user's ID on the server side.
- Avoid including sensitive data (e.g., API keys) in redirect URLs, headers, or responses; use secure storage and short-lived tokens instead.
- Enable web application firewall (WAF) rules to detect parameter tampering and anomalous redirects.
- Log all access to user-specific endpoints and monitor for discrepancies between requested UserID and session user.
- Use Content Security Policy (CSP) and HttpOnly/Secure flags on cookies to prevent session hijacking post-leakage.

## Objectives

1. Access authorized account details using the legitimate UserID to establish a baseline.
2. Manipulate the UserID parameter to target another user's data, triggering the IDOR.
3. Capture and extract the leaked sensitive information (e.g., API key) from the redirect response.
4. Verify the leakage by inspecting the response for unauthorized data exposure.

## Instructions

### Step 1: Authenticate and Access Account Details

**Context**: Log in to the application as the authorized user (e.g., 'wiener') and retrieve the account details request, which includes the UserID parameter set to the current user's value. This establishes the valid request format and session.

Use [[commands/curl-access-account-details]] to send the request with the legitimate UserID:

```bash
curl -X GET "$_TARGET_URL/my-account?UserID=$_LEGIT_USERID" -H "Cookie: session=$_SESSION_COOKIE" -v
```

> This command fetches the account details for the authenticated user. The -v flag enables verbose output to show headers and response code. Expected: A 200 OK response with the user's account information displayed, confirming successful access without errors.

### Step 2: Modify UserID Parameter to Trigger IDOR

**Context**: Alter the UserID parameter to a different valid user (e.g., 'carlos') to attempt unauthorized access. The server accepts the invalid reference, redirects to the home page (likely 302), but leaks sensitive data in the process.

Use [[commands/curl-modify-userid-for-leakage]] to send the modified request:

```bash
curl -X GET "$_TARGET_URL/my-account?UserID=$_TARGET_USERID" -H "Cookie: session=$_SESSION_COOKIE" -L -v
```

> The -L flag follows the redirect to capture the full response chain. Inspect the Location header or response body for leaked data like an API key. Expected: A 302 redirect to the home page (/), with the redirect URL or response containing sensitive information (e.g., api_key=sk-abc123).

### Step 3: Extract and Verify Leaked Data

**Context**: Analyze the redirect response for the leaked API key or other secrets. If using Burp Suite, inspect the Repeater tab for the full HTTP exchange.

Manually review the verbose output from the curl command or Burp's response viewer. Look for patterns like 'api_key=' in the Location header (e.g., /home?api_key=leakedvalue) or body.

> No specific command needed here; use grep on the output if saved to file: `curl ... > response.txt && grep -i 'api_key' response.txt`. Expected: Identification of the leaked credential, confirming the IDOR success. If no leak, the vulnerability may not be present or require further parameter testing.
