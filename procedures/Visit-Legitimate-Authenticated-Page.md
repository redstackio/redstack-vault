---
tags:
  - discovery
  - web-navigation
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Data from Cloud Storage]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: de8a103b-7138-4776-b194-4674a8000e8d
created_at: '2025-12-13T09:00:34.332Z'
updated_at: '2025-12-13T09:00:34.332Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Data from Cloud Storage]]'
---
# Visit Legitimate Authenticated Page

## Summary

This procedure guides the victim in navigating to a legitimate authenticated page, loading personalized content that can be exploited in caching attacks.

## Description

After authentication, the victim visits a dynamic endpoint like /my_collection/, which displays personal data. This step ensures the content is generated and ready for caching manipulation. It is part of the setup for web cache deception attacks.

## Requirements

1. Active authenticated session
2. Web browser
3. Knowledge of the target endpoint URL

## Defense

Defensive measures and detection strategies:

- Use proper caching headers to prevent caching of dynamic content
- Monitor access logs for unusual URL patterns

## Objectives

1. Load authenticated content
2. Confirm display of personal data
3. Prepare content for caching

## Instructions

### Step 1: Navigate to Endpoint

**Context**: Enter the URL in the authenticated browser session.

Use [[tools/Web-Browser]] to visit https://chaturbate.com/my_collection/.

> The page loads with user-specific data.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Data from Cloud Storage]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Web-Browser]]

## Tags

- discovery
- web-navigation
