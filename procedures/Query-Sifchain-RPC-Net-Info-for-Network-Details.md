---
id: proc-sifchain-rpc-query-001
tags:
  - information-disclosure
  - rpc
  - blockchain
  - cosmos-sdk
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-sifchain-net-info]]'
verified: false
platforms:
  - Web
  - Blockchain
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Network Information]]'
updated_at: '2025-12-14T17:24:55.652Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Network Information]]'
---
# Query Sifchain RPC /net_info for Network Details

## Summary

This procedure demonstrates how to query the public /net_info RPC endpoint on Sifchain's mainnet or testnet to disclose internal network information, including peer IP addresses and ports. This is a standard feature of Cosmos SDK-based blockchains but can reveal origin infrastructure details, potentially allowing attackers to bypass CDN protections like Cloudflare.

## Description

In the Sifchain blockchain application, the RPC endpoints at rpc.sifchain.finance and rpc-testnet.sifchain.finance expose the /net_info endpoint without authentication. Accessing this endpoint returns JSON data about the network, including listening addresses of connected peers (e.g., tcp://IP:PORT). While intentional for blockchain transparency, this can lead to information disclosure of internal IPs and services. The procedure involves direct HTTP GET requests to these endpoints, observable via browser or curl. Expected outcomes include mapping the network topology for further reconnaissance or targeted attacks. Prerequisites include internet access; no credentials are needed as it's public.

## Requirements

1. Internet connectivity to reach public RPC endpoints
2. Web browser or curl tool for HTTP requests
3. Basic JSON parsing ability to extract IPs and ports

## Defense

Defensive measures and detection strategies:

- Restrict /net_info endpoint to authenticated or internal access if not required for public use
- Implement rate limiting on RPC endpoints to prevent abuse
- Use CDN or proxy configurations that do not leak origin IPs in responses
- Monitor access logs for unusual queries to /net_info from external IPs

## Objectives

1. Gather internal IP addresses and ports from Sifchain peers
2. Identify potential bypass paths around front-end protections
3. Map blockchain network infrastructure for reconnaissance

## Instructions

### Step 1: Access Mainnet RPC Endpoint

**Context**: Query the production Sifchain RPC to retrieve network info, exposing peer details.

**Command** ([[commands/curl-sifchain-net-info]]):
```bash
curl https://rpc.sifchain.finance/net_info
```

> This command sends a GET request to the /net_info endpoint and returns JSON with network details. Look for the "peers" array containing "listen_addr" fields like "tcp://192.0.2.1:26656", revealing IPs and ports.

### Step 2: Access Testnet RPC Endpoint

**Context**: Repeat the query on the testnet for additional exposure, useful for testing or broader reconnaissance.

**Command** ([[commands/curl-sifchain-net-info]]):
```bash
curl https://rpc-testnet.sifchain.finance/net_info
```

> Similar to the mainnet query, this outputs JSON with testnet peer information. Compare responses to identify consistent infrastructure patterns.

### Step 3: Analyze Response for Sensitive Data

**Context**: Parse the JSON output to extract and document exposed IPs and ports for potential targeting.

**Command** (Manual or jq for parsing):
```bash
curl https://rpc.sifchain.finance/net_info | jq '.result.peers[].node_info.listen_addr'
```

> If jq is available, this filters the response to list only listening addresses. Manually note IPs that appear to be origin servers, bypassing any CDN.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Network Information]]

### Sub-Techniques


## Commands Used

- [[commands/curl-sifchain-net-info]]

## Tools Used


## Tags

- information-disclosure
- rpc
- blockchain
- cosmos-sdk
- reconnaissance
