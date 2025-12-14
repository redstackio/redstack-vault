---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
name: Save-Post-Rebuild-Site-and-Verify-Persistent-XSS
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:37.034Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - persistence
  - site-rebuild
  - xss-verification
commands:
  - '[[commands/hexo-clean]]'
  - '[[commands/hexo-generate]]'
  - '[[commands/hexo-server-deploy]]'
platforms:
  - Web
  - Node.js
tools:
  - '[[tools/HexoJS]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Save-Post-Rebuild-Site-and-Verify-Persistent-XSS

## Summary

This procedure saves the XSS-injected post, cleans and regenerates the static site, restarts the server, and verifies that the payload executes persistently when viewing the published post.

## Description

Saving stores the unsanitized content in Hexo's source files. Rebuilding with hexo clean and generate processes the post into static HTML without escaping the script, embedding it in the output. Restarting serves the updated site, where any viewer triggers the XSS, enabling attacks like session theft on admins or visitors.

## Requirements

1. Injected post ready in editor
2. Hexo CLI access in project directory
3. Browser for verification

## Defense

Defensive measures and detection strategies:

- Output encode all post content during generation with Hexo filters
- Deploy site with CSP headers to prevent XSS execution
- Audit generated HTML for unescaped scripts post-build

## Objectives

1. Persist the malicious payload in site source
2. Confirm execution in rebuilt static pages
3. Validate impact on unauthenticated viewers

## Instructions

### Step 1: Save the Post

**Context**: Commit the injected content to Hexo's data store.

No command; UI action:

Click 'Save' or 'Publish' in the editor.

> Post saved to source/_posts/ with raw payload.

### Step 2: Clean and Generate Site

**Context**: Remove old builds and regenerate static files to include the new post.

**Command** ([[commands/hexo-clean]]):

```bash
hexo clean
```

> Clears public/ and cache; expected: Database has been cleaned.

**Command** ([[commands/hexo-generate]]):

```bash
hexo generate
```

> Builds HTML in public/; expected: INFO 1 posts generated.

### Step 3: Restart Server and Verify

**Context**: Serve the updated site and test XSS on post view.

**Command** ([[commands/hexo-server-deploy]]):

```bash
hexo server -d
```

> Restarts server; then visit http://localhost:4000/[post-slug]/ to see alert.

> Expected: Alert 'XSS' pops on page load.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/hexo-clean]]
- [[commands/hexo-generate]]
- [[commands/hexo-server-deploy]]

## Tools Used

- [[tools/HexoJS]]

## Tags

- persistence
- site-rebuild
- xss-verification
