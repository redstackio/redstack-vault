---
id: 9d6b06d7-45ad-4b26-b8ed-748afc366205
name: Demonstrate-Credentials-Exposure-in-GET-Login-Forms
type: procedure
verified: true
submitted: true
created_at: '2020-07-22T18:04:12.377007+00:00'
updated_at: '2023-05-26T01:05:23.567944+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Unsecured Credentials]]'
sub_techniques: []
tags:
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/Sensitive Data Exposure]]'
  - '[[tags/Web Applications]]'
  - get-method
  - credential-exposure
commands:
  - '[[commands/curl-simulate-get-login-request]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: beginner
impact_level: high
detection_risk: low
validated: true
---

# Demonstrate-Credentials-Exposure-in-GET-Login-Forms

## Summary

This procedure demonstrates how using the GET method in a web login form exposes usernames and passwords in plain text within browser history, referrer headers, and web server access logs, violating secure transmission practices and enabling easy credential harvesting by attackers or auditors.

## Description

Web applications that use GET requests for login forms append sensitive data like usernames and passwords directly to the URL as query parameters. This design flaw leads to credential exposure in multiple vectors: browser history retains the full URL, server access logs record the requests, and intermediary systems (like proxies) can log or cache them. This is a common OWASP Top 10 issue under Sensitive Data Exposure (A3:2017). The procedure simulates and verifies this exposure using proxy interception and command-line requests, assuming a target web application with a vulnerable login endpoint. It requires basic web proxy setup and access to the target or a test environment. Successful execution reveals how credentials persist in non-secure locations, aiding in vulnerability assessment and secure coding education.

## Requirements

1. Access to a web browser (e.g., Firefox or Chrome) with proxy configuration capabilities.
2. Burp Suite or similar proxy tool installed for request interception.
3. curl command-line tool for simulating requests (available on most Unix-like systems).
4. Target web application with a GET-based login form (e.g., http://target.com/login?username=...&password=...).
5. Optional: Administrative access to the web server to view access logs (e.g., /var/log/apache2/access.log).

## Defense

Defensive measures and detection strategies:

- Enforce POST method for all authentication forms to keep credentials out of URLs.
- Implement HTTPS to encrypt traffic, though it doesn't prevent history/log exposure.
- Configure web servers to avoid logging query strings in access logs (e.g., Apache CustomLog format without %q).
- Use browser security headers like HSTS and educate users on clearing history.
- Monitor for anomalous access patterns in logs using tools like ELK Stack or Splunk.

## Objectives

1. Intercept and analyze a login request to confirm GET method usage.
2. Verify credential persistence in browser history.
3. Demonstrate logging of credentials on the server side.
4. Highlight remediation steps to prevent exposure.

## Instructions

### Step 1: Configure Proxy for Request Interception

**Context**: Set up a proxy like Burp Suite to capture traffic and observe how the login form transmits data via GET, revealing credentials in the URL.

Use [[tools/Burp-Suite]] to intercept browser traffic. Configure your browser to proxy through Burp (default: 127.0.0.1:8080). Navigate to the target's login page without submitting yet.

**Expected Output**: Burp's Proxy tab shows incoming HTTP requests to the login endpoint, but no credentials yet.

### Step 2: Submit Login Form and Intercept Request

**Context**: Perform the login action to trigger the GET request, allowing inspection of the exposed parameters.

Enter test credentials (e.g., username: admin, password: password123) in the login form and submit. In Burp, intercept the request and forward it.

**Command** (alternative simulation using [[commands/curl-simulate-get-login-request]]):
```bash
curl "http://$_TARGET_URL/login?$_USERNAME=admin&$_PASSWORD=password123" -v
```

> This command replicates the GET request, displaying the full URL with credentials in the terminal output. The -v flag shows verbose details, including the request line with query parameters. In a real browser, the same URL would appear in Burp's history.

**Expected Output**: Intercepted request shows: GET /login?username=admin&password=password123 HTTP/1.1. Response may indicate login success or failure, but the URL exposure is confirmed.

### Step 3: Verify Exposure in Browser History

**Context**: Check the browser's history to confirm that the full URL with credentials is stored in plain text, accessible to anyone using the device.

After submission, open the browser's history (Ctrl+H in most browsers) and search for the login URL.

**Expected Output**: History entry displays the complete URL: http://target.com/login?username=admin&password=password123, with credentials visible.

### Step 4: Check Web Server Access Logs

**Context**: If you have server access (e.g., in a test environment), inspect logs to show how credentials are recorded, enabling post-incident harvesting.

Access the server's access log file (e.g., tail -f /var/log/apache2/access.log on Linux) and trigger the login request again.

**Expected Output**: Log entry like: 192.168.1.100 - - [date] "GET /login?username=admin&password=password123 HTTP/1.1" 200 1234, with credentials in the query string.

### Step 5: Validate and Remediate

**Context**: Confirm the exposure and note remediation to ensure the procedure educates on secure practices.

Review all vectors (intercept, history, logs). If credentials are exposed, recommend switching to POST and sanitizing logs.

**Expected Output**: Documentation of exposure points, with no credentials in URLs for fixed forms.
