---
tags:
  - web-access
  - judge-me
type: procedure
tools: []
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
id: 4e0542a4-40db-4567-a152-123c55df68eb
created_at: '2025-12-14T17:24:19.336Z'
updated_at: '2025-12-14T17:24:19.336Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Judge.me-People-Page

## Summary

This procedure involves navigating to the Judge.me people page to access user profiles and the follow/like functionality, serving as the initial entry point for exploiting the race condition vulnerability.

## Description

The Judge.me platform hosts a people page at https://judge.me/people where users can view profiles and perform follow or like actions. This step sets up the attack by loading the page in a browser, identifying a target user, and preparing for subsequent interception. No authentication is strictly required for public access, but a logged-in session enhances realism. The expected outcome is visibility of the vulnerable follow buttons, enabling the next steps in the chain.

## Requirements

1. Web browser (e.g., Chrome, Firefox)
2. Internet access to https://judge.me
3. Optional: Judge.me user account for authenticated follows

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on page loads to detect automated access
- Monitor for unusual traffic patterns to the people page

## Objectives

1. Gain access to the vulnerable follow functionality
2. Identify target user profiles
3. Prepare for request interception

## Instructions

### Step 1: Navigate to People Page

**Context**: Load the target page to expose the follow/like interface.

No command required; use browser navigation.

> Open your web browser and enter the URL https://judge.me/people. Browse to a specific user profile if needed.

**Expected Output**: The page renders with user profiles and follow buttons.

### Step 2: Locate Target User

**Context**: Select a user to target for the follow action.

No command required.

> Scroll or search for a user profile on the page.

**Expected Output**: Target user's profile is visible with a follow/like button.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web-access]]
- [[judge-me]]
