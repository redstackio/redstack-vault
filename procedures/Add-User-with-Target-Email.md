---
tags:
  - wordpress
  - user-addition
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - WordPress
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: a0a0e7a4-ac0e-4d77-832b-e87f8a6bd7f5
created_at: '2025-12-13T09:01:26.555Z'
updated_at: '2025-12-13T09:01:26.555Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Add User with Target Email

## Summary

This procedure adds a new user to a WordPress site using a specific target email address, facilitating later SSO bypass.

## Description

Adding the user links the email to the site, which can be exploited when a verified WordPress.com account with the same email attempts SSO login.

## Requirements

1. Admin access to WordPress site
2. Target email address
3. Web browser

## Defense

Defensive measures and detection strategies:

- Restrict user addition privileges
- Log and review new user creations

## Objectives

1. Associate target email with WordPress user
2. Prepare for email matching in SSO
3. Ensure user is added successfully

## Instructions

### Step 1: Navigate to Users

**Context**: Access the user management section.

Go to the WordPress admin panel > Users > Add New.

> This opens the add user form.

### Step 2: Enter User Details

**Context**: Input the target email and other details.

Add user with email like something@company.com.

> User is created and listed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[wordpress]]
- [[user-addition]]
