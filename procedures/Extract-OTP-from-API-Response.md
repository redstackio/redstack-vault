---
tags:
  - credential-access
  - information-disclosure
  - otp-extraction
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Sniffing]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:32:48.207Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques:
  - '[[Cloud Instance Metadata API]]'
id: d753ef97-de2d-4524-8eae-17858e9a0b54
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Network Sniffing]]'
  - '[[Unsecured Credentials]]'
---
# Extract-OTP-from-API-Response

## Summary

This procedure involves inspecting the intercepted API response from the MTN Group OTP request to extract the leaked one-time password, enabling its use for unauthorized authentication and account takeover.

## Description

After interception, the API response body (typically JSON) from the phone number submission endpoint includes the generated OTP code plainly visible, without encryption or access controls. For example, the response might contain {"otp": "123456", "phone": "+27821234567"}. The attacker copies this OTP and uses it in the application's verification field to complete login or sign-up. This targets the web API in the insurance quote flow, requiring prior traffic capture. Outcomes include full credential access for the target account, leading to potential data theft or further compromise.

## Requirements

1. Captured API response from previous interception
2. Knowledge of the target phone number
3. Access to the OTP entry form in the application

## Defense

Defensive measures and detection strategies:

- Remove OTP from API responses; send only via SMS/secure channels
- Implement response validation to ensure requester matches phone owner
- Audit API logs for mismatched OTP usage

## Objectives

1. Locate and copy the OTP from the response body
2. Authenticate using the extracted OTP
3. Achieve account access without legitimate verification

## Instructions

### Step 1: Inspect Response in Proxy

**Context**: Analyze the captured API response for the OTP field.

In Burp Suite's Proxy or Repeater tab, view the response body after the OTP request submission.

> Look for JSON keys like "otp" or "code"; the value is the 6-digit OTP sent to the phone.

### Step 2: Use OTP for Authentication

**Context**: Enter the extracted OTP into the application to bypass verification.

Return to the OTP entry screen and input the code from the response.

> The application accepts the OTP, granting access to the account associated with the phone number.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Network Sniffing]] Network Sniffing
- [[Unsecured Credentials]] Unprotected Service

### Sub-Techniques

- [[Cloud Instance Metadata API]] Unsecured Credentials

## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[credential-access]]
- [[information-disclosure]]
- [[otp-extraction]]
