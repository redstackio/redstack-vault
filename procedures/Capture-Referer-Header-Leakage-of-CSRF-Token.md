---
id: proc-capture-referer-csrf-leak
tags:
  - csrf
  - information-disclosure
  - referer-header
  - third-party-leak
  - web-vulnerability
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1213.003]]'
updated_at: '2025-12-14T17:27:22.779Z'
skill_level: basic
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[T1213.003]]'
---
# Capture-Referer-Header-Leakage-of-CSRF-Token

## Summary

This procedure captures how the CSRF token-exposed login URL is automatically sent to external third-party sites via the HTTP Referer header during post-login resource loading, disclosing sensitive information to analytics and tracking services.

## Description

The HTTP Referer header includes the originating URL when navigating to cross-origin resources, such as scripts from Google Analytics or New Relic. If the login uses GET, the full URL with CSRF token is leaked without user intervention. This targets web environments with integrated third-party services like CloudFront, Mixpanel, and TrackJS. Outcomes include evidence of leakage, enabling assessment of risks like token misuse for CSRF attacks if third-parties are breached.

## Requirements

1. Browser with network inspection capabilities
2. Completion of login process from prior procedure
3. Awareness of target's third-party integrations (e.g., via source code inspection)

## Defense

Defensive measures and detection strategies:

- Strip or suppress Referer headers using meta tags (e.g., `<meta name="referrer" content="no-referrer">`)
- Load third-party resources via POST or same-origin iframes
- Audit and minimize third-party scripts; use server-side analytics where possible
- Log and alert on unexpected Referer values in third-party request logs

## Objectives

1. Intercept and document Referer header contents post-login
2. Identify affected third-party domains
3. Evaluate disclosure impact on CSRF protections

## Instructions

### Step 1: Initiate Post-Login Resource Load

**Context**: Trigger loading of external resources after login to simulate real user behavior.

With developer tools open, complete the login from Step 1 of the previous procedure. Allow the page to fully load, including any analytics or tracking scripts.

> External domains like `ssl.google-analytics.com` or `api.mixpanel.com` will be contacted.

### Step 2: Monitor Outgoing Requests

**Context**: Capture headers sent to third-party endpoints.

In the Network tab, filter for requests to external domains (e.g., `*.cloudfront.net`, `bam.nr-data.net`). Select a request and inspect the Request Headers section.

> Look for `Referer: https://target.com/login?csrf_token=TOKEN_VALUE&...`.

### Step 3: Document Leakage Evidence

**Context**: Verify and screenshot the leaked token for reporting.

Copy the full Referer value and cross-reference with the original login URL. Note all affected services (e.g., New Relic, Google Analytics).

> Success: Multiple instances of token leakage confirmed, e.g., to `usage.trackjs.com`.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[T1213.003]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[information-disclosure]]
- [[referer-header]]
- [[third-party-leak]]
