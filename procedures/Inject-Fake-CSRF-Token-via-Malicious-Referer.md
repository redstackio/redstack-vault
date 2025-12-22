---
tags:
  - csrf
  - cookie-injection
  - referer-forgery
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:29.184Z'
sub_techniques: []
id: 2b88efaf-b2d8-4c74-a76a-060e99f12d2f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# Inject Fake CSRF Token via Malicious Referer

## Summary

This procedure tricks the authenticated user into visiting a malicious link that forges a Referer header, causing Google Analytics on translate.twitter.com to set a __utmz cookie with an injected fake CSRF token 'm5_csrf_tkn=x'.

## Description

By controlling the Referer, the attacker exploits unfiltered path inclusion in Google Analytics cookie setting. Multiple repeated 'path=' attributes in the cookie header override the domain to .twitter.com in Chrome, which limits attribute processing. The injected value uses commas to delimit a fake token, persisting for 6 months.

## Requirements

1. Authenticated session on twitter.com
2. Control over a malicious domain (e.g., blackfan.ru)
3. Google Chrome browser for attribute override

## Defense

Defensive measures and detection strategies:

- Filter Referer paths in analytics cookie setting
- Validate cookie attributes strictly on server-side
- Use SameSite=Strict for CSRF cookies

## Objectives

1. Set persistent __utmz cookie with injection
2. Ensure cookie domain covers Twitter subdomains
3. Prepare for parsing exploitation

## Instructions

### Step 1: Craft Malicious Link

**Context**: Create a link with forged Referer to trigger cookie set.

Host on attacker server: http://blackfan.ru/r/,m5_csrf_tkn=x,;domain=.twitter.com;path=/;path=/;...;?r=http://translate.twitter.com/ (repeat path= 13 times for Chrome override).

> Link tricks user into visit; Referer sets utmcct=/r/,m5_csrf_tkn=x, in __utmz.

### Step 2: User Visits Link

**Context**: Social engineer victim to click and load translate.twitter.com.

No command; browser handles redirect and cookie set via Google Analytics.

> __utmz cookie appears in dev tools with injected value.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome]]

## Tags

- csrf
- injection
