---
id: proc-gitlab-enumerate-milestones-api-001
tags:
  - gitlab
  - api-bypass
  - information-disclosure
  - access-control
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-gitlab-search-milestones]]'
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:32:29.120Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Gather Victim Host Information]]'
---
# Enumerate-Milestones-via-GitLab-Search-API

## Summary

This procedure exploits an improper access control vulnerability in GitLab's search API to allow non-project members to enumerate milestones in restricted public projects, leaking potentially sensitive project information.

## Description

The GitLab search API at /api/v4/projects/<project-id>/search does not enforce the same restrictions as the UI for milestones when the project is public but features are limited to members. Using a non-member's API token, an attacker can query for milestones by name, retrieving details like titles, descriptions, and dates. This targets GitLab instances vulnerable to CVE-like issues (e.g., HackerOne #460815), with outcomes including full milestone disclosure. Prerequisites: Project ID and a valid non-member token.

## Requirements

1. GitLab API access with a PRIVATE-TOKEN from a non-project member
2. Known project ID from setup
3. curl or similar HTTP client
4. Network access to GitLab API endpoint

## Defense

Defensive measures and detection strategies:

- Patch GitLab to enforce uniform access controls on API and UI
- Log and alert on search API queries for restricted scopes
- Use web application firewalls (WAF) to block unauthorized API patterns
- Regularly audit project visibility settings

## Objectives

1. Bypass member-only restrictions to access milestone data
2. Enumerate all milestones matching search terms
3. Expose sensitive timeline information for reconnaissance

## Instructions

### Step 1: Prepare API Token

**Context**: Obtain or generate a personal access token for a user without project membership.

Create token via GitLab user settings > Access Tokens, with api scope.

### Step 2: Execute Search Query

**Context**: Use curl to send a GET request to the search endpoint, targeting milestones.

Execute [[commands/curl-gitlab-search-milestones]] to query for the milestone:

```bash
curl --request GET --header "PRIVATE-TOKEN: <YOUR-TOKEN>" https://gitlab.example.com/api/v4/projects/<project-id>/search?search=milestone&scope=milestones
```

> This command authenticates with the token and searches for 'milestone' in the milestones scope. Despite restrictions, it returns the data if vulnerable.

**Expected Output**: JSON response with milestone array, e.g., [{"id":123,"iid":1,"title":"milestone","description":"milestone","state":"active","due_date":null,...}].

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Gather Victim Host Information]] Gather Victim Organization Information

### Sub-Techniques


## Commands Used

- [[commands/curl-gitlab-search-milestones]]

## Tools Used

- [[tools/curl]]

## Tags

- gitlab
- api
- enumeration
