---
id: proc-uuid-2
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
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:26.509Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Craft-Phishing-Redirect-Link

## Summary

This procedure involves constructing deceptive links that exploit open redirect vulnerabilities to direct users from a legitimate login page to a malicious phishing site, capturing credentials or session data. It is used in simulated phishing campaigns or vulnerability exploitation demos.

## Description

For Moneybird's login, the attacker crafts a URL like https://moneybird.com/login?redirect_to=https://attacker-controlled-phish-site.com, embeds it in an email or message mimicking official communication (e.g., 'Click here to log in securely'). Upon user login, the redirect sends them to the fake site, which mirrors the real login to harvest inputs. Expected outcomes include credential theft; requires hosting a phishing page and social engineering to distribute the link.

## Requirements

1. Control of a malicious domain and hosting for phishing page
2. Knowledge of the vulnerable redirect parameter
3. Email or messaging platform for link distribution

## Defense

Defensive measures and detection strategies:

- Educate users on verifying URLs before clicking
- Implement redirect validation and URL encoding checks
- Monitor for anomalous traffic to login endpoints with external redirects

## Objectives

1. Trick users into authenticating via the malicious link
2. Redirect to phishing site for data exfiltration
3. Simulate full phishing attack chain

## Instructions

### Step 1: Construct Malicious URL

**Context**: Build the exploit link using the identified vulnerable parameter.

**Command**:
```bash
# Manual URL construction; no CLI command needed
# Example: https://moneybird.com/login?redirect_to=https://fake-site.com/phish
```

> Create the link in a text editor or script; encode if necessary to bypass filters. Test locally before distribution.

### Step 2: Distribute and Monitor

**Context**: Embed the link in a phishing vector and observe user interaction.

**Command**:
```bash
# Use email client or script to send; monitor with server logs on phish site
# e.g., tail -f /var/log/phish-access.log
```

> Expected output: Incoming requests to the phishing site with user credentials submitted via POST.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.002]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[redirect]]
- [[social-engineering]]
