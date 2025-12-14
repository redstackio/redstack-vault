---
tags:
  - weblate
  - translation
type: procedure
tools: []
tactics: []
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-04T00:00:00Z'
techniques: []
updated_at: '2025-12-14T03:15:47.094Z'
sub_techniques: []
id: 19505eeb-cf9c-4daa-a227-3f369494cc8e
validated: true
---
# Navigate to Weblate Translation Page

## Summary

This procedure involves accessing a translation project page in Weblate to expose source string locations that will reference the injected Editor Link payload.

## Description

After payload injection, the user must interact with translation components where source file links are generated using the stored Editor Link. This step targets specific translation views, such as language-specific projects, to load the interface containing clickable source locations. It assumes an authenticated session and prepares for the final trigger.

## Requirements

1. Saved payload in preferences
2. Access to a translation project (e.g., 'hello' project in demo instance)
3. Web browser session

## Defense

Defensive measures and detection strategies:

- Restrict translation page access to verified users
- Audit navigation patterns for suspicious sequences post-preferences changes

## Objectives

1. Load a page with source string interactions
2. Display clickable file locations
3. Position for payload retrieval

## Instructions

### Step 1: Select Translation Project

**Context**: Choose a project containing translatable strings with source locations.

Navigate to a URL like `https://demo.weblate.org/translate/hello/master/zh_CN/?checksum=6412684aaf018e8e`.

> This loads the translation editor for the specified project and language, showing strings and their source files.

### Step 2: Verify Interface

**Context**: Ensure source string locations are visible and clickable.

Inspect the page for elements like file names (e.g., 'main.c') next to strings.

> Presence of these links confirms the setup for triggering the stored payload.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- weblate
- translation
- navigation
