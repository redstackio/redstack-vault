---
id: a1aafff6-3c98-499f-af2a-47624ca33779
name: otp-bypass-through-response-manipulation
type: procedure
verified: true
submitted: true
created_at: '2020-08-18T11:39:10.802616+00:00'
updated_at: '2023-05-26T01:34:52.133914+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - authentication-bypass
  - otp
  - web-applications
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# OTP Bypass Through Response Manipulation

## Summary

This procedure demonstrates how to bypass one-time password (OTP) verification during account creation by intercepting and manipulating the server's HTTP response using a proxy tool like Burp Suite. By altering the response status code and body to simulate a successful verification, an attacker can create an account without providing a valid OTP, exploiting improper server-side validation.

## Description

In web applications that rely on OTP for user registration, the server typically validates the OTP sent via email or SMS. This procedure targets a vulnerability where the client-side or proxy-intercepted response can be tampered with to trick the application into accepting an invalid OTP. The attack involves creating a legitimate account to understand the success response format, then replicating that format for a victim account using an incorrect OTP. This is a business logic flaw often found in applications with weak response validation, allowing unauthorized account creation. The technique is applicable to any web-based registration flow using OTP without robust server-side checks.

## Requirements

1. Access to the target web application's registration endpoint (e.g., via browser).
2. A proxy tool like [[tools/Burp-Suite]] configured to intercept HTTP traffic.
3. Valid email addresses for testing (e.g., attacker-controlled emails like abc123@gmail.com and victim123@gmail.com).
4. Network access to the application without restrictions on request interception.
5. Basic understanding of HTTP requests/responses and JSON payloads.

## Defense

Defensive measures and detection strategies:

- Implement server-side OTP validation that does not rely on client responses; always re-verify OTP on the server before proceeding.
- Use HTTPS to encrypt traffic and prevent interception (though this procedure assumes a proxy setup, which may bypass via MITM).
- Monitor for anomalous response patterns or proxy-like delays in application logs.
- Rate-limit registration attempts and log all OTP validation failures.
- Employ web application firewalls (WAFs) to detect response manipulation attempts.

## Objectives

1. Capture and understand the structure of a successful OTP verification response.
2. Intercept and modify a failed OTP response to mimic success, bypassing validation.
3. Successfully create an account for a target email without a valid OTP.
4. Gain unauthorized access to the application via the bypassed registration.

## Instructions

### Step 1: Create a Test Account with Valid OTP

**Context**: Register a test account using a controlled email to receive a legitimate OTP and capture the successful verification response. This establishes the baseline for response manipulation.

Navigate to the application's registration page. Enter the test email (e.g., abc123@gmail.com) and submit to trigger OTP delivery. Check the email for the OTP code, then enter it in the verification field and submit.

Configure [[tools/Burp-Suite]] as a proxy to intercept the OTP submission request. Right-click the request in Burp's Proxy history and select "Do Intercept > Response to this request" to capture the server's response.

**Expected Output**: HTTP 200 OK response with a JSON body indicating successful account creation, such as {"status": "success", "message": "Account created"}.

### Step 2: Analyze the Successful Response

**Context**: Examine the captured success response to note key elements like status code, headers, and body structure, which will be replicated in the manipulation step.

In Burp Suite's Interceptor, observe the response details: status code (e.g., HTTP/1.1 200 Created), content-type (application/json), and body (e.g., empty object {} or success message).

Document the exact format for later use, ensuring no unique tokens or signatures are present that could invalidate the manipulation.

**Expected Output**: Clear view of the response body and headers in Burp, confirming elements like empty JSON {} for success.

### Step 3: Attempt Victim Account Creation with Invalid OTP

**Context**: Initiate registration for the target (victim) email with an incorrect OTP to trigger a failure response, setting up for interception and modification.

Return to the registration page and enter the victim email (e.g., victim123@gmail.com) to receive an OTP. Intentionally enter a wrong OTP code and submit the verification.

Ensure Burp Suite is intercepting: capture the request in Proxy, then right-click and select "Do Intercept > Response to this request" to hold the failure response.

**Expected Output**: HTTP 400 Bad Request response with an error body, such as {"error": "Invalid OTP"}.

### Step 4: Manipulate the Response to Simulate Success

**Context**: Modify the intercepted failure response to match the successful format from Step 1, tricking the client application into proceeding as if verification passed.

In Burp's Interceptor, edit the response:
- Change the status line from "HTTP/1.1 400 Bad Request" to "HTTP/1.1 200 Created".
- Replace the error body (e.g., {"error": "Invalid OTP"}) with an empty JSON object {} or the exact success body from Step 1.
- Ensure headers like Content-Length are updated to match the new body size.

Forward the modified response and observe the application's behavior.

**Expected Output**: The application proceeds to the success page or dashboard, confirming the victim account has been created without valid OTP verification.

### Step 5: Verify Account Creation

**Context**: Confirm the bypass worked by attempting to log in to the new account or checking application logs/emails.

Use the victim email and a default or set password to log in. If successful, the bypass is complete.

**Expected Output**: Successful login or account confirmation, indicating unauthorized access achieved.
