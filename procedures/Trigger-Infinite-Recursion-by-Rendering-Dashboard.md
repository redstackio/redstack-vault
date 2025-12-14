---
tags:
  - phabricator
  - rendering
  - recursion
  - dos
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 5e85532a-01a7-47f9-8dfa-db96447dc6e8
created_at: '2025-12-14T17:26:30.473Z'
updated_at: '2025-12-14T17:26:30.473Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Trigger-Infinite-Recursion-by-Rendering-Dashboard

## Summary

This procedure triggers the denial of service by forcing Phabricator to render the self-referential panel, causing infinite recursion and resource exhaustion.

## Description

Once the self-embed is in place, rendering the dashboard or embedding the panel elsewhere (e.g., in a Maniphest task comment) causes the engines to loop indefinitely. The lack of cycle detection results in a "choke" where pages fail to load, affecting tasks, feeds, and homepages for all users. This exploits the interaction between PhabricatorDashboardPanelRenderingEngine and the Remarkup engine in PHP-based Phabricator.

## Requirements

1. Self-referential panel already created and saved
2. Ability to view or embed the dashboard/panel
3. Target pages where the panel can be referenced (e.g., comments)

## Defense

Defensive measures and detection strategies:

- Implement recursion depth limits in rendering
- Timeout rendering processes and log failures
- Disable or sandbox dashboard embeds in high-traffic areas

## Objectives

1. Initiate rendering to exploit the recursion
2. Disrupt service across multiple views
3. Achieve widespread DoS impact

## Instructions

### Step 1: View or Save Dashboard

**Context**: Force initial rendering of the dashboard containing the malicious panel.

Navigate to the dashboard and refresh or save it to trigger processing.

**Expected Output**: Rendering hangs or times out due to infinite loop.

### Step 2: Embed in Broader Context

**Context**: Propagate the DoS to other areas like task comments.

Copy the panel reference or embed it in a Maniphest comment using {W1} syntax, then submit or view the task.

**Expected Output**: Affected page (task, feed, homepage) fails to render.

### Step 3: Verify Impact

**Context**: Confirm DoS across users and pages.

Attempt to access various Phabricator views; observe failures for all users.

**Expected Output**: Multiple pages become inaccessible, confirming resource exhaustion.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[phabricator]]
- [[rendering]]
- [[recursion]]
- [[dos]]
