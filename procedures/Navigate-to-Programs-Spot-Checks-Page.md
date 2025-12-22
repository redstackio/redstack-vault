---
tags:
  - web-access
  - hackerone
  - spot-checks
type: procedure
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
updated_at: '2025-12-14T17:30:35.436Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: bbc48cb4-17b8-4d07-9801-def12d3d4f6f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Navigate to Program's Spot Checks Page

## Summary

This procedure establishes initial access to the HackerOne program's Spot Checks interface from an authenticated hacker's viewpoint, positioning for subsequent exploitation of URL-based information disclosure.

## Description

In the context of the HackerOne platform, authenticated users (hackers) can view certain program details but should not access confidential Spot Check metadata. This step involves logging in and navigating to a program's Spot Checks page using the standard web interface. It requires an active session and visibility into the program. The expected outcome is loading the page without errors, setting up for URL modification. Prerequisites include a HackerOne account invited to the program.

## Requirements

1. Authenticated HackerOne account with invitation to the target program
2. Web browser with JavaScript enabled
3. Network connectivity to hackerone.com

## Defense

Defensive measures and detection strategies:

- Implement session monitoring for unusual navigation patterns to admin-like pages
- Rate-limit access to Spot Checks endpoints
- Log all URL parameter changes and GraphQL query invocations

## Objectives

1. Achieve visibility into the program's Spot Checks without alerting defenses
2. Prepare the environment for targeted URL manipulation
3. Confirm authenticated access level

## Instructions

### Step 1: Authenticate and Access Program Dashboard

**Context**: Log in to ensure a valid session, then navigate to the target program's page to reach the Spot Checks section.

No specific command required; use the web interface:

- Visit https://hackerone.com and log in with hacker credentials.
- From the dashboard, select the target program.
- Click on the "Spot Checks" tab or link.

> This loads the initial Spot Checks view, confirming access.

### Step 2: Verify Page Load

**Context**: Ensure the page renders correctly, displaying only hacker-visible information.

Inspect the URL, which should be in the format https://hackerone.com/organizations/[organization-id]/spot_checks.

> Successful load indicates readiness for the next step; look for any visible Spot Check IDs in the interface.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web-access
- authentication
- reconnaissance
