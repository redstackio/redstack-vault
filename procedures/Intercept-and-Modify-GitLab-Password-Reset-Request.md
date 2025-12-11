---
tags:
  - gitlab
  - improper-access-control
  - web-exploitation
  - account-takeover
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Content-Type-Converter]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 96fe0a6d-989b-4da3-9c80-990c81d066c2
created_at: '2025-12-11T03:48:06.091Z'
updated_at: '2025-12-11T03:48:06.091Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Intercept and Modify GitLab Password Reset Request

## Summary

This procedure exploits an improper access control vulnerability in GitLab's password reset functionality by intercepting and modifying the reset request to include an array of emails, causing the reset link to be sent to an attacker-controlled address.

## Description

The attack targets the password reset endpoint, which accepts JSON payloads and processes email arrays without validation. By using Burp Suite to intercept and alter the request, an attacker can receive the reset link for a victim's account, enabling account takeover. This requires knowledge of the victim's email and access to the GitLab web interface. The expected outcome is receipt of the reset link without victim interaction.

## Requirements

1. Burp Suite installed and configured for proxy interception
2. Content-Type Converter extension installed in Burp Suite
3. Victim's email address known
4. Attacker-controlled email address
5. Network access to the GitLab instance

## Defense

Defensive measures and detection strategies:

- Implement strict input validation on password reset endpoints to reject array inputs
- Monitor for anomalous password reset requests with multiple emails or unusual payloads
- Use rate limiting and CAPTCHA on reset forms to prevent automated exploitation

## Objectives

1. Intercept and modify the password reset request to include attacker email
2. Cause the server to send reset link to attacker
3. Enable subsequent account takeover

## Instructions

### Step 1: Access Password Reset Form

**Context**: Begin by navigating to the password reset page on GitLab.

Access the 'Forgot Your Password?' link via the web interface.

> This loads the form for email submission.

### Step 2: Submit and Intercept Request

**Context**: Submit the form with the victim's email and capture the request.

Enter victim@gmail.com and intercept using [[tools/Burp-Suite]].

> The request is captured for editing.

### Step 3: Convert Request to JSON

**Context**: Change the request format to allow JSON modification.

Right-click in Burp Suite and select Extensions -> [[tools/Content-Type-Converter]] -> Convert to JSON.

> Payload is now in JSON format.

### Step 4: Modify Email Parameter to Array

**Context**: Edit the JSON to include an email array.

Replace the email parameter with: {'user': {'email': ['victim@gmail.com', 'attacker@gmail.com']}}.

> This tricks the endpoint into sending to both emails.

### Step 5: Forward the Modified Request

**Context**: Send the altered request to the server.

Forward the request using [[tools/Burp-Suite]].

> Server processes and sends reset emails.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Content-Type-Converter]]

## Tags

- gitlab
- improper-access-control
