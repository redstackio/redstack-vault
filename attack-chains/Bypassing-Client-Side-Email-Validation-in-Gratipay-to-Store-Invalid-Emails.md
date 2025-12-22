---
id: ac-gratipay-email-bypass-001
tags:
  - input-validation
  - web-vulnerability
  - email-bypass
  - request-interception
type: attack_chain
tools:
  - '[[tools/Burp-Repeater]]'
  - '[[tools/Live-HTTP-Headers]]'
  - '[[tools/Tamper-Data]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Intercept-and-Modify-Email-Addition-Request]]'
step_count: 6
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:10.731Z'
description: >-
  A multi-step attack exploiting the absence of server-side validation in
  Gratipay's email settings, allowing storage of malformed or oversized email
  addresses via HTTP request interception, leading to potential email delivery
  issues and high bounce rates.
skill_level: intermediate
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypassing Client-Side Email Validation in Gratipay to Store Invalid Emails

Multi-stage attack chain demonstrating how to exploit improper input validation in Gratipay's user email settings by intercepting and modifying HTTP requests, bypassing client-side checks to store invalid or excessively long email addresses. This can lead to high email bounce rates (e.g., 13.58% observed with Mandrill) and potential service disruptions, though no direct security compromise like account takeover is achieved.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Navigate to Settings] --> B[Client-Side Validation Test]
    B --> C[Intercept Valid Request]
    C --> D[Modify to Invalid Email]
    D --> E[Replay Modified Request]
    E --> F[Length Limit Bypass Test]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Repeater]]
- [[tools/Live-HTTP-Headers]]
- [[tools/Tamper-Data]]

### Target Environment

- Web platform (Gratipay application)
- Required services: Gratipay user account with access to settings
- Network access: Direct HTTP access to https://gratipay.com

### Initial Access Requirements

- Authenticated user session in Gratipay
- Browser with proxy/interception tool configured (e.g., Burp Suite proxy)
- No special credentials beyond standard user login

## Detailed Attack Procedures

### Step 1: Navigate to Settings

procedure: [[procedures/Intercept-and-Modify-Email-Addition-Request]]

**Objective**: Access the email management section to prepare for validation testing.

**Instructions**: Open a browser and log in to your Gratipay account. Navigate to the settings page at https://gratipay.com/~username/settings/ where username is your account handle. Locate the email addition form.

**Expected Output**: Email management interface loaded, ready for input.

**Success Indicators**:
- Settings page accessible without errors
- Email addition form visible

### Step 2: Test Client-Side Validation

procedure: [[procedures/Intercept-and-Modify-Email-Addition-Request]]

**Objective**: Confirm that direct submission of invalid emails is blocked by client-side JavaScript.

**Instructions**: In the email field, enter an invalid address like 'myemail@gmail.com'' (note the extra quote). Click 'Add E-Mail Address' to submit.

**Expected Output**: Error message displayed, preventing addition due to client-side validation.

**Success Indicators**:
- Submission fails with validation error
- No request sent to server

### Step 3: Add Valid Email and Intercept Request

procedure: [[procedures/Intercept-and-Modify-Email-Addition-Request]]

**Objective**: Capture a legitimate POST request for modification.

**Instructions**: Enter a valid email like 'mail01@gmail.com' in the form and click 'Add E-Mail Address'. Use an interception tool (e.g., [[tools/Burp-Repeater]]) configured as a proxy to capture the POST request to https://gratipay.com/~username/emails/modify.json. The request body should include 'action=add-email&address=mymail%40gmail.com'.

**Expected Output**: Intercepted request visible in the tool, showing URL-encoded valid email.

**Success Indicators**:
- Valid email added successfully
- POST request captured with correct parameters

### Step 4: Modify Request to Invalid Email

procedure: [[procedures/Intercept-and-Modify-Email-Addition-Request]]

**Objective**: Alter the email parameter to inject invalid syntax, bypassing client-side checks.

**Instructions**: In the interception tool, edit the 'address' parameter from 'mymail%40gmail.com' to an invalid value like 'mymail%40gmail.com%22%3E%3Ch1%3E' (URL-encoded form of 'mymail@gmail.com"><h1>'). Ensure the action remains 'add-email'.

**Expected Output**: Modified request ready for replay, with invalid email encoded.

**Success Indicators**:
- Parameter successfully changed without tool errors
- Encoded invalid string verified

### Step 5: Replay Modified Request

procedure: [[procedures/Intercept-and-Modify-Email-Addition-Request]]

**Objective**: Submit the tampered request to store the invalid email on the server.

**Instructions**: Forward or replay the modified POST request to https://gratipay.com/~username/emails/modify.json using the interception tool.

**Expected Output**: Server accepts the request without rejection; invalid email stored in account settings.

**Success Indicators**:
- No server error (e.g., 200 OK response)
- Invalid email appears in settings upon refresh

### Step 6: Bypass Email Length Limits

procedure: [[procedures/Intercept-and-Modify-Email-Addition-Request]]

**Objective**: Test and exploit lack of length validation by submitting an oversized email.

**Instructions**: Repeat the interception process but set the 'address' parameter to a string exceeding 255 characters (RFC limit), e.g., a repeated valid domain padded to 300+ chars, URL-encoded. Replay the request.

**Expected Output**: Oversized email accepted and stored, violating standards.

**Success Indicators**:
- Long email saved without truncation or error
- Potential Mandrill bounce alerts if emails are sent

## Attack Chain Summary

### Key Achievements

1. Successfully bypassed client-side email validation to store malformed addresses like 'mymail@gmail.com"><h1>'.
2. Demonstrated length limit bypass, allowing emails >255 characters.
3. Highlighted risks of high bounce rates (e.g., 13.58% via Mandrill) from invalid data storage.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
