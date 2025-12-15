---
id: proc-wpscan-user-enum
tags:
  - wordpress
  - username-enumeration
  - account-discovery
type: procedure
tools:
  - '[[tools/WPScan]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/wpscan-enumerate-users]]'
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:36.650Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Enumerate-WordPress-Usernames-with-WPScan

## Summary

This procedure uses WPScan to exploit WordPress login page response differences, enumerating valid usernames like 'frank' without authentication, enabling targeted follow-on attacks such as brute forcing.

## Description

In a typical attack scenario, attackers target public-facing WordPress sites where the /wp-admin endpoint returns distinguishable errors (e.g., "Invalid username" vs. "Invalid password" for valid users). WPScan automates this by sending requests and analyzing HTTP responses. Prerequisites include network access to the target and WPScan installed on a Linux environment. Expected outcomes: A list of valid usernames, facilitating account discovery in web applications.

## Requirements

1. Network access to the target WordPress site (e.g., https://nextcloud.com/wp-admin)
2. WPScan tool installed (Ruby-based, requires API key for full features but basic enum works without)
3. No rate limiting evasion needed for basic scans, but proxies can be added for stealth

## Defense

Defensive measures and detection strategies:

- Implement consistent error messages on login pages (e.g., always "Invalid credentials")
- Enable rate limiting or CAPTCHA on /wp-admin
- Monitor for WPScan user-agent strings in web logs and block suspicious IPs

## Objectives

1. Discover valid admin usernames for targeted attacks
2. Assess exposure of user accounts on WordPress sites
3. Enable brute force or phishing against identified users

## Instructions

### Step 1: Run WPScan User Enumeration

**Context**: Launch WPScan to probe the login endpoint for username validity by comparing response lengths or content.

**Command** ([[commands/wpscan-enumerate-users]]):
```bash
wpscan --url https://nextcloud.com --enumerate u
```

> This command scans the target URL for users, outputting valid ones based on response analysis. Expect output like "Valid username: frank" if successful. Run time: 1-2 minutes depending on site responsiveness.

### Step 2: Verify Enumeration Results

**Context**: Review the output to confirm valid usernames and note any additional findings like plugin versions.

**Command** ([[commands/wpscan-enumerate-users]]):
```bash
wpscan --url https://nextcloud.com --enumerate u -v
```

> The verbose flag (-v) provides detailed response info. Successful verification shows no false positives and lists usernames accurately.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques

- N/A

## Commands Used

- [[commands/wpscan-enumerate-users]]

## Tools Used

- [[tools/WPScan]]

## Tags

- [[wordpress]]
- [[username-enumeration]]
- [[tools/WPScan]]
