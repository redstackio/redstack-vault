---
id: 18745c81-60a7-4076-b45b-09f603757bf9
name: Recover-Source-Code-from-Insecure-Git-Repository-Using-Git-Dumper
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:59.900017+00:00'
updated_at: '2023-04-10T20:33:54.538320+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Data from Information Repositories]]'
sub_techniques: []
tags:
  - git
  - source-code-recovery
  - insecure-git
  - reconnaissance
  - collection
commands:
  - '[[commands/git-clone-git-dumper-repository]]'
  - '[[commands/pip-install-git-dumper-requirements]]'
  - '[[commands/git-dumper-dump-repository]]'
platforms:
  - Web
  - Linux
tools:
  - '[[tools/git-dumper]]'
validated: true
---

# Recover-Source-Code-from-Insecure-Git-Repository-Using-Git-Dumper

## Summary

This procedure uses the git-dumper tool to recover the full history of a Git repository exposed insecurely through a web server's .git directory. By downloading objects from the exposed .git folder, attackers can reconstruct the entire repository, including past versions of source code, to identify vulnerabilities, hardcoded credentials, or other sensitive information.

## Description

Insecurely configured web servers may expose the .git directory, allowing remote access to Git repository data via HTTP. Git-dumper exploits this by mimicking Git protocol requests to fetch packfiles, objects, and refs, rebuilding the repository locally. This technique is useful in web application reconnaissance to uncover source code leaks, API keys, database credentials, or logic flaws. It targets misconfigurations where .git is not properly restricted by web server rules (e.g., missing .htaccess denies in Apache). Success depends on the .git/info/refs and .git/HEAD being accessible, enabling full repo reconstruction. This maps to MITRE ATT&CK [[Data from Information Repositories]] Data from Information Repositories under the Discovery tactic [[Discovery]], as it collects internal code repositories.

## Requirements

1. Network access to the target's web server exposing the .git directory (e.g., http://target.com/.git/).
2. Python 3 installed on the attacker's machine, along with pip for dependency management.
3. Git installed for local repository reconstruction after dumping.
4. The target .git directory must be publicly accessible without authentication.

## Defense

- Configure web servers to deny access to .git directories (e.g., Apache: <Directory "*.git"> Require all denied </Directory>; Nginx: location ~ ^/.git { deny all; }).
- Use repository managers like GitHub or GitLab with proper access controls instead of exposing repos on web roots.
- Regularly scan for exposed .git directories using tools like git-dumper in defensive mode or automated crawlers.
- Monitor web server logs for unusual requests to .git paths and implement WAF rules to block them.

## Objectives

1. Download and reconstruct the full Git repository from an exposed .git directory.
2. Analyze recovered source code for vulnerabilities, secrets, or business logic insights.
3. Enable further attacks such as credential extraction or custom exploit development based on leaked code.

## Instructions

### Step 1: Clone the Git-Dumper Repository

**Context**: Obtain the git-dumper tool from its official GitHub repository to prepare for installation and usage. This step ensures you have the latest version of the script.

**Command** ([[commands/git-clone-git-dumper-repository]]):
```bash
git clone https://github.com/arthaud/git-dumper
```

> This command clones the repository into a local directory named 'git-dumper'. Navigate into it with `cd git-dumper` after execution. Expected output includes progress messages like 'Cloning into 'git-dumper'... remote: Enumerating objects... done.' If Git is not installed, install it first via your package manager (e.g., `apt install git` on Ubuntu).

### Step 2: Install Dependencies

**Context**: Install the required Python packages for git-dumper to function, including libraries for HTTP requests and Git object handling. This step is necessary to avoid runtime errors during dumping.

**Command** ([[commands/pip-install-git-dumper-requirements]]):
```bash
pip install -r requirements.txt
```

> Run this from within the cloned git-dumper directory. It installs dependencies like requests and GitPython. Expected output: 'Successfully installed <package>-<version>' for each package. If using a virtual environment, activate it first with `python -m venv env && source env/bin/activate` to isolate dependencies.

### Step 3: Dump the Target Repository

**Context**: Execute git-dumper against the exposed .git URL to fetch and reconstruct the repository locally. This step performs the core recovery, downloading refs, objects, and packfiles to build a complete Git history.

**Command** ([[commands/git-dumper-dump-repository]]):
```bash
./git-dumper.py $_TARGET_GIT_URL $_OUTPUT_DIR
```

> Replace $_TARGET_GIT_URL with the exposed .git path (e.g., 'http://target.com/.git') and $_OUTPUT_DIR with a local path (e.g., '~/recovered-repo'). The tool will output progress like 'Getting info/refs' and 'Dumping objects'. Upon success, a new Git repository is created in $_OUTPUT_DIR, verifiable with `cd $_OUTPUT_DIR && git log` to view commit history. If the .git is incomplete, the dump may fail partially—retry or check server accessibility.
