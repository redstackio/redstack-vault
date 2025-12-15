---
id: proc-uuid-001
name: Discover-Leaked-AWS-Credentials-in-GitHub-Repository
tags:
  - reconnaissance
  - github
  - credential-leak
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:32:29.064Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Discover-Leaked-AWS-Credentials-in-GitHub-Repository

## Summary

This procedure outlines how to identify and access a public GitHub repository that inadvertently exposes sensitive AWS credentials, serving as the initial reconnaissance step in credential theft attacks.

## Description

In this scenario, attackers scan public GitHub repositories for misconfigurations where developers commit AWS Access Keys and Secret Keys in plain text. The target environment is GitHub's public repository hosting, with no authentication required. Expected outcomes include gaining the repository URL and confirming public access, setting the stage for credential extraction. Prerequisites include internet access and basic knowledge of GitHub navigation.

## Requirements

1. Web browser with internet connectivity
2. Knowledge of target organization or keywords for GitHub search (e.g., 'AWS_ACCESS_KEY')
3. No special permissions needed

## Defense

Defensive measures and detection strategies:

- Use GitHub's secret scanning feature to detect and alert on committed credentials
- Implement pre-commit hooks to scan for sensitive data before pushing to repositories
- Regularly audit public repositories and rotate credentials upon exposure

## Objectives

1. Locate the public repository containing leaked credentials
2. Verify public accessibility
3. Prepare for credential extraction

## Instructions

### Step 1: Search for Target Repository

**Context**: Use GitHub's search functionality to find repositories with potential leaks based on organization or keywords.

No specific command required; use browser to navigate to github.com and enter search terms like 'org:target AWS key'.

> This step accomplishes identifying candidate repositories. Expected output: List of matching public repos.

### Step 2: Access Repository URL

**Context**: Directly navigate to the specific repository URL to confirm access.

Open the URL (e.g., https://github.com/target/repo) in a browser.

> Verifies the repo is public. Expected output: Repository page loads without login prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[github]]
- [[credential-leak]]
