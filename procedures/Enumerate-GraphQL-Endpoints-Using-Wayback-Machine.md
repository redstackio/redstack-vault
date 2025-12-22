---
id: proc-885539-enumerate-endpoints
tags:
  - graphql
  - enumeration
  - reconnaissance
type: procedure
tools:
  - '[[tools/Wayback-Machine]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T17:26:00.376Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Enumerate GraphQL Endpoints Using Wayback Machine

## Summary

This procedure involves using the Wayback Machine to archive and analyze Twitter's client JavaScript files, extracting over 700 GraphQL endpoint names and their associated queryIds for further testing.

## Description

In the context of discovering API vulnerabilities, this reconnaissance step targets JavaScript bundles from Twitter's web (main.[Hex].js), Android (l63.java), and TweetDeck (bundle.[Hex].js) clients. By retrieving historical versions via the Wayback Machine, attackers can parse these files to identify persisted GraphQL queries without direct access to current production code. This enables mapping of internal API surfaces, leading to the identification of the vulnerable ListMembers query (queryId: iUmNRKLdkKVH4WyBNw9x2A). Prerequisites include basic scripting knowledge for parsing JS files and access to archived content.

## Requirements

1. Access to https://web.archive.org for retrieving snapshots.
2. Tools for parsing JavaScript (e.g., grep or custom scripts).
3. Knowledge of GraphQL query structures in client code.

## Defense

Defensive measures and detection strategies:

- Obfuscate or minify production JavaScript to hinder endpoint extraction.
- Monitor for unusual traffic to archived client files or Wayback Machine queries.
- Implement client-side query validation to prevent reverse-engineering.

## Objectives

1. Collect a comprehensive list of GraphQL endpoints and queryIds.
2. Identify potential entry points for API abuse.
3. Enable targeted testing of persisted queries.

## Instructions

### Step 1: Retrieve Archived JavaScript Files

**Context**: Search for historical versions of Twitter's client JS files to capture endpoint definitions.

Navigate to https://web.archive.org and search for URLs like https://twitter.com/i/web/main.[Hex].js or similar for mobile/TweetDeck.

**Expected Output**: Downloaded JS files containing GraphQL query strings and IDs.

### Step 2: Parse Files for Endpoints

**Context**: Extract pairs of endpoint names (e.g., ListMembers) and random queryIds from the JS code.

Use text search tools to find patterns like 'queryId: "[random-string]"' associated with query names.

**Expected Output**: CSV or list with over 700 entries, e.g., ListMembers:iUmNRKLdkKVH4WyBNw9x2A.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Gather Victim Org Information: Domains

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- [[tools/Wayback-Machine]]

## Tags

- [[graphql]]
- [[Reconnaissance]]
