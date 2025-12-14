---
id: proc-001
name: Access-Exposed-Readme-Files-for-Version-Reconnaissance
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:26.660Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Hardware]]'
sub_techniques: []
tags:
  - information-disclosure
  - reconnaissance
  - wordpress
commands:
  - '[[commands/curl-access-readme]]'
platforms:
  - Web
tools:
  - '[[tools/curl]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---

# Access-Exposed-Readme-Files-for-Version-Reconnaissance

## Summary

This procedure involves directly accessing publicly exposed readme files on a WordPress blog to disclose software version numbers and plugin details, aiding in reconnaissance for further targeted attacks.

## Description

In scenarios where WordPress installations leave readme files accessible without authentication, attackers can enumerate version information from files like readme.html. This exposure allows identification of outdated components vulnerable to known exploits. The target environment is a public web blog, with no prerequisites beyond internet access. Expected outcomes include version details that facilitate vulnerability research, such as confirming outdated plugins.

## Requirements

1. Internet connectivity to reach the target URL (e.g., www.drchrono.com/blog)
2. Basic knowledge of HTTP requests
3. No authentication or special permissions needed

## Defense

Defensive measures and detection strategies:

- Restrict access to /readme.html and plugin directories via .htaccess or server configuration
- Regularly update WordPress and plugins to patch exposures
- Monitor access logs for unusual GET requests to sensitive files

## Objectives

1. Gather software version details for reconnaissance
2. Identify potential vulnerabilities based on versions
3. Enable chaining to exploitation steps

## Instructions

### Step 1: Fetch Blog Readme File

**Context**: Retrieve the main readme file to extract version and configuration details.

**Command** ([[commands/curl-access-readme]]):
```bash
curl https://www.drchrono.com/blog/readme.html
```

> This command performs a simple HTTP GET to download the file content. Expected output includes HTML or text with version strings like WordPress core or theme versions. Save to a file with `-o readme.html` for analysis.

### Step 2: Analyze Output for Sensitive Data

**Context**: Review the fetched content for exploitable information.

No command needed; manually inspect for keywords like "Version:" or plugin names.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Software

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-access-readme]]

## Tools Used

- [[tools/curl]]

## Tags

- [[information-disclosure]]
- [[Reconnaissance]]
- [[wordpress]]
