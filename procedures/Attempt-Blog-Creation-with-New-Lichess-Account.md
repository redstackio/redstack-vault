---
tags:
  - account-discovery
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Account Discovery]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: a17ed5d3-1afd-4dab-8451-adf1baf2d00a
created_at: '2025-12-14T17:30:07.262Z'
updated_at: '2025-12-14T17:30:07.262Z'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Attempt-Blog-Creation-with-New-Lichess-Account

## Summary

This procedure tests the blog creation restrictions on a newly created Lichess account to confirm ineligibility, setting the stage for bypass attempts.

## Description

In the Lichess platform, new accounts are restricted from creating blog posts to prevent spam. This step involves registering a fresh account and attempting to submit a blog post, resulting in an error that highlights the access control in place. It requires no special tools and serves as reconnaissance for the vulnerability.

## Requirements

1. Access to lichess.org for account registration
2. Basic web browser
3. No prior account needed beyond the new one

## Defense

Defensive measures and detection strategies:

- Enforce strict account age/activity thresholds before granting blog privileges
- Log all blog creation attempts and flag new accounts
- Implement client-side validation alongside server-side checks

## Objectives

1. Confirm the restriction exists for new accounts
2. Understand the error response for later comparison
3. Prepare for request interception in subsequent steps

## Instructions

### Step 1: Register New Account

**Context**: Create an ineligible account to test restrictions.

Navigate to lichess.org, complete registration with email and password. Log in immediately.

### Step 2: Attempt Blog Creation

**Context**: Submit a blog post to trigger the eligibility check.

Go to the blog creation page (e.g., /blog/new), fill in title and content fields, solve any CAPTCHA if present, and submit the form.

**Expected Output**: Server returns an error message like "Your account is not eligible to create blogs yet. Please play more games or wait."

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-discovery]]
- [[web]]
