---
tags:
  - arbitrary-file-read
  - symlink
  - discourse
  - backup-restore
  - local-file-read
type: attack_chain
tools: []
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Discourse-Admin-Interface]]'
  - '[[procedures/Create-and-Download-Discourse-Backup]]'
  - '[[procedures/Modify-Backup-with-Symlink]]'
  - '[[procedures/Upload-and-Restore-Modified-Backup]]'
  - '[[procedures/Access-Symlinked-File-for-Read]]'
step_count: 12
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:30:18.628Z'
description: >-
  Exploits a vulnerability in Discourse's backup restore feature by embedding
  symlinks in uploaded tar backups to read arbitrary local files accessible by
  the server process.
skill_level: intermediate
impact_level: high
id: 488ba687-3031-40b0-b930-5fccf14db59f
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Arbitrary Local File Read in Discourse via Symlink in Backup Restore

Multi-stage attack chain demonstrating exploitation of Discourse's backup restore feature to achieve arbitrary local file read using symlinks in tar archives.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 12 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Admin Access] --> B[Backup Creation]
    B --> C[Symlink Modification]
    C --> D[Restore Backup]
    D --> E[File Access and Read]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser for admin interface interaction
- Local machine with tar and ln utilities (Linux/Unix-like)

### Target Environment

- Discourse instance running on Ruby on Rails
- Admin access to the Discourse site
- Server process permissions allowing read access to target files (e.g., /etc/passwd)
- Backup restore feature enabled in site settings

### Initial Access Requirements

- Valid admin credentials for the target Discourse site
- Direct network access to the web interface (typically port 80/443)
- Local environment for backup modification

## Detailed Attack Procedures

### Step 1: Load the Target Discourse Instance
procedure: [[procedures/Access-Discourse-Admin-Interface]]

**Objective**: Gain initial access to the Discourse site to begin the admin workflow.

**Instructions**: Open a web browser and navigate to the main URL of the target Discourse instance.

**Expected Output**: The homepage of the Discourse forum loads successfully.

**Success Indicators**:
- Site homepage accessible without errors
- No authentication barriers at this stage

### Step 2: Login as an Admin User
procedure: [[procedures/Access-Discourse-Admin-Interface]]

**Objective**: Authenticate with admin privileges to access restricted features.

**Instructions**: Enter admin credentials in the login form and submit.

**Expected Output**: Successful login redirects to the user dashboard with admin indicators (e.g., admin badge).

**Success Indicators**:
- Admin menu visible in the interface
- Access to /admin/ endpoints granted

### Step 3: Navigate to the Backups Page
procedure: [[procedures/Access-Discourse-Admin-Interface]]

**Objective**: Reach the admin backups management interface.

**Instructions**: From the admin dashboard, click on the backups section or visit /admin/backups/ directly.

**Expected Output**: Backups page loads, showing options to create or restore backups.

**Success Indicators**:
- Backups interface visible
- Options for backup creation present

### Step 4: Create a New Backup Including Files
procedure: [[procedures/Create-and-Download-Discourse-Backup]]

**Objective**: Generate a legitimate backup archive containing database and upload files for modification.

**Instructions**: In the backups page, select to create a new backup including files from /public/uploads/* and initiate the process.

**Expected Output**: Backup generation completes, and a downloadable tar.gz file is available.

**Success Indicators**:
- Backup file ready for download
- File includes uploads directory structure

### Step 5: Extract the Backup Files to a Local Folder
procedure: [[procedures/Create-and-Download-Discourse-Backup]]

**Objective**: Unpack the backup to prepare for symlink insertion.

**Instructions**: Download the tar.gz file and extract it locally using tar -xzf backup.tar.gz.

**Expected Output**: Extracted directory structure including /uploads/ folder.

**Success Indicators**:
- Files and folders from backup accessible locally
- Uploads subdirectory present

### Step 6: Create a Symlink to /etc/passwd in the /uploads/ Folder
procedure: [[procedures/Modify-Backup-with-Symlink]]

**Objective**: Embed a symlink pointing to a sensitive file within the backup's uploads structure.

**Instructions**: Navigate to the extracted /uploads/default/original/1X/ directory and execute [[commands/create-symlink-to-sensitive-file]] to create the symlink.

```bash
ln -s /etc/passwd /home/symlink/files/uploads/default/original/1X/7ad2e8f5fe02890f20503044b604e29e6f3718fd.png
```

**Expected Output**: Symlink created without errors, verifiable with ls -l showing the link to /etc/passwd.

**Success Indicators**:
- Symlink file exists and points to target
- Masquerades as an image file (e.g., .png)

### Step 7: Create a .tar.gz from the Extracted Files
procedure: [[procedures/Modify-Backup-with-Symlink]]

**Objective**: Repackage the modified contents into a new backup archive.

**Instructions**: From the root of the extracted backup, run tar -czf modified-backup.tar.gz . to compress the directory.

**Expected Output**: New tar.gz archive containing the symlink.

**Success Indicators**:
- Archive created successfully
- Size similar to original backup

### Step 8: Upload the Newly Crafted Tar to the Server
procedure: [[procedures/Upload-and-Restore-Modified-Backup]]

**Objective**: Upload the tampered backup to the Discourse server.

**Instructions**: In the admin backups page, use the upload option to select and upload the modified tar.gz file.

**Expected Output**: File uploads and appears in the backups list.

**Success Indicators**:
- Upload completes without validation errors
- Backup listed as available

### Step 9: Enable 'Restore from Backups' in Settings if Not Already Enabled
procedure: [[procedures/Upload-and-Restore-Modified-Backup]]

**Objective**: Ensure the restore functionality is permitted.

**Instructions**: Navigate to site settings in admin panel and toggle the 'allow restore' option if disabled.

**Expected Output**: Setting enabled, no errors.

**Success Indicators**:
- Restore button active on backups page

### Step 10: Restore from the Uploaded Backup
procedure: [[procedures/Upload-and-Restore-Modified-Backup]]

**Objective**: Trigger the extraction of the backup, resolving the symlink to place the file in uploads.

**Instructions**: Select the uploaded backup and initiate the restore process.

**Expected Output**: Restore completes, site may briefly go offline then return; symlink resolves during extraction.

**Success Indicators**:
- Restore success message
- No extraction errors reported

### Step 11: Access the Uploaded File via Browser
procedure: [[procedures/Access-Symlinked-File-for-Read]]

**Objective**: Navigate to the symlinked file's URL to trigger the read.

**Instructions**: In the browser, visit the URL corresponding to the symlink, e.g., https://target.com/uploads/default/original/1X/7ad2e8f5fe02890f20503044b604e29e6f3718fd.png.

**Expected Output**: Browser displays the contents of the linked file (/etc/passwd).

**Success Indicators**:
- File contents visible in browser
- No 404 or access denied

### Step 12: Read the Contents of /etc/passwd
procedure: [[procedures/Access-Symlinked-File-for-Read]]

**Objective**: Confirm arbitrary file read by viewing sensitive data.

**Instructions**: Inspect the displayed content to verify it's the target file.

**Expected Output**: User account listings from /etc/passwd shown as text or raw output.

**Success Indicators**:
- Sensitive file contents exfiltrated via web access
- Potential for reading other files by adjusting symlink target

## Attack Chain Summary

### Key Achievements

1. Admin access to create and manipulate backups
2. Successful embedding and resolution of symlink during restore
3. Arbitrary local file read via web-accessible URL, exposing server-readable files

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[File and Directory Discovery]] File and Directory Discovery

### MITRE ATT&CK Tactics

- [[Collection]] Collection

---

*Last updated: 2023-10-01T00:00:00Z*
