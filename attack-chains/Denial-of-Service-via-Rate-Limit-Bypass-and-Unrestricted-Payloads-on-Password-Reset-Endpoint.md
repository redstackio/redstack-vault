---
id: ac-uuid-123
tags:
  - dos
  - rate-limit-bypass
  - unrestricted-input
  - email-spam
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Password-Reset-Endpoint]]'
  - '[[procedures/Capture-Password-Reset-Request-with-Burp-Suite]]'
  - '[[procedures/Automate-Email-Spam-with-Burp-Intruder]]'
  - '[[procedures/Escalate-to-Server-DoS-with-Large-Payloads]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:48.254Z'
description: >-
  Multi-stage attack exploiting lack of rate limiting and input size
  restrictions on a password reset endpoint to spam emails and cause server
  denial of service.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
  - '[[Endpoint Denial of Service]]'
---
# Denial of Service via Rate Limit Bypass and Unrestricted Payloads on Password Reset Endpoint

Multi-stage attack chain demonstrating exploitation of a web application's password reset functionality to spam victim emails and overload the server, leading to denial of service.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~30-45 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Endpoint] --> B[Capture Request]
    B --> C[Spam Emails]
    C --> D[Overload Server]
    D --> E[DoS Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#f39c12
    style E fill:#e74c3c
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web application with password reset functionality
- Accessible HTTPS endpoint for password reset
- Mail server integration for email delivery

### Initial Access Requirements

- Network access to the target website
- No authentication required (public-facing endpoint)
- Proxy tool configured for request interception

## Detailed Attack Procedures

### Step 1: Access Password Reset Endpoint
procedure: [[procedures/Access-Password-Reset-Endpoint]]

**Objective**: Locate and trigger the password reset functionality to understand the endpoint behavior.

**Instructions**: Manually navigate to the password reset page and submit a test email to confirm the endpoint responds by sending a reset email.

**Expected Output**: Confirmation email sent to the provided address, indicating the POST request is processed.

**Success Indicators**:
- Password reset email received
- No immediate rate limiting observed

### Step 2: Capture Password Reset Request with Burp Suite
procedure: [[procedures/Capture-Password-Reset-Request-with-Burp-Suite]]

**Objective**: Intercept the legitimate password reset request to prepare for automation and modification.

**Instructions**: Configure Burp Suite as a proxy, submit the password reset form, and capture the POST request containing the email parameter.

**Expected Output**: Captured HTTP POST request visible in Burp Suite Proxy history, showing the email field and content-length.

**Success Indicators**:
- Request intercepted successfully
- Email parameter visible for modification

### Step 3: Automate Email Spam with Burp Intruder
procedure: [[procedures/Automate-Email-Spam-with-Burp-Intruder]]

**Objective**: Flood the endpoint with multiple requests to spam the target's email inbox without rate limiting interference.

**Instructions**: Send the captured request to Burp Intruder, configure sniping on the email payload with null or repeated values, and launch the attack to send hundreds of requests rapidly.

**Expected Output**: Multiple password reset emails received in quick succession, demonstrating unlimited spamming capability.

**Success Indicators**:
- Emails arrive in batches (e.g., 100 in 2-3 minutes)
- No blocking or CAPTCHA triggered

### Step 4: Escalate to Server DoS with Large Payloads
procedure: [[procedures/Escalate-to-Server-DoS-with-Large-Payloads]]

**Objective**: Overload the server and mail infrastructure by sending oversized payloads, causing resource exhaustion and site unavailability.

**Instructions**: Modify the Intruder configuration to inject large payloads (e.g., 2MB content-length) into the email field, launch 40-50 requests, and monitor for performance degradation.

**Expected Output**: Slowdown in email delivery (e.g., later batches take 25-30 minutes), followed by 503/502 errors and site downtime for 5-10 minutes.

**Success Indicators**:
- Server responses shift to errors
- Website becomes unresponsive
- Mail server delivery delays observed

## Attack Chain Summary

### Key Achievements

1. Successful email inbox spamming without limits, enabling phishing opportunities
2. Resource exhaustion on mail servers, delaying legitimate communications
3. Full denial of service on the web application, rendering it unavailable

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Network Denial of Service]]
- [[Endpoint Denial of Service]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Impact]]

---
*Last updated: 2023-10-01T00:00:00Z*
