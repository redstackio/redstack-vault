---
tags:
  - node-info
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Blockchain
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Client Configurations]]'
updated_at: '2025-12-14T17:24:55.685Z'
sub_techniques: []
id: 5120f25a-33f1-497c-8558-ebfe1eaa6f68
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Client Configurations]]'
---
# Query-Node-Status-Endpoint

## Summary

This procedure queries the /status endpoint of a Cosmos SDK RPC to retrieve detailed node information, including IP addresses, versions, and sync status, for infrastructure mapping.

## Description

The /status endpoint provides comprehensive node metadata essential for reconnaissance. In Sifchain's case, it exposes internal IP (34.228.72.160), ports (26656, 26657), version (0.33.9), moniker (helen), and network (sifchain). This data can inform DDoS targeting, version-specific exploits, or chain analysis. Queries are simple HTTP GETs, fully public.

## Requirements

1. Accessible RPC URL with /status path
2. HTTP GET capability (curl or browser)
3. JSON parsing for output analysis

## Defense

Defensive measures and detection strategies:

- Sanitize /status responses to hide IPs and versions
- Proxy RPC through a gateway that strips sensitive fields
- Rate-limit status queries to prevent abuse

## Objectives

1. Extract node identification details
2. Gather network and sync information
3. Identify potential vulnerabilities from version exposure

## Instructions

### Step 1: Query the Status Endpoint

**Context**: Send a GET request to retrieve node status.

**Command** (curl):
```bash
curl http://rpc.sifchain.finance/status
```

> Expected output: JSON object with node_info {id, listen_addr: "tcp://0.0.0.0:26656", network: "sifchain", version: "0.33.9", moniker: "helen"}, sync_info {latest_block_height, catching_up}, and validator_info.

### Step 2: Parse and Analyze Response

**Context**: Extract key fields like IP from listen_addr or external sources.

**Command** (jq for JSON):
```bash
curl http://rpc.sifchain.finance/status | jq '.node_info'
```

> Expected output: Filtered JSON revealing IP 34.228.72.160, ports 26656/26657.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Client Configurations]] Gather Victim Host Information: Client Configurations

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[node-info]]
- [[Reconnaissance]]
