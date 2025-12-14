---
tags:
  - phishing
  - impact
  - revive-adserver
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-open-redirect]]'
platforms:
  - Web
techniques:
  - '[[T1566.002]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 5b2d9799-4273-4188-99b6-30a1922f46eb
created_at: '2025-12-14T17:24:23.014Z'
updated_at: '2025-12-14T17:24:23.014Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Demonstrate Open Redirect Impact

## Summary

This procedure illustrates the real-world impact of the open redirect by redirecting users from a trusted Revive Adserver domain to a malicious URL, simulating phishing or drive-by attacks.

## Description

Users clicking ad links or viewing impressions on sites using Revive Adserver can be seamlessly redirected to attacker-controlled sites. The trusted domain obscures the malicious intent, increasing success rates for phishing credential theft or malware delivery in a web-based attack scenario.

## Requirements

1. Vulnerable Revive Adserver endpoint confirmed
2. Control over a malicious domain or test phishing page
3. Browser for simulation or curl for verification

## Defense

Defensive measures and detection strategies:

- Educate users on suspicious redirects
- Implement referrer checks and HTTPS enforcement
- Use browser extensions or security software to warn on untrusted redirects

## Objectives

1. Redirect from trusted to malicious site
2. Simulate user deception
3. Highlight phishing risks

## Instructions

### Step 1: Craft Malicious URL

**Context**: Replace test URL with a phishing endpoint to show impact.

Construct: http://target.com/ck.php?dest=http://malicious-phish.com/login

### Step 2: Simulate User Visit

**Context**: Execute or visit the URL to follow the redirect.

Use [[commands/curl-test-open-redirect]]:

```bash
curl -L -v "http://target.com/ck.php?dest=http://malicious-phish.com" -o /dev/null
```

> In a browser, visit to observe seamless transition without alerts.

**Expected Output**: Final location is the malicious site; no blocking.

### Step 3: Validate Deception

**Context**: Confirm the redirect appears legitimate from the ad server.

Check browser history or curl output for the chain.

**Expected Output**: Trusted domain in initial URL, malicious in final.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.002]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-open-redirect]]

## Tools Used


## Tags

- [[Phishing]]
- [[Impact]]
