---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - xss
  - injection
  - rails
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/rails-create-malicious-skill]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.798Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Skill-with-XSS-Payload

## Summary

This procedure creates a malicious skill record in the HackerOne Rails database containing an XSS payload, exploiting the lack of input sanitization for skill names, which are later rendered unsafely in user profiles.

## Description

In the context of HackerOne's Support Backend, skill names are user-controlled but not sanitized before being interpolated into HTML elements like title attributes and spans. This procedure uses the Rails console to insert a script tag payload, setting up the stored XSS for subsequent profile viewing. Prerequisites include local Rails environment access and database write permissions. Expected outcome is a persistent payload that executes JavaScript when rendered.

## Requirements

1. Access to Rails console in a local development setup
2. Ruby on Rails environment with HackerOne codebase
3. Database connectivity for Skill model

## Defense

Defensive measures and detection strategies:

- Implement HTML escaping or sanitization libraries like Rails' html_safe or Loofah for user inputs
- Validate and whitelist allowed characters in skill names
- Monitor database inserts for script tags or suspicious patterns

## Objectives

1. Inject executable JavaScript into a skill record
2. Store the payload persistently for later retrieval
3. Prepare for profile assignment to trigger execution

## Instructions

### Step 1: Access Rails Console

**Context**: Launch the Rails console to interact with the database models.

No command; run `rails console` in the project directory.

### Step 2: Create Malicious Skill

**Context**: Use the Skill model to insert a record with the XSS payload in the name field.

**Command** ([[commands/rails-create-malicious-skill]]):
```ruby
Skill.create! name:'<script>alert(/XSS/);</script>'
```

> This command creates a new Skill instance with the name set to the payload. Expected output is a confirmation of the created object, e.g., => #<Skill id: 1, name: "<script>alert(/XSS/);</script>">. Verify by querying Skill.last.name.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/rails-create-malicious-skill]]

## Tools Used


## Tags

- [[xss]]
- [[injection]]
