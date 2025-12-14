---
id: proc-brave-uri-test-tor-001
tags:
  - brave
  - uri-navigation
  - tor
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
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:24:56.254Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---
# Test-Brave-URI-Navigation-Tor

## Summary

This procedure tests navigation to brave:// URIs in Tor mode via drag-and-paste methods, further exposing inconsistencies in privacy handling as shown in proof-of-concept videos.

## Description

Brave's protocol handling allows brave:// URIs to load in Tor without proper isolation, potentially from network contexts. Targets Brave 1.29.81; requires Tor window. Outcomes validate bypass of expected redirects, aiding broader disclosure scenarios.

## Requirements

1. Active Tor session
2. A brave:// URI to test (e.g., from clipboard or drag)
3. Local browser interaction

## Defense

Defensive measures and detection strategies:

- Enforce strict URI validation in private modes
- Disable drag-and-drop for internal URIs in Tor
- Log protocol navigation attempts for anomalies

## Objectives

1. Bypass URI restrictions in Tor
2. Confirm navigation flaws
3. Enhance disclosure testing

## Instructions

### Step 1: Prepare URI for Input

**Context**: Obtain a brave:// URI from another context or manually.

No command; preparation:

- Copy a URI like `brave://inspect/#devices` to clipboard.

> Expected: URI ready for paste or drag.

### Step 2: Initiate Navigation in Tor

**Context**: Use drag or paste to trigger loading in Tor address bar.

No command; UI action:

- Drag the URI into Tor address bar or paste and press Enter.

> Successful: URI loads directly in Tor, without redirect, as per PoC video demonstrations.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Information Repositories]] Data from Information Repositories

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[navigation-test]]
- [[brave-uri]]
- [[poc]]
