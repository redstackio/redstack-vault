---
id: 4cee11ac-6a74-423c-be02-b5de4a71e2f4
name: Enumerate-GUID-UUID-for-System-Fingerprinting
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:59.818517+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/GUID / UUID]]'
  - '[[tags/Insecure Randomness]]'
  - '[[tags/Tools]]'
commands:
  - '[[commands/guidtool-inspect-version1-guid]]'
  - '[[commands/guidtool-attack-version1-guid-with-timestamp-and-clock-sequence]]'
platforms:
  - Linux
tools:
  - '[[tools/guidtool]]'
validated: true
---

# Enumerate-GUID-UUID-for-System-Fingerprinting

## Summary

This procedure uses the `guidtool` utility to inspect and manipulate version 1 GUIDs (UUIDs), extracting embedded system information such as timestamps, MAC addresses, and clock sequences. It enables attackers to fingerprint target systems by revealing hardware details and timing data from GUIDs obtained during reconnaissance or data collection, potentially aiding in further network impersonation or targeted attacks.

## Description

Version 1 GUIDs are generated based on the system's current timestamp and the unique MAC address of the network interface, making them a source of valuable reconnaissance data. If an attacker obtains a version 1 GUID—perhaps from logs, artifacts, or API responses—they can reverse-engineer it to uncover the generating system's MAC address, creation time, and other identifiers. This information supports system fingerprinting, which can inform subsequent attacks like MAC spoofing for network access or correlating events across systems. The procedure leverages `guidtool` for both passive inspection (extracting data) and active manipulation (testing variations with custom timestamps and clock sequences to simulate or forge GUIDs). It is particularly useful in environments where GUIDs are exposed in web applications, databases, or file metadata, and assumes the attacker has obtained at least one sample GUID from the target.

## Requirements

1. Access to a sample version 1 GUID from the target system (e.g., via prior reconnaissance or data leak).
2. The `guidtool` tool installed on the attacker's system.
3. Basic command-line access (Linux/Unix-like environment recommended).
4. Knowledge of potential timestamps or clock sequences if attempting manipulation (optional for inspection).

## Defense

- Avoid using version 1 GUIDs in sensitive contexts; prefer version 4 (random) or version 5 (namespace-based) GUIDs to prevent information leakage.
- Implement strict access controls on systems generating or storing GUIDs, limiting exposure in logs, APIs, or public artifacts.
- Monitor for anomalous tool usage or GUID-related queries on endpoints, using logging for command-line tools and network traffic analysis.
- Employ endpoint detection to flag execution of GUID manipulation tools like `guidtool`.

## Objectives

1. Extract timestamp, MAC address, and clock sequence from a version 1 GUID to fingerprint the target system.
2. Manipulate GUID parameters to test for vulnerabilities in GUID-dependent authentication or validation.
3. Identify opportunities for MAC spoofing or time-based attacks based on revealed system details.

## Instructions

### Step 1: Inspect Version 1 GUID for Embedded Information

**Context**: Begin by analyzing a known version 1 GUID to extract its components. This step reveals the system's MAC address and creation timestamp, providing initial fingerprinting data without altering the GUID.

**Command** ([[commands/guidtool-inspect-version1-guid]]):
```bash
guidtool -i $_GUID
```

> This command parses the input GUID and outputs its version, timestamp (in both human-readable and numeric formats), node ID (derived from MAC), MAC address, and clock sequence. Use a placeholder for the GUID obtained from the target. Success is indicated by the version confirming as '1' and valid MAC extraction.

### Step 2: Attack GUID with Custom Timestamp and Clock Sequence

**Context**: If inspection yields useful data, proceed to manipulate the GUID by supplying alternative timestamps and clock sequences. This tests for weaknesses in systems that validate GUIDs based on time or sequence, potentially allowing forgery for impersonation.

**Command** ([[commands/guidtool-attack-version1-guid-with-timestamp-and-clock-sequence]]):
```bash
guidtool $_GUID -t '$_TIMESTAMP' -p $_CLOCK_SEQUENCE
```

> Provide the original GUID, a custom timestamp in 'YYYY-MM-DD HH:MM:SS' format (e.g., based on reconnaissance), and a clock sequence value (e.g., 10000 for testing). The tool generates a modified GUID; compare it against target expectations to identify bypasses. If the output produces a valid-looking GUID without errors, the manipulation succeeded, indicating potential for further exploitation.
