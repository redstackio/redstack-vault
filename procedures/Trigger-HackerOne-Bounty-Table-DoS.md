---
id: proc-1043372-trigger-dos
tags:
  - dos
  - client-side
  - memory-exhaustion
  - browser-crash
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:56.110Z'
skill_level: novice
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[Application or System Exploitation]]'
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Trigger-HackerOne-Bounty-Table-DoS

## Summary

This procedure exploits a client-side vulnerability in HackerOne's bounty table update feature by accessing a page with a corrupted or excessively large bounty table, causing browser memory exhaustion, UI unresponsiveness, and eventual tab crash. It demonstrates uncontrolled resource consumption during JavaScript rendering of high-activity program data.

## Description

The vulnerability occurs when HackerOne's web application renders bounty table versions without proper limits or pagination for programs with high activity, such as Clario. Viewing the page via a notification link triggers excessive memory allocation in the browser's JavaScript engine, leading to 'Out of Memory' errors and crashes. This affects all users who access the page, spiking CPU and RAM to maximum levels and preventing interactions. No server-side exploitation is needed; it's purely client-side impact, reproducible in Chrome and Firefox on various devices.

## Requirements

1. Access to a HackerOne account (authenticated or public view, depending on program settings)
2. A notification link or direct URL to a vulnerable bounty table (e.g., for a high-activity program like Clario with nid parameter)
3. Modern web browser (Chrome or Firefox recommended for reproduction)

## Defense

Defensive measures and detection strategies:

- Implement client-side resource limits and pagination in bounty table rendering to prevent excessive data loading
- Sanitize and validate bounty table data on the server before serving to clients
- Monitor browser console for memory warnings and add error handling in JavaScript to gracefully degrade on large datasets
- Use browser extensions or policies to limit per-tab resource usage

## Objectives

1. Cause browser tab crash and resource exhaustion on the target user
2. Prevent user interactions with the HackerOne interface
3. Demonstrate impact on system stability for low-spec devices

## Instructions

### Step 1: Navigate to the Vulnerable URL

**Context**: Access the bounty table versions page to start the rendering process that triggers memory exhaustion.

No specific command required; use browser navigation:

Open your web browser and enter or click the URL: https://hackerone.com/clario/bounty_table_versions?nid=115515717&utm_campaign=user_652675&utm_content=team_url&utm_medium=email&utm_source=bounty_table_update

> This loads the page, initiating JavaScript rendering of the complex table data, which begins consuming excessive memory.

### Step 2: Monitor Resource Usage and Interactions

**Context**: Observe the effects of rendering on browser performance and UI responsiveness.

No specific command required; interact with the page:

Attempt to click buttons like profile or inbox while the table loads.

> UI elements freeze due to resource spikes; check browser task manager (e.g., Chrome Task Manager via Shift+Esc) for high CPU/RAM usage by the tab.

### Step 3: Await and Confirm Crash

**Context**: Allow the full rendering to complete, forcing the out-of-memory condition.

No specific command required; keep the tab open:

Wait 10-30 seconds for the crash to occur.

> An 'Out of Memory' error displays, and the tab crashes. Verify by attempting to reload; reproduction confirms success.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques

- [[Application or System Exploitation]]

## Commands Used


## Tools Used


## Tags

- dos
- client-side
- memory-exhaustion
- browser-crash
- hackerone
