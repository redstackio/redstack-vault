---
id: proc-brave-tor-launch-001
tags:
  - brave
  - tor
  - browser
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
updated_at: '2025-12-14T17:24:56.305Z'
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
# Launch-Brave-Tor-Mode

## Summary

This procedure initiates a private browsing session in Brave using Tor integration, establishing an isolated environment intended for enhanced privacy but vulnerable to inconsistent URI protections.

## Description

In Brave browser (version 1.29.81 on Chromium 93.0.4577.82), Tor mode creates a window that routes traffic through the Tor network. However, this procedure sets up the context for testing privacy leaks via accessible privileged URIs. The target environment is a local browser instance, with no external network dependencies beyond Tor bootstrapping. Expected outcomes include a functional Tor window ready for URI navigation tests.

## Requirements

1. Brave browser installed (version 1.29.81 or compatible)
2. Internet connection for Tor bootstrap
3. Local user access to the browser

## Defense

Defensive measures and detection strategies:

- Use browser extensions to block privileged URI access in private modes
- Monitor browser logs for unexpected chrome:// navigations in Tor sessions
- Educate users on Tor mode limitations and avoid mixing sessions

## Objectives

1. Establish a privacy-focused Tor browsing context
2. Prepare for testing URI accessibility inconsistencies
3. Isolate traffic to demonstrate potential leaks

## Instructions

### Step 1: Open Brave and Enable Tor

**Context**: Launch the browser and activate Tor mode to create the isolated session.

No specific command; perform via UI:

- Open Brave browser.
- Click the menu (three lines) > New Private Window with Tor.

> This opens a new window with Tor enabled, indicated by the onion icon. Traffic routes through Tor, and the session does not persist history.

### Step 2: Verify Tor Connection

**Context**: Confirm the session is active and privacy protections are in place.

No command; check UI:

- Look for the Tor connection status in the address bar.
- Attempt to load a .onion site to validate routing.

> Successful output: Tor bootstrap completes, and .onion sites load. This confirms the privacy context before proceeding to URI tests.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[brave]]
- [[tor]]
- [[privacy]]
