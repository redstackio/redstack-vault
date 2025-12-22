---
type: procedure
tactics:
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - >-
    [[techniques/Exfiltration Over Alternative Protocol|T1048 - Exfiltration
    Over Alternative Protocol]]
  - >-
    [[techniques/Exfiltration Over Command and Control Channel|T1041 -
    Exfiltration Over Command and Control Channel]]
sub_techniques: []
tags:
  - '[[tags/Insecure Source Code Management]]'
  - '[[tags/Mercurial]]'
  - '[[tags/rip-hg.pl]]'
  - '[[tags/Tools]]'
commands:
  - '[[commands/download-rip-hg-pl-script]]'
  - '[[commands/run-dvcs-ripper-docker-container]]'
tools:
  - '[[tools/dvcs-ripper]]'
platforms:
  - Linux
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Mercurial Source Code Extraction with rip-hg.pl

## Summary

This procedure uses the rip-hg.pl tool from the dvcs-ripper project to clone and extract source code from a remote Mercurial repository. It enables attackers to exfiltrate sensitive code by mimicking legitimate repository access, potentially revealing proprietary logic, credentials, or configurations for further exploitation or sale.

## Description

In scenarios where an attacker has discovered a publicly accessible or weakly protected Mercurial (Hg) repository, this procedure allows bulk extraction of the entire repository history and files to a local directory. The tool automates the cloning process, handling authentication if needed, and supports verbose logging for troubleshooting. It can be executed directly on a host with Perl or via Docker for isolation. This technique targets insecure source code management systems, common in legacy or misconfigured development environments, leading to intellectual property theft. Success depends on the repository's visibility and lack of access controls.

## Requirements

1. Network access to the target Mercurial repository URL (e.g., https://example.com/repo).
2. Docker installed and running on the attacker's system for containerized execution, or Perl environment for direct run.
3. Write permissions to a local working directory for storing extracted files.
4. Optional: Valid credentials if the repository requires authentication (rip-hg.pl supports basic auth).

## Defense

Defensive measures and detection strategies:

- Restrict repository access to authenticated users via HTTPS and IP whitelisting.
- Monitor for anomalous clone/pull requests from unfamiliar IPs or high-volume data transfers.
- Implement data loss prevention (DLP) tools to scan outbound traffic for code patterns or repository metadata.
- Use repository managers like Bitbucket or self-hosted Hg servers with audit logging enabled.

## Objectives

1. Clone the full Mercurial repository to obtain all source code files and history.
2. Exfiltrate sensitive code for analysis, reuse, or monetization.
3. Verify extraction completeness without alerting defenders.

## Instructions

### Step 1: Download the rip-hg.pl Script

**Context**: Obtain the rip-hg.pl tool from its GitHub repository to prepare for repository ripping. This step ensures you have the latest version of the script.

**Command** ([[commands/download-rip-hg-pl-script]]):
```bash
wget https://raw.githubusercontent.com/kost/dvcs-ripper/master/rip-hg.pl
```

> This downloads the Perl script to your current directory. Verify the file with `ls -l rip-hg.pl` to confirm it's present and executable (chmod +x if needed). Expected output is a progress bar showing the download completion, followed by the file listing.

### Step 2: Run the Docker Container to Extract the Repository

**Context**: Use the pre-built Docker image for dvcs-ripper to execute rip-hg.pl in an isolated environment, mounting your local directory for output. Provide the target repository URL as an argument to initiate the clone and extraction.

**Command** ([[commands/run-dvcs-ripper-docker-container]]):
```bash
docker run --rm -it -v $_LOCAL_DIR:/work:rw k0st/alpine-dvcs-ripper rip-hg.pl -v -u $_REPO_URL
```

> Replace $_LOCAL_DIR with your host path (e.g., /home/user/extracted-repo) and $_REPO_URL with the target (e.g., https://hg.example.com/my-repo). The -v flag enables verbose output for monitoring progress, and -u updates if the repo partially exists. The container removes itself (--rm) after execution. Expected output includes cloning progress logs, file listings, and confirmation of extracted commits. If authentication is required, add credentials via rip-hg.pl's --user and --pass options.

### Step 3: Verify Extraction

**Context**: Check the mounted directory for the cloned repository to confirm successful exfiltration and completeness.

**Instructions**: After the Docker run completes, navigate to $_LOCAL_DIR and inspect the contents.
```bash
ls -la $_LOCAL_DIR
find $_LOCAL_DIR -name '*.py' | head -10  # Example: List Python files if applicable
```

> Look for .hg directory and source files. Success is indicated by the presence of repository files matching the remote structure. If incomplete, rerun with -u to resume.
