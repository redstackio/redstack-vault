---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
tags:
  - reconnaissance
  - exposed-service
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Default Accounts]]'
updated_at: '2025-12-14T17:31:19.634Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Default Accounts]]'
---
# Discover-Tiny-File-Manager-Instance

## Summary

This procedure identifies an exposed Tiny File Manager during exploration of the 'link your NIN' site, revealing a potential entry for privilege escalation.

## Description

Tiny File Manager is a PHP-based tool for file operations; if left exposed with defaults, it allows easy access. By inspecting the NIN section, attackers can find its path, often due to poor directory segregation in web apps.

## Requirements

1. Active session on the NIN page
2. Browser developer tools for inspection (optional)
3. Public exposure of the manager

## Defense

Defensive measures and detection strategies:

- Remove or secure unused admin tools
- Implement web application firewalls (WAF) to block access

## Objectives

1. Uncover hidden administrative interfaces
2. Expected outcome: File manager URL found

## Instructions

### Step 1: Explore NIN Site

**Context**: Scan for file management indicators.

Browse the 'link your NIN' page, checking URLs, source code, or sub-links for Tiny File Manager references.

> Look for paths like /filemanager or similar; access directly.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Default Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[exposed-service]]
