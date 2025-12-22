---
type: code
language: bash
verified: true
tags:
  - setup
  - tunnel
  - ngrok
platforms:
  - Linux
validated: true
---

# ngrok-complete-setup-script

## Code

```bash
# get the binary
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip 

# log into the service
./ngrok authtoken 3U[REDACTED_TOKEN]Hm

# deploy a port forwarding for 4433
./ngrok http 4433
./ngrok tcp 4433
```

## Description

This bash script automates the full setup of ngrok, including downloading the binary, authenticating, and starting both HTTP and TCP tunnels on port 4433. It serves as a quick one-liner deployment for establishing tunnels in red team operations or bypassing network restrictions.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 3U[REDACTED_TOKEN]Hm | Ngrok authentication token (replace with your own) | 2YourActualTokenHere |
| 4433 | Local port for tunneling | 8080 |

## Usage

Save as a .sh file, make executable with `chmod +x script.sh`, and run `./script.sh`. Note that HTTP and TCP commands are sequential; only one tunnel runs at a time unless run in background. Use in scenarios requiring rapid C2 setup behind firewalls.

## Detection

- Monitor for wget/unzip to ngrok URLs or processes named 'ngrok'.
- Network logs showing connections to ngrok.io domains.
- File creation of ngrok binary in temp directories.

## Related

- [[procedures/Setup-Ngrok-Port-Forwarding-Tunnel]]
- [[tools/ngrok]]
