---
id: proc-uuid-5678
tags:
  - oauth
  - token-leak
  - information-disclosure
  - rocketchat
  - hubot
  - logs
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Linux
  - Docker
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:24:55.809Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
  - '[[Credentials In Files]]'
---
# Inspect-Hubot-Logs-for-OAuth-Tokens

## Summary

This procedure involves reviewing Hubot log files in a Rocket.Chat deployment to identify and extract unintentionally logged OAuth tokens in plaintext, which can lead to unauthorized access to OAuth-integrated services.

## Description

In Rocket.Chat versions like 4.1.0 with Hubot integration, OAuth tokens may be logged without obfuscation during authentication flows, exposing them in server log files. This information disclosure vulnerability allows anyone with log access—such as administrators or compromised insiders—to obtain tokens granting full control over scoped services (e.g., GitHub, Google). The procedure targets the Hubot log files on a Linux/Docker environment running NodeJS and MongoDB, requiring server-level access. Expected outcomes include token extraction and validation of their validity via API calls to the issuing service.

## Requirements

1. Server access to the Rocket.Chat instance (root or sudo privileges on Linux/Docker host)
2. Knowledge of log file locations (typically /opt/rocketchat/logs or Docker volume mounts)
3. Basic familiarity with log formats and OAuth token structures

## Defense

Defensive measures and detection strategies:

- Implement log redaction policies to substitute sensitive data like OAuth tokens with placeholders (e.g., using log filters in NodeJS)
- Enable log access controls and monitoring for unauthorized file reads (e.g., via auditd on Linux)
- Regularly audit logs for sensitive data exposure using automated scanners

## Objectives

1. Discover plaintext OAuth tokens in Hubot logs
2. Assess the scope and validity of exposed tokens
3. Evaluate potential impact on connected services

## Instructions

### Step 1: Locate and Access Hubot Log Files

**Context**: Identify the directory containing Hubot logs, which store authentication events including OAuth flows.

Navigate to the log directory on the server or Docker container:

```bash
cd /path/to/hubot/logs  # Adjust path based on installation, e.g., /opt/rocketchat/apps/meteor/app/hubot/logs
ls -la hubot.log*
```

> This lists log files; focus on recent ones where OAuth events occurred.

### Step 2: Search for OAuth Tokens

**Context**: Scan logs for entries containing OAuth data, looking for unredacted tokens.

Use grep to filter for relevant patterns:

```bash
grep -i "oauth\|token\|access_token" hubot.log | head -20
```

> Output shows lines with tokens like "access_token: <plaintext_token>"; tokens are typically JWTs or opaque strings 100+ characters long. No redaction (e.g., [REDACTED]) indicates vulnerability.

### Step 3: Extract and Validate Tokens

**Context**: Copy extracted tokens and test their usability to confirm exposure.

Manually extract the token string from the log line. To validate, use curl to query the OAuth provider's introspection endpoint (if available) or attempt an API call:

```bash
curl -H "Authorization: Bearer <extracted_token>" https://api.service.com/user
```

> Successful response (e.g., 200 OK with user data) confirms the token is active and grants access.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials
- [[Credentials In Files]] Credentials In Files

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- oauth
- token-leak
- information-disclosure
- rocketchat
- hubot
- logs
