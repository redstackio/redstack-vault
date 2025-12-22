---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:59.857938+00:00'
updated_at: '2023-04-10T20:33:54.190310+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
  - '[[sub-techniques/Private Keys|T1552.004 - Private Keys]]'
tags:
  - '[[tags/Git]]'
  - '[[tags/Insecure Source Code Management]]'
  - '[[tags/Recovering file contents from .git/index]]'
commands:
  - '[[commands/install-gin-and-parse-git-index]]'
  - '[[commands/extract-names-and-sha1-from-git-index]]'
platforms:
  - Linux
tools: []
validated: true
---

# Git-Index-File-Recovery

## Summary

Git Index File Recovery is a post-exploitation technique used to extract sensitive file names, SHA1 hashes, and potentially file contents from the .git/index file in a compromised Git repository. This allows attackers to identify and recover unsecured credentials, private keys, or proprietary data that may have been committed accidentally, enabling further persistence or lateral movement without direct file access.

## Description

In a compromised environment where an attacker has access to a Git repository's .git directory, the index file (.git/index) serves as a staging area that records file paths, metadata, and SHA1 hashes of tracked files. By parsing this binary file using tools like the 'gin' Python library, attackers can enumerate all staged or committed files, including those containing sensitive information such as API keys, passwords, or configuration files. Once file names and hashes are obtained, attackers can cross-reference them with Git objects in .git/objects to reconstruct file contents, even if the working directory has been cleaned. This technique is particularly effective against developers or CI/CD pipelines where secrets are inadvertently stored in source code. It maps to credential access scenarios in environments with insecure source code management practices.

## Requirements

1. File system access to the .git directory of a compromised Git repository (e.g., via initial access or persistence on a development server).
2. Python 3.x installed on the attacker's or compromised machine.
3. Internet access if installing the 'gin' library via pip (or pre-install it on air-gapped systems).
4. Basic command-line proficiency for parsing output.

## Defense

Defensive measures and detection strategies:

- Implement strict access controls on Git repositories using role-based authentication (e.g., GitHub, GitLab RBAC) and avoid exposing .git directories in web roots or public shares.
- Use secret scanning tools (e.g., GitHub Secret Scanning, TruffleHog) to detect and remove sensitive data from commits before pushing.
- Monitor for anomalous file access or process execution involving Git tools (e.g., via EDR rules for 'gin' or unusual Python pip installs in production environments).
- Enforce .gitignore rules for sensitive files and conduct regular repository audits to remove historical secrets using tools like BFG Repo-Cleaner.

## Objectives

1. Recover sensitive information such as credentials, private keys, and configuration files from Git history.
2. Maintain persistence by extracting usable secrets for further attacks without alerting defenders.
3. Evade detection by operating on existing repository artifacts rather than active network exfiltration.

## Instructions

### Step 1: Install Gin Library and Parse Git Index

**Context**: Install the 'gin' Python package, which is designed to parse Git index files, and immediately use it to dump the contents of the target .git/index file. This step provides the raw metadata needed for file enumeration. The 'gin' tool outputs the index in a human-readable key-value format, revealing file entries without requiring full Git checkout.

**Command** ([[commands/install-gin-and-parse-git-index]]):
```bash
pip3 install gin
gin $_GIT_INDEX_PATH
```

> This command first installs 'gin' if not present, then parses the specified index file. Replace $_GIT_INDEX_PATH with the path to the .git/index (e.g., /path/to/repo/.git/index). If 'gin' is already installed, the pip step can be skipped to reduce noise.

### Step 2: Extract File Names and SHA1 Hashes

**Context**: From the parsed index output, filter for file names and their corresponding SHA1 hashes using grep. This isolates the key information for identifying sensitive files. The SHA1 hashes can then be used to locate and extract actual file contents from the .git/objects directory by constructing object paths (e.g., hash prefix in subdirs).

**Command** ([[commands/extract-names-and-sha1-from-git-index]]):
```bash
gin $_GIT_INDEX_PATH | egrep -e "name|sha1"
```

> Run this after Step 1 to filter the output. Expected results will show pairs like 'name = sensitive/config.md' followed by 'sha1 = abc123...', allowing manual or scripted recovery of file blobs. If no output appears, verify the index path and ensure the repository has staged files.
