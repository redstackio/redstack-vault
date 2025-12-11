---
tags:
  - token-leak
  - reconnaissance
  - information-disclosure
type: procedure
tools:
  - '[[tools/Travis-CI]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-travis-logs]]'
  - '[[commands/github-api-token-verify]]'
platforms:
  - Web
  - CI/CD
techniques:
  - '[[Search Open Technical Databases]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 05c5a9b2-f47a-4bea-b395-eeaedd7dd3ca
created_at: '2025-12-11T06:10:15.519Z'
updated_at: '2025-12-11T06:10:15.519Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0043]]'
mitre_techniques:
  - '[[T1596]]'
---
# Identify Leaked Tokens in CI Build Logs

## Summary

This procedure involves scanning public continuous integration (CI) build logs, such as those from Travis CI, to identify accidentally exposed sensitive information like API tokens or credentials.

## Description

In this attack scenario, public build logs from Travis CI are analyzed for Grammarly-related repositories, revealing a leaked GitHub token due to improper logging in build scripts. The procedure targets web-based CI/CD environments where logs are publicly accessible, enabling reconnaissance without authentication.

## Requirements
1. Internet access to Travis CI API or web interface
2. Basic scripting tools like curl and jq for log retrieval
3. Knowledge of target repositories (e.g., via GitHub search)

## Defense

- Configure CI pipelines to mask sensitive variables in logs
- Regularly audit and rotate API tokens
- Monitor for anomalous access to public logs using web application firewalls

## Objectives
1. Discover exposed tokens in build outputs
2. Document the leak for further verification
3. Assess potential impact on repository access

## Instructions

### Step 1: Fetch Public Build Logs

**Context**: Retrieve build logs from Travis CI for the target repository.

**Command** ([[commands/curl-travis-logs]]):
```bash
curl -s https://api.travis-ci.org/repos/grammarly/repo/builds | jq
```

> This command fetches build metadata; follow up by accessing specific log URLs to search for tokens.

### Step 2: Analyze Logs for Leaks

**Context**: Manually or script searches for token patterns in the retrieved logs.

Search the output for strings matching GitHub token formats (e.g., ghp_ or similar prefixes).

## MITRE ATT&CK Mapping

### Tactics
- [[Reconnaissance]]

### Techniques
- [[Search Open Technical Databases]]

### Sub-Techniques

## Commands Used
- [[commands/curl-travis-logs]]

## Tools Used
- [[tools/Travis-CI]]

## Tags
- token-leak
- reconnaissance
