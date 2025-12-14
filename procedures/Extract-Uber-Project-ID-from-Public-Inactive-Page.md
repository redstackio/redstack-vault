---
id: proc-uuid-001
tags:
  - reconnaissance
  - project-id
  - source-inspection
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
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-13T23:52:33.895Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Extract-Uber-Project-ID-from-Public-Inactive-Page

## Summary

This procedure involves inspecting the source code of a public inactive page on Uber's ReadMe.io documentation to extract the internal project ID, which is necessary for subsequent privilege escalation attacks.

## Description

The ReadMe.io platform exposes project identifiers in the HTML source of public pages, such as the inactive status page. By loading https://uber.readme.io/inactive and examining the DOM element with id 'project-info', attackers can retrieve the project ID (e.g., 578cd33dc27ce20e004e397b). This ID is used to target the Uber project in API requests. No authentication is required, making this an initial reconnaissance step in web-based access control exploits.

## Requirements

1. Web browser with developer tools (e.g., Chrome DevTools)
2. Access to the public URL https://uber.readme.io/inactive
3. Basic HTML inspection skills

## Defense

Defensive measures and detection strategies:

- Remove sensitive identifiers like project IDs from public-facing HTML source code.
- Implement client-side obfuscation or server-side rendering to hide internal IDs.
- Monitor for unusual traffic to inactive or error pages.

## Objectives

1. Obtain the Uber project ID for targeting.
2. Enable preparation for authenticated API abuse.
3. Identify exposed configuration data.

## Instructions

### Step 1: Load the Inactive Page

**Context**: Access the public page to retrieve its HTML source without authentication.

No command required; use browser:

1. Navigate to https://uber.readme.io/inactive (note: avoid typos like /inactiveand).
2. Right-click and select "View Page Source" or use F12 to open DevTools.

> This loads the page and exposes the full HTML for inspection.

### Step 2: Inspect for Project ID

**Context**: Locate the specific DOM element containing the project ID.

In DevTools, search for 'project-info' div:

1. In the Elements tab, use Ctrl+F to search for "project-info".
2. Extract the ID value, e.g., 578cd33dc27ce20e004e397b.

> Successful extraction confirms the ID is available; save it for later use in API calls.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- Browser DevTools

## Tags

- [[Reconnaissance]]
- [[web]]
