---
id: cmd-curl-sifchain-net-info-001
data: 'curl https://rpc.sifchain.finance/net_info'
tags:
  - reconnaissance
  - information-disclosure
type: command
output: JSON response with network info
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:55.648Z'
verified: false
validated: true
submitted: true
---
# curl-sifchain-net-info

## Command

```bash
curl https://rpc.sifchain.finance/net_info
```

## Description

This command uses curl to perform a GET request to the Sifchain RPC /net_info endpoint, retrieving JSON data that discloses internal network information such as peer IP addresses and ports. Use it for reconnaissance on Cosmos SDK-based blockchains to identify origin infrastructure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | The RPC endpoint URL (e.g., https://rpc.sifchain.finance/net_info) | Yes |
| -s | Silent mode to suppress progress meter | No |

## Examples

### Basic Usage

```bash
curl https://rpc.sifchain.finance/net_info
```

### Advanced Usage

```bash
curl -s https://rpc.sifchain.finance/net_info | jq '.'
```

## Expected Output

A JSON object like {"jsonrpc":"2.0","id":null,"result":{"listening":true,"listeners":["..."],"peers":[{"node_info":{"listen_addr":"tcp://IP:PORT"}}]}}, containing exposed network details.

## Related

- [[Related Procedure|procedures/Query-Sifchain-RPC-Net-Info-for-Network-Details]]
