---
id: proc-chaturbate-open-redirect-bypass
tags:
  - open-redirect
  - bypass
  - phishing
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:31.596Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-Chaturbate-Open-Redirect-with-Decimal-IP

## Summary

This procedure exploits an open redirection vulnerability in Chaturbate's login endpoint by bypassing improper validation of the 'next' parameter. It uses a capitalized 'Http:' scheme to evade simple string blocking of 'http' and encodes an external IP address in decimal form (e.g., 3627732462 for google.com's IP 64.233.183.103), allowing post-login redirects to arbitrary sites for phishing or reflected file downloads.

## Description

The vulnerability stems from weak input validation on the 'next' parameter in https://chaturbate.com/auth/login/, where the application blocks 'http' but permits 'Http:' followed by numeric values, interpreting them as decimal IPs. This enables attackers to craft phishing links that redirect authenticated users to malicious external sites. While Content Security Policy (CSP) limits some impacts like reflected file downloads, it simplifies social engineering attacks. The procedure requires a valid account for testing but can be adapted for unauthenticated phishing lures.

## Requirements

1. Web browser for accessing and testing the endpoint
2. Valid Chaturbate credentials to simulate post-login redirect
3. Knowledge of target IP decimal conversion (e.g., via Python: `int.from_bytes(socket.inet_aton('64.233.183.103'), 'big')`)
4. Optional proxy like Burp Suite for parameter inspection

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation allowing only whitelisted internal domains/paths for 'next' parameter
- Normalize schemes to lowercase before checking (e.g., block all variants of 'http')
- Enforce CSP headers to restrict navigations and resource loads from external origins
- Log and monitor unusual 'next' parameter values, especially numeric sequences post-scheme
- Use referrer checks or state tokens to prevent untrusted redirects

## Objectives

1. Bypass validation to enable external post-login redirection
2. Demonstrate phishing potential by redirecting to controlled external site
3. Assess mitigations like CSP on reflected attacks

## Instructions

### Step 1: Convert External IP to Decimal

**Context**: Encode the target site's IP to bypass domain name checks, as the validation only permits numerics after 'Http:'.

For google.com (IP 64.233.183.103), calculate decimal: Use a calculator or command line.

**Command** (Python one-liner for conversion):
```bash
python3 -c "import socket; print(int.from_bytes(socket.inet_aton('64.233.183.103'), 'big'))"
```

> This outputs 3627732462. Use this value in the URL.

### Step 2: Craft Malicious Login URL

**Context**: Construct the 'next' parameter with bypassed scheme and decimal IP to set redirection target.

Access the endpoint with: `https://chaturbate.com/auth/login/?next=Http:3627732462`

**Command** (Using curl to fetch and inspect, optional for verification):
```bash
curl -v "https://chaturbate.com/auth/login/?next=Http:3627732462"
```

> Observe the response; the page should load without blocking the parameter. In a browser, proceed to login.

### Step 3: Perform Login and Trigger Redirect

**Context**: Authenticate to activate the redirect logic, confirming the bypass.

Enter credentials on the form and submit.

**Expected Output**: After login, browser redirects to https://google.com/ (decoded from decimal IP).

### Step 4: Validate and Test Impact

**Context**: Repeat with a phishing-controlled site to assess real-world use; check for CSP blocks on downloads.

Replace decimal with your test IP and observe.

**Expected Output**: Successful external redirect post-auth; note any blocked resources.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- open-redirect
- bypass
- phishing
