---
tags:
  - rpc
  - blockchain
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Blockchain
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T17:24:55.692Z'
sub_techniques: []
id: 4b9434b2-afe4-424d-a193-311cd16d9b21
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Discover-Public-RPC-Endpoint

## Summary

This procedure entails locating publicly documented or discoverable RPC endpoints for Cosmos SDK-based blockchains, such as Sifchain, to initiate node reconnaissance.

## Description

Blockchain networks often expose RPC endpoints for querying chain state. Attackers search project docs, explorers, or common patterns (e.g., rpc.<chain>.finance) to find these. For Sifchain, http://rpc.sifchain.finance/ is public, allowing unauthenticated access to node details. This passive discovery aids in mapping network topology without direct interaction.

## Requirements

1. Knowledge of the target blockchain (Sifchain)
2. Access to public internet and search engines
3. Basic URL pattern recognition for RPC services

## Defense

Defensive measures and detection strategies:

- Restrict RPC endpoints behind authentication or IP whitelisting
- Use load balancers to mask internal IPs
- Monitor RPC logs for anomalous queries

## Objectives

1. Identify the base RPC URL
2. Confirm public accessibility
3. Prepare for endpoint enumeration

## Instructions

### Step 1: Search for RPC URL

**Context**: Use web search or chain explorers to find the endpoint.

**Command** (Browser Search):
Search "Sifchain RPC endpoint"

> Expected output: Discovery of http://rpc.sifchain.finance/.

### Step 2: Verify Accessibility

**Context**: Ping or curl the URL to ensure it's live.

**Command** (curl):
```bash
curl http://rpc.sifchain.finance/
```

> Expected output: JSON-RPC response listing methods.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Active Scanning: Vulnerability Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[rpc]]
- [[blockchain]]
