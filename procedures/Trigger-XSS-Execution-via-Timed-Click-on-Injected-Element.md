---
tags:
  - xss-execution
  - clickjacking
  - flash
  - payload-trigger
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Flash (SWF)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:18.433Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 6428ea5f-1f9b-4143-b3d1-e554633fe247
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger XSS Execution via Timed Click on Injected Element

## Summary

This procedure exploits the rapid reload setup by clicking the injected HTML element during a brief window when the SWF's event override is disrupted, leading to JavaScript execution on the target domain and demonstrating full XSS impact.

## Description

With the flickering iframe active, the injected <a> tag's javascript: URI can fire if clicked precisely during a reload cycle, before the SWF reattaches its button event. This results in domain-level JS execution, enabling alerts, cookie theft, or session hijacking on imgur.com.

## Requirements

1. Running exploit page from prior procedure
2. Patience for timing the click
3. Flash-enabled browser

## Defense

Defensive measures and detection strategies:

- Enforce same-origin policy strictly
- Log client-side JS execution attempts
- Deprecate Flash entirely

## Objectives

1. Execute JS payload via click
2. Confirm domain access (e.g., alert)
3. Assess impact like data exfiltration

## Instructions

### Step 1: Load Exploit Page

**Context**: Start the flickering iframe.

Open the HTML file in browser; observe rapid reloads and wait for 'CLICKME' to appear.

**Expected Output**: Active flickering with visible payload.

### Step 2: Time the Click

**Context**: Click during reload window.

Rapidly click the 'CLICKME' text as it flickers; try multiple times to hit the MouseClick on HTML.

**Expected Output**: Alert('imgur.com') pops up.

### Step 3: Validate Impact

**Context**: Extend payload for real attacks.

Replace alert with fetch for cookies or keylogging; confirm execution on main domain.

**Expected Output**: Successful JS run, potential data access.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-execution]]
- [[payload-trigger]]
