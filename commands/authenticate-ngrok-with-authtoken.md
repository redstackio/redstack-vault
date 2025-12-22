---
type: command
executor: bash
data: ./ngrok authtoken $_AUTH_TOKEN
tags:
  - authentication
  - setup
platforms:
  - Linux
verified: true
validated: true
---

# authenticate-ngrok-with-authtoken

## Command

```bash
./ngrok authtoken $_AUTH_TOKEN
```

## Description

Authenticates the ngrok client with your account token, enabling tunnel creation and advanced features.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_AUTH_TOKEN | Your ngrok authentication token from dashboard | Yes |

## Examples

### Basic Usage

```bash
./ngrok authtoken 2abc123def456ghi789
```

### Advanced Usage

```bash
./ngrok authtoken $_AUTH_TOKEN --config /path/to/config.yaml
```

## Expected Output

Authtoken saved to configuration file: /root/.ngrok2/ngrok.yml
https://dashboard.ngrok.com/get-started/your-authtoken

## Related

- [[procedures/Setup-Ngrok-Port-Forwarding-Tunnel]]
