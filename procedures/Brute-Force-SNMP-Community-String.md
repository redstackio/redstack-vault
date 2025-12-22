---
type: procedure
verified: true
tactics:
  - '[[Discovery]]'
techniques:
  - '[[System Service Discovery]]'
sub_techniques: []
tags:
  - brute-force
  - network
  - discovery
commands:
  - '[[commands/onesixtyone-brute-force-community]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/onesixtyone]]'
skill_level: beginner
impact_level: medium
detection_risk: high
validated: true
---

# Brute-Force-SNMP-Community-String

## Summary

This procedure brute-forces SNMP community strings on a target device to gain unauthorized access to management information, such as system details, services, and network configuration. It uses the onesixtyone tool to test a wordlist of potential community strings against the target IP, enabling discovery of sensitive internal information if a weak or default string is in use.

## Description

Simple Network Management Protocol (SNMP) facilitates the exchange of management data between network devices, protected by a community string acting as a basic password. Attackers can brute-force this string to query the device for information like running services, installed patches, and hardware details. This technique is effective against devices with default or predictable community strings (e.g., 'public' or 'private') and is commonly used in reconnaissance phases to map network infrastructure. The procedure assumes network access to the target on UDP port 161 and focuses on version 1/2c, which rely solely on community strings for authentication.

## Requirements

1. Network connectivity to the target device on UDP port 161 (SNMP service).
2. A wordlist file containing potential community strings (e.g., common defaults like 'public', 'private', 'admin').
3. The onesixtyone tool installed on the attacker's system.
4. Administrative privileges on the attacker's machine to run network tools.

## Defense

Defensive measures and detection strategies:

- Disable SNMP or restrict it to trusted management networks using firewalls (block UDP 161 from external sources).
- Use SNMPv3, which supports strong authentication and encryption, instead of v1/v2c.
- Implement network intrusion detection systems (NIDS) to monitor for high-volume UDP traffic to port 161 or repeated failed queries.
- Regularly audit and change default community strings; use unique, complex strings.
- Enable logging on network devices to track SNMP queries and alert on suspicious patterns.

## Objectives

1. Identify a valid SNMP community string to authenticate to the target device.
2. Enumerate system information, services, and configuration details via SNMP queries.
3. Gather intelligence for further network discovery or exploitation.
4. Validate the success of the brute-force attempt through response data.

## Instructions

### Step 1: Prepare the Wordlist

**Context**: Create or obtain a wordlist of common SNMP community strings to use in the brute-force attempt. This ensures efficient testing without unnecessary noise.

Use a text editor or existing wordlist tool to compile strings like 'public', 'private', 'admin', 'default', etc. Save as a plain text file, one string per line.

> No specific command is required here, but ensure the file path is accessible.

### Step 2: Execute the Brute-Force Attack

**Context**: Run the onesixtyone tool to test the wordlist against the target IP. This sends SNMP queries for each community string and reports successful matches along with any retrieved information.

**Command** ([[commands/onesixtyone-brute-force-community]]):
```bash
onesixtyone -c $_WORDLIST $_TARGET_IP
```

> This command performs a dictionary attack on SNMP v1/v2c. The -c flag specifies the community wordlist file. Monitor the output for successful authentications, which will display the valid string and any queried data (e.g., system description). If no match is found, consider expanding the wordlist or checking network/firewall issues.

### Step 3: Verify and Query Further

**Context**: Once a valid community string is identified, use it to perform additional SNMP queries to extract more details, confirming access and gathering useful reconnaissance data.

Use snmpwalk or similar (not covered in this procedure) with the discovered string, e.g., `snmpwalk -v2c -c <discovered_string> $_TARGET_IP`. Look for OIDs like 1.3.6.1.2.1.1 (system group) to enumerate services and versions.

> Success is indicated by detailed responses beyond basic authentication, such as host OS, uptime, or interface details.
