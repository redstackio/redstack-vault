---
type: code
language: ini
verified: true
platforms:
  - Linux
tags:
  - configuration
  - mitm
  - responder
validated: true
---

# Responder-Config-Disable-SMB-HTTP

## Code

```ini
[Responder Core]
; Servers to start
...
SMB = Off     # Turn this off
HTTP = Off    # Turn this off
```

## Description

Configuration snippet for Responder.conf to disable built-in SMB and HTTP servers, preventing self-poisoning in relay-focused attacks. This ensures Responder only performs poisoning without serving responses that could interfere.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| SMB | Set to 'Off' to disable SMB server | Off |
| HTTP | Set to 'Off' to disable HTTP server | Off |

## Usage

Edit the Responder.conf file (e.g., /etc/responder/Responder.conf) and insert this under [Responder Core]. Restart Responder or run with the updated config: `Responder -I eth0 -w -r -d`. Used in NTLM relay scenarios to cleanly forward captures to tools like ntlmrelayx.

## Detection

- File monitoring on Responder.conf changes in security tools.
- Process monitoring for Responder executions without SMB/HTTP modules.
- No direct network signatures, as this is config-only.

## Related

- [[procedures/Perform-NTLM-Relay-Attack-with-Responder-and-Impacket]]
- [[tools/Responder]]
