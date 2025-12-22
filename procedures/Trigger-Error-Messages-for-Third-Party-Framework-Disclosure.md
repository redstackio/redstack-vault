---
id: b104bb3a-2855-4894-99d3-e557dc6abe12
name: Trigger-Error-Messages-for-Third-Party-Framework-Disclosure
type: procedure
verified: true
submitted: true
created_at: '2020-07-28T15:48:31.313898+00:00'
updated_at: '2023-05-26T18:18:05.854995+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Client Configurations]]'
sub_techniques: []
tags:
  - information-disclosure
  - injection
  - owasp-top-10
  - web-applications
commands:
  - '[[commands/curl-send-malformed-parameter-request]]'
platforms:
  - Web
tools: []
validated: true
---

# Trigger-Error-Messages-for-Third-Party-Framework-Disclosure

## Summary

This procedure identifies and exploits parameter validation weaknesses in web applications to trigger error messages that disclose third-party framework details, such as the Apache Struts version. By modifying numeric parameters to strings, attackers can force exceptions that leak technology stack information, aiding in reconnaissance for targeted exploits like known vulnerabilities in the disclosed framework.

## Description

Web applications often expose sensitive information through unsanitized error messages when invalid input is provided. This technique targets parameters expecting numeric values (e.g., product IDs) by injecting string values, causing type mismatch errors. In the observed scenario, altering an 'id' parameter from a number to a string in a product endpoint reveals the backend use of Apache Struts and its specific version (e.g., 2.5.x). This disclosure enables attackers to research framework-specific vulnerabilities, such as remote code execution flaws, and chain them with other attacks. The procedure assumes a public-facing web app and focuses on manual or proxied request manipulation. Success depends on the application's error handling; generic errors reduce effectiveness, while verbose ones provide actionable intel.

## Requirements

1. Network access to the target web application (no authentication required for public endpoints).
2. Tools for request interception and modification, such as a browser developer console or proxy like Burp Suite.
3. Basic knowledge of HTTP requests and parameter tampering.
4. A wordlist of common string injections (e.g., 'abc', 'test') to test variations.

## Defense

Defensive measures and detection strategies:

- Implement custom error pages that log exceptions internally without exposing stack traces or framework details to users.
- Enforce strict input validation and sanitization on all parameters, rejecting non-numeric inputs for numeric fields with generic messages.
- Enable web application firewall (WAF) rules to detect and block anomalous parameter types (e.g., strings in ID fields).
- Monitor application logs for frequent error triggers on specific endpoints, indicating potential reconnaissance attempts.

## Objectives

1. Identify endpoints with numeric parameters vulnerable to type injection.
2. Trigger and capture error responses revealing third-party framework names and versions.
3. Gather intelligence on the technology stack to inform subsequent attack planning, such as targeting known CVEs.
4. Validate the disclosure without causing denial-of-service.

## Instructions

### Step 1: Identify Target Endpoint and Parameters

**Context**: Examine the web application's pages or API endpoints to locate parameters that expect numeric values, such as 'productid' or 'id' in query strings or form data. This step establishes the baseline request structure for modification.

Use browser developer tools or a proxy to inspect network traffic. Look for GET/POST requests to pages like product details.

**Expected Output**: A normal response rendering the page with valid numeric parameter (e.g., HTTP 200 with product info for id=123).

### Step 2: Send Baseline Request with Valid Parameter

**Context**: Confirm the endpoint behaves correctly with a numeric value to establish expected behavior before tampering. This verifies the parameter's role and response format.

**Command** ([[commands/curl-send-malformed-parameter-request]]):

```bash
curl -X GET "$_TARGET_URL?id=$_NUMERIC_VALUE" -v
```

> This sends a standard request to the endpoint. Replace $_TARGET_URL with the full endpoint (e.g., http://target.com/product) and $_NUMERIC_VALUE with a valid number (e.g., 123). The -v flag provides verbose output including headers and response code.

**Expected Output**: Successful response (HTTP 200) displaying application content without errors, confirming the parameter is processed as numeric.

### Step 3: Modify Parameter to String and Send Request

**Context**: Inject a string value into the numeric parameter to force a type conversion error, triggering a verbose exception that may disclose framework details. Common strings like 'abc' or non-numeric text often cause backend parsing failures.

**Command** ([[commands/curl-send-malformed-parameter-request]]):

```bash
curl -X GET "$_TARGET_URL?id=$_STRING_VALUE" -v
```

> Modify the request by changing $_NUMERIC_VALUE to $_STRING_VALUE (e.g., 'abc'). Observe the response for error details. If using a proxy like Burp Suite, intercept and edit the request inline. Retry with variations if the first attempt yields a generic error.

**Expected Output**: HTTP error response (e.g., 500 Internal Server Error) containing stack trace or message like "org.apache.struts2.StrutsException: Invalid id format" revealing Apache Struts and version (e.g., 2.5.12).

### Step 4: Analyze and Document Disclosure

**Context**: Review the error output for specific indicators of third-party frameworks, versions, or other leaks (e.g., library paths). This step validates the intelligence gathered and plans next actions, such as searching for CVEs.

Parse the response body for keywords like 'Struts', 'Apache', or version numbers. Save the full response for reference.

**Expected Output**: Extracted details, e.g., "Framework: Apache Struts 2.5.x", confirming disclosure success.

**Success Indicators**:
- Error message includes framework name and version.
- No generic "Invalid input" without technical details.
