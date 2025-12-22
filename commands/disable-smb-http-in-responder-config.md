---
type: command
executor: text
data: |-
  [Responder Core]
  ; Servers to start
  ...
  SMB = Off     # Turn this off
  HTTP = Off    # Turn this off
output: null
platforms:
  - Linux
tags:
  - configuration
  - mitm
verified: true
validated: true
---

# disable-smb-http-in-responder-config

## Command

This is a configuration snippet for manual editing, not an executable command. Paste into Responder.conf under [Responder Core].

```ini
[Responder Core]
; Servers to start
...
SMB = Off     # Turn this off
HTTP = Off    # Turn this off
```

## Description

Disables Responder's SMB and HTTP servers to prevent self-poisoning during NTLM relay attacks. Use when relaying to external targets only.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| SMB = Off | Disables SMB server | Yes |
| HTTP = Off | Disables HTTP server | Yes |

## Examples

### Basic Usage

Edit /etc/responder/Responder.conf and add the snippet, then save.

### Verification

Run `Responder -w -r -d` and check logs for no SMB/HTTP startup messages.

## Expected Output

No output from edit; confirm by grepping the config: `grep -E 'SMB|HTTP' /etc/responder/Responder.conf` should show 'Off'.

## Related

- [[procedures/Perform-NTLM-Relay-Attack-with-Responder-and-Impacket]]
- [[tools/Responder]]
