---
tags:
  - phishing
  - social-engineering
  - 2fa-bypass
  - line-app
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Desktop (Windows/Mac)
  - Web
techniques:
  - '[[Phishing]]'
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[T1566.001]]'
id: 15bde1ea-63cf-4952-831b-cca524519820
created_at: '2025-12-14T17:24:48.139Z'
updated_at: '2025-12-14T17:24:48.139Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
  - '[[Valid Accounts]]'
---
# Phish-Victim-to-Click-Bypass-URL

## Summary

This procedure uses social engineering to trick the victim into clicking the crafted 2FA bypass URL, completing the unauthorized login on the server-side due to flawed verification logic in LINE's secondary client.

## Description

After crafting the URL, the attacker sends it via phishing (e.g., email or message impersonating LINE support) to prompt the victim to "verify" their login. Clicking it exploits the missing ownership check, allowing the attacker's session to inherit the victim's access. This targets users on Windows/Mac LINE apps and combines technical bypass with human manipulation.

## Requirements

1. Crafted bypass URL from previous procedure
2. Communication channel to victim (e.g., email, SMS, external chat)
3. Plausible phishing pretext (e.g., "Confirm your recent login")

## Defense

Defensive measures and detection strategies:

- Train users to verify URLs before clicking, especially from untrusted sources
- Implement URL whitelisting and anti-phishing filters in LINE
- Detect rapid 2FA completions from mismatched devices/IPs

## Objectives

1. Induce victim interaction to trigger server-side bypass
2. Achieve full account takeover without additional credentials
3. Minimize detection by mimicking legitimate flow

## Instructions

### Step 1: Prepare Phishing Message

**Context**: Create a convincing lure to encourage URL click.

Draft a message like: "LINE Security Alert: Please verify your login by clicking here: [crafted URL]".

> Use social engineering to build urgency or trust.

### Step 2: Deliver the URL

**Context**: Send via channel likely to reach the victim.

Transmit the message through email, SMS, or another app.

> Ensure the URL appears legitimate (e.g., shorten if needed, but test first).

### Step 3: Monitor and Confirm Access

**Context**: Wait for click and verify login success.

Observe the attacker's LINE session for access grant.

> Server logs 2FA as complete; attacker now controls the account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Phishing]] Phishing
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- [[T1566.001]] Spearphishing Attachment (adapted to URL)

## Commands Used

- None

## Tools Used

- None

## Tags

- [[Phishing]]
- [[social-engineering]]
