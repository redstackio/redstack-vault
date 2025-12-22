---
type: procedure
tactics:
  - '[[Defense Evasion]]'
  - '[[Reconnaissance]]'
techniques:
  - '[[Gather Victim Network Information]]'
  - '[[Network Boundary Bridging]]'
  - '[[Search Open Technical Databases]]'
sub_techniques: []
tags:
  - active-directory-attacks
  - dns-reconnaissance
commands:
  - '[[commands/standin-dns-lookup-with-limit-20]]'
  - '[[commands/standin-dns-lookup-sql-filter-limit-10]]'
  - '[[commands/standin-dns-lookup-forest-with-credentials]]'
  - '[[commands/standin-dns-lookup-legacy-with-credentials]]'
tools:
  - '[[tools/standin]]'
platforms:
  - Windows
skill_level: intermediate
impact_level: medium
detection_risk: high
verified: true
validated: true
---

# DNS Reconnaissance Using StandIn ADIDNS Queries

## Summary

This procedure uses the StandIn tool to perform DNS reconnaissance on an Active Directory environment by querying ADIDNS records. It enables attackers to gather information about network topology, domain controllers, DNS zones, and services, facilitating identification of attack vectors such as DNS cache poisoning or zone transfers. The procedure covers basic, filtered, forest-wide, and legacy authentication queries to enumerate DNS-related objects in the target domain.

## Description

In Active Directory attacks, DNS reconnaissance is essential for mapping the network and identifying exploitable services. StandIn leverages LDAP queries against ADIDNS (Active Directory Integrated DNS) to extract records about DNS servers, zones, and domain infrastructure without direct DNS zone transfers. This technique allows discovery of domain names, controllers, and potential misconfigurations. It is particularly useful in authenticated scenarios where the attacker has domain credentials, providing insights into the forest structure and legacy systems. The procedure assumes access to a Windows environment with PowerShell and the StandIn executable, targeting enterprise networks with Active Directory. Expected outcomes include lists of DNS records that reveal service locations and authentication dependencies, aiding further lateral movement or evasion planning.

## Requirements

1. Authenticated access to the target Active Directory domain (valid username and password).
2. Network connectivity to the domain controller or DNS server (typically ports 389/636 for LDAP, 53 for DNS).
3. StandIn.exe tool downloaded and placed in a local directory.
4. PowerShell execution environment on a Windows host with domain-joined access.

## Defense

- Implement DNSSEC to validate record integrity and prevent spoofing.
- Enable DNS logging and monitor for anomalous LDAP queries to ADIDNS.
- Restrict StandIn-like tools via application whitelisting and endpoint detection.
- Use network segmentation to limit lateral querying from compromised hosts.

## Objectives

1. Enumerate DNS records to map network topology and services.
2. Identify domain controllers, zones, and potential vulnerabilities like legacy authentication.
3. Gather intelligence for targeted attacks such as DNS spoofing or cache poisoning.

## Instructions

### Step 1: Prepare the Environment

**Context**: Download and position the StandIn tool in your working directory to enable execution of ADIDNS queries. This ensures the executable is ready for PowerShell invocation without path issues.

Navigate to the directory containing StandIn.exe using PowerShell:

```powershell
cd C:\path\to\standin
```

> This step verifies tool accessibility. Expected output: PowerShell prompt changes to the tool directory. If the file is missing, download from the official repository.

### Step 2: Perform Basic DNS Lookup with Result Limit

**Context**: Execute a standard ADIDNS query limited to 20 results to quickly enumerate core DNS records without overwhelming output, ideal for initial scoping.

**Command** ([[commands/standin-dns-lookup-with-limit-20]]):
```bash
StandIn.exe --dns --limit 20
```

> This command queries ADIDNS for up to 20 DNS objects using current credentials. It reveals basic topology like domain controllers and zones. Run in PowerShell for Windows compatibility.

### Step 3: Conduct Filtered DNS Lookup

**Context**: Apply a SQL-like filter to narrow results (e.g., for specific keywords like 'SQL'), limited to 10 entries, to focus on relevant services such as database hosts.

**Command** ([[commands/standin-dns-lookup-sql-filter-limit-10]]):
```bash
StandIn.exe --dns --filter SQL --limit 10
```

> The filter targets records containing 'SQL', useful for discovering SQL Server instances via DNS. Expected output: Filtered list of matching ADIDNS entries.

### Step 4: Query Forest-Wide DNS Records with Credentials

**Context**: Expand the search across the entire Active Directory forest using provided credentials to uncover multi-domain DNS infrastructure.

**Command** ([[commands/standin-dns-lookup-forest-with-credentials]]):
```bash
StandIn.exe --dns --forest --domain redhook --user RFludd --pass Cl4vi$Alchemi4e
```

> Authenticates with specified domain user and searches forest-level ADIDNS. Replace placeholders with actual credentials. This step is key for large environments.

### Step 5: Perform Legacy Authentication DNS Lookup

**Context**: Use legacy authentication methods to query DNS records, bypassing modern security controls in older AD setups.

**Command** ([[commands/standin-dns-lookup-legacy-with-credentials]]):
```bash
StandIn.exe --dns --legacy --domain redhook --user RFludd --pass Cl4vi$Alchemi4e
```

> Targets legacy-compatible queries for environments with NTLM or older protocols. Expected output: DNS records from legacy zones, indicating outdated configurations.

### Step 6: Analyze and Verify Results

**Context**: Review outputs from prior steps to identify actionable intelligence, such as exposed services or weak zones.

Parse results manually or pipe to a file:

```powershell
StandIn.exe --dns --limit 20 | Out-File -FilePath dns_results.txt
```

> Cross-reference with known domain structure. Success if records reveal new targets; if empty, check credentials or network access.
