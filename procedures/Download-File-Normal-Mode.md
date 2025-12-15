---
id: proc-brave-download-normal-001
tags:
  - brave
  - download
  - normal-mode
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web Browser
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:24:56.294Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Download-File-Normal-Mode

## Summary

This procedure performs a file download in a standard Brave browsing session to generate history entries that can later be leaked into Tor mode.

## Description

In non-Tor Brave windows, downloads are recorded globally, including file names and source URLs. This targets Brave 1.29.81, creating data for disclosure testing. No external tools needed; outcomes include a visible download entry ready for cross-session visibility check.

## Requirements

1. Standard Brave window open
2. Internet access for download source
3. Local storage for file save

## Defense

Defensive measures and detection strategies:

- Clear download history regularly in mixed sessions
- Use incognito modes consistently without mixing
- Monitor for cross-session data access in browser logs

## Objectives

1. Generate download history in normal context
2. Record file details for leakage verification
3. Prepare data for Tor disclosure test

## Instructions

### Step 1: Navigate to Download Source

**Context**: Visit a site with downloadable content to initiate the process.

No command; UI action:

- Open a normal Brave window.
- Navigate to `https://docs.oracle.com/javase/tutorialJWS/samples/deployment/dynamictree_webstartJWSProject/dynamictree_webstart.jnlp`.

> Expected: Page loads, presenting the download option.

### Step 2: Initiate and Save Download

**Context**: Trigger the download and save locally to create history entry.

No command; UI action:

- Click to download the .jnlp file.
- Choose a local save path when prompted.

> Successful: File saves, and entry appears in chrome://downloads with name and URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[download]]
- [[history-leak]]
- [[normal-session]]
