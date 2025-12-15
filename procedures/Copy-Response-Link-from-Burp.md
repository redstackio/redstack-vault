---
id: uuid-5
tags:
  - response-handling
  - browser-view
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite-Community-Edition]]'
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
updated_at: '2025-12-14T17:24:26.972Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Copy-Response-Link-from-Burp

## Summary

Generates and copies a link to view the 302 response in a browser-like interface for further validation.

## Description

Burp's "Show response in browser" feature embeds the response as a viewable page, useful for observing redirect behavior without external tools.

## Requirements

1. 302 response received in Repeater
2. Burp's Collaborator or browser feature enabled

## Defense

Defensive measures and detection strategies:

- N/A (client-side observation)

## Objectives

1. Create browser-viewable response link
2. Facilitate redirect testing

## Instructions

### Step 1: Select Response

**Context**: Target the 302 response.

In Repeater response pane, right-click the response.

### Step 2: Generate Link

**Context**: Copy for browser use.

Choose "Show response in browser" and copy the provided URL.

**Expected Output**: Clipboard contains a http://burp/link-to-response URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Community-Edition]]

## Tags

- [[response-handling]]
- [[browser-view]]
- [[web]]
