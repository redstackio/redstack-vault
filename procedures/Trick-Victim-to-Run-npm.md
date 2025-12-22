---
tags:
  - social-engineering
  - phishing
  - tutorial-hijack
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-help]]'
  - '[[commands/npm-whoami]]'
  - '[[commands/sudo-npm-i-g-eslint]]'
  - '[[commands/sudo-npm]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Phishing]]'
updated_at: '2025-12-14T17:28:44.408Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[T1566.001]]'
id: eb25391f-4a7a-430c-9880-924fc7cb9e88
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Trick-Victim-to-Run-npm

## Summary

This procedure uses social engineering to convince the victim to execute npm commands in a directory containing the malicious .npmrc, triggering the onload-script.

## Description

Attackers craft scenarios like fake tutorials or emails directing users to clone repositories and run seemingly innocent npm commands. This leads to loading the local .npmrc and executing the onload-script with user or root privileges if sudo is involved. High impact in development environments or infected repos.

## Requirements

1. Control over communication channels (e.g., email, forums, git repos)
2. Malicious .npmrc already placed
3. Victim with npm installed

## Defense

Defensive measures and detection strategies:

- Educate users on verifying repo sources and commands
- Scan for suspicious npm invocations in logs
- Use sandboxed environments for running untrusted code

## Objectives

1. Lure victim to the infected directory
2. Trigger npm execution without suspicion
3. Achieve code execution via onload-script

## Instructions

### Step 1: Craft Social Engineering Lure

**Context**: Create a tutorial or message instructing the victim to perform actions in the target directory.

No command; example: "Clone this repo and run `sudo npm i -g eslint` to set up linting."

> Expected: Victim follows instructions.

### Step 2: Direct to Innocent Command

**Context**: Suggest running a harmless command like [[commands/npm-help]] to load .npmrc.

**Command** ([[commands/npm-help]]):
```bash
npm help
```

> Displays help but loads .npmrc. Expected output: npm help documentation, with script execution.

### Step 3: Escalate with Sudo Command

**Context**: For root access, trick into using sudo, e.g., [[commands/sudo-npm-i-g-eslint]].

**Command** ([[commands/sudo-npm-i-g-eslint]]):
```bash
sudo npm i -g eslint
```

> Installs eslint globally as root, executing script with elevated privileges. Expected output: Installation logs, payload runs as root.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Phishing]]

### Sub-Techniques

- [[T1566.001]]

## Commands Used

- [[commands/npm-help]]
- [[commands/npm-whoami]]
- [[commands/sudo-npm-i-g-eslint]]
- [[commands/sudo-npm]]

## Tools Used


## Tags

- [[social-engineering]]
- [[Phishing]]
