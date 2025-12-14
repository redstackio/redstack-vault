---
tags:
  - web-access
  - reconnaissance
  - xss-prereq
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:22.143Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 12c72fd8-01b7-4ea6-a193-e2c59520341d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Access-Judge-me-Discover-People-Page

## Summary

This procedure outlines the initial access to Judge.me's 'Discover People' page, a public endpoint that displays user profiles and bios, serving as the entry point for identifying XSS vulnerabilities in unsanitized user content.

## Description

In the context of testing for Cross-Site Scripting (XSS) on Judge.me, a Shopify app for reviews, this procedure involves navigating to the /reviews/people endpoint. The page renders user-submitted bios without proper sanitization, making it susceptible to stored XSS attacks. No authentication is required, and the procedure is performed via a standard web browser. Expected outcomes include visibility of user profiles, setting the stage for payload inspection.

## Requirements

1. Web browser with JavaScript enabled
2. Internet access to public Judge.me domains
3. No special permissions or credentials

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict script execution
- Monitor for unusual traffic to profile pages
- Sanitize all user inputs on the server-side before rendering

## Objectives

1. Gain access to the vulnerable page to view user-generated content
2. Confirm page accessibility and rendering of bios
3. Prepare for subsequent vulnerability identification

## Instructions

### Step 1: Navigate to the Target Page

**Context**: Directly access the Discover People page to load user profiles.

Open your web browser and enter the URL https://judge.me/reviews/people in the address bar.

> This loads the page displaying a list of users. Verify that bios are visible in the profile previews.

### Step 2: Verify Page Load

**Context**: Ensure the page renders correctly without blocking mechanisms.

Scroll through the page to confirm user profiles are listed and bios are displayed.

> Successful load indicates no client-side protections are interfering with content rendering.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web-access]]
- [[Reconnaissance]]

