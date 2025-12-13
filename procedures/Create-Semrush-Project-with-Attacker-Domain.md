---
tags:
  - xxe
  - semrush
  - initial-setup
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 7bdf60b5-462f-4a38-87ae-add617602273
created_at: '2025-12-13T09:00:33.780Z'
updated_at: '2025-12-13T09:00:33.780Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create Semrush Project with Attacker Domain

## Summary

This procedure involves setting up a new project in Semrush using an attacker-controlled domain, which serves as the foundation for hosting and submitting a malicious sitemap.xml to exploit the XXE vulnerability.

## Description

By creating a project tied to a domain under attacker control, you enable the configuration of Site Audit to process a custom sitemap. This is a prerequisite for injecting malicious XML entities that the Java XML processor will resolve, potentially exposing server files. The target environment is the Semrush web platform running on Linux with a vulnerable Java XML processor. Expected outcomes include successful project creation without alerts.

## Requirements

1. Semrush account with project creation permissions
2. Control over a domain (e.g., semrush.webhooks.pw) for hosting files
3. Web browser for interacting with Semrush UI

## Defense

Defensive measures and detection strategies:

- Implement strict validation on user-provided URLs and XML files
- Monitor for unusual project creations or sitemap submissions from new domains

## Objectives

1. Establish a project linked to attacker domain
2. Prepare for Site Audit configuration
3. Enable malicious sitemap submission

## Instructions

### Step 1: Log into Semrush

**Context**: Access the Semrush dashboard to begin project creation.

Navigate to the projects section in Semrush using a web browser like [[tools/Firefox]] or [[tools/Google-Chrome]].

> Log in with valid credentials.

### Step 2: Create New Project

**Context**: Set up the project with the attacker domain.

Click 'Create Project' and enter the attacker-controlled domain, e.g., semrush.webhooks.pw.

> Confirm the project details and save.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Firefox]]
- [[tools/Google-Chrome]]

## Tags

- [[xxe]]
- [[semrush]]
- [[initial-setup]]
