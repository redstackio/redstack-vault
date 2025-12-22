---
id: ea9edc75-ade5-4c9d-85ae-e145585d6b55
name: Sniff-Unencrypted-LDAP-Queries-via-Loopback
type: procedure
verified: true
submitted: true
created_at: '2019-10-09T21:17:13.602531+00:00'
updated_at: '2023-05-25T19:46:39.379615+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Sniffing|T1040 - Network Sniffing]]'
sub_techniques: []
tags:
  - data-exposure
  - network
commands:
  - '[[commands/tcpdump-capture-ldap-on-loopback]]'
  - '[[commands/tshark-extract-hex-ascii-from-pcap]]'
platforms:
  - Linux
tools:
  - '[[tools/tcpdump]]'
  - '[[tools/TShark]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Sniff-Unencrypted-LDAP-Queries-via-Loopback

## Summary

This procedure demonstrates how to intercept unencrypted LDAP queries transmitted over the loopback interface on a Linux system. By capturing network traffic locally during LDAP authentication or query operations, an attacker can extract plaintext credentials, user details, or other sensitive information from vulnerable LDAP implementations that do not enforce encryption like LDAPS.

## Description

LDAP (Lightweight Directory Access Protocol) is commonly used for directory services in enterprise environments, often running on port 389. In some configurations, especially on localhost (loopback interface), queries may be sent unencrypted, exposing bind credentials, search filters, or attribute values. This procedure assumes the attacker has local access to the target system where LDAP queries originate or are processed. It involves capturing packets with tcpdump, waiting for or triggering LDAP activity, and analyzing the capture file with tshark to reveal hexadecimal and ASCII dumps containing credentials. This technique is effective against legacy or misconfigured LDAP servers and can lead to credential theft or enumeration of directory objects. Prerequisites include root privileges for packet capture and an active unencrypted LDAP service.

## Requirements

1. Root or elevated privileges on a Linux system to perform packet capture.
2. Unencrypted LDAP service running on the loopback interface (127.0.0.1:389).
3. Tools tcpdump and tshark installed.
4. Ongoing or triggerable LDAP queries (e.g., via authentication attempts or directory lookups).

## Defense

- Enforce LDAPS (LDAP over TLS) on port 636 for all connections to encrypt traffic.
- Restrict loopback interface monitoring and disable unencrypted LDAP binds.
- Implement host-based firewalls to block unauthorized packet capture tools.
- Enable logging for LDAP operations and monitor for anomalous local network activity.
- Use application-level controls to validate and sanitize LDAP queries.

## Objectives

1. Capture unencrypted LDAP traffic on the loopback interface to intercept sensitive data.
2. Extract and analyze plaintext credentials or directory information from captured packets.
3. Validate the presence of vulnerabilities in LDAP configurations for further exploitation.

## Instructions

### Step 1: Capture LDAP Packets on Loopback Interface

**Context**: Initiate packet capture on the loopback interface (lo) to intercept traffic on LDAP port 389. Limit the capture to 10 packets to avoid excessive data, saving to a PCAP file for later analysis. This step requires root access and assumes LDAP queries will occur soon after starting the capture.

**Command** ([[commands/tcpdump-capture-ldap-on-loopback]]):
```bash
tcpdump -i lo -w $_DUMP.pcap -c 10 port $_PORT
```

> This command listens on the loopback interface, writes captured packets to a file named by $_DUMP (e.g., ldap_capture.pcap), stops after 10 packets matching the port filter ($_PORT=389), and displays capture statistics upon completion. Run this in a terminal with sudo.

### Step 2: Trigger or Wait for LDAP Query

**Context**: With the capture running, perform or wait for an action that generates LDAP traffic, such as a user login, directory search, or authentication bind. If no natural traffic occurs, manually trigger it using tools like ldapsearch against localhost.

**Command** (no specific command; use ldapsearch if needed):
```bash
ldapsearch -x -H ldap://127.0.0.1:389 -b "dc=example,dc=com" "(uid=testuser)"
```

> This optional command (not captured in PCAP but triggers traffic) performs a simple LDAP search. Monitor the tcpdump output to confirm packets are captured. Stop the capture manually if more than 10 packets are needed by pressing Ctrl+C.

### Step 3: Extract Hex and ASCII Dump from PCAP

**Context**: Analyze the saved PCAP file to dump packet contents in hexadecimal and ASCII formats, revealing unencrypted LDAP payloads such as bind DNs, passwords, or attributes.

**Command** ([[commands/tshark-extract-hex-ascii-from-pcap]]):
```bash
tshark -r $_DUMP.pcap -x
```

> This reads the PCAP file specified by $_DUMP and outputs each packet's frame in hex and ASCII. Look for LDAP protocol indicators (e.g., BER-encoded data) and plaintext strings like usernames or passwords in the ASCII column.

### Step 4: Analyze for Credentials

**Context**: Manually inspect the output for sensitive information. Search for patterns like 'uid=', 'password', or base64-encoded strings that may decode to credentials. Use additional tools like strings or Wireshark GUI if needed for deeper analysis.

> No command here; review the tshark output for LDAP bind requests (operation code 0x60) containing cleartext credentials. Success is indicated by visible usernames, passwords, or directory entries in the dump.
