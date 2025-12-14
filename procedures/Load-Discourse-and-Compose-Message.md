---
id: proc-load-discourse-compose
tags:
  - ssrf
  - discourse
  - initial-access
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
updated_at: '2025-12-14T03:53:38.101Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Load-Discourse-and-Compose-Message

## Summary

Access a Discourse instance and open the private message composer to prepare for SSRF payload insertion.

## Description

This initial step involves loading the target Discourse site (e.g., try.discourse.org) in a browser and navigating to the private message interface. No authentication is required for public instances. It sets the stage for embedding malicious URLs in message content, which triggers server-side image fetching.

## Requirements

1. Web browser (e.g., Chrome/Firefox)
2. Access to public Discourse instance
3. No special credentials

## Defense

Defensive measures and detection strategies:

- Rate-limit message composition and submissions
- Log user sessions for anomaly detection
- Implement CAPTCHA on high-risk actions

## Objectives

1. Gain access to message composer
2. Prepare recipient and topic fields

## Instructions

### Step 1: Access Target Site

**Context**: Load the Discourse homepage to confirm availability.

**Command** (Browser action):
Navigate to http://try.discourse.org/

> Site loads with forum interface. Expected: No errors, public access granted.

### Step 2: Open Message Composer

**Context**: Initiate a new private message.

**Command** (Browser action):
Click 'New Message' or equivalent to open composer.

> Form appears with fields for recipient, topic, and content. Expected: Interface ready for input.

### Step 3: Set Recipient and Topic

**Context**: Fill basic fields to make the message valid.

**Command** (Browser action):
Enter a valid username as recipient and a topic title.

> Fields populated without validation errors. Expected: Composer advances to content entry.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- discourse
- compose
