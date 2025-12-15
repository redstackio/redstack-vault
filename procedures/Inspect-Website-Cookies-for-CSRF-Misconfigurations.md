---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - csrf
  - cookies
  - samesite
  - inspection
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T17:27:15.232Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Inspect-Website-Cookies-for-CSRF-Misconfigurations

## Summary

This procedure involves using browser developer tools to inspect cookies on a target website, identifying misconfigurations such as SameSite=None without the Secure attribute, which can enable CSRF attacks by allowing third-party cookies in cross-origin requests.

## Description

In web applications like Yelp's site, cookies manage sessions and user data. If set with SameSite=None (allowing cross-site requests) but without Secure (requiring HTTPS), they become vulnerable to CSRF, where attackers trick users into unintended actions. This procedure targets public-facing web apps, requiring only browser access, and outcomes include vulnerability confirmation and risk assessment, noting low exploit likelihood without absent defenses like CSRF tokens.

## Requirements

1. Modern web browser (e.g., Chrome, Firefox) with developer tools enabled.
2. Internet access to the target site (e.g., www.yelp.com).
3. Basic knowledge of HTTP cookies and browser inspection.

## Defense

Defensive measures and detection strategies:

- Enforce SameSite=Lax or Strict on cookies to block cross-site requests.
- Always pair SameSite=None with Secure attribute over HTTPS.
- Implement CSRF tokens, same-origin checks, or custom headers in forms.
- Monitor browser console for cookie rejection warnings during development.

## Objectives

1. Identify cookies vulnerable to CSRF due to attribute misconfigurations.
2. Assess potential for data modification in cross-origin contexts.
3. Document findings for reporting or mitigation.

## Instructions

### Step 1: Navigate to Target and Open Developer Tools

**Context**: Load the website to trigger cookie setting and access inspection tools.

No command required; perform manually:

1. Open your browser.
2. Navigate to www.yelp.com.
3. Press F12 or right-click page and select "Inspect" to open developer tools.
4. Switch to the "Application" tab (Chrome) or "Storage" tab (Firefox).

> This loads the site's cookies into viewable storage.

### Step 2: Examine Cookie Attributes

**Context**: Review specific cookie properties to detect CSRF-enabling flaws.

No command required; perform manually:

1. Under the target domain (www.yelp.com), expand the "Cookies" section.
2. Select individual cookies (e.g., session or tracking cookies like 'myCookie').
3. Check columns for SameSite (should not be None without Secure) and Secure (must be true for None).
4. Look for console errors like "This Set-Cookie was blocked due to SameSite=None without Secure."

> Expected output includes a table of cookies with attributes; flag any with SameSite=None and Secure=false as vulnerable to CSRF.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Software]] Gather Victim Host Information: Software

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[cookies]]
- [[samesite]]
- [[web-vulnerability]]
