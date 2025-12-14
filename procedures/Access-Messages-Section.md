---
tags:
  - web-navigation
  - feature-access
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
techniques: []
updated_at: '2025-12-13T23:52:49.890Z'
sub_techniques: []
id: 50141b4a-84f1-45b8-9b96-ab51f0b58b73
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Access Messages Section

## Summary

This procedure locates and enters the Messages feature on the MTN Benin website, where the vulnerable input field resides, preparing for payload injection.

## Description

From the homepage, users manually select the Messages section, typically via a menu or link. This feature processes user input for messaging, but lacks proper sanitization, leading to reflection. The target environment is a standard web application; prerequisites include successful site access. Outcomes include visibility of the input field for exploitation.

## Requirements

1. Successful navigation to the homepage
2. Browser capable of following site links
3. No authentication required for this feature

## Defense

Defensive measures and detection strategies:

- Rate-limit access to sensitive features like Messages
- Monitor for repeated navigation patterns indicative of testing

## Objectives

1. Reach the vulnerable Messages interface
2. Expose the input field for payload testing
3. Confirm feature functionality

## Instructions

### Step 1: Select Messages Feature

**Context**: Identify and click the link or menu item for Messages to load the interface.

No specific command; use browser navigation.

> Locate the 'Messages' option on the site (e.g., in the main menu) and click it. The Messages page should load, showing input fields.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web-navigation]]
- [[feature-access]]
