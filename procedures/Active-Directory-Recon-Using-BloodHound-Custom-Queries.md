---
id: 5cb45f41-6083-415a-95ed-25dc70f57e71-rewritten
name: Active-Directory-Recon-Using-BloodHound-Custom-Queries
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Remote System Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Active Directory Recon]]'
  - '[[tags/Using BloodHound]]'
commands:
  - '[[commands/view-bloodhound-customqueries-linux]]'
  - '[[commands/view-bloodhound-customqueries-windows]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/BloodHound]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Active-Directory-Recon-Using-BloodHound-Custom-Queries

## Summary

This procedure uses BloodHound to perform reconnaissance on an Active Directory environment by creating and executing custom Cypher queries. It enables attackers to identify high-value targets such as privileged users, groups, and potential attack paths by visualizing relationships between domain objects, focusing on techniques like querying for users in specific groups using OR operators.

## Description

BloodHound is an identity attack path auditing tool that maps Active Directory relationships using graph theory. In this procedure, custom queries are added to BloodHound's configuration to discover remote systems, users, and groups that could facilitate lateral movement or privilege escalation. This is particularly useful after initial access to a domain-joined system, where an attacker ingests AD data into BloodHound and runs queries to reveal hidden paths to domain admins. The technique leverages BloodHound's GUI for query execution but involves editing the customqueries.json file for persistence and customization. Expected outcomes include a graph visualization highlighting exploitable paths, such as users with delegated rights or weak ACLs. This maps to discovery tactics in environments with domain controllers and LDAP access.

## Requirements

1. Domain credentials with read access to Active Directory (e.g., LDAP query permissions).
2. BloodHound tool installed and SharpHound or AzureHound ingestor executed to collect AD data.
3. Access to the attacker's workstation with BloodHound GUI (Neo4j database running).
4. File system access to edit BloodHound's configuration directory.

## Defense

Defensive measures and detection strategies:

- Implement BloodHound countermeasures like restricting LDAP queries via Group Policy or monitoring for unusual enumeration (Event ID 4662).
- Use tools like Microsoft ATA or Splunk to detect graph database ingestions and custom query patterns.
- Limit service account privileges and audit custom BloodHound installations on endpoints.

## Objectives

1. Identify privileged users and groups in the Active Directory domain.
2. Visualize potential lateral movement paths using custom Cypher queries.
3. Discover high-value targets for further exploitation, such as domain admins or sensitive hosts.

## Instructions

### Step 1: Locate and View the Custom Queries File

**Context**: Before adding custom queries, locate BloodHound's customqueries.json file, which stores user-defined Cypher queries. Use platform-specific commands to view its current content and verify the path.

On Linux, execute [[commands/view-bloodhound-customqueries-linux]]:

```bash
cat ~/.config/bloodhound/customqueries.json
```

> This displays the JSON structure containing query definitions. If the file is empty or missing, it will show an error or empty output, indicating a need to create it.

On Windows, execute [[commands/view-bloodhound-customqueries-windows]] (using PowerShell):

```powershell
Get-Content $env:APPDATA\BloodHound\customqueries.json
```

> This outputs the file contents. Success is confirmed by seeing a valid JSON array with query objects, each having 'name', 'author', and 'query' fields.

**Expected Output**: A JSON array like: `[{ "name": "Example Query", "query": "MATCH (n) RETURN n" }]`.

### Step 2: Edit the Custom Queries File to Add a New Query

**Context**: Manually edit the customqueries.json file to insert a custom Cypher query. This allows persistent custom searches without relying solely on the GUI. Use a text editor like nano (Linux) or Notepad++ (Windows) after backing up the original file.

1. Backup the existing file: On Linux, `cp ~/.config/bloodhound/customqueries.json ~/.config/bloodhound/customqueries.json.bak`; on Windows, `Copy-Item $env:APPDATA\BloodHound\customqueries.json $env:APPDATA\BloodHound\customqueries.json.bak`.
2. Open the file in an editor and add a new query object to the array. For example, to find users in Domain Admins or Enterprise Admins using OR:

```json
{
  "name": "High-Value Users OR Query",
  "author": "Attacker",
  "query": "MATCH (u:User) WHERE u.memberof contains 'Domain Admins' OR u.memberof contains 'Enterprise Admins' RETURN u"
}
```

3. Save the file and re-view it using the commands from Step 1 to confirm changes.

**Expected Output**: Updated JSON with the new query object visible upon re-viewing.

### Step 3: Load Data and Execute the Custom Query in BloodHound GUI

**Context**: With the custom query added, ingest AD data if not already done, then run the query to visualize results. This step reveals relationships for attack planning.

1. Launch BloodHound and ensure the Neo4j database is running (default: http://localhost:7687).
2. If needed, ingest data using SharpHound: Download from GitHub, run `SharpHound.exe -c All`, and import the JSON.zip into BloodHound.
3. In the BloodHound interface, navigate to the 'Queries' tab, select 'Custom Queries', and choose the newly added query (e.g., 'High-Value Users OR Query').
4. Click 'Run Query' and review the resulting graph, which highlights users and their group memberships.
5. Export paths or screenshots for analysis.

**Expected Output**: A graph showing nodes for users in the specified groups, with edges representing memberships. Success if high-value targets like domain admins are identified.

### Step 4: Validate and Plan Next Actions

**Context**: Verify the query's effectiveness and use insights for further recon or attacks.

1. Check for common paths: Re-run the query and look for shortest paths to Domain Admins using BloodHound's built-in analysis.
2. If no results, refine the query (e.g., adjust group names) and repeat Step 2.
3. Document findings, such as user SIDs or computer objects, for procedures like Kerberoasting.

**Expected Output**: List of discovered entities, e.g., user objects with admin privileges.
