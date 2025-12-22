---
type: command
executor: bash
data: >-
  wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip &&
  unzip ngrok-stable-linux-amd64.zip
tags:
  - download
  - setup
platforms:
  - Linux
verified: true
validated: true
---

# download-and-unzip-ngrok-binary

## Command

```bash
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip && unzip ngrok-stable-linux-amd64.zip
```

## Description

Downloads the ngrok binary ZIP for Linux AMD64 and extracts it to the current directory, preparing the tool for use in tunneling operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL (implicit) | Download source for ngrok ZIP | Yes |

## Examples

### Basic Usage

```bash
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip && unzip ngrok-stable-linux-amd64.zip
```

### Advanced Usage

```bash
wget -O ngrok.zip https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip && unzip ngrok.zip && rm ngrok.zip
```

## Expected Output

wget: ~50% [===================>] 10.5M  1.2MB/s    
Archive:  ngrok-stable-linux-amd64.zip
  inflating: ngrok  

The `./ngrok` executable is now available.

## Related

- [[procedures/Setup-Ngrok-Port-Forwarding-Tunnel]]
