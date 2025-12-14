---
id: proc-extract-project-id
tags:
  - reconnaissance
  - project-id
  - source-inspection
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:29:57.377Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Extract-Uber-Project-ID-from-Inactive-Page

## Summary

This procedure involves inspecting the source code of a public inactive page on Uber's ReadMe.io instance to extract the internal project ID, which is necessary for targeting the invite system in subsequent exploitation steps.

## Description

The attack begins with reconnaissance on publicly accessible pages. By loading https://uber.readme.io/inactive and examining the HTML source, the project ID is found in a div with id 'project-info'. This ID (e.g., 578cd33dc27ce20e004e397b) allows association with the target project during the invite bypass. No authentication is required, making this a low-risk initial step. Expected outcome: Acquisition of the project identifier for use in crafted API requests.

## Requirements

1. Web browser with developer tools (e.g., Chrome DevTools)
2. Public access to https://uber.readme.io/inactive
3. Basic HTML inspection knowledge

## Defense

Defensive measures and detection strategies:

- Remove or obfuscate internal IDs from public-facing pages
- Implement client-side rendering to hide backend identifiers
- Monitor for unusual traffic to inactive or error pages

## Objectives

1. Gather internal project details for targeted exploitation
2. Enable association of requests with the specific Uber project
3. Prepare for access control bypass without direct authentication

## Instructions

### Step 1: Load Inactive Page

**Context**: Access the public inactive page to retrieve embedded metadata.

No command required; use browser:

1. Navigate to https://uber.readme.io/inactive
2. Right-click and select 'View Page Source' or press Ctrl+U

> Inspect for <div id="project-info"> containing the ID like 578cd33dc27ce20e004e397b. Note any typos in URL (e.g., avoid /inactiveand).

### Step 2: Extract and Validate ID

**Context**: Confirm the extracted ID's validity by checking its format.

No command; manual validation:

The ID should be a 24-character hexadecimal string typical of MongoDB ObjectIDs.

> Successful extraction yields the project ID for use in later steps.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[web]]

