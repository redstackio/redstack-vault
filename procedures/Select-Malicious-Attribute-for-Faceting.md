---
id: proc-algolia-select-facet-001
tags:
  - xss
  - stored-xss
  - algolia
  - configuration
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:47.221Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Select-Malicious-Attribute-for-Faceting

## Summary

This procedure configures the Algolia index display settings to include the malicious attribute for faceting, setting up the conditions for XSS rendering and execution.

## Description

By selecting the injected malicious attribute in the faceting configuration, this step forces the Algolia UI to retrieve and display the attribute name in HTML contexts. The lack of escaping in the Display settings leads to payload execution upon save or view. This targets the web interface's rendering pipeline. Requires prior injection and admin access. Outcomes include prepared triggers for multiple pages.

## Requirements

1. Authenticated session with index configuration permissions
2. Malicious record already indexed
3. Access to Indices > Display settings

## Defense

Defensive measures and detection strategies:

- Escape HTML in all attribute listings and configs
- Restrict faceting to validated attribute names
- Audit configuration changes for suspicious attributes

## Objectives

1. Integrate payload into UI rendering path
2. Enable execution on save/view
3. Bridge to explorer and public exposures

## Instructions

### Step 1: Configure Faceting

**Context**: Navigate to display settings and add the attribute.

In the dashboard: Go to Indices > Display > Attributes for Faceting, search for and select '<img src=1 onerror=alert(document.domain)>', then click Save.

> The UI renders the attribute name, potentially queuing execution. Confirm by checking the faceting list post-save.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[algolia]]
