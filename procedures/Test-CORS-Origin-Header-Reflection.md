---
id: 4ba67c0d-b88b-4138-a4d6-5ee3bcaeb8bd
name: Test-CORS-Origin-Header-Reflection
type: procedure
verified: true
submitted: true
created_at: '2020-08-13T04:45:58.739545+00:00'
updated_at: '2023-05-26T15:57:27.578418+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Active Scanning]]'
sub_techniques: []
tags:
  - CORS
  - Web Applications
commands:
  - '[[commands/curl-test-cors-origin]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
---

# Test-CORS-Origin-Header-Reflection

## Summary

This procedure tests for Cross-Origin Resource Sharing (CORS) misconfigurations in web applications by checking if the server reflects the Origin header in its response. A reflected Origin indicates that the server may accept requests from unauthorized domains, potentially allowing attackers to steal sensitive data like cookies or API responses from authenticated sessions.

## Description

CORS is a security feature that allows web servers to specify which origins can access their resources. A common misconfiguration occurs when the server echoes the client's Origin header in the Access-Control-Allow-Origin response without validation. This procedure demonstrates how to identify such issues using an intercepting proxy like Burp Suite or a simple curl command. It is typically used during web application penetration testing to assess the risk of cross-site request forgery or data exfiltration. The test requires an authenticated session, as CORS policies often apply to protected endpoints. Successful identification may lead to further exploitation, such as reading responses from a malicious origin.

## Requirements

1. Valid login credentials for the target web application.
2. Access to Burp Suite or curl for sending custom HTTP requests.
3. Network access to the target application (e.g., via browser or command line).
4. Basic understanding of HTTP headers and web proxies.

## Defense

Defensive measures and detection strategies:

- Implement strict CORS policies by explicitly whitelisting trusted origins instead of using wildcard (*) or reflecting the Origin header.
- Use Content Security Policy (CSP) headers to restrict cross-origin requests.
- Monitor application logs for unusual Origin headers from untrusted domains.
- Employ Web Application Firewalls (WAFs) to block requests with suspicious Origin values.

## Objectives

1. Authenticate to the target application and capture a legitimate request.
2. Modify the request to include a custom Origin header and observe the response.
3. Confirm if the Access-Control-Allow-Origin header reflects the custom Origin, indicating a misconfiguration.
4. Assess the potential for data exfiltration from unauthorized origins.

## Instructions

### Step 1: Authenticate to the Application

**Context**: Log in to establish a valid session, as CORS tests often require authenticated requests to protected resources like account pages.

**Instructions**: Open the target web application in a browser configured with Burp Suite as the proxy. Enter your credentials and submit the login form. Ensure the request is intercepted and forwarded to complete authentication.

**Expected Output**: Successful login redirect to the dashboard or account page, with session cookies set.

### Step 2: Intercept a Request to a Protected Endpoint

**Context**: Navigate to a page that makes cross-origin relevant requests, such as the 'myaccount' endpoint, to capture a baseline request for modification.

**Instructions**: After login, browse to the 'myaccount' page. Use Burp Suite's Proxy tab to intercept the GET or POST request. Forward the request and then send it to the Repeater tab for manipulation.

**Expected Output**: The request appears in Repeater with original headers, including any existing Origin if applicable.

### Step 3: Test Origin Header Reflection

**Context**: Add a malicious or arbitrary Origin header to simulate a request from an untrusted domain and check if the server echoes it back.

**Command** ([[commands/curl-test-cors-origin]]):

Use the following curl command as an alternative to Burp for quick testing (replace placeholders with actual values):

```bash
curl -X GET -H "Cookie: $_SESSION_COOKIE" -H "Origin: $_MALICIOUS_ORIGIN" "$_TARGET_URL" -v
```

In Burp Repeater, add the Origin header manually (e.g., Origin: http://evil.com) and send the request.

> This step verifies if the response includes Access-Control-Allow-Origin matching the sent Origin. If reflected, it confirms the misconfiguration.

**Expected Output**: Response headers showing Access-Control-Allow-Origin: http://evil.com (or the custom Origin), indicating the server trusts arbitrary origins.

### Step 4: Verify and Document the Misconfiguration

**Context**: Confirm the vulnerability by testing with multiple Origins and checking if sensitive data can be accessed cross-origin.

**Instructions**: Repeat the test with different Origins (e.g., http://attacker.com). If successful, attempt to read a response that includes sensitive data, such as account details, to gauge impact.

**Expected Output**: Consistent reflection of custom Origins across requests, with no credential or origin validation errors.

**Success Indicators**:
- Access-Control-Allow-Origin header matches the injected Origin.
- No server errors or blocks on arbitrary Origins.
- Ability to fetch protected resources from a simulated malicious site.
