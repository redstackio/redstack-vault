---
id: proc-installer-prep-001
tags:
  - dylib-injection
  - entitlements
  - installer
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/list-macos-directory]]'
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:29:10.017Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Prepare-Vulnerable-Installer

## Summary

Download and mount an old version of the Kaspersky Internet Security installer (20.0.0.829) that includes insecure entitlements, allowing dylib proxying for code injection, and verify the necessary files and entitlements.

## Description

The installer kavmac20.0.0.829aar_cs_da_de_en_es_es_fi_fr_it_nb_nl_pl_pt_pt_ru_sv_tr_21444.dmg contains Kaspersky Downloader.app with entitlements com.apple.security.cs.disable-library-validation and com.apple.security.cs.allow-unsigned-executable-memory set to true. This disables library validation, enabling replacement of libkl_appkit.dylib with a malicious proxy. Preparation involves downloading, mounting, and inspecting the bundle.

## Requirements

1. Internet access to download the specific DMG
2. Disk space for mounting the volume
3. codesign tool for entitlement verification

## Defense

Defensive measures and detection strategies:

- Avoid using outdated installers; enforce signature validation in all binaries
- Monitor downloads of legacy software via firewall logs
- Use Gatekeeper and XProtect to block unsigned or modified executables

## Objectives

1. Obtain vulnerable installer version
2. Confirm entitlements for injection
3. Inspect target dylib location

## Instructions

### Step 1: Download and Mount Installer

**Context**: Acquire the vulnerable DMG and mount it to access the app bundle.

Download from Kaspersky archives or mirrors: kavmac20.0.0.829aar_cs_da_de_en_es_es_fi_fr_it_nb_nl_pl_pt_pt_ru_sv_tr_21444.dmg, then mount with hdiutil attach.

> Expected output: Volume mounted at /Volumes/Kaspersky Internet Security.

### Step 2: Inspect Directory and Entitlements

**Context**: Verify the MacOS contents and check for insecure entitlements.

Execute [[commands/list-macos-directory]] to list files:

```bash
ls -l /Volumes/Kaspersky Internet Security/Kaspersky Downloader.app/Contents/MacOS
```

> Explanation: Lists libkl_appkit.dylib for targeting. Expected output: total 3392
-rwxr-xr-x 1 csaby staff 1015904 Oct 9 2019 Downloader
-rwxr-xr-x 1 csaby staff 569152 Oct 9 2019 libkl_appkit.dylib
-rwxr-xr-x 1 csaby staff 144256 Oct 9 2019 libz.1.2.11.dylib

Then check entitlements:

```bash
codesign -d --entitlements :- /Volumes/Kaspersky Internet Security/Kaspersky Downloader.app
```

> Expected output: <key>com.apple.security.cs.disable-library-validation</key><true/> and <key>com.apple.security.cs.allow-unsigned-executable-memory</key><true/>.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer (downloading installer)

### Sub-Techniques


## Commands Used

- [[commands/list-macos-directory]]

## Tools Used


## Tags

- installer
- entitlements
- macos
