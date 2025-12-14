---
tags:
  - publish
  - rebuild
  - execution
type: procedure
tools:
  - '[[tools/hexo]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/hexo-clean]]'
  - '[[commands/hexo-generate]]'
  - '[[commands/hexo-server-deploy]]'
verified: false
platforms:
  - Node.js
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:09.704Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 21be2086-6afe-42eb-8a0f-a46f3ae1004d
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-and-Publish-Post-to-Trigger-Stored-XSS

## Summary

This procedure saves the injected post, rebuilds the static site, and verifies persistent XSS execution on the published page for victim impact.

## Description

After injection, saving stores the raw payload in Markdown files. Rebuilding generates HTML where the script executes on load, affecting any visitor. This demonstrates the 'stored' nature, as the payload persists across sessions.

## Requirements

1. Injected post ready in editor
2. Hexo CLI access in terminal
3. Browser to view published site

## Defense

Defensive measures and detection strategies:

- Validate and sanitize Markdown before generation
- Implement JS execution blocking via CSP headers
- Monitor generated HTML for suspicious scripts

## Objectives

1. Persist the payload through save and rebuild
2. Confirm execution on the live site
3. Simulate victim impact via repeated loads

## Instructions

### Step 1: Save the Post

**Context**: Commit the changes to store the unsanitized content.

No command; UI action.

> Click 'Save' in the admin editor. The post Markdown file updates with the payload.

### Step 2: Clean and Rebuild Site

**Context**: Clear cache and regenerate static files to apply the post.

**Command** ([[commands/hexo-clean]]):

```bash
hexo clean
```

> Removes public folder and cache.

**Command** ([[commands/hexo-generate]]):

```bash
hexo generate
```

> Builds static HTML from source.

### Step 3: Restart Server and View

**Context**: Serve the updated site and test execution.

**Command** ([[commands/hexo-server-deploy]]):

```bash
hexo server -d
```

> Restarts server. Navigate to the post URL (e.g., /test-xss-here/) and observe alert on load.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/hexo-clean]]
- [[commands/hexo-generate]]
- [[commands/hexo-server-deploy]]

## Tools Used

- [[tools/hexo]]

## Tags

- static-generation
- persistence
