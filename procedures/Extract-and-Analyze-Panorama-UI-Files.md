---
tags:
  - discovery
  - panorama-ui
type: procedure
tools:
  - '[[tools/grep]]'
  - '[[tools/SourceMod]]'
  - '[[tools/Metamod]]'
  - '[[tools/CS:GO-Dedicated-Server]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/disconnect-html-test]]'
  - '[[commands/kickid-test]]'
  - '[[commands/sm-kick-test]]'
  - '[[commands/sm-testkick-rce]]'
platforms:
  - Windows
techniques:
  - '[[Gather Victim Network Information]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 395d7d03-e206-4335-9827-577a09c5ab2d
created_at: '2025-12-11T06:10:15.664Z'
updated_at: '2025-12-11T06:10:15.664Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1590]]'
---
# Extract and Analyze Panorama UI Files

## Summary

This procedure involves extracting the Panorama UI files from a CS:GO installation to identify potential vulnerabilities in the UI framework.

## Description

By unzipping the code.pbin file, attackers can access XML layout files that define UI behavior, setting the stage for vulnerability hunting such as searching for unsanitized HTML attributes.

## Requirements

1. CS:GO installed on Windows
2. Access to the installation directory
3. Basic file extraction tools

## Defense

Defensive measures and detection strategies:

- Monitor file access to game directories
- Use application whitelisting

## Objectives

1. Obtain UI layout files
2. Prepare for grep-based searching
3. Identify entry points for injection

## Instructions

### Step 1: Locate and Extract Files

**Context**: Unzip the Panorama code bundle.

Unzip steamapps\common\Counter-Strike Global Offensive\csgo\panorama\code.pbin to reveal UI files.

> Extracts XML files like popup_generic.xml.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Gather Victim Network Information]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- discovery
- panorama-ui
