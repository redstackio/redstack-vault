---
id: cc26c9d0-cbf1-4c75-b5f0-f6cdf7a820dc
name: Test-Email-Verification-Rate-Limiting-Bypass-with-Burp-Intruder
type: procedure
verified: true
submitted: true
created_at: '2020-08-22T16:05:02.699695+00:00'
updated_at: '2023-05-26T01:24:42.204031+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Direct Network Flood]]'
sub_techniques: []
tags:
  - rate-limiting
  - web-applications
  - email-verification
  - brute-force
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

# Test-Email-Verification-Rate-Limiting-Bypass-with-Burp-Intruder

## Summary

This procedure demonstrates how to test for the absence of rate limiting in a web application's email verification feature by repeatedly sending confirmation link requests using Burp Suite's Intruder tool. It simulates an attacker flooding the system with requests to generate excessive emails, highlighting potential denial-of-service or spam vulnerabilities if no limits are enforced.

## Description

Many web applications include email verification flows to confirm user accounts, but without rate limiting, attackers can abuse this feature to send unlimited confirmation emails. This could lead to resource exhaustion on the email server, increased costs, or spam delivery to users. The procedure uses Burp Suite to intercept and replay the request multiple times, observing response codes and real-world effects like multiple emails received. It targets public-facing web apps with 'Forgot Password' or email confirmation endpoints. Prerequisites include a valid user email in the system and network access to the application. Successful execution reveals 200 OK responses for all requests without throttling, confirming the vulnerability.

## Requirements

1. Burp Suite Professional or Community Edition installed and running with a proxy listener configured (default port 8080).
2. Browser configured to proxy traffic through Burp (e.g., via FoxyProxy or system proxy settings).
3. Access to the target web application with an email verification or confirmation feature.
4. A test email account to monitor incoming verification emails.
5. Basic knowledge of HTTP requests and Burp Suite navigation.

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on email-related endpoints (e.g., using libraries like Flask-Limiter or nginx rate limiting modules) to cap requests per IP or user (e.g., 5 requests per minute).
- Monitor email sending logs for unusual spikes in volume from single sources, using tools like ELK Stack or Splunk to alert on thresholds.
- Require CAPTCHA or secondary authentication (e.g., SMS) after a few failed or repeated attempts.
- Use email service providers with built-in abuse prevention, such as AWS SES with suppression lists.

## Objectives

1. Intercept and identify the email confirmation request payload.
2. Replay the request multiple times to test for throttling.
3. Confirm the absence of rate limiting by observing consistent successful responses and increased email volume.
4. Document the vulnerability for remediation reporting.

## Instructions

### Step 1: Access the Email Verification Feature

**Context**: Navigate to the application's email verification or forgot password page to initiate a legitimate request, setting the stage for interception.

Launch your browser with Burp proxy enabled and go to the target application's email verification endpoint (e.g., /verify-email or /forgot-password). Enter a test email address associated with your monitoring inbox and submit the form to trigger the confirmation link request.

> Ensure Burp's Proxy tab is intercepting traffic; turn on interception if needed via the Intercept button.

### Step 2: Intercept and Capture the Request

**Context**: Use Burp's proxy to capture the POST request sent during email submission, allowing modification and replay.

With interception on, submit the form again. In the Burp Proxy > Intercept tab, review the captured HTTP POST request, which should include parameters like email=yourtest@example.com. Forward the request to complete the initial submission, then right-click the request in the Proxy > HTTP History tab and select "Send to Intruder" to prepare for automated replay.

> Expected: A single verification email arrives in your inbox, confirming the endpoint works.

### Step 3: Configure Intruder Payload Positions

**Context**: Mark positions in the request for payload insertion to simulate variations, though for rate limiting tests, a simple repeat without changes suffices to check throttling.

In the Burp Intruder tab, go to Positions and clear default positions with Clear §. Add payload positions around a non-essential parameter (e.g., a timestamp or nonce if present) or simply use the entire request body for repetition. Set the payload type to "Null payloads" or a simple incrementing number (e.g., Positions: add § before and after a dummy value like '1'). This allows sending identical requests multiple times.

> No specific command; this is GUI-based configuration in Burp.

### Step 4: Set Payload Options and Start the Attack

**Context**: Define the number of attacks to simulate high-volume requests and execute to observe responses.

In the Payloads tab, configure a simple payload set (e.g., numbers 1-100 for 100 requests). Set attack type to "Sniper" if positions are marked, or use defaults for repetition. Click "Start attack" to launch. Monitor the Intruder results table for response codes, lengths, and timings.

> Expected: All or most requests return 200 OK status without delays or errors, indicating no rate limiting.

### Step 5: Validate and Observe Outcomes

**Context**: Check the results for success patterns and verify real-world impact by monitoring email inbox.

Review the Intruder results: Look for consistent 200 responses across all threads, short response times (<1s), and no 429 Too Many Requests or similar errors. Simultaneously, check your test email inbox for a flood of verification emails matching the request count.

> Success: Multiple emails received (e.g., 50+ in quick succession) with no application-side blocking.

## Expected Output

- Burp Intruder results showing 200 OK for all requests, with response lengths consistent and no increasing delays.
- Sample response body: JSON or HTML confirming email sent, e.g., {"message": "Confirmation link sent to your email."}.
- In the email inbox: Repeated identical verification emails arriving rapidly, demonstrating the bypass.
