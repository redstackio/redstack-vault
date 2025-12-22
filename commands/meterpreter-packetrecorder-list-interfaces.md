---
id: 8df0f9aa-1500-4c3e-b98f-9120b2dbbad9
name: meterpreter-packetrecorder-list-interfaces
type: command
executor: meterpreter
data: run packetrecorder -li
output: null
created_at: '2023-04-06T03:56:21.428128+00:00'
updated_at: '2023-04-10T20:24:58.780502+00:00'
platforms:
  - Linux
  - Windows
tags:
  - metasploit
  - meterpreter
  - network-sniffing
verified: true
validated: true
---

# meterpreter-packetrecorder-list-interfaces

## Command

```meterpreter
run packetrecorder -li
```

## Description

This command lists all available network interfaces on the target system within a Meterpreter session, allowing selection for packet capture. Use it during post-exploitation to identify the interface connected to the network of interest.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-li` | List interfaces flag (fixed option) | Yes |

## Examples

### Basic Usage

```meterpreter
run packetrecorder -li
```

### Advanced Usage

No additional parameters needed; run directly in Meterpreter shell.

## Expected Output

[*] Available interfaces:
   1. eth0 (192.168.1.10/24)
   2. lo (127.0.0.1/8)
   3. wlan0 (10.0.0.5/24)

This output shows interface numbers, names, and IP details for selection.

## Related

- [[procedures/Capture-Network-Packets-with-Meterpreter]]
- [[commands/meterpreter-packetrecorder-record-packets]]
