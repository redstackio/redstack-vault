---
id: proc-uuid-2
tags:
  - shopify
  - judge-me
  - settings
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:47:12.945Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Navigate-to-Widget-Form-Settings

## Summary

This procedure details the navigation within the Judge.me app to reach the Widget Form settings, where the vulnerable success message field resides.

## Description

Once inside the Judge.me app, the interface provides various configuration options for review widgets. This step targets the 'Widget Form' subsection under 'Review Widget' settings, exposing fields that lack proper sanitization for user inputs like success messages. This positions the attacker to inject malicious content that will be rendered in previews.

## Requirements

1. Active session in Judge.me app via Shopify admin
2. Standard web browser navigation capabilities
3. No additional permissions beyond basic app access

## Defense

Defensive measures and detection strategies:

- Regularly audit app settings for unauthorized changes
- Enable logging of configuration modifications in Shopify apps
- Use input validation previews in admin interfaces

## Objectives

1. Access the Review Widget configuration
2. Locate the Widget Form options
3. Display editable fields including success message

## Instructions

### Step 1: Enter Settings Menu

**Context**: Begin navigation from the Judge.me main dashboard.

Click the 'Settings' tab or link in the top navigation menu.

> Expected: Settings overview page loads with subsections like General, Review Widget, etc.

### Step 2: Select Review Widget and Widget Form

**Context**: Drill down to the specific form configuration area.

From Settings, click 'Review Widget', then select 'Widget Form' from the available options.

> Expected: Widget Form page appears with text fields for customization, including success message.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[judge-me]]
- [[settings]]
