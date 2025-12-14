---
id: proc-wcd-victim-visit-001
tags:
  - social-engineering
  - phishing-link
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
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:27:57.258Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Trick-Victim-Into-Visiting-Authenticated-URL

## Summary

This procedure uses social engineering to lure an authenticated Shopify user into visiting the malicious WCD URL, causing the server to generate a personalized 404 page that embeds user data and gets cached by the proxy as a static CSS file.

## Description

The attack relies on the victim being logged into Shopify, so their session cookies personalize the 404 response with data like name, email, and CSRF token. Distribute the URL via email, chat, or disguised link (e.g., as a 'resource' on trademarks). The proxy caches it due to the .css extension, making it retrievable unauthenticated. Expected outcome: Cache poisoning with victim-specific content. Prerequisites: Victim's contact info and trust.

## Requirements

1. Malicious URL from prior procedure
2. Social engineering channel (email, messaging app)
3. Victim authenticated to target site (Shopify)

## Defense

Defensive measures and detection strategies:

- Educate users on suspicious links and verify URLs before clicking
- Implement referrer checks or rate-limiting on error pages
- Log and alert on cached error pages with user session data

## Objectives

1. Ensure victim loads URL while authenticated to embed session data
2. Trigger caching of the dynamic response
3. Minimize victim suspicion (e.g., disguise as helpful link)

## Instructions

### Step 1: Distribute the URL

**Context**: Send the URL to the victim in a convincing manner to prompt a click.

No command; craft a message like "Check this Shopify trademark guide: [URL]" and send via email or chat.

> Victim clicks and opens in browser; if authenticated, server returns 404 with personalized HTML/JS including user info.

### Step 2: Verify Caching Trigger

**Context**: Confirm the visit occurred by testing cache state (optional, low-risk probe).

Use browser incognito to request the URL; if it returns the 404 (not fresh 404), caching succeeded.

> Expected: Same 404 content as victim saw, now served from cache.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1566.002]] Spearphishing: Link

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- social-engineering
- victim-trickery
