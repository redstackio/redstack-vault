---
id: 7fd62b13-aa1b-4f1d-b8b7-86f3507cf873
name: Dump-Git-Repository-with-GoGitDumper
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:59.960824+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Collection|TA0009 - Collection]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Data from Local System|T1005 - Data from Local System]]'
  - >-
    [[techniques/File and Directory Discovery|T1083 - File and Directory
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Automatic recovery]]'
  - '[[tags/Git]]'
  - '[[tags/GoGitDumper]]'
  - '[[tags/Insecure Source Code Management]]'
  - '[[tags/Tools]]'
commands:
  - '[[commands/go-get-gogitdumper]]'
  - '[[commands/gogitdumper-dump-repository]]'
  - '[[commands/git-log-repository-history]]'
  - '[[commands/git-checkout-branch]]'
platforms:
  - Linux
  - macOS
tools:
  - '[[tools/GoGitDumper]]'
validated: true
---

# Dump-Git-Repository-with-GoGitDumper

## Summary

This procedure uses the GoGitDumper tool to download and reconstruct a Git repository from an exposed .git directory URL, allowing attackers to extract source code, commit history, configuration files, and potentially sensitive credentials or deleted files. It automates the process of fetching Git objects over HTTP, enabling discovery and collection of insecurely exposed source code management data.

## Description

Exposed .git directories on web servers can reveal the entire history of a Git repository, including source code, credentials in configs, and deleted branches. GoGitDumper leverages the Git protocol over HTTP to download packfiles, objects, and refs from the .git endpoint, reconstructing the repository locally. This is particularly useful in scenarios where attackers identify misconfigured web applications or static sites with accidentally exposed version control directories. The procedure includes post-dumping steps to inspect history and recover content, mapping to MITRE ATT&CK for data collection from remote systems via discovery of file structures. Prerequisites include network access to the target URL and Go environment for tool installation.

## Requirements

1. Go programming language installed (version 1.16 or later) on the attacker's machine.
2. Git installed for post-processing the dumped repository.
3. Network access to the target's exposed .git directory URL (e.g., http://target.com/.git/).
4. Write permissions on the local filesystem for output directory.

## Defense

Defensive measures and detection strategies:

- Ensure .git directories are not web-accessible by configuring web servers (e.g., Apache/Nginx) to deny access to /.git/ paths via .htaccess or location blocks.
- Implement repository access controls, such as authentication and authorization, to prevent unauthorized HTTP requests to Git endpoints.
- Regularly scan for exposed .git directories using tools like git-dumper detectors or web vulnerability scanners.
- Monitor web server logs for anomalous requests to /.git/ paths, such as HEAD or GET to /objects/ or /refs/, and alert on high-volume Git protocol traffic.
- Use web application firewalls (WAF) to block requests matching Git object patterns.

## Objectives

1. Download and reconstruct the full Git repository from an exposed .git URL.
2. Extract sensitive information such as credentials, API keys, or configuration files from the repository contents.
3. Recover deleted files, branches, and commit history for further analysis or exploitation.
4. Verify the dump's integrity and explore the repository structure.

## Instructions

### Step 1: Install GoGitDumper Tool

**Context**: This step installs the GoGitDumper binary using Go's package manager, ensuring the tool is available for dumping the repository. Installation places the binary in your GOPATH/bin, which should be in your PATH for easy execution.

**Command** ([[commands/go-get-gogitdumper]]):
```bash
go get github.com/c-sto/gogitdumper
```

> This command fetches and compiles GoGitDumper from its GitHub repository. Run it in a terminal with Go environment set up. If GOPATH is not configured, set it via `export GOPATH=$HOME/go` and ensure `$GOPATH/bin` is in PATH.

**Expected Output**: Successful installation message, such as "go: downloading github.com/c-sto/gogitdumper v0.0.0-..." followed by no errors. Verify with `gogitdumper --help` to confirm the binary is executable.

### Step 2: Dump the Git Repository

**Context**: Provide the URL of the exposed .git directory and specify a local output path to download the repository objects, refs, and packfiles. GoGitDumper will simulate Git clones over HTTP, reconstructing the .git folder locally. This step collects the raw data for subsequent analysis.

**Command** ([[commands/gogitdumper-dump-repository]]):
```bash
gogitdumper -u $_GIT_URL -o $_OUTPUT_DIR
```

> Replace $_GIT_URL with the target's .git endpoint (e.g., http://target.com/.git/) and $_OUTPUT_DIR with a local path ending in /.git/ (e.g., ./dumped-repo/.git/). The tool will fetch Git objects; if the directory is large, it may take several minutes. Decision point: If the URL requires authentication, prepend credentials to the URL (e.g., http://user:pass@target.com/.git/); otherwise, proceed anonymously.

**Expected Output**: Progress messages like "Downloading refs...", "Fetching packfile...", ending with "Repository dumped successfully." The $_OUTPUT_DIR will contain the .git folder with objects, refs, and config files.

### Step 3: View Repository Commit History

**Context**: After dumping, navigate to the parent directory of the .git folder and use Git to inspect the commit history. This reveals timelines, authors, and changes, helping identify sensitive commits or patterns.

**Command** ([[commands/git-log-repository-history]]):
```bash
cd $_PARENT_DIR && git log
```

> Change to the directory containing the dumped .git (e.g., cd ./dumped-repo). The `git log` command displays the commit graph. For more details, add flags like `--oneline --graph --all` if needed.

**Expected Output**: A list of commits with hashes, authors, dates, and messages, e.g.,
```
commit abc123...
Author: user@example.com
Date:   Mon Jan 1 12:00:00 2023 +0000

    Initial commit with config
```
If no output, the dump may be incomplete—re-run Step 2.

### Step 4: Checkout Branches or Recover Deleted Content

**Context**: Switch to specific branches or force-checkout to recover deleted files and explore the full repository state. This step allows reconstruction of past versions and automatic recovery of lost branches via refs.

**Command** ([[commands/git-checkout-branch]]):
```bash
git checkout $_BRANCH_NAME -b $_NEW_BRANCH_NAME -f
```

> From the repository root (post-Step 3), specify $_BRANCH_NAME (e.g., main) to checkout an existing branch, or use -b to create a new one from a ref. The -f flag discards any local changes. For deleted branches, use `git checkout -b recovered-branch <commit-hash>` based on git log output.

**Expected Output**: Success message like "Switched to branch 'main'" or "Branch 'recovered' set up to track...". Your working directory will now reflect the checked-out state, with files visible via `ls` or `git status` showing clean working tree.

**Success Indicators**:
- Dumped .git directory contains populated objects/ and refs/ folders.
- Git log shows multiple commits with relevant history.
- Checkout succeeds without errors, and files are accessible.
