---
id: 290eaa08-23d9-496d-ae5e-742a886f3952
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:29.208534+00:00'
updated_at: '2023-04-10T20:37:32.224175+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credentials in Files|T1081 - Credentials in Files]]'
sub_techniques: []
tags:
  - '[[tags/EoP - Looting for passwords]]'
  - '[[tags/Sticky Notes passwords]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/powershell-locate-sticky-notes-db]]'
  - '[[commands/sqlite3-query-sticky-notes]]'
platforms:
  - Windows
tools: []
validated: true
---

# windows-sticky-notes-password-extraction

## Summary

This procedure extracts sensitive information, such as passwords stored in plaintext, from the Windows Sticky Notes application's SQLite database. Sticky Notes is a built-in app where users often save quick notes, including credentials, which are persisted unencrypted in a local database file accessible to any user with file system access.

## Description

The modern Windows Sticky Notes app (UWP version) stores user notes in an SQLite database file located at %LOCALAPPDATA%\Packages\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\LocalState\plum.sqlite. The database contains a 'notes' table with columns including 'content' that holds the plaintext text of each note, along with timestamps. This technique is useful during post-exploitation or privilege escalation phases to loot for credentials left by users. It targets environments where users habitually store passwords or API keys in notes for convenience. Success depends on the target user having created such notes, and the procedure assumes local access to the file system. Potential outcomes include obtaining valid credentials for lateral movement or further escalation.

## Requirements

1. Local access to the target Windows system (user-level privileges on the affected account's profile).
2. SQLite query tool installed (e.g., sqlite3.exe or DB Browser for SQLite).
3. Knowledge of the target user's profile path (e.g., via whoami or environment variables).

## Defense

- Educate users on secure password management and discourage storing credentials in applications like Sticky Notes.
- Implement application whitelisting or restrict write access to AppData folders using group policies.
- Enable endpoint detection and response (EDR) tools to monitor anomalous file access in user profile directories, particularly SQLite queries or database reads.
- Regularly audit and clear Sticky Notes data via enterprise management tools.

## Objectives

1. Locate the Sticky Notes SQLite database file on the target system.
2. Query the database to extract note contents containing potential credentials.
3. Identify and validate any sensitive information for use in further attacks.

## Instructions

### Step 1: Locate the Sticky Notes Database

**Context**: Determine the exact path to the plum.sqlite file, which varies by user profile. This step uses PowerShell to construct and output the full path without needing manual navigation.

**Command** ([[commands/powershell-locate-sticky-notes-db]]):
```powershell
$dbPath = "$env:LOCALAPPDATA\Packages\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\LocalState\plum.sqlite"; Write-Output $dbPath
```

> This command retrieves the environment variable for the local app data directory and appends the Sticky Notes package path. Run it in PowerShell to get the full file path. If the file does not exist, the user may not have the app installed or has no notes.

### Step 2: Query the Database for Notes

**Context**: Once the database is located, use an SQLite client to read the contents of the 'notes' table. This reveals all stored notes in plaintext, allowing identification of any containing passwords or credentials. If sqlite3 is not installed, download it or use a GUI like DB Browser for SQLite.

**Command** ([[commands/sqlite3-query-sticky-notes]]):
```cmd
sqlite3 "$dbPath" "SELECT id, content FROM notes;"
```

> Replace $dbPath with the output from Step 1. This queries the 'notes' table for note IDs and content. Look for strings matching password patterns (e.g., 'password:', 'key:', or base64-like strings). If the table structure differs, use ".schema" first to inspect. Success is indicated by output showing note texts; empty results mean no notes or irrelevant content.

### Step 3: Analyze Extracted Content

**Context**: Review the query output for sensitive data. This manual step involves scanning for credentials and testing them if found (e.g., via login attempts elsewhere on the system).

> No specific command is needed here, but pipe the sqlite3 output to a file for easier review: `sqlite3 "$dbPath" "SELECT content FROM notes;" > notes.txt`. Search the file for keywords like 'pass', 'cred', or 'token'. If credentials are found, validate by attempting use in related services.
