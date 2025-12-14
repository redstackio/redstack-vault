---
id: proc-udemy-plugin-readme-001
tags:
  - information-disclosure
  - wordpress
  - plugin-exposure
  - all-in-one-seo
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-access-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T17:24:56.073Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Access-WordPress-Plugin-Readme

## Summary

This procedure accesses an exposed readme.txt file in a WordPress plugin directory to disclose the plugin's version details, such as for the All-in-One SEO Pack, enabling targeted vulnerability research.

## Description

WordPress plugins often include readme.txt files in their directories for documentation, which can be left publicly accessible due to default configurations or oversight. Accessing these files reveals version numbers, stable tags, and changelogs, which attackers use to identify outdated or vulnerable plugin versions. In the Udemy incident, this exposed the All-in-One SEO Pack plugin version on the about subdomain.

## Requirements

1. Network access to the target plugin directory URL
2. Identification of the plugin path (e.g., /wp-content/plugins/all-in-one-seo-pack/)
3. Tool for HTTP GET requests, like curl or a browser

## Defense

Defensive measures and detection strategies:

- Implement directory listing restrictions and file access controls in web server config (e.g., Apache/Nginx deny rules for /wp-content/plugins/*/readme.txt)
- Regularly audit and update plugins to latest versions
- Log and alert on requests to plugin directories from unusual IPs

## Objectives

1. Extract plugin version for exploit compatibility checks
2. Verify misconfiguration in plugin file permissions
3. Support reconnaissance for plugin-specific attacks

## Instructions

### Step 1: Retrieve Plugin Readme Content

**Context**: Fetch the readme.txt from the plugin's directory to obtain version metadata.

**Command** ([[commands/curl-access-url]]):
```bash
curl http://about.udemy.com/wp-content/plugins/all-in-one-seo-pack/readme.txt
```

> The command retrieves the plain text file. Scan for sections like "Stable tag:" or "Version:" to find details, e.g., "Stable tag: 2.6.15".

### Step 2: Analyze Output

**Context**: Review the text for actionable intelligence on the plugin.

No command required; grep or manually inspect for keywords like "version" or "changelog".

> Output includes plugin name, version, and requires, confirming exposure as in the HackerOne report.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Software]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-url]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[wordpress]]
- [[Reconnaissance]]
