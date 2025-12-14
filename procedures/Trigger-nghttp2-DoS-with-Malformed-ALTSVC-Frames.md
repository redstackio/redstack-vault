---
tags:
  - dos
  - exploit
  - http2
  - altsvc
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Node.js
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:37.445Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 3554edcb-6e42-4e4c-8d72-dbd87a952c67
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
---
# Trigger-nghttp2-DoS-with-Malformed-ALTSVC-Frames

## Summary

This procedure exploits a NULL pointer dereference in nghttp2 by sending malformed ALTSVC and GOAWAY HTTP/2 frames to a Node.js server (or from a malicious server to a client), causing an immediate process crash and denial of service.

## Description

The vulnerability stems from nghttp2's failure to initialize pointers when processing ALTSVC frames, leading to a dereference crash upon malformed input. A remote attacker can send these frames over an HTTP/2 connection to crash the target Node.js process without authentication. This affects Node.js versions before 10.4.1 and requires HTTP/2 support. Expected outcome is service unavailability until restart.

## Requirements

1. Remote network access to the target Node.js HTTP/2 endpoint (port 443 typically)
2. Ability to craft custom HTTP/2 frames (e.g., via scripting or fuzzing tools)
3. Vulnerable Node.js setup (pre-10.4.1) with nghttp2 integrated

## Defense

Defensive measures and detection strategies:

- Upgrade to Node.js 10.4.1 or later where the nghttp2 patch is applied
- Implement HTTP/2 frame validation at the proxy level (e.g., NGINX with strict parsing)
- Log and alert on abnormal HTTP/2 frame types or crash events

## Objectives

1. Deliver malformed ALTSVC frame to trigger uninitialized pointer use
2. Follow with GOAWAY to force immediate processing and crash
3. Achieve denial of service on the target service

## Instructions

### Step 1: Establish HTTP/2 Connection

**Context**: Initiate a secure HTTP/2 session with the target to prepare for frame injection.

Use a tool or script to connect via ALPN h2 to the target's HTTPS port, ensuring HTTP/2 negotiation succeeds.

### Step 2: Craft and Send Malformed ALTSVC Frame

**Context**: Construct an ALTSVC frame with invalid data to exploit the uninitialized pointer in nghttp2 processing.

Create a frame where the ALTSVC origin or value points to uninitialized memory (e.g., zero-length or malformed origin). Send it within the HTTP/2 stream. Example pseudocode in Python using hyperframe library:

```python
import socket
import ssl
from hyperframe.frame import HeadersFrame, AltSvcFrame

# Connect and negotiate HTTP/2
context = ssl.create_default_context()
context.set_alpn_protocols(['h2'])
sock = context.wrap_socket(socket.create_connection(('target.com', 443)), server_hostname='target.com')

# Send malformed ALTSVC (invalid origin length or pointer)
altsvc = AltSvcFrame(0)
altsvc.origin_len = 0  # Triggers uninit pointer
altsvc.serialize()  # Send over socket
```

Adapt to send raw bytes mimicking uninitialized data.

### Step 3: Send GOAWAY Frame to Force Crash

**Context**: Append a GOAWAY frame to close the stream and trigger immediate dereference.

Immediately after ALTSVC, send GOAWAY with error code 0x0 to process the malformed state:

```python
from hyperframe.frame import GoAwayFrame
goaway = GoAwayFrame(0, 0)
goaway.serialize()  # Send
```

This forces nghttp2 to handle the invalid ALTSVC, causing the crash.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Impact

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- dos
- exploit
- http2
