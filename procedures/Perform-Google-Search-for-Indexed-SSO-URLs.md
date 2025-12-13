---
tags:
  - google-dorking
  - reconnaissance
  - information-disclosure
type: procedure
tools:
  - '[[tools/Google-Search]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/google-dork-query]]'
platforms:
  - Web
techniques:
  - '[[Search Open Websites-Domains]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 49fdda87-addf-4f38-b952-1b4c2d7fa583
created_at: '2025-12-13T09:01:26.442Z'
updated_at: '2025-12-13T09:01:26.442Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Search Open Websites-Domains]]'
---
# Perform Google Search for Indexed SSO URLs

## Summary

This procedure involves using Google search queries to identify and retrieve indexed internal URLs from an SSO domain that lack proper robots.txt restrictions, exposing sensitive information like login names.

## Description

In this attack scenario, the target is a web-based SSO gateway behind a corporate network. Due to the absence of a robots.txt file, web crawlers like Google can index internal pages. These pages may be reported via browsers or toolbars, leading to public exposure. The procedure uses targeted Google dorks to find URLs like https://████/people/[username], revealing valid employee login names. Expected outcomes include a list of indexed URLs for further analysis.

## Requirements

1. Access to Google Search (public internet)
2. Knowledge of the target domain (e.g., SSO gateway domain)
3. No special tools beyond a web browser or curl for automation

## Defense

Defensive measures and detection strategies:

- Implement a robots.txt file to prevent crawling of sensitive directories
- Monitor for unusual Google search traffic or indexing alerts in web server logs

## Objectives

1. Discover inadvertently indexed internal URLs
2. Retrieve patterns indicating valid login names
3. Enable further reconnaissance or attacks

## Instructions

### Step 1: Construct and Execute Google Dork Query

**Context**: This step performs a site-specific search to find all indexed pages without filters.

**Command** ([[commands/google-dork-query]]):
```bash
echo "site:██████████&filter=0" | xargs -I {} curl -s "https://www.google.com/search?q={}"
```

> This command queries Google for the site and saves the results, revealing URLs like https://████/people/[username].

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Search Open Websites-Domains]]

### Sub-Techniques



## Commands Used

- [[commands/google-dork-query]]

## Tools Used

- [[tools/Google-Search]]

## Tags

- [[google-dorking]]
- [[Reconnaissance]]
