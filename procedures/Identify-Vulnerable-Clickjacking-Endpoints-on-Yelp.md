---
tags:
  - clickjacking
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 9079aea2-de80-4e17-9115-b61bc9cf7689
created_at: '2025-12-14T17:28:05.225Z'
updated_at: '2025-12-14T17:28:05.225Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Identify-Vulnerable-Clickjacking-Endpoints-on-Yelp

## Summary

This procedure involves manually inspecting Yelp.com to identify endpoints that handle sensitive user actions, such as flagging profiles, following users, or sending compliments, and confirming they lack frame-busting protections like X-Frame-Options or CSP frame-ancestors directives.

## Description

In a clickjacking attack scenario, attackers target web applications where state-changing endpoints can be embedded in iframes. For Yelp, endpoints like /flag_content, /following_user/add, and /thanx accept parameters (e.g., message, flag_id, dst_user_id) without restrictions, enabling coerced actions. This procedure focuses on reconnaissance to pinpoint these vulnerabilities, assuming public access to the site. Expected outcomes include a list of exploitable URLs that can lead to user manipulation and platform abuse.

## Requirements

1. Internet access to Yelp.com
2. Web browser with developer tools for header inspection
3. Basic knowledge of HTTP parameters and web security headers

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN on all pages
- Use CSP with frame-ancestors 'none' directive
- Monitor for unusual action patterns, like bulk flagging from single IPs

## Objectives

1. Locate endpoints performing user actions without frame protections
2. Document parameters for later exploitation
3. Assess potential for clickjacking-based user coercion

## Instructions

### Step 1: Examine Site Functions

**Context**: Browse Yelp to find features involving user interactions like reporting, following, or complimenting, and note the underlying URLs.

Inspect network requests in browser dev tools while performing actions (e.g., attempt to flag a profile) to capture endpoints like https://www.yelp.com/flag_content?flag_id=...&message=....

### Step 2: Check for Protections

**Context**: Verify absence of anti-framing measures by loading the endpoint and inspecting response headers.

Use browser dev tools (Network tab) to confirm no X-Frame-Options or Content-Security-Policy frame-ancestors in responses for endpoints like /following_user/add and /thanx.

### Step 3: Document Vulnerabilities

**Context**: Compile a list of vulnerable endpoints with example parameters.

Record details: e.g., /flag_content accepts flag_id, message, flag_type=user_profile; /thanx accepts message, user_id, previous_url.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[web-recon]]
