---
id: proc-lgtm-setup-project
tags:
  - setup
  - lgtm
  - project-init
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Linux
  - Docker
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:29.980Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-LGTM-Compatible-Project

## Summary

This procedure initializes a simple GitHub repository with a buildable project structure that LGTM can analyze successfully, serving as the foundation for exploiting the build process.

## Description

The LGTM platform analyzes code from GitHub repositories using containerized builds. To exploit this, a basic project must be created that triggers a successful build without errors. This involves setting up minimal files for a supported language like Java, ensuring the build command executes cleanly. The example repository https://github.com/testanull/test11 provides a template with basic structure. Prerequisites include a GitHub account; no LGTM-specific access is needed initially.

## Requirements

1. GitHub account with repository creation permissions
2. Git installed locally for repository management
3. Basic knowledge of project structures for languages like Java

## Defense

Defensive measures and detection strategies:

- Monitor new repository creations linked to LGTM integrations
- Implement repository scanning for unusual file patterns before analysis

## Objectives

1. Establish a valid target for LGTM build triggering
2. Ensure build success to reach file retention phase
3. Prepare for symlink injection

## Instructions

### Step 1: Initialize Repository

**Context**: Create a new empty repository on GitHub and clone it locally to add basic files.

Go to GitHub, create a new public repository named e.g., 'test-lgtm-project', then clone it:

```bash
git clone https://github.com/yourusername/test-lgtm-project.git
cd test-lgtm-project
```

> This sets up the local working directory.

### Step 2: Add Basic Project Files

**Context**: Add minimal files to make the project buildable, referencing the example at https://github.com/testanull/test11.

Create a simple Java file or equivalent:

```bash
echo 'public class Hello { public static void main(String[] args) { System.out.println("Hello"); } }' > Hello.java
```

> Ensures LGTM can compile and analyze without failures.

### Step 3: Commit and Push

**Context**: Push the initial structure to GitHub to make it available for LGTM.

```bash
git add .
git commit -m "Initial project setup"
git push origin main
```

> Repository is now live and ready for configuration.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[lgtm]]
- [[project-init]]
