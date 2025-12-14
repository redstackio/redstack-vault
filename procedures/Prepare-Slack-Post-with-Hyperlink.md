---
tags:
  - slack
  - post-creation
  - hyperlink
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
  - Desktop
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:26:56.270Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 6215f4f1-450a-4e97-bc54-da470b230c82
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Prepare-Slack-Post-with-Hyperlink

## Summary

This procedure outlines the initial steps to create a Slack post with a hyperlink, setting the stage for interception and payload injection to exploit DOM clobbering vulnerabilities.

## Description

In the context of attacking Slack's post editor, this involves navigating the interface, adding content, and initiating hyperlink creation to trigger an interceptable HTTP POST request. The target environment is any Slack client with post permissions. Expected outcomes include a prepared post ready for modification, enabling subsequent HTML injection without alerting defenses.

## Requirements

1. Valid Slack account with post creation permissions in a workspace
2. Access to Slack application (web, desktop, or mobile)
3. Proxy setup (e.g., Burp Suite) to intercept traffic

## Defense

Defensive measures and detection strategies:

- Implement client-side input validation in post editors to block suspicious URLs
- Monitor for anomalous HTTP requests with HTML-like payloads in link parameters
- Use web application firewalls to sanitize hyperlink inputs

## Objectives

1. Set up a post that generates an interceptable request
2. Avoid triggering any immediate sanitization checks
3. Prepare for payload injection in the link field

## Instructions

### Step 1: Access Post Creation

**Context**: Open the Slack interface to begin post composition.

No specific command; navigate via UI to a channel or DM and click compose.

> This loads the editor without network calls yet.

### Step 2: Add Content

**Context**: Input text to create context for the hyperlink.

Enter arbitrary title and body text in the editor.

> Content is local until submission.

### Step 3: Invoke Link Creation

**Context**: Select text and open the link dialog to prepare the POST.

Highlight text and click the link button.

> Dialog opens, ready for URL input.

### Step 4: Enter Placeholder URL

**Context**: Input a benign URL to initiate request.

Type "https://example.com" and confirm.

> Triggers the interceptable POST request.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[slack]]
- [[hyperlink-injection]]
