---
id: proc-access-discourse-topic
tags:
  - discourse
  - web
  - access
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
updated_at: '2025-12-14T03:47:12.764Z'
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
# Access-Discourse-Topic-Creation

## Summary

This procedure outlines accessing a Discourse forum instance and initiating the topic creation interface, serving as the entry point for injecting payloads into the composer.

## Description

In a Discourse environment, public or guest access to topic creation allows attackers to prepare for XSS exploitation. This step involves navigating to the site and opening the composer, requiring no authentication on demo instances. The target is any Discourse-powered forum, with the goal of reaching the title field where links can be pasted.

## Requirements

1. Web browser with JavaScript enabled
2. Publicly accessible Discourse instance (e.g., try.discourse.org)
3. No credentials needed for unauthenticated access

## Defense

Defensive measures and detection strategies:

- Require authentication for topic creation to prevent guest abuse
- Monitor for unusual traffic to composer endpoints
- Implement rate limiting on preview fetches

## Objectives

1. Gain access to the topic composer interface
2. Position for payload injection
3. Validate site accessibility without errors

## Instructions

### Step 1: Load the Discourse Site

**Context**: Navigate to the target forum to confirm availability and locate the creation entry point.

No specific command; use browser navigation to http://try.discourse.org/.

> The homepage loads, displaying forum categories and the 'New topic' button.

### Step 2: Open Composer

**Context**: Initiate the topic creation form to access input fields.

Click the 'New topic' button.

> The composer interface appears with title and body fields; placeholder text in title field indicates link pasting capability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[discourse]]
- [[web-access]]
