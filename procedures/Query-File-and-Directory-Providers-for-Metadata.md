---
tags:
  - android
  - content-provider
  - file-discovery
type: procedure
tools:
  - '[[tools/Android-Debug-Bridge]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/query-content-provider-files]]'
  - '[[commands/query-content-provider-directory]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[T1420]]'
updated_at: '2025-12-14T17:24:40.086Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 87d66738-802c-411c-b123-bc95fbf0178e
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1420]]'
---
# Query-File-and-Directory-Providers-for-Metadata

## Summary

This procedure queries the exported 'content://org.nextcloud/file' and 'content://org.nextcloud/dir/[dir ID]' Content Providers to leak names and metadata of synced Nextcloud files and folders.

## Description

Additional exported providers in the Nextcloud app store synced metadata without access controls, revealing file names that may contain sensitive information (e.g., personal documents). Directory queries require a dir ID from file listings or app inspection.

## Requirements

1. ADB shell access
2. Synced files/folders in Nextcloud app
3. Dir ID obtained from initial file query

## Defense

Defensive measures and detection strategies:

- Restrict provider exports in app updates
- Avoid syncing sensitive files to mobile
- Audit app permissions and local storage

## Objectives

1. Enumerate synced file names
2. Map directory structure
3. Identify potential sensitive data leaks

## Instructions

### Step 1: Query Files Provider

**Context**: Retrieve file metadata.

**Command** ([[commands/query-content-provider-files]]):
```bash
content query --uri content://org.nextcloud/file
```

> Lists file entries; note dir IDs for next step. Expected output: File names, paths, sizes.

### Step 2: Query Directory Provider

**Context**: Drill into folder contents using ID.

**Command** ([[commands/query-content-provider-directory]]):
```bash
content query --uri content://org.nextcloud/dir/[dir ID]
```

> Replace [dir ID] with numeric ID (e.g., 123). Expected output: Subfolder listings.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[T1420]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/query-content-provider-files]]
- [[commands/query-content-provider-directory]]

## Tools Used

- [[tools/Android-Debug-Bridge]]

## Tags

- [[file-discovery]]
- [[directory-enumeration]]
