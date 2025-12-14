---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - dns
  - github-pages
  - dangling-records
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:51:26.477Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify-Dangling-GitHub-Pages-DNS

## Summary

This procedure verifies if a target domain has dangling DNS records pointing to unclaimed GitHub Pages, indicating vulnerability to takeover by observing default repository pages.

## Description

Post-acquisition, domains like obviousengine.com may point via CNAME to GitHub Pages (e.g., username.github.io) without an active repository, resulting in a default 404 or unclaimed page. This step uses simple HTTP access to detect such misconfigurations, requiring only a browser. Successful identification confirms the domain is hijackable without altering DNS.

## Requirements

1. Web browser for domain access
2. List of candidate domains from prior research
3. Basic understanding of DNS resolution

## Defense

Defensive measures and detection strategies:

- Implement DNS monitoring tools to detect unresolved or default service responses
- Remove or redirect CNAME records for unused services after acquisitions
- Scan for subdomain takeovers using tools like Subjack

## Objectives

1. Confirm DNS points to unclaimed GitHub infrastructure
2. Validate absence of active content
3. Assess takeover feasibility

## Instructions

### Step 1: Access the Domain

**Context**: Resolve and observe the domain's current state.

Open a web browser and navigate to the target domain, e.g., http://obviousengine.com.

### Step 2: Analyze Response

**Context**: Look for GitHub Pages indicators.

Check if the page shows a GitHub 404 error, "Repository not found," or default unclaimed site template, confirming dangling DNS.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[DNS]]
- [[github-pages]]
- [[dangling-records]]
