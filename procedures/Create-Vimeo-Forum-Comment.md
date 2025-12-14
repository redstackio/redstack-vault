---
tags:
  - forum
  - comment-creation
  - vimeo
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
updated_at: '2025-12-14T17:25:23.419Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 5ad07a54-a84e-49e9-95cb-69d477a0c78a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Vimeo-Forum-Comment

## Summary

This procedure involves posting a comment in a Vimeo forum topic using an authenticated account, which generates a unique comment_id necessary for subsequent IDOR exploitation.

## Description

In the context of exploiting Vimeo's IDOR in forum comments, creating your own comment allows observation of the application's request patterns and ID assignment. This step requires a valid Vimeo login and access to a forum topic. The outcome is a posted comment that serves as a reference for manipulating IDs later. No tools are strictly needed beyond a browser, but network inspection is recommended.

## Requirements

1. Authenticated Vimeo account with forum posting permissions
2. Access to a specific forum topic, e.g., /forums/wanted_and_offered/topic:130606
3. Web browser for UI interaction

## Defense

Defensive measures and detection strategies:

- Rate limiting on comment postings to prevent abuse
- Logging of comment creation events tied to user sessions

## Objectives

1. Generate a legitimate comment_id for analysis
2. Establish baseline request flow for editing
3. Prepare for ID manipulation in IDOR chain

## Instructions

### Step 1: Navigate to Forum Topic

**Context**: Access the target forum to prepare for posting.

Log in to Vimeo and navigate to the forum topic.

### Step 2: Post the Comment

**Context**: Submit a simple comment to trigger ID generation.

Enter comment text in the UI and submit. Monitor network tab for the POST request creating the comment.

**Expected Output**: Comment appears in the topic; note the comment_id from subsequent requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- forum
- comment-creation
