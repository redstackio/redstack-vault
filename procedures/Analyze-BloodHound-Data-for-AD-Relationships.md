---
id: 43dd85fc-31bc-4249-ab9b-373e2bd8d9df
name: Analyze-BloodHound-Data-for-AD-Relationships
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
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/BloodHound]]'
validated: true
---

# Analyze-BloodHound-Data-for-AD-Relationships

## Summary

This procedure imports SharpHound-collected data into BloodHound to query and visualize AD relationships, identifying attack paths like paths to Domain Admin via permission abuses.

## Description

BloodHound graphs AD objects and edges (e.g., GenericAll, WriteDACL), using Neo4j for queries. Pre-built analytics highlight shortest paths and common attacks, aiding in planning privilege escalation.

## Requirements

- BloodHound GUI installed and Neo4j running
- SharpHound ZIP file
- Basic graph query knowledge

## Defense

- Reduce excessive permissions in AD
- Use BloodHound yourself for audits
- Monitor for data exfiltration of AD dumps

## Objectives

1. Import and validate data
2. Run queries for attack paths
3. Identify exploitable relationships

## Instructions

### Step 1: Import Data

**Context**: Load JSON files into BloodHound database.

No command; in BloodHound UI, click 'Import Data' and select ZIP.

### Step 2: Execute Pre-Built Queries

**Context**: Use analytics to find paths to high-value targets.

No command; expand Queries menu, select 'Shortest Paths to Domain Admins', run on a starting user.

> Right-click edges for 'Abuse Info' with tool suggestions like PowerView.

### Step 3: Review and Document Paths

**Context**: Note suggested abuses (e.g., AddMembers via GenericAll).

No command; screenshot or export graphs.

**Expected Output**: Visual graphs showing paths, e.g., User -> GenericWrite -> Group -> DA.

## Expected Output

Query results: 3 paths found, with abuse details for each edge.
