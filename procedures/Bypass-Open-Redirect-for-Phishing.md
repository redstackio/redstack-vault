---
id: proc-smule-open-redirect-bypass
tags:
  - open-redirect
  - bypass
  - phishing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-open-redirect-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[T1566.002]]'
updated_at: '2025-12-14T03:53:38.332Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Bypass-Open-Redirect-for-Phishing

## Summary

This procedure exploits an open redirect vulnerability in Smule's web application by bypassing validation mechanisms, allowing redirection to unauthorized external URLs for phishing attacks or session hijacking.

## Description

In the Smule application, an open redirect flaw exists where user-supplied URLs in redirect parameters are not properly validated, enabling attackers to craft links that redirect users to malicious sites. The bypass involves techniques like protocol-relative URLs (//evil.com) or encoding to evade filters. This was reported in January 2020 and could lead to phishing by tricking users into entering credentials on fake pages. Prerequisites include access to the public web app and a tool for crafting HTTP requests.

## Requirements

1. Public access to Smule's web application endpoints
2. HTTP client like curl or Burp Suite for testing redirects
3. Knowledge of the vulnerable parameter (e.g., ?url= or ?redirect=)

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation allowing only whitelisted domains
- Use Content Security Policy (CSP) to restrict redirects
- Monitor access logs for suspicious redirect patterns to external domains

## Objectives

1. Craft a functional malicious redirect URL
2. Verify bypass success without application blocks
3. Enable phishing by distributing the malicious link

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Locate the open redirect parameter in Smule's app, often in login or share features.

**Command** ([[commands/curl-open-redirect-test]]):
```bash
curl -X GET "https://app.smule.com/redirect?url=https://example.com" -v
```

> This tests a benign redirect. Look for 302 status and Location header pointing to example.com. If blocked, proceed to bypass.

### Step 2: Attempt Bypass with Protocol-Relative URL

**Context**: Use // to bypass protocol checks, forcing redirect to attacker-controlled domain.

**Command** ([[commands/curl-open-redirect-test]]):
```bash
curl -X GET "https://app.smule.com/redirect?url=//phishingsite.com" -v
```

> Success if redirect header shows phishingsite.com. Encode if needed (e.g., %2F%2F for //).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.002]]

### Sub-Techniques


## Commands Used

- [[commands/curl-open-redirect-test]]

## Tools Used


## Tags

- open-redirect
- bypass
- phishing
