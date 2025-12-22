---
id: proc-uuid-1
tags:
  - recon
  - user-agent
  - web
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
  - '[[Active Scanning]]'
updated_at: '2025-12-13T23:52:33.827Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Mobile User-Agent Dependency on Snapchat Add Page

## Summary

This procedure identifies that Snapchat's add page serves different content based on the User-Agent header, exposing a mobile-optimized version vulnerable to parameter injection.

## Description

The Snapchat add page at https://www.snapchat.com/add/snapchat renders distinct HTML for desktop and mobile User-Agents. By switching to a mobile User-Agent, the page displays elements like meta tags and headers that reflect URL parameters without sanitization, setting up XSS exploitation. This reconnaissance step is crucial for targeting the vulnerable rendering path.

## Requirements

1. Web browser with User-Agent spoofing (e.g., Chrome DevTools or extension)
2. Access to public internet
3. No authentication needed

## Defense

Defensive measures and detection strategies:

- Implement consistent rendering regardless of User-Agent
- Log and monitor unusual User-Agent switches
- Use WAF to detect mobile-specific probes

## Objectives

1. Confirm mobile content delivery
2. Identify reflection points in mobile HTML
3. Establish baseline for payload crafting

## Instructions

### Step 1: Access Page with Desktop User-Agent

**Context**: Load the page normally to observe baseline desktop content.

Access https://www.snapchat.com/add/snapchat in a standard browser session.

> Expected: Desktop-optimized page without username reflection in visible elements.

### Step 2: Switch to Mobile User-Agent

**Context**: Spoof a mobile User-Agent to trigger vulnerable rendering.

Use browser tools to set User-Agent to something like "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1". Reload https://www.snapchat.com/add/snapchat.

> Expected: Mobile page loads with potential parameter reflection in meta and header tags.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[user-agent]]
