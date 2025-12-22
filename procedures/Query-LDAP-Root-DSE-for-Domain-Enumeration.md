---
id: f1e7dffb-48e4-4fad-b3a8-ac49380a527b
type: procedure
verified: true
submitted: true
created_at: '2020-03-17T22:31:20.816208+00:00'
updated_at: '2023-05-25T20:00:20.591866+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[System Information Discovery]]'
sub_techniques: []
tags:
  - active-directory
  - enumeration
  - ldap
commands:
  - '[[commands/nmap-ldap-rootdse-query]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/Nmap]]'
validated: true
---

# Query-LDAP-Root-DSE-for-Domain-Enumeration

## Summary

This procedure connects to an LDAP server and queries the Root DSE (Directory System Agent Specific Entry) to enumerate essential directory service information, such as supported LDAP versions, naming contexts (e.g., domain components), and schema locations. It is a foundational step in Active Directory enumeration, providing insights into the domain structure without requiring authentication in many configurations.

## Description

The Root DSE is an LDAP object that exposes metadata about the directory server, including its capabilities and configuration. In Active Directory environments, this includes details like the default naming context (e.g., dc=example,dc=com), supported controls, and extensions. This technique is low-risk and non-intrusive, often succeeding via anonymous binds, and serves as a starting point for deeper reconnaissance such as user enumeration or trust discovery. It is particularly useful in red team engagements targeting Windows domain controllers over port 389 (LDAP) or 636 (LDAPS), helping attackers map the environment for subsequent lateral movement or privilege escalation.

## Requirements

1. Network connectivity to the target LDAP server (typically port 389 open and accessible).
2. Nmap installed on the attacking machine (version 7.0 or later with NSE scripts enabled).
3. Knowledge of the target's IP address or resolvable hostname.
4. No credentials needed for anonymous Root DSE queries, but firewall rules must allow inbound LDAP traffic.

## Defense

- Disable anonymous binds on LDAP servers by configuring 'dsHeuristics' in AD to require authentication.
- Implement network segmentation to restrict LDAP port access to trusted internal networks only.
- Enable LDAP query auditing via Windows Event Logs (Event ID 2886-2889) and monitor for anomalous Root DSE queries.
- Use intrusion detection systems (IDS) to flag unauthenticated LDAP traffic from external sources.

## Objectives

1. Gather server capabilities to confirm LDAP service presence and version.
2. Extract naming contexts to identify domain and forest structure.
3. Collect schema and extension details for planning advanced enumeration techniques.

## Instructions

### Step 1: Perform LDAP Root DSE Query with Nmap

**Context**: Launch an Nmap scan targeting port 389 on the LDAP server using the built-in ldap-rootdse script. This performs an anonymous LDAP search for the Root DSE object, retrieving key attributes without authentication. The step verifies the service is responsive and extracts domain-related information from the namingContexts attribute, which reveals the base DN for further queries.

**Command** ([[commands/nmap-ldap-rootdse-query]]):

```bash
nmap -script ldap-rootdse -p 389 $_TARGET_IP
```

> Run this command from a Kali Linux or similar environment. Replace $_TARGET_IP with the actual IP (e.g., 10.10.10.10). The script will output LDAP results if successful, including supportedLDAPVersion (typically 3 for AD), namingContexts (e.g., dc=corporatehq,dc=com indicating the domain), and other details like subschemaSubentry. If the port is filtered or anonymous access is denied, Nmap will report no results—consider pivoting to authenticated queries or alternative ports.

### Step 2: Analyze and Verify Output

**Context**: Review the Nmap output to confirm successful enumeration and note key findings. This step ensures the data is actionable; for example, use the namingContexts DN as input for subsequent LDAP searches (e.g., via ldapsearch tool). If no output appears, check for LDAPS on port 636 by modifying the command to -p 636 and adding --script-args ldap.rootdse.ldaps=1.

**Command** ([[commands/nmap-ldap-rootdse-query]]):

```bash
nmap -script ldap-rootdse -p 636 --script-args ldap.rootdse.ldaps=1 $_TARGET_IP
```

> Parse the output manually or pipe to a file (e.g., nmap ... > ldap_info.txt). Look for indicators like supportedExtension values, which may reveal advanced features. Success is confirmed if namingContexts is populated; otherwise, investigate firewall or bind restrictions.
