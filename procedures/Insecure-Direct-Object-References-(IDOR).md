---
id: 24b6117a-912c-4e52-949d-c98231777b26
type: procedure
verified: true
submitted: true
created_at: '2020-07-23T14:51:37.891148+00:00'
updated_at: '2024-01-01T00:00:00Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Account Discovery]]'
sub_techniques: []
tags:
  - '[[tags/IDOR]]'
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/Web Applications]]'
commands:
  - '[[commands/curl-get-user-orders]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: beginner
impact_level: high
detection_risk: low
validated: true
---

# Insecure Direct Object References (IDOR)

## Summary

This procedure demonstrates how to identify and exploit Insecure Direct Object References (IDOR), a vulnerability where an application exposes internal object identifiers (such as user IDs) directly in URLs or parameters without proper access controls, allowing unauthorized access to other users' data.

## Description

IDOR vulnerabilities occur in web applications when user-supplied input directly maps to internal objects like database records, files, or user profiles without validating the user's permission to access them. For example, an endpoint like /orders?user=123 might allow any authenticated user to change the 'user' parameter to 456 and view another user's orders. This procedure assumes a web application with predictable identifiers (e.g., sequential integers) and focuses on testing URL query parameters. It is commonly found in applications handling user-specific data such as profiles, orders, or documents. Successful exploitation can lead to data leakage, account takeover, or further compromise.

## Requirements

1. Valid authenticated session in the target web application (e.g., logged-in user account).
2. Knowledge or ability to guess/enumerate other user IDs (e.g., via sequential guessing or prior enumeration).
3. HTTP client such as curl or a browser with developer tools.
4. Optional: Intercepting proxy like [[tools/Burp-Suite]] to capture and modify requests.
5. Target application must expose object references via GET/POST parameters.

## Defense

- Implement server-side access controls to verify object ownership (e.g., check if the requested user ID matches the authenticated user's ID).
- Use indirect references like cryptographically secure UUIDs instead of sequential IDs.
- Apply role-based access control (RBAC) and validate permissions on every request.
- Monitor for anomalous access patterns, such as a user requesting multiple unrelated IDs.
- Use web application firewalls (WAFs) to detect parameter tampering.

## Objectives

1. Identify endpoints that use direct object references without authorization checks.
2. Manipulate parameters to access unauthorized data belonging to other users.
3. Confirm the vulnerability by observing leaked sensitive information.

## Instructions

### Step 1: Identify Vulnerable Endpoints

**Context**: Log in to the application and navigate to pages displaying user-specific data (e.g., profile, orders, or documents). Inspect URLs, forms, or API calls to find parameters like 'user', 'id', 'account', or 'order_id' that directly reference objects. This step helps pinpoint where direct references are exposed.

Use browser developer tools (F12) or [[tools/Burp-Suite]] to examine requests. Look for predictable patterns, such as integer-based IDs in query strings.

**Expected Output**: A request like GET /orders?user=123, where '123' is your user ID.

### Step 2: Manipulate the Object Reference

**Context**: Authenticated as your user (e.g., ID 123), modify the parameter to target another user's ID (e.g., 456). This tests if the application enforces access controls.

**Command** ([[commands/curl-get-user-orders]]):
```bash
curl -X GET "https://target.com/orders?user=456" -H "Cookie: session=your_session_cookie"
```

> This command sends a request for user 456's data using your session. Replace the URL, user ID, and session cookie with actual values captured from your legitimate session. The 'why' is to bypass authorization by directly referencing an unauthorized object.

**Expected Output**: If vulnerable, the response contains data for user 456 (e.g., JSON with orders or HTML rendering their profile). If not vulnerable, expect a 403 Forbidden or empty results.

### Step 3: Verify and Document Unauthorized Access

**Context**: Analyze the response to confirm it includes data not belonging to your account, such as another user's name, email, or sensitive details. This validates the IDOR and assesses impact.

Compare against your own data request (repeat Step 2 with your ID). If using [[tools/Burp-Suite]], repeat the request in Repeater to test multiple IDs efficiently.

**Expected Output**: Leaked information, e.g., {"user_id":456, "orders":["Item A", "Item B"], "email":"victim@example.com"}.

**Success Indicators**:
- Response includes data for the manipulated ID without permission errors.
- No rate limiting or additional auth prompts triggered.
