---
tags:
  - dos
  - curl
  - mqtt
  - exploitation
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-mqtt-dos-trigger]]'
  - '[[commands/curl-mqtt-with-timeout]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:36.676Z'
sub_techniques: []
id: 8f3c4c68-9401-467a-8f88-70efbbb14a62
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[OS Exhaustion Flood]]'
---
# Trigger-curl-DoS-with-MQTT-URL

## Summary

This procedure exploits a flaw in curl's MQTT parsing by connecting to a server serving a partial response, causing an infinite loop in the mqtt_doing function and leading to 100% CPU consumption until interrupted.

## Description

The vulnerability occurs in lib/mqtt.c around line 2132 in the MQTT_FIRST state, where curl repeatedly calls Curl_read after connection closure (FIN/RST), receiving 0 bytes without proper error handling, resulting in a busy loop. Target environment requires curl compiled with MQTT support (--enable-mqtt). Prerequisites include a running malicious server from the setup procedure. Expected outcome: curl hangs indefinitely, impacting any automated MQTT-fetching applications like crawlers.

## Requirements

1. curl with MQTT protocol enabled
2. Local MQTT server on port 12345 serving the poc response
3. No network restrictions on localhost

## Defense

Defensive measures and detection strategies:

- Apply curl patches for the vulnerability (post-2023 fixes)
- Enforce timeouts in curl invocations (--max-time <seconds>)
- Log and alert on prolonged high CPU in network client processes

## Objectives

1. Initiate MQTT connection to trigger parsing loop
2. Demonstrate uncontrolled resource exhaustion
3. Validate impact on client-side applications

## Instructions

### Step 1: Basic Trigger

**Context**: Connect to the MQTT server without timeout to reproduce the infinite loop.

**Command** ([[commands/curl-mqtt-dos-trigger]]):
```bash
curl mqtt://localhost:12345
```

> This uses the mqtt:// URL scheme to connect and parse the response, entering the loop on closure. Expected output: Repeated debug logs like 'mqtt_doing: state [0]' and no exit.

### Step 2: Mitigated Test

**Context**: Add a timeout to safely observe the behavior without indefinite hang.

**Command** ([[commands/curl-mqtt-with-timeout]]):
```bash
curl -m3 mqtt://localhost:12345
```

> The -m3 flag limits to 3 seconds. Expected output: Runs for 3s, then times out with error, avoiding full DoS.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[OS Exhaustion Flood]]

### Sub-Techniques


## Commands Used

- [[commands/curl-mqtt-dos-trigger]]
- [[commands/curl-mqtt-with-timeout]]

## Tools Used

- [[tools/curl]]

## Tags

- [[dos]]
- [[tools/curl]]
