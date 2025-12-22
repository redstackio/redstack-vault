---
type: procedure
description: >-
  Test for improper logout and page caching that allows access to sensitive
  information using the browser back button.
verified: true
submitted: true
tactics:
  - '[[Collection]]'
techniques:
  - '[[Steal Web Session Cookie]]'
sub_techniques: []
tags:
  - information-disclosure
  - owasp
  - owasp-top-10
  - web-applications
commands: []
platforms:
  - Web
tools:
  - '[[tools/Chrome-Developer-Tools]]'
skill_level: beginner
impact_level: medium
detection_risk: low
validated: true
---

# Sensitive-Information-Disclosure-via-Browser-Back-Button

## Summary

This procedure tests web applications for sensitive information disclosure due to inadequate logout mechanisms and client-side caching. By logging in, accessing sensitive data, logging out, and then using the browser's back button, attackers or unauthorized users may still view cached sensitive pages, bypassing session termination.

## Description

Many web applications fail to properly invalidate sessions or prevent browser caching of sensitive pages upon logout. This can lead to information disclosure where previously viewed sensitive content (e.g., user profiles, financial data) remains accessible via the browser history. The technique exploits browser behavior to retain page state, highlighting issues in session management and cache control headers like Cache-Control: no-cache or Pragma: no-cache. This is common in applications without proper HTTP headers or JavaScript to clear history. The procedure simulates an attacker with initial legitimate access testing for persistence of sensitive views post-logout.

## Requirements

1. Valid user credentials for the target web application.
2. A modern web browser (e.g., Chrome, Firefox) with developer tools enabled.
3. Network access to the target web application.
4. Basic understanding of browser session management and caching.

## Defense

Defensive measures include implementing proper session invalidation on logout, setting strict cache-control headers (e.g., Cache-Control: private, no-cache, no-store), using HTTPS to prevent interception, and employing JavaScript to disable or clear browser history on sensitive pages. Detection can involve monitoring for anomalous access patterns post-logout via web application firewalls (WAFs) or session logs.

- Enforce cache headers on all sensitive endpoints.
- Use token-based authentication with short-lived sessions.
- Monitor for back-button navigation attempts through client-side logging.

## Objectives

1. Verify if sensitive pages are cached and accessible after logout.
2. Identify weaknesses in session termination and caching controls.
3. Demonstrate potential for unauthorized data exposure via browser history.

## Instructions

### Step 1: Login and Access Sensitive Information

**Context**: Authenticate to the application and navigate to a page containing sensitive data to establish a baseline session state.

Open the target web application in your browser and log in using valid credentials. Navigate to a page displaying sensitive information, such as a user dashboard or account details. Take note of the visible data (e.g., personal info, balances) and confirm the page loads fully.

### Step 2: Perform Logout and Verify Session Clearance

**Context**: Terminate the session and check that authentication tokens or cookies are removed to ensure proper logout implementation.

Click the logout button or link in the application. After logout, inspect the browser's cookies and session storage to confirm no active session data remains. Use [[tools/Chrome-Developer-Tools]] by pressing F12, navigating to the Application tab, and checking Cookies under the domain.

**Expected Output**: No authentication cookies (e.g., session ID, JWT) should be present; the user should be redirected to a login page without access to protected areas.

### Step 3: Test Back Button for Cached Sensitive Data

**Context**: Attempt to retrieve previously viewed sensitive content using browser navigation to assess caching vulnerabilities.

After confirming logout, click the browser's back button to return to the previously visited sensitive page. Observe if the page reloads with the original sensitive data visible without re-authentication.

**Expected Output**: If vulnerable, the sensitive page loads fully with data intact; otherwise, it redirects to login or shows an empty/error state.

### Step 4: Validate and Document the Issue

**Context**: Confirm the disclosure and gather evidence for reporting or remediation.

If data is accessible, screenshot the cached page, note the browser used, and test in incognito mode or different browsers for consistency. Clear browser cache and retest to differentiate between cache and history issues.
