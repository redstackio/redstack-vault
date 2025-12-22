---
id: 9677c26b-e369-43db-8e84-0721ca2f8ddf
name: Recover-Git-Repository-from-Exposed-Dot-Git-Directory
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:59.994368+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
  - >-
    [[techniques/Data from Information Repositories|T1213 - Data from
    Information Repositories]]
sub_techniques: []
tags:
  - git
  - source-code-leak
  - rip-git
  - dvcs-ripper
  - unsecured-credentials
  - web-exposure
commands:
  - '[[commands/git-clone-dvcs-ripper-repo]]'
  - '[[commands/perl-run-rip-git-on-target]]'
  - '[[commands/git-cat-file-show-commit]]'
  - '[[commands/git-ls-tree-show-directory]]'
  - '[[commands/git-rev-parse-parent-commit]]'
  - '[[commands/git-cat-file-show-blob]]'
platforms:
  - Web
  - Linux
tools:
  - '[[tools/DVCS-Ripper]]'
validated: true
---

# Recover-Git-Repository-from-Exposed-Dot-Git-Directory

## Summary

This procedure uses the DVCS-Ripper tool to recover an entire Git repository from a web server where the .git directory is accidentally exposed via HTTP. By ripping the Git objects over the network, attackers can reconstruct the full source code history, potentially revealing hardcoded credentials, API keys, or other sensitive data stored in the repository.

## Description

Many web applications expose their .git directory due to misconfigurations in web servers like Apache or Nginx, allowing unauthenticated access to Git metadata files (e.g., index, objects, refs). The DVCS-Ripper (specifically the rip-git component) automates the download and reconstruction of the Git repository by crawling and fetching all necessary objects from the exposed .git/ path. Once recovered, standard Git commands can be used to inspect commits, files, and history for valuable information. This technique is particularly effective against development or staging servers and maps to MITRE ATT&CK techniques for collecting unsecured credentials and data from information repositories. The target environment is typically a publicly accessible web server hosting a Git-managed application.

## Requirements

1. Network access to the target web server (HTTP/HTTPS connectivity to the .git directory).
2. Installed Git and Perl on the attacker's machine.
3. The DVCS-Ripper tool cloned and ready to execute.
4. Basic knowledge of Git to explore the recovered repository.

## Defense

- Remove or restrict access to .git directories using web server configurations (e.g., Apache: <Location ".git"> Require all denied </Location>).
- Monitor web server logs for anomalous requests to .git paths and implement WAF rules to block them.
- Use Git remotes with authentication and avoid committing secrets (integrate secret scanning tools like git-secrets or TruffleHog).
- Regularly audit exposed directories with tools like git-dumper or automated scanners.

## Objectives

1. Download and reconstruct the full Git repository from the exposed .git directory.
2. Inspect repository contents to identify and extract sensitive information like credentials or source code.
3. Use recovered data for further attacks, such as credential reuse or code analysis.

## Instructions

### Step 1: Clone the DVCS-Ripper Repository

**Context**: Obtain the rip-git tool by cloning its repository from GitHub. This provides the Perl script needed to perform the recovery.

**Command** ([[commands/git-clone-dvcs-ripper-repo]]):
```bash
git clone https://github.com/kost/dvcs-ripper $_TARGET_DIR
```

> This clones the DVCS-Ripper tool into a local directory. Navigate to the cloned directory (cd $_TARGET_DIR/dvcs-ripper) before proceeding. Expected output includes progress messages and a successful clone confirmation.

### Step 2: Run Rip-Git to Recover the Repository

**Context**: Execute the rip-git Perl script against the target's .git URL to download all Git objects and reconstruct the repository locally. This step automates the exfiltration of the entire version history.

**Command** ([[commands/perl-run-rip-git-on-target]]):
```bash
perl rip-git.pl -v -u "$_TARGET_URL/.git/"
```

> Replace $_TARGET_URL with the web application's base URL (e.g., http://example.com). The -v flag enables verbose output. If successful, a new Git repository directory will be created in the current folder, containing all objects, refs, and the index. Monitor for errors like 404s, which indicate the .git path is not exposed.

### Step 3: Inspect Commit History and Authors

**Context**: Once the repository is recovered, use Git to view commit details, including authors and committers, which may reveal internal usernames or emails for further reconnaissance.

**Command** ([[commands/git-cat-file-show-commit]]):
```bash
git cat-file -p $_COMMIT_HASH
```

> Use git log to find commit hashes first (e.g., git log --oneline). This displays the commit object, showing author, committer, timestamp, and message. Look for patterns in author fields that could indicate user accounts.

### Step 4: View Directory Structure

**Context**: Examine the file tree at a specific commit or tree hash to understand the project's structure and identify potential files with sensitive data (e.g., config files, scripts).

**Command** ([[commands/git-ls-tree-show-directory]]):
```bash
git ls-tree -r $_TREE_HASH
```

> Obtain tree hashes from git cat-file or log. This lists all files and directories recursively, helping prioritize which blobs to inspect next. Expected output is a table of mode, type, hash, and path.

### Step 5: View Parent Commits

**Context**: Trace the commit history backward to access previous versions of files, which might contain removed secrets that were committed earlier.

**Command** ([[commands/git-rev-parse-parent-commit]]):
```bash
git rev-parse $_COMMIT_HASH^1
```

> The ^1 denotes the first parent. This outputs the parent commit hash, which can then be used with other Git commands to diff changes or view historical states.

### Step 6: Extract File Contents

**Context**: Retrieve the actual content of files or blobs from the repository to search for credentials, API keys, or other plaintext secrets.

**Command** ([[commands/git-cat-file-show-blob]]):
```bash
git cat-file -p $_BLOB_HASH
```

> Blob hashes come from ls-tree output. Pipe the output to grep for keywords like 'password', 'key', or 'secret' (e.g., | grep -i password). Success is indicated by readable file content; use tools like TruffleHog on the entire repo for automated scanning.
