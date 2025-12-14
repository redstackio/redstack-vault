---
tags:
  - enumeration
  - cosmos-sdk
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Client Configurations]]'
updated_at: '2025-12-14T17:24:55.689Z'
sub_techniques: []
id: 5e4aafe3-e39d-4191-aa42-722af7691135
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Client Configurations]]'
---
# Access-RPC-Endpoints

## Summary

This procedure involves enumerating available endpoints on a public Cosmos SDK RPC server to identify queryable paths for information gathering.

## Description

Cosmos SDK nodes expose standard ABCI and JSON-RPC endpoints. Accessing the root URL reveals a catalog of methods like /status and /net_info. For Sifchain, this is unauthenticated, allowing attackers to map capabilities without tools. Outcomes include selection of high-value endpoints for deeper queries.

## Requirements

1. Valid RPC base URL (http://rpc.sifchain.finance/)
2. HTTP client like browser or curl
3. No authentication needed

## Defense

Defensive measures and detection strategies:

- Disable or hide endpoint listing on RPC servers
- Implement rate limiting on public endpoints
- Log and alert on endpoint access patterns

## Objectives

1. List all exposed RPC paths
2. Identify standard Cosmos SDK endpoints
3. Select targets for detailed querying

## Instructions

### Step 1: Query Root Endpoint

**Context**: Fetch the root path to see available methods.

**Command** (curl):
```bash
curl http://rpc.sifchain.finance/
```

> Expected output: JSON with methods array including "status", "net_info".

### Step 2: Browse in Browser

**Context**: Use a web browser for visual inspection.

**Command** (Browser):
Open http://rpc.sifchain.finance/

> Expected output: Readable list of endpoints like /abci_info, /status.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Client Configurations]] Gather Victim Host Information: Client Configurations

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[enumeration]]
- [[cosmos-sdk]]
