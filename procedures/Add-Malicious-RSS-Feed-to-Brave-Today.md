---
id: uuid-placeholder-002
tags:
  - xss
  - rss-feed
  - ios
  - brave-browser
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - iOS
  - Mobile
submitted: true
created_at: '[TIMESTAMP]'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-13T23:52:20.852Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Add-Malicious-RSS-Feed-to-Brave-Today

## Summary

This procedure outlines the steps to configure and add a malicious RSS feed to the Brave iOS app's Brave Today feature, setting up the environment for a DOM-based XSS attack by injecting a feed with javascript: URL payloads in entry links.

## Description

The Brave iOS app allows users to add custom RSS feeds to Brave Today without validating URL schemes in the <link> href attributes of RSS entries. By adding a feed like https://csrf.jp/brave/rss.php containing a <entry> with <link href="javascript:alert(document.domain)" />, the app parses and renders it, enabling exploitation upon user interaction. This targets the app's internal handling on http://localhost:65XX, potentially exposing features like reader-view and error pages. Prerequisites include a vulnerable Brave iOS version and access to the malicious feed host.

## Requirements

1. iOS device running Brave Browser app (vulnerable version)
2. Internet access to fetch the malicious RSS feed
3. No app-level restrictions on RSS sources

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all URL schemes in RSS parsers to block javascript: and similar
- Implement content security policies (CSP) for internal localhost domains
- Monitor app logs for unexpected JS execution on localhost ports

## Objectives

1. Integrate malicious RSS feed into Brave Today
2. Enable feed to load XSS payload entries
3. Prepare for payload triggering without alerting the user

## Instructions

### Step 1: Open Settings and Navigate to Brave Today

**Context**: Access the configuration for custom RSS sources.

Launch Brave app, tap the settings icon, then select "Brave Today".

> This opens the feed management interface.

### Step 2: Initiate Add Source and Search for Malicious Feed

**Context**: Locate and prepare to add the PoC RSS feed.

Tap "Add Source", enter `https://csrf.jp/brave/rss.php`, and tap Search. Select the "PoC" feed.

> Search fetches the feed metadata; no validation occurs here.

### Step 3: Add and Enable the Feed

**Context**: Integrate and activate the feed to parse entries.

Tap "Add" on the PoC feed, then toggle it enabled in the sources list.

> Feed is now active, entries including the malicious <link> are queued for display.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[xss]]
- [[rss-feed]]
- [[ios]]
- [[brave-browser]]
