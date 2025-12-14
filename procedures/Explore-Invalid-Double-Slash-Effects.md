---
id: proc-explore-invalid-double-slash-effects
tags:
  - cloudflare
  - dos
  - disruption
type: procedure
tools:
  - '[[tools/Chrome-Browser]]'
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
updated_at: '2025-12-14T17:24:26.315Z'
skill_level: intermediate
impact_level: low
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Explore Invalid Double Slash Effects

## Summary

This procedure examines how invalid double-slash URLs on hackerone.com trigger CloudFlare alerts and serve cached pages, disrupting user experience and potentially aiding in denial-of-service or evasion scenarios.

## Description

Invalid paths like //hackerone.com1 cause CloudFlare to intervene, showing offline alerts with cached content. After such access, navigating to legitimate pages (e.g., /hacktivity) amplifies disruption. Requires browser testing on the web platform; outcomes include temporary site inaccessibility.

## Requirements

1. Browser access
2. hackerone.com with CloudFlare protection
3. Ability to navigate multiple pages

## Defense

Defensive measures and detection strategies:

- Configure CloudFlare to handle malformed paths gracefully
- Rate-limit invalid URL requests
- Monitor for repeated double-slash anomalies

## Objectives

1. Trigger CloudFlare security responses
2. Observe cached page serving
3. Assess disruption potential

## Instructions

### Step 1: Access Invalid Double Slash

**Context**: Use an invalid domain with double slashes to invoke CloudFlare.

Navigate to: `https://hackerone.com//hackerone.com1`

> Triggers alert; expected output: CloudFlare page indicating offline status.

### Step 2: Navigate to Legitimate Page

**Context**: Test persistence by accessing another endpoint.

Go to: `https://hackerone.com/hacktivity`

> Cached page or continued alert appears, disrupting access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-Browser]]

## Tags

- cloudflare
- disruption
