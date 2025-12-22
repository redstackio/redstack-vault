---
id: proc-reddit-bruteforce-intruder-001
tags:
  - brute-force
  - password-guessing
  - intruder-attack
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Credential Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
  - '[[Password Guessing]]'
updated_at: '2025-12-14T17:32:58.352Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Password Guessing]]'
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Password Guessing]]'
---
# Brute-Force-Old-Password-with-Burp-Intruder

## Summary

This procedure uses Burp Suite's Intruder to automate brute-forcing the old password parameter in Reddit's password change request, exploiting no rate limiting to guess the correct password and takeover the account.

## Description

From the intercepted request, configure Intruder to iterate over a wordlist in the old_password field while keeping new password fixed. The attack succeeds when the response changes (e.g., 200 OK instead of error), changing the password without throttling. Requires ~8000 requests for this wordlist; real impact amplifies with session theft.

## Requirements

1. Intercepted request sent to Burp Intruder
2. Wordlist file with 8890 entries including target password (!23Qweasdzxc)
3. Burp Suite Professional or Community edition with Intruder enabled

## Defense

Defensive measures and detection strategies:

- Implement server-side rate limiting (e.g., 5 attempts per minute per session/IP)
- Add CAPTCHA after 3 failed attempts
- Monitor for high-volume requests to /prefs/update and block suspicious patterns

## Objectives

1. Guess the correct old password via exhaustive wordlist attacks
2. Trigger password change to new attacker-controlled credentials
3. Achieve full account takeover without detection

## Instructions

### Step 1: Configure Payload in Intruder

**Context**: Set up the attack positions and load the wordlist for the old_password parameter.

In Burp Intruder, mark §old_password§ as payload position, select 'Sniper' mode, load wordlist via Payloads tab (e.g., rockyou.txt augmented to 8890 entries).

> Ensure new_password and confirm_new_password are fixed to desired values.

### Step 2: Launch Brute-Force Attack

**Context**: Execute the attack and monitor responses for success.

Click 'Start Attack'; Intruder sends requests sequentially, highlighting differing responses (e.g., length or status code change on success).

> After iterating, identify the payload that yields success (e.g., !23Qweasdzxc); no throttling observed across 8000+ requests.

### Step 3: Verify Takeover

**Context**: Confirm the password has been updated.

Log in with new password; check account settings.

> Successful access indicates takeover complete.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Brute Force]] Brute Force
- [[Password Guessing]] Password Guessing

### Sub-Techniques

- [[Password Guessing]] Password Guessing

## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[brute-force]]
- [[password-guessing]]
- [[intruder-attack]]
