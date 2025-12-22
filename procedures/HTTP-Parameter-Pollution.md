---
id: 2bab2eea-1488-472c-8f69-c90b1afc3439
name: HTTP Parameter Pollution
type: procedure
verified: true
submitted: true
created_at: '2020-08-03T18:05:48.202895+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - '[[tags/HPP]]'
  - '[[tags/Parameter Pollution]]'
  - '[[tags/Web Applications]]'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
commands:
  - '[[commands/curl-normal-parameter-request]]'
  - '[[commands/curl-parameter-pollution-request]]'
tools: []
validated: true
---

# HTTP Parameter Pollution

## Summary

HTTP Parameter Pollution (HPP) is a web application vulnerability that exploits how servers and applications handle multiple instances of the same parameter name in HTTP requests. When an attacker appends duplicate parameters, the application may process only the first, last, or a combination of values, leading to unintended behavior such as bypassing input validation, altering data processing, or manipulating application logic like vote casting in the example scenario.

## Description

In web applications, HTTP requests often include query parameters (e.g., ?movie=4) that influence server-side processing. Different web servers (e.g., Apache vs. IIS) and frameworks parse these parameters variably: some concatenate values with commas, others take the first or last occurrence. HPP abuses this by sending requests like ?movie=4&movie=1, potentially tricking the application into using the attacker's intended value. This technique is commonly used against poorly sanitized inputs in features like search, voting, or authentication flows. In the target scenario, a voting system for movies can be manipulated to redirect votes from one option to another, demonstrating logic bypass without authentication escalation.

## Requirements

1. Network access to the target web application (e.g., via browser or HTTP client).
2. Ability to craft and send custom HTTP requests, such as using curl, browser developer tools, or a proxy like Burp Suite.
3. Knowledge of the application's parameter structure, identified through normal usage or reconnaissance.
4. A vulnerable endpoint that processes query parameters without proper multi-value handling.

## Defense

Defensive measures and detection strategies:

- Implement strict parameter parsing in the application code to handle all occurrences explicitly (e.g., always use the first value or reject duplicates).
- Use web application firewalls (WAFs) with rules to detect and block requests containing duplicate parameter names.
- Perform input validation and sanitization on the server side, logging anomalous requests for review.
- Employ frameworks like OWASP ESAPI that natively handle multi-value parameters securely.

## Objectives

1. Identify if the target application is vulnerable to HPP by observing behavior changes with duplicate parameters.
2. Manipulate application logic, such as altering vote targets in a polling system.
3. Demonstrate potential for broader impacts like bypassing filters or injecting malicious data.
4. Validate success through observable changes in application output or state.

## Instructions

### Step 1: Establish Normal Parameter Behavior

**Context**: First, send a standard HTTP request with a single instance of the target parameter to understand the baseline application response. This confirms the endpoint's normal processing, such as casting a vote for a specific movie ID.

**Command** ([[commands/curl-normal-parameter-request]]):
```bash
curl "http://target.com/vote?movie=4"
```

> This command sends a GET request to the voting endpoint with movie=4. The application should process this as a vote for the 4th movie. Why: Establishes expected behavior for comparison. Expected output: A success response indicating the vote was cast for movie 4, such as a confirmation message or updated vote count visible in the application.

### Step 2: Introduce Parameter Pollution

**Context**: Append a duplicate parameter with a different value to pollute the request. If the application takes the last occurrence (common in some parsers), it will override the original value, redirecting the vote to the attacker's choice (e.g., movie 1). This step exploits the parsing ambiguity.

**Command** ([[commands/curl-parameter-pollution-request]]):
```bash
curl "http://target.com/vote?movie=4&movie=1"
```

> This sends the polluted request. Why: Tests if the server prioritizes the second 'movie' value, bypassing the intended input. Expected output: A success response showing the vote was cast for movie 1 instead of 4, verifiable by checking the application's vote tally or response body. If no change occurs, the application may be using the first value or rejecting duplicates—try POST requests or other parameters.

### Step 3: Verify and Iterate

**Context**: Compare the outcomes and iterate on other parameters or methods (e.g., POST body pollution) if needed. Use application feedback or logs to confirm exploitation.

**Instructions**: Refresh the application page or query the vote results endpoint to observe the manipulated state. If using a proxy, inspect the full request/response cycle for anomalies. Decision point: If the vote redirected successfully, the vulnerability is confirmed; otherwise, test with different parameter orders or encodings (e.g., %26movie%3D1 for URL encoding).

> Expected output: Updated application state reflecting the polluted value (e.g., vote count for movie 1 increased). Success criteria: Clear evidence of logic manipulation without errors.
