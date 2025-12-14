---
id: proc-uuid-004
name: Create-Malicious-Repository-and-Issue-on-GitHub
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:21.068Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - payload-creation
  - github
  - issue-injection
platforms:
  - Web
tools:
  - '[[tools/GitHub]]'
skill_level: intermediate
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Create-Malicious-Repository-and-Issue-on-GitHub

## Summary

This procedure creates a GitHub repository and issue containing a full XSS payload in the title and description, allowing controlled reproduction once indexed by Algolia for extension rendering.

## Description

User-controlled fields like issue titles are indexed by Algolia and fetched by the extension without sanitization. The payload `"><script>alert("XSS on " + document.domain + ". Cookies: " + document.cookie)</script><h1>A</h1>` breaks out of HTML context to execute JavaScript, targeting authenticated users for data theft.

## Requirements

1. Authenticated GitHub account with repository creation permissions
2. Understanding of XSS payload crafting
3. Patience for Algolia indexing (2-5 minutes)

## Defense

Defensive measures and detection strategies:

- Sanitize repository and issue metadata on GitHub backend before indexing
- Rate-limit or validate special characters in titles/descriptions
- Monitor for suspicious alert() calls in browser consoles

## Objectives

1. Establish a controllable injection point via GitHub content
2. Embed JavaScript for domain and cookie exfiltration
3. Ensure payload is searchable post-indexing

## Instructions

### Step 1: Create Repository

**Context**: Set up a new repo to host the malicious issue.

Log in to GitHub, click "New repository", name it (e.g., test-xss-repo), and create it.

> Repository URL will be github.com/username/test-xss-repo.

### Step 2: Add Malicious Issue

**Context**: Insert the XSS payload into issue fields for indexing.

In the repo, click "New issue", set title and description to: `"><script>alert("XSS on " + document.domain + ". Cookies: " + document.cookie)</script><h1>A</h1>`.

```html
"><script>alert("XSS on " + document.domain + ". Cookies: " + document.cookie)</script><h1>A</h1>
```

> Submit the issue and wait for indexing; search for the repo name to confirm visibility.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/GitHub]]

## Tags

- [[payload-creation]]
- [[tools/GitHub]]
