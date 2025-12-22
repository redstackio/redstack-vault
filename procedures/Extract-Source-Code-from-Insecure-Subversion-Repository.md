---
id: 8c04d263-1dc4-4852-b5c1-f517b2b2f4aa
name: Extract-Source-Code-from-Insecure-Subversion-Repository
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:00.298881+00:00'
updated_at: '2023-04-10T20:33:57.605889+00:00'
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
techniques:
  - '[[T1213.003]]'
sub_techniques: []
tags:
  - '[[tags/Insecure Source Code Management]]'
  - '[[tags/Subversion]]'
  - '[[tags/svn-extractor]]'
  - '[[tags/Tools]]'
commands:
  - '[[commands/git-clone-svn-extractor]]'
  - '[[commands/run-svn-extractor-on-url]]'
platforms:
  - Linux
  - Web
tools:
  - '[[tools/svn-extractor]]'
validated: true
---

# Extract-Source-Code-from-Insecure-Subversion-Repository

## Summary

This procedure uses the svn-extractor tool to identify and extract sensitive information, such as source code, usernames, and passwords, from insecure Subversion (SVN) repositories exposed over the web. It automates the discovery of .svn directories that are publicly accessible due to misconfigurations, allowing attackers to reconstruct repository contents without authentication.

## Description

Subversion (SVN) is a centralized version control system often used for managing source code in development environments. If not properly secured, SVN repositories can expose hidden directories like .svn, which contain metadata files (e.g., entries, props, text-base) that hold historical versions of files, commit logs, and credentials. The svn-extractor tool, a Python script, exploits this by recursively downloading and reconstructing the repository structure from a given URL ending in .svn. This technique is useful in reconnaissance and collection phases to gather intellectual property, configuration secrets, or application code from targets with poor web server configurations (e.g., Apache without mod_dav_svn restrictions). It requires only HTTP access to the .svn path and works against anonymous repositories. Defenders should monitor for anomalous downloads from .svn paths and enforce strict access controls on version control endpoints.

## Requirements

1. Network access to a target URL with an exposed .svn directory (e.g., http://target.com/repo/.svn/).
2. Python 2 or 3 installed on the attacker's machine.
3. Git installed for cloning the tool repository.
4. No authentication required for the target SVN repository; it must be anonymously accessible.

## Defense

- Disable directory listing and access to .svn directories in web server configurations (e.g., via Apache's <Location> blocks or Nginx deny rules).
- Use authentication and authorization on all SVN endpoints, such as requiring HTTPS and user credentials.
- Regularly scan for exposed .svn paths using tools like this one from a defender's perspective and remediate misconfigurations.
- Implement web application firewalls (WAFs) to block requests to hidden directories and monitor logs for suspicious .svn accesses.

## Objectives

1. Identify publicly accessible SVN repositories with exposed .svn directories.
2. Download and reconstruct source code, commit history, and sensitive data from the repository.
3. Collect potential credentials or intellectual property for further exploitation.

## Instructions

### Step 1: Clone the SVN Extractor Tool

**Context**: Obtain the svn-extractor tool from its GitHub repository. This step ensures you have the latest version of the Python script needed to perform the extraction.

**Command** ([[commands/git-clone-svn-extractor]]):
```bash
git clone https://github.com/anantshri/svn-extractor.git
```

> This clones the repository into a local directory named svn-extractor. Navigate into the directory after cloning to access the main script (svn-extractor.py). Expected output includes progress messages from Git, ending with a summary of cloned objects. Verify success by checking that svn-extractor.py exists in the cloned folder.

### Step 2: Run SVN Extractor on the Target URL

**Context**: Execute the tool against the target SVN repository URL to download and extract the contents. Replace the URL placeholder with the actual path to the .svn directory. The tool will recursively fetch files and attempt to reconstruct the repository structure in a local output directory.

**Command** ([[commands/run-svn-extractor-on-url]]):
```bash
python svn-extractor.py --url "http://target.com/repo/.svn/"
```

> This runs the Python script, specifying the target URL. The tool will output progress as it downloads files like entries, wc.db, and text-base contents. If successful, it creates a mirrored directory structure with extracted source files, diffs, and metadata. Handle errors like 404s by verifying the .svn path exists and is accessible. Decision point: If the URL requires authentication, this procedure won't work; consider alternative tools like svn export with creds.
