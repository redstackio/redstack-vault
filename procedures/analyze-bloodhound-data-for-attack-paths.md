---
id: 43dd85fc-31bc-4249-ab9b-373e2bd8d9df
name: analyze-bloodhound-data-for-attack-paths
type: procedure
verified: true
submitted: true
created_at: '2020-03-15T02:59:54.711144+00:00'
updated_at: '2023-05-25T19:44:48.675147+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Domain Trust Discovery]]'
  - '[[Permission Groups Discovery]]'
  - '[[System Owner-User Discovery]]'
sub_techniques: []
tags:
  - active-directory
  - enumeration
commands: []
tools:
  - '[[tools/BloodHound]]'
platforms:
  - Linux
  - Windows
skill_level: intermediate
impact_level: low
detection_risk: low
validated: true
---

# analyze-bloodhound-data-for-attack-paths

## Summary

Import SharpHound-collected data into BloodHound and query for relationships to identify privilege escalation paths like WriteDACL abuse.

## Description

BloodHound visualizes AD as a graph, allowing queries for shortest paths to Domain Admins, exploitable ACLs (e.g., GenericAll, WriteDACL), and other misconfigurations.

## Requirements

- BloodHound GUI installed ([[tools/BloodHound]])
- SharpHound ZIP file
- Neo4j database running

## Defense

- Regularly audit AD ACLs
- Remove unnecessary permissions
- Monitor for BloodHound ingestors

## Objectives

1. Visualize AD structure
2. Find attack paths
3. Identify escalation opportunities

## Instructions

### Step 1: Import Data

**Context**: Load ZIP into BloodHound interface.

In GUI: Click "Import Data" and select ZIP.

> Wait for ingestion.

### Step 2: Run Queries

**Context**: Use pre-built analytics for paths.

In GUI: Select "Queries" > "Pre-built Analytics" > "Shortest Paths to Domain Admins from Current User".

> Look for edges with WriteDACL or DCSync rights.

### Step 3: Investigate Relationships

**Context**: Right-click edges for abuse info.

In graph: Right-click > "Help" for tool suggestions like PowerView.

> Note paths for escalation.

## Expected Output

Graph showing paths, e.g., Current User -> WriteDACL on Domain -> Domain Admins.
