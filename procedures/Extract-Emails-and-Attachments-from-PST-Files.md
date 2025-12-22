---
id: e4bb54e5-aa4b-4f17-9ad2-139b56145e1c
name: Extract-Emails-and-Attachments-from-PST-Files
type: procedure
verified: true
submitted: false
created_at: '2019-12-13T22:39:54.291817+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Data from Local System]]'
sub_techniques: []
tags:
  - data-exposure
  - extract
  - collection
commands:
  - '[[commands/readpst-extract-pst-contents]]'
platforms:
  - Windows
tools:
  - '[[tools/libpst-utils]]'
skill_level: beginner
impact_level: medium
detection_risk: low
validated: true
---

# Extract-Emails-and-Attachments-from-PST-Files

## Summary

This procedure outlines how to extract emails and attachments from Microsoft Outlook Personal Storage Table (PST) files using the readpst tool from the libpst-utils package. PST files are commonly used to archive emails, calendars, and attachments in Outlook and can contain sensitive user data, making them a valuable target for data collection during post-exploitation activities on Windows systems.

## Description

PST files serve as local storage for Outlook data, including emails, contacts, and attachments from versions like Outlook 2010, 2007, 2003, and 2002. In a compromised environment, attackers can locate these files (often in user profiles like %USERPROFILE%\Documents\Outlook Files) and transfer them to a controlled system for extraction. The readpst utility parses the proprietary PST format, outputting emails in mbox format for easy review and saving attachments to separate directories. This technique is useful for collecting credentials, intellectual property, or communication logs without needing Outlook installed, as it runs on Linux systems like Kali. The process assumes the PST file has been exfiltrated or is accessible on the attacker's machine.

## Requirements

1. A PST file obtained from the target Windows system (e.g., via file share, RDP, or exfiltration tools like [[commands/crackmapexec-smb-share-list]]).
2. Linux environment (e.g., Kali Linux) with administrative privileges for package installation.
3. libpst-utils package installed, which provides the readpst tool.
4. Sufficient disk space for output files, as large PSTs can generate gigabytes of extracted data.

## Defense

Defensive measures and detection strategies:

- Enable BitLocker or full-disk encryption on Windows systems to protect PST files at rest.
- Implement Data Loss Prevention (DLP) tools to monitor and block exfiltration of PST files over network shares or email.
- Use endpoint detection and response (EDR) solutions to alert on unusual file access patterns in user directories, such as bulk reads of Outlook data.
- Regularly audit and archive PST files to servers with strict access controls, reducing local storage of sensitive data.

## Objectives

1. Parse the PST file to recover individual emails and metadata.
2. Extract attachments for further analysis or malware hunting.
3. Collect sensitive information embedded in email content, such as passwords or API keys.
4. Output data in readable formats (mbox for emails, directories for attachments) for offline review.

## Instructions

### Step 1: Install libpst-utils

**Context**: The readpst tool is part of the libpst-utils package, which must be installed on a Debian-based Linux system like Kali or Ubuntu to parse PST files. This step ensures the necessary binaries are available without relying on Windows-specific tools like Outlook.

Install the package using the following command:

```bash
apt update && apt install libpst-utils -y
```

> This updates the package list and installs libpst-utils, including readpst. Verify installation by running `readpst --version`, which should output the tool version (e.g., libpst 0.6.XX).

### Step 2: Extract Emails and Attachments

**Context**: With the tool installed, use readpst to process the PST file. The -t flag outputs emails as text files, -e separates them into individual files, -a extracts attachments to a directory, and -m generates an mbox file for email import into tools like Thunderbird. This step accomplishes the core objective of breaking down the monolithic PST into accessible components, allowing manual review or automated parsing of contents for sensitive data.

**Command** ([[commands/readpst-extract-pst-contents]]):

```bash
readpst -tea -m $_FILENAME.pst
```

> Replace $_FILENAME with the path to your PST file (e.g., backup.pst). The command will create an output directory named after the PST file, containing mbox files for emails and subfolders for attachments. Processing may take time for large files (>1GB), and progress is shown via folder-by-folder updates. If the PST is password-protected, readpst may fail—consider using tools like [[tools/pst-password-remover]] for recovery.

### Step 3: Review Extracted Data

**Context**: After extraction, inspect the output to identify valuable intelligence. Emails in mbox format can be opened in email clients, while attachments (e.g., PDFs, docs) should be scanned for malware or analyzed for credentials.

Navigate to the output directory:

```bash
ls -la $_FILENAME/
```

> Expected contents include files like `000001`, `000002` (individual emails), an `mbox` file, and an `attachments` folder. Use tools like `grep` for keyword searches (e.g., `grep -r "password" $_FILENAME/`) to quickly find sensitive info. Success is confirmed if emails are readable and attachments are intact without corruption.
