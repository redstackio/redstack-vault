---
id: proc-semrush-navigate-rankings
tags:
  - navigation
  - discovery
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:39.482Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Navigate-to-Rankings-Distribution-Tab

## Summary

This procedure guides navigation within the SEMrush Position Tracking interface to the Rankings Distribution tab, where the vulnerable competitor domain field is accessible for payload injection.

## Description

Once authenticated and a project is created, this step involves traversing the UI to the specific tab containing the input field susceptible to stored XSS. It targets the web-based SEMrush application, requiring an active session. The goal is to position the attacker at the injection point without triggering defenses, setting up for request interception.

## Requirements

1. Active SEMrush session from prior login
2. Created Position Tracking project
3. Standard web browser

## Defense

Defensive measures and detection strategies:

- Log UI navigation patterns to detect unusual paths or rapid traversals
- Rate-limit access to sensitive project features
- Employ client-side monitoring for anomalous form interactions

## Objectives

1. Access the Position Tracking dashboard for the project
2. Reach the Rankings Distribution tab and competitor list editor
3. Prepare the interface for payload entry

## Instructions

### Step 1: Enter Position Tracking Dashboard

**Context**: Load the project-specific dashboard to begin configuration.

No specific command; use the UI:

- From the main dashboard, click on the created Position Tracking project
- Ensure the project loads with overview metrics

> Dashboard displays tracking data and configuration options.

### Step 2: Access Rankings Distribution

**Context**: Navigate to the tab with the vulnerable domain input.

No specific command; use the UI:

- Click 'Rankings Distribution' in the left sidebar or top tabs
- Select 'Add domains' if prompted, then click 'Edit competitor's list'

> Form opens with 'new competitor's domain' field ready for input.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web-navigation
- ui-discovery
