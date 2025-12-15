---
id: uuid4
tags:
  - phishing
  - social-engineering
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
  - '[[T1566.001]]'
updated_at: '2025-12-14T17:27:50.228Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Trick-Authenticated-User-to-Visit-Malicious-Page

## Summary

Use social engineering to direct an authenticated Argo CD user to the malicious subdomain page, triggering the embedded CSRF JavaScript.

## Description

The Lax SameSite policy allows cross-subdomain requests with credentials if from the same site (parent domain). No user interaction beyond visiting is needed, as JS runs automatically.

## Requirements

1. Injected JS on subdomain
2. Target user with Argo CD session active
3. Phishing vector (email, link in chat)

## Defense

Defensive measures and detection strategies:

- User training on suspicious links
- Monitor cross-subdomain traffic
- Session timeouts

## Objectives

1. Ensure active Argo CD authentication
2. Trigger CSRF on visit
3. Confirm request transmission

## Instructions

### Step 1: Craft Lure

**Context**: Send phishing link to https://marketing.victim.com.

**Command** (no specific, manual):

> Email: "Check this marketing update: [link]". Expected output: User clicks while logged in.

### Step 2: Monitor Trigger

**Context**: Watch for request in Argo CD logs.

> Expected output: POST logged from subdomain IP.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1566.001]] Phishing: Spearphishing Attachment (adapt to link)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- phishing
