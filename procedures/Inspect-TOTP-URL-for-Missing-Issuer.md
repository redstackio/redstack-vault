---
id: proc-uuid-inspect-totp-issuer
tags:
  - 2fa
  - totp
  - misconfiguration
  - authentication
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:24:45.511Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Inspect-TOTP-URL-for-Missing-Issuer

## Summary

This procedure involves examining the TOTP URL generated during 2FA setup to detect the absence of the Issuer parameter, which is a required component for proper labeling and management of authentication tokens in software authenticators like Google Authenticator or Authy.

## Description

In scenarios like the Legal Robot platform's 2FA challenge, the TOTP URL for QR code generation may omit the 'Issuer' parameter, violating RFC 6238 standards for time-based one-time passwords. This misconfiguration does not enable unauthorized access but causes practical issues for users, such as unlabeled tokens that are hard to distinguish when multiple accounts are managed. The procedure targets web-based 2FA enrollment flows and requires only observational access during setup. Expected outcomes include confirmation of the flaw and recommendations for remediation by adding the Issuer to the URL (e.g., '&issuer=ServiceName').

## Requirements

1. Access to a user account on the target web platform
2. Ability to initiate the 2FA setup or enrollment process
3. A QR code scanner or browser developer tools to inspect the TOTP URL
4. Basic knowledge of TOTP URL format (otpauth://totp/...?secret=...&issuer=...)

## Defense

Defensive measures and detection strategies:

- Ensure all TOTP URLs include the Issuer parameter during generation to comply with standards
- Implement client-side validation in authenticator apps to warn on missing Issuer
- Monitor 2FA setup logs for incomplete URL parameters and alert developers

## Objectives

1. Detect misconfiguration in TOTP URL structure
2. Assess usability impact on end-users managing 2FA tokens
3. Provide evidence for vulnerability reporting without exploitation

## Instructions

### Step 1: Initiate 2FA Setup

**Context**: Start the 2FA enrollment process to trigger QR code generation, simulating a legitimate user flow.

Log in to the target platform (e.g., Legal Robot) and navigate to the security settings to enable 2FA. Follow the prompts until the QR code is displayed for scanning.

### Step 2: Extract and Inspect TOTP URL

**Context**: Retrieve the underlying TOTP URL from the QR code to analyze its components for the missing Issuer parameter.

Use a QR code decoder (e.g., browser extension or online tool) to scan the QR code and reveal the otpauth URL. Alternatively, inspect the page source or network requests in browser developer tools (F12) for the TOTP secret and URL data. Look for the format: otpauth://totp/[Label]?secret=[SecretKey]&issuer=[IssuerName]. Verify if '&issuer=' is present and properly set to the service name (e.g., 'Legal Robot').

> If missing, the URL will appear as otpauth://totp/user@example.com?secret=ABC123, leading to generic labeling in the authenticator app.

### Step 3: Validate Impact

**Context**: Test the generated token in an authenticator app to confirm management difficulties.

Scan the QR code into a software authenticator (e.g., Google Authenticator). Observe that the token entry lacks a clear issuer label, making it indistinguishable from other accounts. Attempt to rename manually if possible, noting the extra user effort required.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[2fa]]
- [[totp]]
- [[misconfiguration]]
- [[authentication]]
