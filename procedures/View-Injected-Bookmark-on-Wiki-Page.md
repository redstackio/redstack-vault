---
tags:
  - xss
  - web
  - confluence
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:02.540Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: b8f67135-367d-465a-8b7e-ab8c068f959e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# View-Injected-Bookmark-on-Wiki-Page

## Summary

This procedure involves navigating to the wiki page where the malicious bookmark is displayed, allowing the stored payload to be rendered as a clickable link for victims.

## Description

After creation, the bookmark integrates into the wiki page via the socialbookmarking plugin, rendering the title as an anchor tag with the unsanitized href. Any user viewing the page (authenticated or not, depending on permissions) sees the link, setting up the XSS trigger. This step confirms the payload's persistence in the wiki environment.

## Requirements

1. Knowledge of the bookmark title used
2. Access to the wiki display endpoint
3. Web browser

## Defense

Defensive measures and detection strategies:

- Scan stored content for dangerous protocols in links
- Restrict wiki page visibility to authenticated users
- Implement server-side rendering checks for href attributes

## Objectives

1. Load the page containing the bookmark
2. Verify the malicious link is visible
3. Simulate victim access without triggering

## Instructions

### Step 1: Construct Page URL

**Context**: Build the display URL using the bookmark title.

Replace <TITLE> with the bookmark title, e.g., https://apps.topcoder.com/wiki/display/tcwiki/powerpuff_hackerone_test.

> URL is ready for navigation.

### Step 2: Load the Page

**Context**: Access the page to render the bookmark.

Enter the URL in the browser and load the page.

> Page displays with the bookmark title shown as a link.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[web]]
- [[Confluence]]
