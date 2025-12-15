---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - open-redirect
  - phishing
  - bypass
  - revive-adserver
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-open-redirect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Phishing]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:26.583Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques:
  - '[[T1566.002]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
  - '[[Exploit Public-Facing Application]]'
---
# Bypass Open Redirect Filter in Revive Adserver with Multiple Slashes

## Summary

This procedure exploits an open redirect vulnerability in Revive Adserver's campaign-modify.php by bypassing the return_url parameter filter using multiple consecutive slashes (////), allowing redirection to external malicious sites and enabling phishing attacks on authenticated users.

## Description

Revive Adserver, a PHP-based ad management platform, includes an open redirect in the /www/admin/campaign-modify.php endpoint via the return_url parameter. The filter is intended to restrict redirects to internal paths but fails to normalize or block payloads starting with multiple slashes, such as ////external.com. This bypass allows attackers to redirect authenticated admin users to arbitrary external domains, facilitating phishing for credential theft or malware delivery. The attack requires authentication but no elevated privileges beyond standard admin access. Expected outcomes include successful redirection without triggering filters, confirmed via HTTP headers or browser behavior.

## Requirements

1. Valid authentication credentials for Revive Adserver admin panel
2. Network access to the target web server hosting Revive Adserver
3. HTTP client like curl or a browser for testing redirects

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation in redirects, normalizing paths and blocking external domains using whitelists
- Use Content Security Policy (CSP) headers to restrict navigation
- Monitor access logs for suspicious return_url parameters containing multiple slashes
- Enable multi-factor authentication (MFA) to mitigate phishing risks

## Objectives

1. Bypass the return_url filter to enable external redirects
2. Redirect authenticated users to a controlled phishing site
3. Harvest credentials or deliver malware via the phishing page

## Instructions

### Step 1: Authenticate and Access the Endpoint

**Context**: Log in to the Revive Adserver admin panel to gain authenticated access, as the vulnerability affects logged-in users.

No specific command needed; use the web interface to authenticate.

> Upon successful login, the session cookie enables access to admin endpoints.

### Step 2: Craft and Test the Malicious Redirect

**Context**: Construct the return_url with multiple slashes to bypass the filter, then test the redirect using [[commands/curl-test-open-redirect]]. The %2F encoding represents /, so %2F%2F%2F%2F decodes to ////.

**Command** ([[commands/curl-test-open-redirect]]):
```bash
curl -X GET "http://target.com/www/admin/campaign-modify.php?clientid=&campaignid=&returnurl=%2F%2F%2F%2Fhackerone.com" -i -L
```

> This command sends a GET request to the endpoint with the crafted parameter. The -i flag shows headers, and -L follows redirects. Expected output includes a 302 status with Location: http://hackerone.com (resolving from ////hackerone.com). If successful, the filter is bypassed, and the external site loads.

### Step 3: Deploy in Phishing Attack

**Context**: Once verified, embed the crafted URL in a phishing email or link to lure the victim into clicking while authenticated.

No command; manually craft the link as http://target.com/www/admin/campaign-modify.php?clientid=&campaignid=&returnurl=%2F%2F%2F%2Fmalicious-phish.com.

> Victim clicks lead to the admin page, which redirects to the phishing site, appearing legitimate.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Phishing]] Phishing
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- [[T1566.002]] Spearphishing Link

## Commands Used

- [[commands/curl-test-open-redirect]]

## Tools Used

None

## Tags

- open-redirect
- phishing
- bypass
- revive-adserver
