---
tags:
  - graphql
  - baseline
  - recon
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/baseline-graphql-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:25:53.220Z'
sub_techniques: []
id: c8418f08-cbab-4be6-97da-f44042f23b51
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Baseline-GraphQL-Search-Query

## Summary

This procedure establishes a baseline response time for the GraphQL search endpoint to compare against exploitative payloads in a ReDoS attack scenario.

## Description

In the context of discovering ReDoS vulnerabilities, start by querying the /graphql endpoint with a normal search term like 'AAA' to measure typical latency. This helps identify delays caused by malicious regex inputs later. The target is a Node.js-based Apollo Server handling search queries on wiki.cs.money, where the 'q' parameter is processed.

## Requirements

1. Network access to https://wiki.cs.money/graphql
2. curl installed for HTTP requests
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Monitor baseline query latencies with application logs
- Implement request rate limiting on GraphQL endpoints

## Objectives

1. Confirm endpoint accessibility and normal behavior
2. Record baseline response time
3. Prepare for anomaly detection in subsequent steps

## Instructions

### Step 1: Send Baseline Query

**Context**: Execute a standard search to gauge normal performance.

**Command** ([[commands/baseline-graphql-query]]):
```bash
curl 'https://wiki.cs.money/graphql' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36' -H 'content-type: application/json' -H 'accept: */*' --data-binary '{"query":"query { search(q: \"AAA\", lang: \"en\") { _id weapon_id rarity collection{ _id name } collection_id } }"}' --compressed
```

> This sends a POST request with a benign GraphQL query. Expect a fast JSON response with search results.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Network Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/baseline-graphql-query]]

## Tools Used

- [[tools/curl]]

## Tags

- graphql
- baseline
- recon
