---
tags:
  - information-disclosure
  - web-recon
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[File and Directory Discovery]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: d9daaeb2-86d1-42a9-ae47-497eac3fa80e
created_at: '2025-12-14T17:32:39.196Z'
updated_at: '2025-12-14T17:32:39.196Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Trigger-404-Page-to-Reveal-JavaScript-Files

## Summary

This procedure involves navigating to a non-existent URL on the target web application to trigger a 404 error page, which due to poor configuration, loads and exposes references to internal JavaScript files in its source code.

## Description

In the Semrush vulnerability, the 404 error handler incorrectly includes script tags for internal JS files in the page source, making them discoverable without authentication. This step initiates the reconnaissance phase by exploiting the error page's misconfiguration to reveal potential sensitive assets. Expected outcomes include visibility into application file structure, setting the stage for further disclosure.

## Requirements

1. Web browser with internet access
2. Knowledge of the target domain (e.g., semrush.com)
3. No special privileges or tools needed

## Defense

Defensive measures and detection strategies:

- Configure 404 pages to exclude internal script references or use minimal error handlers
- Implement content security policies (CSP) to restrict script loading on error pages
- Monitor access logs for unusual 404 requests to non-standard paths

## Objectives

1. Generate a 404 response to expose hidden file references
2. Identify potential internal assets in the page source
3. Establish initial footprint of the application's file structure

## Instructions

### Step 1: Navigate to Non-Existent URL

**Context**: This action simulates a broken link or typo to trigger the error page without raising suspicion.

Open your web browser and enter a URL like https://www.semrush.com/random-nonexistent-path. Press Enter to load the page.

> The browser will display a 404 Not Found error, but the underlying HTML will include unintended script includes.

### Step 2: Verify 404 Response

**Context**: Confirm the error status to ensure the page is the target 404 handler.

Check the browser's developer tools (F12) > Network tab for a 404 status code on the request.

> Expected: HTTP 404 response with HTML content loading additional resources.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[information-disclosure]]
- [[web-recon]]
