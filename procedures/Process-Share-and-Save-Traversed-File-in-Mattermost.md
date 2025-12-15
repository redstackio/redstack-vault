---
id: proc-uuid-3
tags:
  - path-traversal
  - file-overwrite
  - android
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hijack Execution Flow]]'
updated_at: '2025-12-14T17:24:45.203Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Hijack Execution Flow]]'
---
# Process-Share-and-Save-Traversed-File-in-Mattermost

## Summary

This procedure details how the Mattermost app processes the malicious share intent, querying the content provider and using the unsanitized DISPLAY_NAME to create a file with traversal path in its cache directory, effectively overwriting native libraries like libyoga.so.

## Description

In RealPathUtil.getPathFromSavingTempFile, Mattermost retrieves the cursor from the provider query, extracts DISPLAY_NAME (e.g., "../../lib-main/libyoga.so"), and constructs a new File(cacheDir, displayName) without path normalization or validation. It then copies the input stream from openFile() into this file. The traversal resolves relative to cacheDir, allowing access to parent directories like /lib-main/. Prerequisites: Intent received. Expected outcome: Malicious content copied to app's lib directory.

## Requirements

1. Vulnerable Mattermost version installed
2. Malicious intent processed
3. File system write permissions in app sandbox

## Defense

Defensive measures and detection strategies:

- Sanitize filenames with path canonicalization (e.g., File.getCanonicalPath())
- Restrict file saves to safe directories
- Audit file operations in logcat

## Objectives

1. Exploit lack of filename validation
2. Overwrite critical app files
3. Prepare for code execution

## Instructions

### Step 1: Query Content Provider

**Context**: Mattermost calls query() on the URI.

Internal app flow: Cursor cursor = getContentResolver().query(uri, null, null, null, null);

> Returns MatrixCursor with traversed DISPLAY_NAME.

### Step 2: Extract and Use Filename

**Context**: Retrieve and apply DISPLAY_NAME without checks.

In RealPathUtil:

```java
String displayName = cursor.getString(cursor.getColumnIndex("_display_name"));
File tempFile = new File(cacheDir, displayName);
```

> Creates file with traversal, e.g., /data/data/com.mattermost.rn/cache/../../lib-main/libyoga.so.

### Step 3: Copy Malicious Content

**Context**: Stream the payload to the target file.

Use InputStream from provider.openFile(uri) to copy to tempFile.outputStream().

> Overwrites libyoga.so with malicious .so content.

### Step 4: Verify Overwrite

**Context**: Check file integrity post-copy.

Via ADB:

```bash
adb shell ls -l /data/data/com.mattermost.rn/lib-main/libyoga.so
```

> Expected: File size matches malicious payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Hijack Execution Flow]] Hijack Execution Flow

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- path-traversal
- file-overwrite
- android
