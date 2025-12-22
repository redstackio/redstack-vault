---
id: c9dffefa-6a0e-4348-8454-7fbf0c33f2fe
name: Download-Git-Repository-Object-Using-Diggit
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:59.935947+00:00'
updated_at: '2023-04-10T20:33:56.592422+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[T1213.003]]'
sub_techniques: []
tags:
  - git
  - diggit
  - source-code
  - credentials-leak
  - insecure-source-code-management
commands:
  - '[[commands/git-clone-security-tools-repo-and-cd-to-diggit]]'
  - '[[commands/diggit-download-git-object]]'
platforms:
  - Linux
tools:
  - '[[tools/diggit]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
---

# Download-Git-Repository-Object-Using-Diggit

## Summary

This procedure uses the diggit.py tool to download specific Git objects, such as blobs or commits, from a remote repository without cloning the entire repo. It is particularly useful in red team operations or security assessments to extract potentially sensitive information like hardcoded credentials, API keys, or configuration files that may have been committed to a public or accessible Git repository.

## Description

In scenarios where attackers identify a vulnerable or exposed Git repository (e.g., via reconnaissance on platforms like GitHub), they can target individual objects using their hashes to retrieve sensitive data efficiently. The diggit tool interacts with the remote .git directory over HTTP to fetch objects, allowing recovery of deleted or historical items if the -r flag is used. This technique maps to MITRE ATT&CK T1213.003 (Code Repositories) under the Discovery tactic, as it involves gathering information from source code repositories. It requires knowledge of a specific object hash, which might be obtained from prior enumeration or leaks. The target environment is typically a web-accessible Git server, and success depends on the repository not being fully private or protected against such access.

## Requirements

1. Network access to the remote Git repository's .git directory (e.g., http://example.com/.git/).
2. The diggit.py tool installed locally (obtained by cloning the bl4de/security-tools repository).
3. Knowledge of the target Git object hash (e.g., from prior reconnaissance or directory traversal findings).
4. A temporary local directory for initializing a dummy Git repo to store downloaded blobs.

## Defense

- Restrict access to Git repositories using authentication (e.g., OAuth tokens, SSH keys) and ensure .git directories are not publicly accessible via web servers.
- Implement secure coding practices to avoid committing sensitive information; use tools like git-secrets or pre-commit hooks to scan for secrets.
- Monitor repository access logs for anomalous requests to .git endpoints and set up alerting for unusual HTTP traffic patterns to Git objects.
- Regularly audit and purge historical commits containing sensitive data using git filter-branch or BFG Repo-Cleaner.

## Objectives

1. Obtain the diggit.py tool for Git object retrieval.
2. Download a specific Git object (e.g., a blob containing credentials) from the remote repository.
3. Recover deleted objects if applicable, to access historical sensitive information.
4. Verify the downloaded content for exploitable data like passwords or keys.

## Instructions

### Step 1: Install Diggit Tool

**Context**: Clone the repository containing diggit.py and navigate to its directory. This sets up the tool for use in subsequent steps.

**Command** ([[commands/git-clone-security-tools-repo-and-cd-to-diggit]]):
```bash
git clone https://github.com/bl4de/security-tools/ && cd security-tools/diggit
```

> This command clones the bl4de/security-tools repository and changes into the diggit subdirectory, making diggit.py executable available. Expected output includes clone progress messages and a directory listing confirming the presence of diggit.py. If the clone fails due to network issues, verify Git installation and internet connectivity.

### Step 2: Download Specific Git Object

**Context**: Use diggit.py to fetch the target Git object by hash from the remote repository. Initialize a dummy Git repo in the temp folder to store blobs with their original names. The -r flag enables recovery of deleted objects.

**Command** ([[commands/diggit-download-git-object]]):
```bash
./diggit.py -u remote_git_repo -t temp_folder -o object_hash [-r=True]
./diggit.py -u http://web.site -t /path/to/temp/folder/ -o d60fbeed6db32865a1f01bb9e485755f085f51c1
```

> Replace 'remote_git_repo' with the URL to the .git directory (e.g., http://example.com/.git), 'temp_folder' with a local path (and run 'git init' there beforehand), and 'object_hash' with the SHA-1 hash of the target object. The tool downloads the object and saves blobs as files. Expected output includes progress messages and confirmation of download, with files appearing in the temp folder. If the object is not found, check the hash and remote accessibility; for deleted objects, ensure -r=True is used.
