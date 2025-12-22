---
tags:
  - navigation
  - setup
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques: []
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 03cf92b9-022e-4140-bfdc-f4aeef59df0a
created_at: '2025-12-14T03:16:14.382Z'
updated_at: '2025-12-14T03:16:14.382Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Navigate-to-Inventory-Zones-Invocation-Code

## Summary

This procedure guides navigation through the Revive Adserver interface to the Inventory > Zones > Invocation Code section, creating prerequisite websites and zones if necessary to access the vulnerable form.

## Description

The Invocation Code page in Revive Adserver generates embeddable code for ad zones. Without existing websites or zones, the section may be inaccessible, so test entities must be created. This targets the web-based admin panel and sets up the environment for payload injection.

## Requirements

1. Authenticated session in Revive Adserver
2. Web browser access
3. Basic knowledge of the application's menu structure

## Defense

Defensive measures and detection strategies:

- Restrict access to admin sections via role-based access control (RBAC)
- Audit navigation logs for unusual paths
- Use session timeouts to limit exposure

## Objectives

1. Reach the Invocation Code interface
2. Ensure prerequisites like zones are available
3. Position for vulnerability exploitation

## Instructions

### Step 1: Access Inventory Menu

**Context**: From the dashboard, enter the Inventory section to manage zones.

Click on 'Inventory' in the top menu, then select 'Zones'.

### Step 2: Create Prerequisites if Needed

**Context**: If no zones exist, create a test website and zone to unlock Invocation Code.

Navigate to Inventory > Websites > Add new website, then Inventory > Zones > Add new zone linked to the website.

**Expected Output**: Zones list populates, allowing access to Invocation Code.

### Step 3: Enter Invocation Code Page

**Context**: Load the specific page with the Close text parameter.

Select a zone and click on 'Invocation Code' or equivalent to open the form.

**Expected Output**: Form with parameters including Close text loads.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[navigation]]
- [[revive-adserver]]
