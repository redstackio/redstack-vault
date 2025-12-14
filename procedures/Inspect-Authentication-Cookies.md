---
id: proc-inspect-twitter-cookies-37822
tags:
  - cookies
  - inspection
  - persistence
  - web
type: procedure
tools:
  - '[[tools/FireBug]]'
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:28:20.589Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Inspect-Authentication-Cookies

## Summary

This procedure uses browser developer tools to examine authentication cookies set during Twitter login with 'Remember Me' enabled, revealing their excessively long expiration dates and associated persistence risks.

## Description

Following authentication, this step involves inspecting the HTTP cookies in the browser to identify the 'auth_token' and 'remember_checked_on' cookies. Discovered in 2014, these cookies were set to expire in November 2024—nearly 10 years later—indicating a misconfiguration in session management. This allows attackers who obtain the cookies (e.g., through physical device access, malware, or XSS attacks) to impersonate the user for an extended period without re-authentication. The procedure targets web environments and requires post-login access; it's essential for vulnerability validation in authentication assessments.

## Requirements

1. Successful login session with 'Remember Me' enabled
2. Browser with inspection capabilities (e.g., Firefox with FireBug)
3. Basic knowledge of browser developer tools

## Defense

Defensive measures and detection strategies:

- Audit cookie expiration policies and enforce shorter durations (e.g., 90 days)
- Use session binding to devices/IPs and monitor for cookie reuse from unusual locations
- Implement client-side warnings and server-side logging of long-lived sessions

## Objectives

1. Identify cookie names, values, and expiration attributes
2. Quantify the persistence duration to assess risk
3. Document evidence for vulnerability reporting

## Instructions

### Step 1: Open Browser Developer Tools

**Context**: Launch the inspection interface to access cookie storage.

In Firefox, install and activate the FireBug extension if not already present. After login, right-click on the page and select 'Inspect Element with FireBug' or open FireBug via the toolbar.

### Step 2: Navigate to Cookies Panel

**Context**: Locate and view the cookies associated with the twitter.com domain.

In FireBug, switch to the 'Net' or 'Console' tab, or directly to the 'Cookies' panel if available. Filter for cookies from https://twitter.com.

### Step 3: Analyze Specific Cookies

**Context**: Examine the 'auth_token' and 'remember_checked_on' for expiration details.

Select the cookies in the list. Note the 'Expires' field: for a login in 2014, it should show a date around November 2024, equating to ~3651 days (10 years).

> The 'auth_token' holds the session identifier, while 'remember_checked_on' flags the persistence choice. Both lack short-term expiry, enabling long-term replay attacks.

**Expected Output**: Detailed cookie attributes, including name, value (obfuscated), domain (.twitter.com), path (/), and long expiration timestamp.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/FireBug]]

## Tags

- [[cookies]]
- [[inspection]]
- [[Persistence]]
- [[web]]
