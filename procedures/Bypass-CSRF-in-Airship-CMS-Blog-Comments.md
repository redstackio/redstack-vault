---
id: b1c2d3e4-f5g6-7890-bcde-f12345678901
tags:
  - csrf
  - bypass
  - web
  - php
  - airship-cms
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
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:15.360Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-CSRF-in-Airship-CMS-Blog-Comments

## Summary

This procedure exploits a CSRF protection bypass in the Airship CMS blog comment feature by removing the CSRF token from POST requests, leveraging the $ignoreCSRFToken=true flag in the post() method. It allows attackers to forge comments on behalf of authenticated users with publish permissions, bypassing both CSRF and CAPTCHA checks, primarily for spam or impersonation.

## Description

The Airship CMS (PHP-based) implements CSRF protection via tokens in forms, but the blog comment endpoint in src/Cabin/Hull/Controller/BlogPosts.php calls the post() method from src/Engine/Controller.php with $ignoreCSRFToken=true, intentionally skipping validation. Additionally, users with 'publish' permissions are exempt from CAPTCHA (g-recaptcha-response), removing a secondary safeguard. An attacker can craft a malicious page or link that, when visited by an authenticated user, submits a forged POST request without the token, resulting in a successful comment post (302 redirect). This enables actions like posting spam, impersonating authors, or embedding phishing links. Severity is low as comments are public, deletable, and do not compromise data integrity or confidentiality.

## Requirements

1. Access to the target Airship CMS instance with a blog post (e.g., via public URL)
2. Authenticated session cookie for a user with publish permissions (e.g., admin)
3. Web proxy tool like Burp Suite for request interception and modification
4. Basic knowledge of HTTP requests and form parameters

## Defense

Defensive measures and detection strategies:

- Enforce CSRF token validation universally in all POST endpoints; remove or condition the $ignoreCSRFToken flag
- Require CAPTCHA for all anonymous or low-privilege comment submissions, regardless of permissions
- Implement rate limiting on comment submissions per IP/session to detect automated forging
- Monitor server logs for anomalous 302 redirects on comment endpoints without CSRF tokens
- Use Content-Security-Policy (CSP) headers to prevent cross-site POSTing from external domains

## Objectives

1. Forge a blog comment without valid CSRF token to impersonate an authenticated user
2. Demonstrate bypass of both CSRF and CAPTCHA protections
3. Highlight potential for spam/phishing without alerting the victim

## Instructions

### Step 1: Access Target Blog Post and Generate Request

**Context**: Load the blog post and interact with the comment form to capture a baseline POST request, understanding the parameters involved.

Intercept using [[tools/Burp-Suite]] or browser dev tools. Fill the form with test data and submit to observe the full request.

> The request targets the comment endpoint and includes the CSRF token for normal validation.

### Step 2: Modify Request to Remove CSRF Token

**Context**: Edit the intercepted POST request to eliminate the _CSRF_TOKEN parameter, exploiting the backend's ignore flag. Optionally remove g-recaptcha-response if the user has publish permissions.

In Burp Suite Repeater, alter the body: Remove _CSRF_TOKEN=... entirely, keeping other params like author=47, message=Test+Spam, etc.

> This simulates a cross-site request from a malicious page, bypassing validation since post(true) ignores the token.

### Step 3: Submit and Validate the Forged Comment

**Context**: Forward the modified request to confirm the bypass and check for successful posting.

Send the request and follow the 302 redirect to the post page.

> Success is indicated by the comment appearing on the page without errors, posted as the victim's user.

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

- [[csrf]]
- [[bypass]]
- [[web]]
- [[php]]
- [[airship-cms]]
