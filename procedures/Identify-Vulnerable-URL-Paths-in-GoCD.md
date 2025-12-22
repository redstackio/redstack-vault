---
tags:
  - path-traversal
  - web
  - recon
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: e16572e7-671e-446f-8059-f6031f355f41
created_at: '2025-12-14T03:16:30.881Z'
updated_at: '2025-12-14T03:16:30.881Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable URL Paths in GoCD

## Summary

This procedure tests for path traversal vulnerabilities in the URL routing of GoCD's public websites (www.go.cd and docs.go.cd), hosted on GitHub Pages, by crafting malformed URLs that bypass validation and access unintended directories.

## Description

GoCD's sites lack proper sanitization for path traversal sequences like ..%2F in URL paths, allowing attackers to probe for and access unexpected resources without errors or redirects. This is particularly risky on static GitHub Pages hosting, where routing is handled client-side or via limited server configs. The procedure involves manual URL testing to identify acceptance of traversal payloads, setting the stage for further exploitation like XSS. Expected outcomes include successful loading of traversed paths, confirming the vulnerability for potential script injection.

## Requirements

1. Web browser with developer tools (e.g., Chrome DevTools for inspecting responses)
2. Public access to GoCD domains (www.go.cd, docs.go.cd)
3. Basic knowledge of URL encoding (%2F for /)

## Defense

Defensive measures and detection strategies:

- Implement strict URL path normalization and validation on the server or via GitHub Pages redirects.
- Use Content Security Policy (CSP) headers to block inline or unexpected script loading.
- Monitor access logs for anomalous path traversal patterns (e.g., sequences of ..%2F).

## Objectives

1. Confirm acceptance of path traversal in URL routing.
2. Identify accessible unintended directories.
3. Validate lack of redirects or error handling for malformed paths.

## Instructions

### Step 1: Craft and Test Base Traversal URL

**Context**: Start with a known directory like /user/upoad/ (noting the typo in the original path, likely /upload/) and append traversal to escape it.

Navigate to the following URL in a web browser:

```plaintext
https://www.go.cd/user/upoad/..%2F..%2F
```

> The server processes this without 404 or redirect, indicating vulnerable routing. Check the page source and network tab for any loaded resources from root or parent directories.

### Step 2: Test on Secondary Domain

**Context**: Repeat on the documentation site to confirm consistency across GoCD properties.

Navigate to:

```plaintext
https://docs.go.cd/current/user/upoad/..%2F..%2F
```

> Observe similar behavior: path accepted as valid, potentially exposing docs or other static assets. Use browser console to log any errors or unexpected loads.

### Step 3: Validate No Sanitization

**Context**: Escalate by trying deeper traversals or combined payloads to ensure no partial blocks.

Test variations like:

```plaintext
https://www.go.cd/user/upoad/..%2F..%2F..%2Fetc/passwd
```

> Expected: No block; if a file like passwd exists, it may serve content. Success is confirmed by lack of rejection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- path-traversal
- web-exploit
- github-pages
