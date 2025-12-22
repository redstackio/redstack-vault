---
id: dca3231a-95a9-4ce7-a30b-80ca8b74e9b2
name: Scan-Remote-Git-Repo-for-Sensitive-Information-with-Gitleaks
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T17:11:21.872587+00:00'
updated_at: '2023-05-26T00:44:36.829598+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Unsecured Credentials]]'
sub_techniques: []
tags:
  - gitleaks
  - secrets-scanning
  - reconnaissance
  - credentials
commands:
  - '[[commands/gitleaks-scan-remote-repo]]'
platforms:
  - Linux
  - macOS
  - Windows
tools:
  - '[[tools/Gitleaks]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Scan-Remote-Git-Repo-for-Sensitive-Information-with-Gitleaks

## Summary

This procedure uses Gitleaks to scan a remote Git repository, such as one hosted on GitHub, for accidentally committed sensitive information including API keys, hardcoded passwords, tokens, and other secrets. It is a key reconnaissance technique for identifying potential credential leaks that could lead to further compromise in offensive security operations or security audits.

## Description

Gitleaks is an open-source tool designed to detect hardcoded secrets in Git repositories by scanning commit history, files, and configurations against a predefined set of regex patterns for common secret types. This procedure focuses on remote repositories accessible via URL, allowing testers to identify exposures without cloning the entire repo. It is particularly useful in red team engagements for discovering valid credentials during initial reconnaissance phases, mapping to MITRE ATT&CK's Discovery tactic where unsecured credentials are harvested from public or accessible sources. The scan runs efficiently on remote repos, outputting matches with context like file paths and line numbers for quick validation.

## Requirements

1. Gitleaks tool installed and accessible in the PATH (see [[tools/Gitleaks]] for installation).
2. Network access to the target remote Git repository (e.g., public GitHub URL).
3. Basic command-line proficiency; no elevated privileges required.
4. Optional: A wordlist or custom config for extended pattern matching, though defaults suffice for standard secrets.

## Defense

Defensive measures and detection strategies:

- Use Git pre-commit hooks or tools like GitGuardian to prevent secret commits.
- Regularly scan repositories with automated CI/CD pipelines integrating secret detection.
- Monitor for anomalous outbound scans from security tools via network logs (e.g., unusual HTTPS requests to GitHub APIs).
- Implement repository access controls and private repos for sensitive projects.

## Objectives

1. Identify and extract potential secrets from a remote Git repository's history and files.
2. Validate findings for usability in further attacks, such as API access or authentication.
3. Document exposed credentials to inform risk assessment or exploitation paths.

## Instructions

### Step 1: Verify Tool and Prepare Target

**Context**: Ensure Gitleaks is installed and gather the target repository URL. This step confirms prerequisites and avoids runtime errors.

Run the Gitleaks version check to verify installation.

**Command** ([[commands/gitleaks-version-check]]):
```bash
gitleaks version
```

> This command outputs the installed version (e.g., v8.18.0), confirming the tool is ready. If not installed, refer to [[tools/Gitleaks]]. Obtain the full HTTPS URL of the remote repo, such as https://github.com/zricethezav/gitleaks.

### Step 2: Execute the Remote Repo Scan

**Context**: Perform the core scan using the --repo flag to detect secrets without local cloning. This leverages Gitleaks' remote detection capabilities for efficiency.

**Command** ([[commands/gitleaks-scan-remote-repo]]):
```bash
gitleaks detect --source=https://github.com/zricethezav/gitleaks
```

> Replace the URL with the target repo. The command scans all commits and files for matches against default patterns (e.g., AWS keys, private keys). Use --verbose for detailed progress if needed. Expected runtime is seconds to minutes depending on repo size.

### Step 3: Review and Validate Findings

**Context**: Analyze the output for actionable secrets, extracting context like commit hashes and file locations for verification. This step ensures findings are not false positives.

No specific command; parse the JSON or text output manually or pipe to jq for filtering.

**Command** (optional, using jq for JSON output):
```bash
gitleaks detect --source=https://github.com/zricethezav/gitleaks --report-format json | jq '.'
```

> Output includes secret type, rule, commit, file, and snippet. Manually test extracted secrets (e.g., via curl for API keys) in a controlled environment to confirm validity. If no secrets found, consider custom configs with --config-path.
