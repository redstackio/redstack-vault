---
type: procedure
description: >-
  A step-by-step guide to installing Hashcat from source on a Debian-based Linux
  system, including dependency setup and compilation.
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Brute Force]]'
sub_techniques: []
tags:
  - hashcat
  - installation
  - password-cracking
  - credential-access
commands:
  - '[[commands/apt-install-hashcat-build-dependencies]]'
  - '[[commands/git-clone-and-build-hashcat]]'
platforms:
  - Linux
tools:
  - '[[tools/Hashcat]]'
verified: true
validated: true
---

# Install-Hashcat-from-Source

## Summary

This procedure outlines the installation of Hashcat, a powerful password recovery tool, from source on Debian-based Linux distributions like Ubuntu or Kali. It covers installing build dependencies, cloning the repository, compiling, and installing the tool to enable GPU-accelerated password cracking for security testing and credential analysis.

## Description

Hashcat is an advanced password cracking utility that supports numerous hash types and attack modes, leveraging GPU hardware for high-speed cracking. This installation method builds from source to ensure the latest version and compatibility with specific hardware, such as NVIDIA GPUs with CUDA support. It is typically used in penetration testing to assess password strength, recover credentials from captured hashes, or validate security policies. The process requires administrative privileges and assumes a clean Linux environment. Upon completion, Hashcat can be used for offline cracking tasks, contributing to identifying weak credentials in organizational environments.

## Requirements

1. Administrative (sudo) access on a Debian-based Linux system (e.g., Ubuntu, Kali).
2. Internet connectivity for downloading dependencies and the Hashcat repository.
3. A GPU with CUDA support (optional but recommended for performance; CPU-only mode is available).
4. Sufficient disk space (~500MB) and RAM (at least 2GB for compilation).

## Defense

- Restrict software installation privileges to authorized users only to prevent unauthorized tool deployments.
- Monitor system logs for package installations and git clones from external repositories.
- Implement endpoint detection rules for Hashcat execution or related GPU-intensive processes to identify cracking attempts.
- Enforce strong password policies and multi-factor authentication to reduce the impact of cracked credentials.

## Objectives

1. Successfully install Hashcat and its dependencies on the target system.
2. Verify the installation by running basic Hashcat commands.
3. Enable password cracking capabilities for security assessments.

## Instructions

### Step 1: Install Build Dependencies

**Context**: This step installs the essential packages required to compile Hashcat, including build tools, version control, and packaging utilities. These dependencies ensure the build process completes without errors.

**Command** ([[commands/apt-install-hashcat-build-dependencies]]):
```bash
apt install cmake build-essential -y
apt install checkinstall git -y
```

> This command updates the package index implicitly and installs cmake for build configuration, build-essential for compilers, checkinstall for creating .deb packages, and git for repository cloning. Run as sudo if not root. Expected output includes package download progress and confirmation messages like "cmake is already the newest version" or installation summaries. If errors occur (e.g., no sudo), elevate privileges.

### Step 2: Clone and Build Hashcat

**Context**: After dependencies are in place, clone the official Hashcat repository and compile it using make. This produces the executable binary optimized for the system.

**Command** ([[commands/git-clone-and-build-hashcat]]):
```bash
git clone https://github.com/hashcat/hashcat.git && cd hashcat && make -j 8 && make install
```

> This clones the repository, changes directory, compiles with 8 parallel jobs (adjust -j based on CPU cores), and installs to /usr/local/bin. Expected output includes git clone progress, make compilation logs (e.g., "CC example0.c"), and installation confirmation. Verify success by running `hashcat --version`. If compilation fails, check for missing GPU drivers (e.g., install nvidia-cuda-toolkit for CUDA support).
