---
tags:
  - xss
  - stored-xss
  - mapbox
  - sharing
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:08.172Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6acb6451-a6d7-41da-aae9-7f7c9fc3f2dd
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Share-Malicious-Map-to-Obtain-URL

## Summary

This procedure generates a public share URL for the malicious map project, hosting it on api.mapbox.com and making the stored XSS payload accessible to victims.

## Description

After creating the project with the injected payload, the share feature in the classic editor produces a URL that points to the api.mapbox.com share page. This page displays the map and unsanitized title. The procedure requires the project to be saved and shared publicly. Outcomes include a URL ready for distribution, with the payload embedded but not yet executed until victim interaction.

## Requirements

1. Existing malicious map project
2. Access to share functionality in the editor
3. Public sharing permissions on the account

## Defense

Defensive measures and detection strategies:

- Scan shared content for malicious patterns before URL generation
- Rate-limit share requests to prevent abuse
- Log and review share URLs for suspicious titles

## Objectives

1. Obtain a persistent URL hosting the payload
2. Ensure the share page renders the malicious title
3. Facilitate victim targeting via the URL

## Instructions

### Step 1: Navigate to Share Option

**Context**: Locate the sharing interface.

In the map editor, find and click the 'Share' button for the project.

### Step 2: Generate Share URL

**Context**: Create the public link.

Select public sharing and copy the generated URL, typically in the format `https://api.mapbox.com/maps/...`.

> The URL embeds the map ID, pulling the stored title.

### Step 3: Test URL

**Context**: Verify the payload is present.

Open the URL in a browser and inspect the page source to confirm the title contains the injected payload.

**Expected Output**: Share page loads with map and title visible in HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[mapbox]]
