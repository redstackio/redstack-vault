---
id: proc-uuid-1
tags:
  - authentication
  - web-access
  - coinbase
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:01.703Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-and-Initiate-Money-Request-on-Coinbase

## Summary

This procedure outlines logging into a Coinbase account, navigating to the transactions page, and initiating a money request to prepare for capturing the HTTP POST request, setting the stage for rate limit bypass and enumeration attacks.

## Description

In the context of exploiting Coinbase's web application, authentication provides access to user-specific features like money requests. The procedure targets the /transactions page where requests are managed. Expected outcomes include a submittable form that triggers a POST to /transactions/request_money, which lacks rate limiting, allowing subsequent replays. Prerequisites include valid Coinbase credentials and a proxy like Burp Suite configured to intercept traffic.

## Requirements

1. Valid Coinbase account credentials (email and password).
2. Web browser with proxy support (e.g., Firefox configured for Burp).
3. Network access to https://coinbase.com.

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to secure logins.
- Monitor login attempts and unusual session activity for anomalies.

## Objectives

1. Gain authenticated access to the transactions interface.
2. Initiate a baseline money request for request capture.
3. Prepare the environment for request interception and modification.

## Instructions

### Step 1: Log In to Coinbase

**Context**: Authenticate to access protected features like money requests.

Navigate to https://coinbase.com and enter credentials.

**Expected Output**: Redirect to dashboard upon successful login.

### Step 2: Navigate to Transactions Page

**Context**: Access the page where money requests are initiated and viewed.

Click on the "Transactions" tab or visit https://coinbase.com/transactions directly.

**Expected Output**: Transactions history and request button visible.

### Step 3: Initiate Money Request Form

**Context**: Prepare a form submission to capture the POST request structure.

Click the "Request Money" button, enter a test email (e.g., your own) in the from field, amount (e.g., 0.001 BTC), and notes (e.g., "Test").

**Expected Output**: Form ready for submission, with fields like transaction[from], transaction[amount], and transaction[notes].

### Step 4: Submit to Trigger Capture

**Context**: Submit the form while proxy is active to intercept the request.

Click submit; ensure Burp Suite is intercepting.

**Expected Output**: POST request captured with parameters including utf8=✓, authenticity_token, and CSRF headers.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- authentication
- web-access
- coinbase
