---
id: proc-002
tags:
  - csrf
  - twitter
  - web
  - drive-by
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:22.821Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Trigger-CSRF-via-User-Visit-to-Malicious-Site

## Summary

This procedure triggers the CSRF attack by luring a logged-in Twitter user to visit the malicious site, causing their browser to automatically load the vulnerable endpoint and mark notifications as read.

## Description

Once the malicious HTML is hosted, the attack relies on social engineering to get the victim to visit the site. The browser, using the active Twitter session (cookies), will execute the cross-origin script load, performing the state change. This exploits the absence of anti-CSRF measures like tokens or origin checks on the endpoint. Impact is limited to user annoyance, as no data is exfiltrated, but it demonstrates session hijacking for actions.

## Requirements

1. Hosted malicious webpage from prior procedure
2. Method to contact or lure the target (e.g., email, link sharing)
3. Target must visit while authenticated to Twitter

## Defense

Defensive measures and detection strategies:

- Use browser extensions to block cross-origin scripts (e.g., NoScript)
- Twitter-side: Enforce CSRF tokens and validate referer/origin headers
- Log anomalous notification clears and alert users

## Objectives

1. Induce victim visit to execute CSRF
2. Confirm unauthorized action (notifications cleared)
3. Demonstrate vulnerability impact

## Instructions

### Step 1: Lure Target to Site

**Context**: Use social engineering to get the user to load the malicious page, triggering the script.

Share the URL via phishing email, social post, or direct message: "Check out this interesting article: https://evil.com".

> No code execution here; relies on user action. Expected: User navigates to the site in their browser.

### Step 2: Verify Execution

**Context**: Confirm the CSRF fired by checking the target's Twitter notifications.

After visit, inspect the victim's Twitter: Unread count should reset to zero.

> If testing on self, log in, visit site, and observe notification changes. Success if all notifications are marked read without manual action.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[twitter]]
- [[web]]
