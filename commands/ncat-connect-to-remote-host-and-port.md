---
id: e9aff3c0-e1ef-4e0e-9494-1ee946a32778
name: ncat-connect-to-remote-host-and-port
type: command
executor: bash
data: ncat $_TARGET_IP $_TARGET_PORT
output: null
created_at: '2019-10-09T22:21:56.380000+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - network
  - connection
verified: true
validated: true
---

# ncat-connect-to-remote-host-and-port

## Command

```bash
ncat $_TARGET_IP $_TARGET_PORT
```

## Description

This command uses ncat (from the Netcat suite, often bundled with Nmap) to establish a TCP connection to a remote host and port. It simulates a client connection, such as to a service like IRC, web server, or custom listener. Commonly used for manual interaction with remote services, sending raw data payloads, or testing connectivity in penetration testing scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the target host | Yes |
| $_TARGET_PORT | Port number on the target (e.g., 80 for HTTP, 6667 for IRC) | Yes |

## Examples

### Basic Usage

```bash
ncat 192.168.1.100 6667
```

Connects to the target at 192.168.1.100 on port 6667, opening an interactive session for input/output.

### Advanced Usage

```bash
ncat -v 10.0.0.5 6667
```

Adds verbose (-v) output to display detailed connection information, such as handshake details and errors.

## Expected Output

```
Ncat: Version 7.91 ( https://nmap.org/ncat )
Ncat: Connected to 192.168.1.100 6667.
```

The prompt becomes interactive, ready for user input. No further output appears until data is sent or received from the remote host. If the connection fails, an error like "Ncat: Connection refused" is shown.

## Related

- [[procedures/Exploit-Backdoor-in-UnrealIRCd-3.2.8]]
- [[tools/Netcat]]
