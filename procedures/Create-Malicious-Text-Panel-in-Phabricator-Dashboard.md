---
tags:
  - phabricator
  - dashboard
  - text-panel
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
impact_level: low
detection_risk: low
sub_techniques: []
id: 2a06575a-e62e-4819-94d2-a701ce96261d
created_at: '2025-12-14T17:26:30.484Z'
updated_at: '2025-12-14T17:26:30.484Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Create-Malicious-Text-Panel-in-Phabricator-Dashboard

## Summary

This procedure creates a new Text Panel in a Phabricator dashboard, which serves as the foundation for a self-referential embed attack leading to denial of service.

## Description

In Phabricator, dashboards allow users to create customizable panels, including Text Panels for custom content. This step involves navigating to the Dashboards area and initiating a new Text Panel, which automatically receives a unique object reference (e.g., W1). This reference is crucial for the subsequent self-embedding step. The procedure assumes authenticated access with dashboard creation permissions and targets Phabricator installations vulnerable to recursive rendering issues.

## Requirements

1. Authenticated session in Phabricator with dashboard creation permissions
2. Access to the web interface via browser
3. Enabled dashboard feature in the target installation

## Defense

Defensive measures and detection strategies:

- Restrict dashboard creation to trusted users via role-based access controls
- Monitor for unusual panel creation patterns in audit logs
- Implement rate limiting on dashboard edits

## Objectives

1. Establish a target panel for self-referencing
2. Obtain the panel's object ID for embedding
3. Prepare for recursion without triggering it prematurely

## Instructions

### Step 1: Navigate to Dashboards

**Context**: Access the dashboard management interface to begin panel creation.

Log in to Phabricator and go to the Dashboards section (typically under Applications > Dashboards).

### Step 2: Create New Text Panel

**Context**: Initiate and configure a basic Text Panel.

Click "Create Dashboard" or edit an existing one, then add a new panel selecting "Text" type. Provide minimal content if needed, and save to generate the object reference.

**Expected Output**: Panel created with reference like {W1} displayed in the URL or panel details.

### Step 3: Verify Panel Reference

**Context**: Confirm the unique ID for use in the next procedure.

Inspect the panel's properties or URL to note the reference ID (e.g., W1).

**Expected Output**: Reference ID confirmed, ready for embedding.

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
- [[dashboard]]
- [[text-panel]]
