---
id: proc-uuid-5
tags:
  - zendesk
  - content-creation
  - help-center
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
updated_at: '2025-12-14T05:32:23.588Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create Unpublished Help Center Guide in Zendesk

## Summary

This procedure sets up an unpublished guide in Zendesk's Help Center to prepare for hosting controlled content on the taken-over subdomain.

## Description

With domain control, create draft content structures in the Help Center to mimic legitimate support pages without immediate visibility, allowing stealthy preparation for attacks like phishing.

## Requirements

1. Active Zendesk account with mapped domain
2. Access to Help Center admin
3. Basic content creation knowledge

## Defense

Defensive measures and detection strategies:

- Monitor for unauthorized Help Center activity on claimed subdomains
- Require approval workflows for content publication
- Scan for draft content matching brand keywords

## Objectives

1. Establish content framework under subdomain
2. Prepare for article addition
3. Demonstrate partial control

## Instructions

### Step 1: Navigate to Help Center

**Context**: Access guide management.

In Zendesk admin, go to Help Center > Guides.

> Expected: Guide creation interface.

### Step 2: Create New Guide

**Context**: Add a draft guide section.

Create a new guide and save without publishing.

> Expected: Guide in draft status, editable.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[zendesk]]
- [[content-creation]]
- [[help-center]]
