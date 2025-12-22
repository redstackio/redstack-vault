---
id: ac-sifchain-rpc-disclosure-001
tags:
  - information-disclosure
  - rpc
  - blockchain
  - cosmos-sdk
  - reconnaissance
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
  - Blockchain
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Query-Sifchain-RPC-Net-Info-for-Network-Details]]'
step_count: 1
techniques:
  - '[[Gather Victim Network Information]]'
updated_at: '2025-12-14T17:24:55.666Z'
description: >-
  A reconnaissance attack chain that leverages public RPC endpoints in the
  Sifchain blockchain to disclose internal network information, including IP
  addresses and ports, potentially exposing origin services.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Network Information]]'
---
# Information Disclosure via Sifchain Public RPC Endpoints

Multi-stage attack chain demonstrating a complete attack workflow for reconnaissance on Sifchain's public RPC endpoints.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance] --> B[Information Disclosure]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or [[commands/curl-sifchain-net-info]]

### Target Environment

- Sifchain mainnet or testnet RPC endpoints (rpc.sifchain.finance or rpc-testnet.sifchain.finance)
- Public internet access
- No authentication required

### Initial Access Requirements

- None; endpoints are publicly accessible
- Network position: External attacker
- Prior access needed: None

## Detailed Attack Procedures

### Step 1: Query RPC Endpoint for Network Information
procedure: [[procedures/Query-Sifchain-RPC-Net-Info-for-Network-Details]]

**Objective**: Access the /net_info endpoint to retrieve JSON data exposing internal network details, such as IP addresses and ports of peers in the Sifchain blockchain network.

**Instructions**: Navigate to the RPC endpoint URL in a web browser or use [[commands/curl-sifchain-net-info]] to fetch the data. For mainnet:

```bash
curl https://rpc.sifchain.finance/net_info
```

For testnet:

```bash
curl https://rpc-testnet.sifchain.finance/net_info
```

Parse the JSON response to identify exposed IPs and ports.

**Expected Output**: JSON object containing network information, including "peers" array with IP addresses (e.g., {"result": {"peers": [{"node_info": {"listen_addr": "tcp://123.45.67.89:26656"}}] }}).

**Success Indicators**:
- JSON response received without errors
- IP addresses and ports visible in the "listen_addr" fields
- Potential bypass of front-end protections like Cloudflare identified

## Attack Chain Summary

### Key Achievements

1. Successful disclosure of internal network topology via public RPC
2. Identification of origin IP addresses for direct targeting
3. Demonstration of standard Cosmos SDK behavior leading to info exposure

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Gather Victim Network Information]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]

---
*Last updated: 2023-10-01T00:00:00Z*
