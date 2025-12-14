---
id: proc-distribute-link
tags:
  - phishing
  - distribution
  - social-engineering
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
  - '[[Phishing]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:58.423Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques:
  - '[[T1566.001]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
  - '[[Exploit Public-Facing Application]]'
---
# Distribute Malicious Link to Victim

## Summary

This procedure involves delivering the crafted malicious OAuth URL to potential victims, tricking them into initiating the Pixiv authentication flow that leads to code leakage.

## Description

Distribution relies on social engineering tactics, such as phishing emails or messages claiming a Pixiv-related promotion or login prompt. The victim clicks the link, authenticates with Pixiv, and due to the path traversal, gets redirected to the attacker's Booth.pm page with the OAuth code in the query string. This step is victim-dependent and requires no technical tools beyond communication channels. Expected outcome: Victim completes login, triggering the redirect.

## Requirements

1. Access to victim contact methods (email, social media, etc.)
2. Crafted malicious URL from prior procedure
3. Plausible pretext for Pixiv interaction

## Defense

Defensive measures and detection strategies:

- User education on phishing and suspicious OAuth prompts
- Email filters for links to authorization endpoints
- Monitor for mass distribution of OAuth URLs

## Objectives

1. Lure victim into clicking and authenticating
2. Trigger the exploited OAuth flow
3. Ensure redirect occurs to attacker page

## Instructions

### Step 1: Prepare Distribution Message

**Context**: Craft a convincing lure to encourage clicking.

No command; write message like: "Log in to Pixiv to claim your reward: [malicious URL]"

> Tailor to victim interests, e.g., art community references for Pixiv users.

### Step 2: Send via Channel

**Context**: Deliver the link through chosen medium.

Use email client, messaging app, or social post:

- Embed or append the full malicious URL.
- Avoid shortening if it triggers filters; use raw URL.

> Track opens/clicks if using tracked email services.

### Step 3: Monitor for Interaction

**Context**: Wait for victim engagement without direct involvement.

No command; observe analytics or logs for incoming traffic.

> Victim will see Pixiv login page; upon success, redirect happens automatically.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Phishing]] Phishing
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- [[T1566.001]] Spearphishing Attachment (adapted for links)

## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[distribution]]
- [[social-engineering]]
