---
type: procedure
verified: true
submitted: true
created_at: '2020-02-21T05:35:28.317618+00:00'
updated_at: '2023-05-26T00:45:53.991866+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Service Scanning|T1046 - Network Service Scanning]]'
sub_techniques: []
platforms:
  - Linux
  - Windows
tags:
  - '[[tags/data exposure]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Network]]'
commands:
  - '[[commands/snmp-check-enumerate-server]]'
  - '[[commands/snmpwalk-enumerate-server]]'
tools: []
validated: true
---

# Enumerate-Authenticated-SNMP-Server

## Summary

This procedure enumerates an SNMP server using a valid community string for authentication, retrieving system information, network details, and other configuration data. It is useful during reconnaissance to gather intelligence on target systems, such as hostnames, OS versions, running processes, and interface configurations, without requiring full administrative access.

## Description

SNMP (Simple Network Management Protocol) allows remote querying of device information if the community string (like a password) is known. This procedure assumes authenticated access via SNMPv1, v2c, or v3 and uses tools like snmpwalk and snmp-check to perform comprehensive enumeration. It targets UDP port 161 by default and can reveal sensitive details like user accounts, routing tables, and software inventory. Use this in scenarios where SNMP is exposed on the network, such as misconfigured routers, servers, or IoT devices. If no results are returned, verify the SNMP version and community string, as mismatches can cause failures. For targeted queries, use specific Object Identifiers (OIDs) from resources like oid-info.com.

## Requirements

1. Network access to the target on UDP port 161 (SNMP default).
2. Valid SNMP community string (e.g., 'public' or custom) and version (1, 2c, or 3).
3. SNMP tools installed (snmp package on Linux/Windows).
4. Optional: MIBs installed for human-readable output.
5. Target IP address or hostname.

## Defense

- Restrict SNMP to trusted networks via firewalls and disable on public-facing interfaces.
- Use SNMPv3 with authentication and encryption instead of v1/v2c community strings.
- Monitor SNMP traffic logs for unauthorized queries and implement rate limiting.
- Disable unnecessary MIB exposure and audit community strings regularly.

## Objectives

1. Retrieve general system information (hostname, description, uptime).
2. Enumerate network interfaces, routing, and connected devices.
3. Identify potential vulnerabilities or sensitive data exposure via SNMP.
4. Validate SNMP configuration and version compatibility.

## Instructions

### Step 1: Optional - Install and Configure SNMP MIBs for Readability

**Context**: Installing MIBs (Management Information Bases) translates numeric OIDs into human-readable names, making output easier to interpret. This is recommended for complex enumerations but optional if basic output suffices.

**Code** ([[codes/Install-SNMP-MIBs-Downloader-and-Configure]]):

```bash
apt update && apt install snmp-mibs-downloader -y \
&& sed -i '/mibs/s/^/#/g' /etc/snmp/snmp.conf
```

> Run this on a Debian-based system like Kali Linux. The first command updates packages and installs the downloader, which fetches standard MIB files. The second comments out the 'mibs' line in snmp.conf to enable loading all MIBs. Expected output: Package installation confirmation and no errors in sed operation. Restart any SNMP-related services if needed.

### Step 2: Perform Full SNMP Walk Enumeration

**Context**: Use snmpwalk to traverse the entire SNMP MIB tree, dumping all accessible objects. This provides a broad overview of the target's SNMP data, including system details and network config. Start with this for initial discovery.

**Command** ([[commands/snmpwalk-enumerate-server]]):

```bash
snmpwalk -c $_COMMUNITY_STRING -v $_VERSION $_TARGET_IP
```

> This command walks the SNMP tree starting from the root OID. Replace placeholders with actual values (e.g., -c public -v 2c 10.10.10.10). If using SNMPv3, add authentication options like -u username -a MD5 -A password. Expected output includes lines like SNMPv2-MIB::sysDescr.0 = STRING: [OS description], covering system info, interfaces, and more. If empty, try different versions (1, 2c, 3).

### Step 3: Run Targeted SNMP Check Enumeration

**Context**: snmp-check provides a structured report on SNMP data, categorizing output into sections like system info, interfaces, and processes. It is more user-friendly than raw snmpwalk for quick assessments and highlights potential security issues.

**Command** ([[commands/snmp-check-enumerate-server]]):

```bash
snmp-check -c $_COMMUNITY_STRING -v $_VERSION $_TARGET_IP
```

> Execute this after snmpwalk to get parsed results. It attempts connection and enumerates key areas. Expected output: Sections like [*] System information with hostname, description, contact, location, and uptime. Look for sensitive data like user lists or open ports. If connection fails, verify community and version.

### Step 4: Query Specific OIDs if Needed

**Context**: For focused enumeration, query individual OIDs instead of full walks to avoid noise or detection. Common OIDs include 1.3.6.1.2.1.1.1.0 for system description or 1.3.6.1.2.1.25.4.2.1 for running processes.

**Command** ([[commands/snmpwalk-enumerate-server]]):

```bash
snmpwalk -c $_COMMUNITY_STRING -v $_VERSION $_TARGET_IP $_OID
```

> Append the OID to the snmpwalk command (e.g., 1.3.6.1.2.1.1.5.0 for sysName). Refer to oid-info.com for OID lists. Expected output: Specific value for that OID, e.g., SNMPv2-MIB::sysName.0 = STRING: target-host. This is efficient for verifying known info without full exposure.
