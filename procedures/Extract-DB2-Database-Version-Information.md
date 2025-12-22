---
id: 05ecd9dd-531d-4177-9465-76cbc9a9aa9a
name: Extract-DB2-Database-Version-Information
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:32.544071+00:00'
updated_at: '2023-04-10T20:21:57.257452+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System-Information-Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/DB2-Cheatsheet]]'
  - '[[tags/DB2-Injection]]'
  - '[[tags/Version]]'
  - db2
  - enumeration
  - reconnaissance
commands:
  - '[[commands/db2-select-versionnumber-and-timestamp]]'
  - '[[commands/db2-select-service-level-from-env-get-inst-info]]'
  - '[[commands/db2-select-getvariable-sysibm-version]]'
  - '[[commands/db2-select-prod-release-and-installed-prod-fullname]]'
  - '[[commands/db2-select-service-level-and-bld-level-from-env-inst-info]]'
platforms:
  - Database
  - DB2
tools: []
validated: true
---

# Extract-DB2-Database-Version-Information

## Summary

This procedure extracts version information from an IBM DB2 database using targeted SQL queries against system tables and functions. It reveals the database version number, service level, build details, and product information, which can help identify potential vulnerabilities or misconfigurations in the target database.

## Description

In offensive security operations, extracting version details from a DB2 database is a key reconnaissance step to assess the target's attack surface. With valid access to the database (e.g., via SQL injection, stolen credentials, or direct connection), attackers execute specific queries to query system catalogs like SYSIBM.SYSVERSIONS and administrative functions such as SYSPROC.ENV_GET_INST_INFO(). This information allows attackers to cross-reference known exploits, such as those in older DB2 versions vulnerable to buffer overflows or privilege escalations. The procedure assumes a connected DB2 session and focuses on non-privileged queries that typically succeed with basic read access. Expected outcomes include precise version strings that can be used to search vulnerability databases like CVE or IBM's security bulletins.

## Requirements

1. Valid access to the DB2 database instance (e.g., via db2 command-line tool, JDBC connection, or SQL injection vector).
2. Basic knowledge of SQL syntax and DB2-specific system tables/functions.
3. A SQL client or tool capable of executing queries against DB2 (e.g., db2 CLI, DBeaver, or integrated into a web app exploit).
4. Network connectivity to the DB2 server port (default 50000).

## Defense

- Apply the latest DB2 security patches and fix packs to obscure or protect version details.
- Implement least-privilege access controls, restricting queries to system tables (e.g., via roles and grants on SYSIBM schemas).
- Enable database auditing and logging for SELECT statements on administrative views; monitor for anomalous queries targeting version-related functions.
- Use web application firewalls (WAFs) to block SQL injection attempts that could deliver these queries.

## Objectives

1. Retrieve the core database version number and release timestamp to identify the base version.
2. Gather service level, build level, and product details to pinpoint exact patch status and potential CVEs.
3. Compile version data for vulnerability assessment and planning further exploitation.

## Instructions

### Step 1: Retrieve Database Version Number and Timestamp

**Context**: This step queries the SYSIBM.SYSVERSIONS table to obtain the primary version identifier and the timestamp of the version build, providing foundational details about the DB2 installation.

**Command** ([[commands/db2-select-versionnumber-and-timestamp]]):
```sql
select versionnumber, version_timestamp from sysibm.sysversions;
```

> This query targets the system catalog for version metadata. It requires read access to SYSIBM schema and executes quickly on most DB2 instances.

### Step 2: Retrieve Database Service Level

**Context**: Use the SYSPROC.ENV_GET_INST_INFO() table function to fetch the service level of the database instance, which indicates applied fix packs or updates.

**Command** ([[commands/db2-select-service-level-from-env-get-inst-info]]):
```sql
select service_level from table(sysproc.env_get_inst_info()) as instanceinfo;
```

> The table function returns instance-specific details; aliasing as 'instanceinfo' simplifies output parsing. Success confirms instance-level access.

### Step 3: Retrieve Database Product Version (v8+)

**Context**: For DB2 versions 8 and later, this retrieves the product version via the GETVARIABLE function, offering a concise version string.

**Command** ([[commands/db2-select-getvariable-sysibm-version]]):
```sql
select getvariable('sysibm.version') from sysibm.sysdummy1;
```

> SYSIBM.SYSDUMMY1 acts as a dummy table for scalar functions like GETVARIABLE. The comment '(v8+)' notes compatibility; test on older versions if needed.

### Step 4: Retrieve Installed Product Information

**Context**: Query the SYSPROC.ENV_GET_PROD_INFO() function to get the product release and full name of installed DB2 components, revealing editions like Express or Enterprise.

**Command** ([[commands/db2-select-prod-release-and-installed-prod-fullname]]):
```sql
select prod_release, installed_prod_fullname from table(sysproc.env_get_prod_info()) as productinfo;
```

> This provides broader product context, useful for identifying feature-specific vulnerabilities.

### Step 5: Retrieve Database and Instance Service and Build Level

**Context**: Access the SYSIBMADM.ENV_INST_INFO view for service level and build level, combining instance and database specifics for a complete picture.

**Command** ([[commands/db2-select-service-level-and-bld-level-from-env-inst-info]]):
```sql
select service_level, bld_level from sysibmadm.env_inst_info;
```

> SYSIBMADM views require administrative read access in some configurations; if denied, fall back to prior steps.
