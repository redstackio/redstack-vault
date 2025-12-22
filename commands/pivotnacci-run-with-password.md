---
id: b95d8e60-9ae2-47e9-b607-8132fc342a90
name: pivotnacci-run-with-password
type: command
executor: bash
data: pivotnacci $_AGENT_URL --password "$_PASSWORD"
output: null
created_at: '2023-04-06T03:56:22.599807+00:00'
updated_at: '2023-04-10T20:25:18.048816+00:00'
platforms:
  - Linux
tags:
  - pivoting
  - socks-proxy
verified: true
validated: true
---

# pivotnacci-run-with-password

## Command

```bash
pivotnacci $_AGENT_URL --password "$_PASSWORD"
```

## Description

This command starts a Pivotnacci SOCKS proxy connected to an HTTP agent, secured with a password for authentication during polling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_AGENT_URL` | URL of the HTTP agent on the compromised server (e.g., https://domain.com/agent.php) | Yes |
| `--password` | Sets the authentication password for agent callbacks | Yes |
| `$_PASSWORD` | The actual password value (e.g., s3cr3t) | Yes |

## Examples

### Basic Usage

```bash
pivotnacci https://domain.com/agent.php --password "s3cr3t"
```

### Advanced Usage

```bash
pivotnacci https://domain.com/agent.php --password "s3cr3t" --local-port 1081
```

## Expected Output

The command will output something like:

Starting SOCKS proxy on 127.0.0.1:1080
Polling agent at https://domain.com/agent.php every 1000ms
Proxy ready for connections.

## Related

- [[procedures/Web-SOCKS-Pivoting-with-Pivotnacci]]
