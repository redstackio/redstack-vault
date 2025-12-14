---
tags:
  - phabricator
  - remarkup
  - self-reference
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
impact_level: medium
detection_risk: medium
sub_techniques: []
id: dbcb89da-fcb2-4d11-8723-36eb80272880
created_at: '2025-12-14T17:26:30.477Z'
updated_at: '2025-12-14T17:26:30.477Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Embed-Self-Reference-in-Panel-Content-Using-Remarkup

## Summary

This procedure embeds a self-referential link into a Phabricator Text Panel's content using Remarkup syntax, setting up the condition for infinite recursion during rendering.

## Description

Remarkup is Phabricator's markup language for embedding objects like panels via syntax such as {W1}. By inserting the panel's own reference into its content, this creates a circular dependency. When rendered, the dashboard engine (PhabricatorDashboardPanelRenderingEngine) calls the Remarkup engine, which re-embeds the panel, leading to recursion. This targets the vulnerability in cycle detection between these engines.

## Requirements

1. Existing Text Panel with known reference ID (from prior procedure)
2. Edit permissions on the dashboard
3. Browser access to the panel edit interface

## Defense

Defensive measures and detection strategies:

- Add cycle detection in rendering pipelines
- Validate embeds for self-references during save
- Log and alert on recursive syntax patterns

## Objectives

1. Introduce self-referential embed syntax
2. Save the malicious content without immediate rendering
3. Enable propagation to other views like comments

## Instructions

### Step 1: Edit Panel Content

**Context**: Access the content field of the target Text Panel.

Navigate to the dashboard, select the Text Panel, and click edit.

### Step 2: Insert Self-Reference Syntax

**Context**: Use Remarkup to embed the panel's own ID.

In the content area, enter the syntax `{W1}` (replace W1 with the actual reference). Add any placeholder text if needed, e.g., "Panel content: {W1}".

**Expected Output**: Syntax inserted; preview may not trigger full recursion yet.

### Step 3: Save Changes

**Context**: Persist the embed without rendering the full dashboard.

Save the panel. Avoid immediate full dashboard view to prevent premature triggering.

**Expected Output**: Edit saved successfully, panel updated with self-reference.

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
- [[remarkup]]
- [[self-reference]]
