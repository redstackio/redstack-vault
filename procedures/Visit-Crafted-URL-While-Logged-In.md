---
tags:
  - web-cache-poisoning
  - initial-trigger
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 4c8b1449-f0a6-4bc6-a2d8-1db7090a7f19
created_at: '2025-12-13T09:00:34.400Z'
updated_at: '2025-12-13T09:00:34.400Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Visit Crafted URL While Logged In

## Summary

This procedure involves a logged-in user accessing a specially crafted URL with a static file extension to trigger improper caching of dynamic content containing sensitive information.

## Description

In this attack scenario, the target is a web application that fails to properly validate cacheable resources, allowing dynamic pages with user data to be cached when appended with extensions like .css. This is the initial step in a web cache poisoning attack, targeting environments with caching web servers.

## Requirements

1. Logged-in session on the target website
2. Access to a web browser
3. Network connectivity to the target URL

## Defense

Defensive measures and detection strategies:

- Implement strict cache controls like Cache-Control: no-store for dynamic content
- Validate file extensions and prevent caching of user-specific data

## Objectives

1. Trigger server-side caching of sensitive data
2. Prepare for unauthorized access in subsequent steps
3. Confirm vulnerability existence through caching behavior

## Instructions

### Step 1: Access the Crafted URL

**Context**: While logged in, navigate to the URL to force the server to cache the response.

Visit https://www.lyst.com/shop/trends/mens-dress-shoes/blahblah.css in your browser.

> This causes the server to cache the dynamic page including user session data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Web-Browser]]

## Tags

- web-cache-poisoning
- initial-trigger
