---
id: 01774f0d-8c64-4893-a8a1-98fc91c25402
name: Test-Open-Redirects-Using-Burp-Suite
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T14:16:33.054961+00:00'
updated_at: '2023-05-26T01:23:25.867376+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - open-redirect
  - owasp
  - web-application
  - burp-suite
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
---

# Test-Open-Redirects-Using-Burp-Suite

## Summary

This procedure demonstrates how to test for open redirect vulnerabilities in web applications using Burp Suite. It involves proxying traffic, identifying endpoints that issue 3xx redirects, modifying URL parameters in the Repeater tool, and validating if arbitrary external URLs can be redirected to, which could enable phishing or bypass mechanisms.

## Description

Open redirects occur when a web application accepts a URL as input and redirects the user to it without validation, potentially allowing attackers to craft malicious links for phishing, session hijacking, or circumventing access controls. This technique is commonly tested during web application security assessments, particularly against OWASP Top 10 risks like broken access control. The procedure targets parameters like 'url', 'redirect', or 'next' in login, logout, or error pages. Using Burp Suite's proxy and Repeater, testers can intercept and manipulate requests to confirm if the application allows redirects to untrusted domains. Success indicates a vulnerability that could be chained with social engineering for initial access.

## Requirements

1. Burp Suite Professional or Community Edition installed and running.
2. Web browser (e.g., Firefox or Chrome) configured to use Burp as a proxy (typically localhost:8080).
3. Valid user credentials or public access to the target web application.
4. Network access to the target application without firewall restrictions on outbound HTTP/HTTPS traffic.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and whitelisting for redirect URLs, allowing only internal or trusted domains.
- Use Content Security Policy (CSP) headers to restrict navigation to external sites.
- Monitor application logs for suspicious redirect parameters containing external domains.
- Employ Web Application Firewalls (WAFs) to block requests with unvalidated URL parameters.

## Objectives

1. Identify endpoints in the application that handle redirects via user-supplied URLs.
2. Validate if redirects can be manipulated to point to arbitrary external sites.
3. Confirm the vulnerability by observing successful redirection in a browser.
4. Document vulnerable parameters for further exploitation or reporting.

## Instructions

### Step 1: Log In to the Application

**Context**: Authenticate to the target application to access protected pages where redirects may occur, such as post-login or error handling flows. This ensures you can browse authenticated areas while proxying traffic through Burp.

Configure your browser to route traffic through Burp Suite's proxy (default: 127.0.0.1:8080). Ensure intercept is disabled to allow seamless browsing. Navigate to the login page and enter valid credentials to log in.

> If using Firefox, go to Settings > Network Settings > Manual proxy configuration and set HTTP Proxy to 127.0.0.1 and Port to 8080. Install Burp's CA certificate to handle HTTPS.

### Step 2: Browse the Application and Capture Traffic

**Context**: Proxy all application interactions through Burp to build a site map of requests and responses, focusing on areas likely to contain redirect logic like authentication flows or user profile pages.

With intercept off, browse through various pages of the application, including login/logout, password reset, and any forms that might redirect (e.g., OAuth callbacks). In Burp's Target tab, select the application's domain to view the captured site map in the right panel.

> This step populates Burp's history with all requests, allowing identification of potential redirect points.

### Step 3: Filter for Redirect Responses

**Context**: Isolate responses with 3xx status codes (e.g., 302 Found, 301 Moved Permanently) as these indicate redirect behavior. Filtering helps narrow down to endpoints that process URL parameters for redirection.

In Burp's Target > Site map, apply a filter for HTTP status codes 300-399. Review the filtered list to identify requests with redirect responses, such as those containing 'Location' headers with dynamic URL parameters.

> Common parameters to note: 'url', 'redirect_uri', 'return_url', or 'next'. Look for GET or POST requests where the parameter value is a full URL.

### Step 4: Send a Request to Repeater for Manipulation

**Context**: Use Burp Repeater to modify and resend requests in a controlled environment, allowing precise testing of redirect parameters without affecting the live session.

Right-click on a filtered request in the site map that shows a 3xx response and select 'Send to Repeater'. In the Repeater tab, inspect the request parameters for any URL-related fields.

> Ensure the request is raw HTTP to easily edit parameters. If the redirect is in a POST body, switch to the appropriate view.

### Step 5: Modify the Redirect Parameter and Test

**Context**: Alter the URL parameter to an external, controlled domain (e.g., your own test server) to check if the application blindly redirects without validation. This simulates an attacker's phishing link.

In Repeater, replace the value of the redirect parameter (e.g., url=http://example.com) with a malicious test URL like http://your-test-domain.com/evil. Click 'Send' and observe the response. If it returns a 3xx with the modified Location header, right-click the response and select 'Copy URL' (or manually construct it from the Location header).

> Use a benign test domain you control to avoid accidental redirects to real malicious sites during testing.

### Step 6: Validate the Redirect in Browser

**Context**: Confirm the vulnerability by executing the modified redirect URL in the browser, verifying if the application follows the untrusted redirect. This step proves the issue is exploitable.

Paste the copied or constructed URL into your proxied browser and navigate to it. Observe if the browser is redirected to the test domain. If successful, the page loads from the external site, confirming the open redirect.

> If the redirect fails (e.g., stays on the original site), the parameter may be validated—test variations like URL encoding (e.g., %68%74%74%70://evil.com) or bypassing filters with double URLs (//evil.com).

### Step 7: Document and Report

**Context**: Record the vulnerable endpoint, parameter, and proof-of-concept for remediation or chaining in attacks.

Note the full request/response in Burp, including the original and modified versions. Test for impact, such as bypassing login or enabling phishing.

> If the redirect allows bypassing authentication (e.g., in a login flow), chain it with social engineering for higher impact.
