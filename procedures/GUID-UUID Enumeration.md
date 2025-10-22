---
id: 4cee11ac-6a74-423c-be02-b5de4a71e2f4
name: GUID/UUID Enumeration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:59.818517+00:00'
updated_at: '2023-04-06T03:55:59.834110+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[System Information Discovery|T1082 - System Information Discovery]]'
tags:
- '[[GUID / UUID]]'
- '[[Insecure Randomness]]'
- '[[Tools]]'
commands:
- '[[GUID Tool with Timestamp and Process ID]]'
- '[[GUID Version 1 Information]]'
---

# GUID/UUID Enumeration

## Summary

The GUID/UUID Enumeration procedure involves using the `guidtool` tool to inspect and attack version 1 GUIDs. This tool can be used to extract information from GUIDs, such as the timestamp, MAC address, and clock sequence. This information can be used by an attacker to fingerprint a target system o

## Description

# Description

The GUID/UUID Enumeration procedure involves using the `guidtool` tool to inspect and attack version 1 GUIDs. This tool can be used to extract information from GUIDs, such as the timestamp, MAC address, and clock sequence. This information can be used by an attacker to fingerprint a target system or to gain further access. A version 1 GUID is generated using the current time and MAC address of the system. As a result, if an attacker is able to obtain a version 1 GUID, they can potentially determine the MAC address of the system that generated it. This can be useful for further attacks, such as MAC address spoofing or network impersonation.

Business Value: By enumerating GUIDs, an attacker can gain valuable information about a target system, which can be used to plan further attacks.

## Requirements

1. Access to the target system

1. The `guidtool` tool installed on the system

## Defense

1. Ensure that version 1 GUIDs are not used in sensitive areas of the system

1. Implement proper access controls to prevent unauthorized access to the `guidtool` tool

1. Monitor for unusual activity, such as an excessive amount of GUID/UUID requests

## Objectives

1. To extract information from version 1 GUIDs

1. To fingerprint a target system

1. To determine the MAC address of a system that generated a version 1 GUID

# Instructions

1. Use the `guidtool` tool to extract information from a version 1 GUID by running the command `guidtool -i <GUID>`. To attack a version 1 GUID, use the `-t` flag to specify the timestamp and the `-p` flag to specify the clock sequence.

**Code**: [[$ guidtool -i 95f6e264-bb00-11ec-8833-00155d01ef00]]

> The `guidtool` tool is used to inspect and attack version 1 GUIDs. The `-i` flag is used to specify the GUID to inspect. The output includes the version, timestamp, node, MAC address, and clock sequence. The `-t` flag is used to specify the timestamp to use when attacking a GUID. The `-p` flag is used to specify the clock sequence to use when attacking a GUID.

**Command** ([[GUID Version 1 Information]]):

```bash
$ guidtool -i 95f6e264-bb00-11ec-8833-00155d01ef00
UUID version: 1
UUID time: 2022-04-13 08:06:13.202186
UUID timestamp: 138691299732021860
UUID node: 91754721024
UUID MAC address: 00:15:5d:01:ef:00
UUID clock sequence: 2099

```

**Command** ([[GUID Tool with Timestamp and Process ID]]):

```bash
$ guidtool 1b2d78d0-47cf-11ec-8d62-0ff591f2a37c -t '2021-11-17 18:03:17' -p 10000
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[System Information Discovery|T1082 - System Information Discovery]]

## Commands Used

- [[GUID Tool with Timestamp and Process ID]]
- [[GUID Version 1 Information]]

## Tags

- [[GUID / UUID]]
- [[Insecure Randomness]]
- [[Tools]]
