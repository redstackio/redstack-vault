---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Remote System Discovery|T1018 - Remote System Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Active Directory Recon]]'
  - '[[tags/Other Interesting Commands]]'
commands:
  - '[[commands/nslookup-domain-resolution]]'
  - '[[commands/nslookup-srv-ldap-domain-controllers]]'
  - '[[commands/nltest-list-domain-controllers]]'
  - '[[commands/get-addomaincontroller-list-all]]'
  - '[[commands/gpresult-display-rsop]]'
  - '[[commands/powershell-get-logonserver]]'
  - '[[commands/cmd-echo-logonserver]]'
platforms:
  - Windows
tools: []
validated: true
---

# Active-Directory-Domain-Controller-Lookup

## Summary

This procedure identifies domain controllers in an Active Directory environment using various built-in Windows tools and commands. It leverages DNS queries, native utilities like nltest and gpresult, and environment variables to enumerate domain controllers, which is essential for reconnaissance, mapping the AD infrastructure, and identifying targets for further attacks such as credential harvesting or lateral movement.

## Description

Domain controllers (DCs) are critical components in Active Directory that handle authentication, policy enforcement, and directory services. Discovering them allows attackers to target high-value systems for privilege escalation or persistence. This procedure covers multiple methods: DNS resolution for IP addresses, SRV record queries for service locations, native Windows tools for listing DCs, and checking the logon server via environment variables or group policy results. These techniques are low-privilege and can be executed from a compromised domain-joined workstation. From a defensive standpoint, monitoring anomalous DNS queries or tool executions can detect early reconnaissance. The procedure assumes access to a domain-joined system or network with DNS resolution to the target domain.

## Requirements

1. Network access to the target domain's DNS servers.
2. Domain-joined Windows system or valid credentials for AD queries.
3. PowerShell Active Directory module installed for certain commands (part of RSAT tools).
4. No elevated privileges required for most methods, but some may need authenticated sessions.

## Defense

- Restrict DNS queries to internal resolvers and monitor for external or anomalous SRV record lookups.
- Implement network segmentation to limit access to DCs from non-administrative systems.
- Enable logging for tools like nltest and gpresult via Windows Event Logs (Security and System channels).
- Use endpoint detection to alert on executions of reconnaissance tools in unusual contexts.

## Objectives

1. Enumerate all domain controllers and their IP addresses in the target AD domain.
2. Identify the specific DC handling the current user's authentication for targeted attacks.
3. Gather infrastructure details to support subsequent AD enumeration or exploitation.
4. Validate success through output showing DC hostnames and IPs.

## Instructions

### Step 1: Resolve Domain IP Addresses via DNS

**Context**: Start with a basic DNS lookup to identify IP addresses associated with the domain, which often include domain controllers. This method uses the standard nslookup tool and requires replacing 'domain.com' with the target domain name. It provides initial host resolution without specific AD knowledge.

**Command** ([[commands/nslookup-domain-resolution]]):
```cmd
nslookup domain.com
```

> This command queries DNS for A records of the domain. Replace 'domain.com' with the actual domain (e.g., contoso.com). It returns IP addresses of servers responding for the domain, typically including DCs.

### Step 2: Query SRV Records for LDAP Services

**Context**: Use SRV records to specifically locate domain controllers providing LDAP services. This targets the _ldap._tcp.dc._msdcs subdomain, which AD registers for DC discovery. It's more precise than basic resolution and reveals service ports and priorities.

**Command** ([[commands/nslookup-srv-ldap-domain-controllers]]):
```cmd
nslookup -type=srv _ldap._tcp.dc._msdcs.domain.com
```

> Replace 'domain.com' with the target domain. The output lists DCs with their hostnames, priorities, weights, ports (389 for LDAP), and IPs. Success is indicated by a list of SRV entries pointing to DC hostnames.

### Step 3: List Domain Controllers Using nltest

**Context**: Employ the nltest utility, a native Windows tool for AD diagnostics, to directly list all DCs in the domain. This requires domain connectivity and provides a clean list of DC names without additional parsing.

**Command** ([[commands/nltest-list-domain-controllers]]):
```cmd
nltest /dclist:domain.com
```

> Replace 'domain.com' with the target. Expected output includes a header like "DC Site Results:" followed by DC names and their sites. If no DCs are listed, check network access or domain name.

### Step 4: Enumerate DCs with PowerShell AD Module

**Context**: For environments with the Active Directory PowerShell module (RSAT), use Get-ADDomainController to query all DCs. This method is scriptable and filters for all objects, selecting names for simplicity. It's useful in automated reconnaissance.

**Command** ([[commands/get-addomaincontroller-list-all]]):
```powershell
Get-ADDomainController -Filter * | Select-Object Name
```

> Run in PowerShell. Output is a table of DC names. If the module is unavailable, install RSAT or use alternative methods. Success shows a list of hostnames like "DC01", "DC02".

### Step 5: Check Group Policy Results for DC Info

**Context**: The gpresult command displays the Resultant Set of Policy (RSoP), which includes the authenticating DC in the output. This indirectly reveals the current logon DC and is stealthy as it mimics legitimate admin tasks.

**Command** ([[commands/gpresult-display-rsop]]):
```cmd
gpresult /r
```

> Output includes sections like "Applied Group Policy Objects" with the site and DC name (e.g., "Default-First-Site-Name\DC01"). Look for the "Computer Site" or policy source lines to identify the DC.

### Step 6: Retrieve Logon Server via PowerShell Environment

**Context**: On a domain-joined system, the LOGONSERVER environment variable holds the DC that authenticated the current session. Query it in PowerShell for quick, local identification without network queries.

**Command** ([[commands/powershell-get-logonserver]]):
```powershell
$Env:LOGONSERVER
```

> This returns the DC name prefixed with "\\" (e.g., "\\DC01"). If empty, the system may not be domain-joined or recently logged on.

### Step 7: Retrieve Logon Server via CMD Environment

**Context**: Similar to PowerShell, use CMD to echo the LOGONSERVER variable. This is a simple, one-liner alternative for non-PowerShell environments.

**Command** ([[commands/cmd-echo-logonserver]]):
```cmd
echo %LOGONSERVER%
```

> Output mirrors PowerShell (e.g., "\\DC01"). Use if PowerShell is restricted or for batch scripting.
