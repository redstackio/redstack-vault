---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
data: >-
  curl -X POST http://127.0.0.1:18081/json_rpc -H "Content-Type:
  application/json" -d
  '{"jsonrpc":"2.0","id":"0","method":"create_wallet","params":{"filename":"/path/to/new_wallet","password":"pass","language":"English"}}'
  -u user:pass
tags:
  - monero
  - rpc
  - wallet
type: command
output: '{"jsonrpc":"2.0","id":"0","result":{"info":{"address":"...","seed":"..."}}}'
executor: rpc
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:10.111Z'
verified: false
validated: true
submitted: true
---
# create-wallet-rpc

## Command

```bash
curl -X POST http://127.0.0.1:18081/json_rpc -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","id":"0","method":"create_wallet","params":{"filename":"/path/to/new_wallet","password":"pass","language":"English"}}' -u user:pass
```

## Description

This RPC command creates a new Monero wallet file with the specified parameters. In the attack, it's intercepted by the fake server, allowing the attacker to capture the filename and password for unauthorized access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| filename | Path to the new wallet file | Yes |
| password | Password for the wallet | Yes |
| language | Wallet language/mnemonic (default English) | No |

## Examples

### Basic Usage

```bash
curl -X POST http://127.0.0.1:18081/json_rpc -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","id":"0","method":"create_wallet","params":{"filename":"wallet","password":"secret"}}' -u rpc_user:rpc_pass
```

### Advanced Usage

```bash
curl -X POST http://127.0.0.1:18081/json_rpc -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","id":"0","method":"create_wallet","params":{"filename":"/tmp/attacker_wallet","password":"hacked","language":"English"}}' --digest -u rpc_user:rpc_pass
```

## Expected Output

Successful creation returns wallet info including address and seed:

```json
{"jsonrpc":"2.0","id":"0","result":{"info":{"address":"4Adk...","seed":"s1 s2 ... s25"},"wallet_file":"/path/to/new_wallet"}}
```

## Related

- [[procedures/Intercept-Client-Commands-via-Fake-Server]]
