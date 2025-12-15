---
id: proc-uuid-001
tags:
  - setup
  - flintcms
  - password-reset
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:06.406Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-FlintCMS-and-Initiate-Reset

## Summary

This procedure sets up a local FlintCMS instance, creates an initial admin user, and initiates the password reset process to prepare for blind injection exploitation.

## Description

FlintCMS is a Node.js-based CMS using Mongoose for MongoDB interactions. The setup involves installing via npm, configuring on localhost:4000, creating an admin via the install route, logging out, and triggering a reset via the forgotpassword endpoint. This generates a backend token vulnerable to injection, allowing subsequent blind extraction. Prerequisites include Node.js and MongoDB installed locally.

## Requirements

1. Node.js and npm installed
2. MongoDB service running
3. Local network access to port 4000

## Defense

Defensive measures and detection strategies:

- Use input validation and sanitization for query parameters in Mongoose queries
- Implement rate limiting on password reset endpoints
- Monitor for unusual request patterns to /admin/verify

## Objectives

1. Establish a testable FlintCMS environment
2. Generate a password reset token for the target account
3. Position for injection-based token extraction

## Instructions

### Step 1: Install FlintCMS

**Context**: Download and set up FlintCMS on localhost.

Follow the guide at https://flintcms.co/docs/installation/ to clone the repo, run `npm install`, and start with `npm start` on port 4000.

### Step 2: Create Admin User

**Context**: Register the initial admin account.

Access http://localhost:4000/admin/install and provide email (e.g., admin@localhost.com) and password to create the account.

### Step 3: Initiate Password Reset

**Context**: Trigger token generation.

Log out from /admin/login, then POST to /admin/forgotpassword with {email: "admin@localhost.com"} using a tool like curl or browser form.

**Expected Output**: No error response; token stored in MongoDB for the user.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[flintcms]]
