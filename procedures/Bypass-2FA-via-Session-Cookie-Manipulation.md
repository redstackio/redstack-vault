---
tags:
  - nextcloud
  - 2fa-bypass
  - cookie-swap
  - session-hijack
type: procedure
tools:
  - '[[tools/requests-Python-Library]]'
  - '[[tools/BeautifulSoup-Python-Library]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/Install-Python-Dependencies-for-Bypass-Script]]'
  - '[[commands/Execute-Nextcloud-2FA-Bypass-Script]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Reversible Encryption]]'
updated_at: '2025-12-14T17:31:52.294Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Reversible Encryption]]'
id: 61c5f4eb-8a78-4b03-9821-ff5862165ece
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Reversible Encryption]]'
---
# Bypass-2FA-via-Session-Cookie-Manipulation

## Summary

This procedure exploits a flaw in Nextcloud's session validation by creating two parallel login sessions with the same credentials and swapping the 'oc_sessionPassphrase' cookie to bypass the 2FA enforcement check, granting access to the user dashboard without setup.

## Description

The vulnerability stems from improper session state validation during 2FA checks, allowing an attacker to manipulate cookies between sessions. This is demonstrated manually via browser dev tools or automated with a Python script using requests and BeautifulSoup to handle logins and cookie extraction. Target: Nextcloud instance with enforced 2FA group. Outcomes include unauthorized access to sensitive data or admin functions.

## Requirements

1. Two separate browser sessions or Python environment
2. Credentials for 'Bypass' user
3. Browser dev tools or Python 3 with libraries installed
4. URL of the Nextcloud instance

## Defense

Defensive measures and detection strategies:

- Implement secure session token binding to prevent swapping
- Monitor for multiple simultaneous logins with same credentials
- Enforce 2FA setup at login without session persistence until complete
- Log cookie modifications and anomalous session behaviors

## Objectives

1. Initiate parallel login sessions
2. Swap 'oc_sessionPassphrase' cookie
3. Gain dashboard access without 2FA

## Instructions

### Step 1: Initiate First Login Session

**Context**: Perform a standard login to generate the initial session cookies.

In the first browser or session, log in with Username: 'Bypass', Password: 'NextCloudEnforcement'. Note the 'oc_sessionPassphrase' cookie value from dev tools (Application > Cookies).

**Expected Output**: Login prompt for 2FA, but cookies generated.

### Step 2: Initiate Second Login Session

**Context**: Start a second session to create a parallel attempt.

In a new browser or incognito window, log in with the same credentials. This will also prompt for 2FA.

### Step 3: Swap Cookies Manually or Automate

**Context**: Replace the cookie in the second session to bypass the check.

Manually: In dev tools of the second session, set 'oc_sessionPassphrase' to the value from the first session, then refresh.

For automation: First, run [[commands/Install-Python-Dependencies-for-Bypass-Script]] to prepare the environment:

```bash
python3 -m pip install requests beautifulsoup4
```

Then execute [[commands/Execute-Nextcloud-2FA-Bypass-Script]] (provide Nextcloud URL, credentials in script):

```bash
python3 bypass.py
```

> The script logs in twice, swaps the cookie, and prints the modified cookies dictionary for import into browser.

**Expected Output**: Printed cookies; upon import and refresh, dashboard access granted.

### Step 4: Access Dashboard

**Context**: Verify bypass success.

With modified cookies, navigate to the dashboard. No 2FA setup required.

**Success Indicators**:
- Dashboard loads
- Session active without 2FA prompt

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Reversible Encryption]] Multi-Factor Authentication Instrument

### Sub-Techniques

- [[Reversible Encryption]] Multi-Factor Authentication Instrument

## Commands Used

- [[commands/Install-Python-Dependencies-for-Bypass-Script]]
- [[commands/Execute-Nextcloud-2FA-Bypass-Script]]

## Tools Used

- [[tools/requests-Python-Library]]
- [[tools/BeautifulSoup-Python-Library]]

## Tags

- 2fa-bypass
- session-manipulation
