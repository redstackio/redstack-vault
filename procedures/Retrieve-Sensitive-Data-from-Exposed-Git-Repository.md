---
id: f2da7d36-5198-47d5-ae10-60d069f97bfd
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T16:11:22.093895+00:00'
updated_at: '2023-05-26T01:04:54.246259+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Unsecured Credentials]]'
sub_techniques:
  - '[[Credentials in Files]]'
tags:
  - broken authentication
  - information disclosure
  - owasp
  - owasp top 10
  - Web Applications
commands:
  - '[[commands/wget-mirror-git-directory]]'
  - '[[commands/git-log-with-patch]]'
platforms:
  - Web
tools: []
skill_level: beginner
impact_level: high
detection_risk: low
validated: true
---

# Retrieve-Sensitive-Data-from-Exposed-Git-Repository

## Summary

This procedure outlines how to exploit an exposed .git directory in a web application to download the version control repository and inspect its commit history for sensitive information, such as hardcoded passwords or API keys. By mirroring the .git folder and reviewing diffs, attackers can uncover credentials that enable further access, such as administrative logins.

## Description

Web applications sometimes inadvertently expose their .git directories due to misconfigurations in the web server, allowing direct access via HTTP. This exposure reveals the entire Git repository history, including commits that may contain sensitive data like configuration files with passwords, private keys, or internal endpoints. The technique leverages standard tools like wget to download the repository and Git to analyze changes. It is particularly effective against applications built with version control systems where secrets were committed before being removed. Success depends on the .git directory being publicly accessible without authentication. This maps to discovery of files and unsecured credentials in the MITRE ATT&CK framework.

## Requirements

1. Network access to the target web application (no authentication required for the .git endpoint).
2. wget installed on the attacker's machine for downloading the repository.
3. Git installed to inspect the downloaded repository history.
4. Target URL of the web application (e.g., http://example.com).

## Defense

Defensive measures include removing or blocking access to .git directories via web server configurations (e.g., .htaccess rules in Apache or location blocks in Nginx). Use .gitignore to prevent committing secrets, implement repository scanning tools like git-secrets or TruffleHog, and regularly audit public-facing directories for exposures. Detection can involve web application firewalls (WAFs) logging requests to /.git/ and monitoring for unusual downloads of repository files.

## Objectives

1. Confirm exposure of the .git directory and download the repository.
2. Analyze commit history to identify and extract sensitive credentials.
3. Use discovered information to gain unauthorized access to the application.
4. Expected outcome: Obtain plaintext credentials for privilege escalation or authentication bypass.

## Instructions

### Step 1: Verify .git Directory Accessibility

**Context**: Before downloading, confirm that the .git directory is exposed and accessible via the browser or a simple HTTP request. This step ensures the target is vulnerable and avoids unnecessary downloads.

Navigate to http://target/.git/ in a web browser. If the index.html or other Git files (like HEAD or config) are visible, the directory is exposed.

**Expected Output**: Browser displays Git repository files or a directory listing, indicating successful access without errors like 404 or 403.

### Step 2: Download the Git Repository

**Context**: Use wget to mirror the entire .git directory to your local machine. This retrieves objects, refs, and other Git data needed to reconstruct the repository history.

**Command** ([[commands/wget-mirror-git-directory]]):
```bash
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent http://target/.git/ -P ./downloaded-git
```

> This command recursively downloads the .git folder, converting links and adjusting extensions for local viewing. The -P flag specifies the local output directory. Run this from a terminal on a Linux/macOS system or compatible environment.

**Expected Output**: A local directory named 'downloaded-git' containing the .git structure, including subfolders like objects/, refs/, and files like HEAD, config, and index. No errors in wget output indicating failed downloads.

### Step 3: Reconstruct and Inspect Repository History

**Context**: Once downloaded, navigate into the directory and use Git to checkout the repository state and review commit history for sensitive data. Focus on diffs to spot removed or modified secrets like passwords.

First, cd into the downloaded directory and initialize Git if needed:
```bash
cd downloaded-git
mv .git ../local-git  # Rename to avoid recursion
cd ../local-git
mkdir .git
mv * .git/  # Move contents if necessary, but typically wget places them correctly
git checkout .
```

Then execute the command to view history.

**Command** ([[commands/git-log-with-patch]]):
```bash
git log -p --all | grep -i "password\|key\|secret\|admin"
```

> This displays the commit history with full diffs (-p) across all branches (--all) and greps for common sensitive terms. Adjust grep patterns based on expected secrets.

**Expected Output**: Console output showing commit diffs, such as lines like "+ADMIN_PASSWORD=secret123" in a file change, revealing hardcoded credentials.

### Step 4: Apply Discovered Credentials

**Context**: Use the extracted sensitive information, such as an admin password from the history, to authenticate to the application. This validates the disclosure and achieves the objective.

Navigate to the application's login page and enter the discovered credentials (e.g., username: admin, password: secret123 from the Git diff).

**Expected Output**: Successful login to the admin dashboard or restricted area, confirming credential validity.

## Expected Output

Overall success is indicated by obtaining usable credentials from Git history, leading to authenticated access. Sample output from git log might include:

```
commit abc123...
--- a/config.php
+++ b/config.php
@@ -1,4 +1,4 @@
 $admin_password = 'secret123';
```

This reveals the password for further exploitation.
