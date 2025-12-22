---
id: proc-uuid-1
name: Identify-IDOR-in-Social-Club-Comment-Functionality
tags:
  - idor
  - discovery
  - web-testing
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:33.789Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-IDOR-in-Social-Club-Comment-Functionality

## Summary

This procedure outlines the discovery of an Insecure Direct Object Reference (IDOR) in the Rockstar Games Social Club Newswire comment section, where user IDs in comment endpoints lack proper authorization checks, allowing testers to access or manipulate comments belonging to other users.

## Description

In the context of web application security testing, IDOR vulnerabilities occur when an application exposes internal object references (like user IDs) in URLs or requests without verifying the user's permission to access them. Here, the Social Club platform's comment functionality under Newswire articles uses direct user ID references in API calls for creating, viewing, or deleting comments. By intercepting and modifying these requests, an attacker can reference any user's ID, leading to unauthorized actions. This procedure assumes access to a logged-in account and focuses on manual testing via browser tools to identify the flaw.

## Requirements

1. Active Social Club account with login credentials
2. Web browser with developer console (e.g., Chrome)
3. Knowledge of target user IDs (from public profiles or enumeration)
4. Network access to socialclub.rockstargames.com

## Defense

Defensive measures and detection strategies:

- Implement server-side authorization checks to validate user ownership of referenced objects
- Use indirect references (e.g., hashed IDs) instead of direct user IDs in APIs
- Monitor for anomalous comment activity, such as rapid insertions/deletions from mismatched IP/user agents
- Enable CSRF tokens on all state-changing endpoints to prevent forged requests

## Objectives

1. Confirm IDOR by successfully accessing another user's comments via ID manipulation
2. Document the vulnerable endpoints for reporting
3. Identify related issues like missing CSRF protections

## Instructions

### Step 1: Access Comment Section and Post Test Comment

**Context**: Establish a baseline by interacting with the legitimate comment functionality to capture the normal request structure.

Log in to Social Club, navigate to a Newswire article, and post a test comment. Open developer tools (F12), go to the Network tab, and filter for comment-related requests (e.g., POST /api/comments).

**Expected Output**: Request payload visible, including your user ID (e.g., {"user_id": "your_id", "content": "test"}).

### Step 2: Modify User ID and Replay Request

**Context**: Test for IDOR by altering the user ID to a known victim's ID and observing if the action succeeds without re-authentication.

Copy the request, change the user_id field to a target user's ID (e.g., from URL parameters in their profile), and resubmit using the console or a tool like Postman. Check if the comment appears under the target's account on the page refresh.

**Expected Output**: No authorization error; comment associated with the modified user ID.

### Step 3: Test for Information Disclosure

**Context**: Extend the test to retrieve sensitive data tied to comments.

Use a GET request to the comment endpoint with the victim's user_id (e.g., GET /api/comments?user_id=victim_id) and inspect the response for leaked details like private comment histories.

**Expected Output**: Unauthorized access to victim's comment data, including metadata.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- idor
- web-vulnerability
- discovery
