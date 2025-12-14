---
id: proc-discover-twitter-creds-github
tags:
  - credential-leak
  - github
  - twitter
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - GitHub
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:32:01.860Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Discover Leaked Twitter API Credentials in GitHub

## Summary

This procedure involves manually browsing a public GitHub repository to identify exposed Twitter API credentials, such as consumer keys, secrets, access tokens, and callback URLs, which can be used to impersonate the repository owner on the Twitter platform.

## Description

In scenarios where developers commit sensitive configuration data to public repositories without proper redaction or .gitignore exclusion, attackers can passively discover API credentials. This procedure targets repositories like Liberapay's, where Twitter-related variables are stored in cleartext. The discovered credentials allow unauthorized API calls, including posting tweets, accessing user data, or manipulating account settings. Prerequisites include basic web browsing skills and knowledge of common credential naming conventions (e.g., TWITTER_CONSUMER_KEY).

## Requirements

1. Access to a web browser with internet connectivity.
2. Knowledge of the target GitHub repository URL.
3. No special permissions needed, as the repository is public.

## Defense

Defensive measures and detection strategies:

- Implement .gitignore rules to exclude sensitive files and use git-secrets or pre-commit hooks to scan commits.
- Regularly audit public repositories with tools like GitHub's secret scanning or TruffleHog.
- Rotate credentials immediately upon leak detection and monitor API usage for anomalies.

## Objectives

1. Locate and extract Twitter API credentials from repository files.
2. Assess potential for service impersonation.
3. Identify any internal details like callback URLs.

## Instructions

### Step 1: Access the Target Repository

**Context**: Begin by navigating to the public GitHub repository to start reconnaissance.

Open a web browser and visit the Liberapay GitHub repository at https://github.com/liberapay/liberapay.com. Use the search function within the repository to look for files containing "twitter" keywords.

### Step 2: Inspect Configuration Files

**Context**: Manually review files for unredacted credentials.

Browse through configuration directories, focusing on files like app-conf-defaults.sql or environment configs. Look for variables such as TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET, and TWITTER_CALLBACK.

**Expected Output**: Credentials in plain text, e.g., TWITTER_CALLBACK pointing to localhost:8537, indicating an internal service.

### Step 3: Document and Validate

**Context**: Record findings and test if credentials are active (optional, for verification).

Copy the credentials and, if safe, test them against the Twitter API developer console to confirm validity without exploitation.

**Expected Output**: Confirmation of credential functionality.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Hardware]] Gather Victim Identity Information: Credentials

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[credential-leak]]
- [[github]]
- [[twitter]]
