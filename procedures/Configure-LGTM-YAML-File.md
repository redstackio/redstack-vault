---
id: proc-lgtm-config-yaml
tags:
  - configuration
  - lgtm
  - yaml
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
updated_at: '2025-12-14T17:26:29.974Z'
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
# Configure-LGTM-YAML-File

## Summary

This procedure adds a valid lgtm.yml configuration file to the repository, defining the build extraction process to ensure LGTM processes the project correctly during analysis.

## Description

LGTM uses lgtm.yml to customize builds, such as specifying language extraction and commands. A valid file prevents build failures and allows the platform to retain files post-build. The content example includes Java extraction with a custom build command. This step is crucial as it coexists with the malicious symlink in the next phase. Target environment is the GitHub repository; expected outcome is LGTM recognizing and using the config.

## Requirements

1. Existing GitHub repository from prior setup
2. YAML syntax knowledge
3. Local Git environment

## Defense

Defensive measures and detection strategies:

- Validate YAML configurations for malicious commands before processing
- Scan for unusual build customizations in integrated repos

## Objectives

1. Enable successful LGTM build execution
2. Set stage for file retention including symlinks
3. Maintain project validity

## Instructions

### Step 1: Create YAML File

**Context**: Generate the lgtm.yml with valid content in the repository root.

```bash
cat > lgtm.yml << EOF
extraction:
  java:
    index:
      build_command: ['./custom-build']
EOF
```

> This defines a basic Java build; adjust for other languages if needed.

### Step 2: Add and Commit

**Context**: Integrate the file into the repository.

```bash
git add lgtm.yml
git commit -m "Add LGTM configuration"
git push origin main
```

> Pushes the config, making it available for LGTM.

### Step 3: Verify

**Context**: Check LGTM dashboard for config recognition.

Navigate to the repository on LGTM (after enabling integration) and confirm the YAML is parsed without errors.

> Success if no syntax warnings appear.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[configuration]]
- [[lgtm]]
- [[yaml]]
