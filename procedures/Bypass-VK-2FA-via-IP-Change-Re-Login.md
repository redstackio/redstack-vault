---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - 2fa-bypass
  - authentication-bypass
  - improper-authentication
  - session-hijacking
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:47.751Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Bypass VK 2FA via IP Change Re-Login

## Summary

This procedure exploits a vulnerability in VK.com's IP address change detection and re-login process, where insufficient user identity verification allows bypassing two-factor authentication (2FA). By triggering an IP change and responding to the re-login prompt with only basic credentials, an attacker can regain full account access without re-verifying 2FA, leading to unauthorized control over the account.

## Description

The attack targets VK.com's session management, which prompts re-authentication upon detecting an IP address change to prevent session hijacking. However, the re-login flow fails to enforce full 2FA checks, relying instead on partial session validation. This loophole was identified through manual testing of re-login behaviors. The procedure assumes the attacker has initial valid credentials and can manipulate their IP. Expected outcomes include account takeover, enabling actions like data exfiltration or profile modification. Prerequisites include a web browser for session handling and network tools to change IP addresses.

## Requirements

1. Valid VK.com account credentials (username/password)
2. Enabled 2FA on the target account
3. Ability to change IP address (e.g., VPN software or network switch)
4. Web browser with developer tools for session inspection

## Defense

Defensive measures and detection strategies:

- Implement strict 2FA enforcement on all re-authentication flows, including IP change prompts
- Log and monitor IP address changes with anomaly detection (e.g., rapid IP switches)
- Use device fingerprinting alongside IP checks to validate session continuity
- Rate-limit re-login attempts to prevent abuse

## Objectives

1. Bypass 2FA verification during IP-induced re-login
2. Restore full session access to the target account
3. Enable unauthorized actions without additional authentication

## Instructions

### Step 1: Establish Initial Authenticated Session

**Context**: Log in normally to create a baseline session bound to the current IP, setting up the context for the IP change trigger.

Navigate to https://vk.com in your browser and enter the target's username and password. Complete the 2FA code verification when prompted to establish a full session.

> Upon success, you should see the VK.com dashboard with full access. Use browser developer tools (F12) to inspect and note session cookies (e.g., remixtc, vk_id) for later reference.

### Step 2: Trigger IP Address Change

**Context**: Simulate a session hijacking scenario by changing the IP, activating VK.com's re-validation without proper safeguards.

While the session is active, disconnect from your current network and connect to a new one (e.g., start a VPN to a different country or switch to mobile data). Refresh the VK.com page or attempt a session-sensitive action like editing profile information.

> VK.com will detect the IP mismatch and redirect to a re-login page. This step confirms the trigger without yet exploiting the bypass.

### Step 3: Execute Re-Login Bypass

**Context**: Exploit the flawed verification by submitting credentials on the re-login prompt, skipping 2FA due to insufficient checks.

On the re-login interface, enter the username and password again but do not provide a 2FA code. Submit the form directly.

> The session should restore using residual cookie data and basic auth, granting access without 2FA. If successful, test by performing a restricted action like changing the account email.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- 2fa-bypass
- authentication-bypass
- web-exploit
