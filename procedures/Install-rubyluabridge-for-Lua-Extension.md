---
id: proc-install-rubyluabridge
tags:
  - setup
  - lua
  - gem-install
type: procedure
tools:
  - '[[tools/rvm]]'
  - '[[tools/git]]'
  - '[[tools/apt]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/install-rvm]]'
  - '[[commands/source-rvm]]'
  - '[[commands/rvm-install-ruby]]'
  - '[[commands/git-clone-rubyluabridge]]'
  - '[[commands/apt-install-deps]]'
  - '[[commands/build-extconf]]'
  - '[[commands/make-build]]'
  - '[[commands/cp-rubyluabridge-so]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Python]]'
updated_at: '2025-12-14T17:23:50.181Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Install-rubyluabridge-for-Lua-Extension

## Summary

This procedure installs the rubyluabridge gem on a GitLab Omnibus server to enable the vulnerable Lua extension in the WikiCloth library, setting up the environment for sandbox bypass and RCE exploitation.

## Description

The rubyluabridge gem bridges Ruby and Lua, allowing WikiCloth to process Lua code in MediaWiki pages. Its insecure sandbox in luawrapper.lua uses loadstring without proper isolation, bypassable via pcall to access global functions like io.popen. This procedure targets Ubuntu-based GitLab installs, requiring root access for dependencies and file placement. Prerequisites include server access; outcomes enable Lua execution during wiki rendering, leading to RCE for authenticated editors.

## Requirements

1. Root or sudo access on GitLab server (Linux/Ubuntu)
2. Internet access for downloading RVM, git clone, and apt packages
3. GitLab Omnibus edition with Ruby 2.7.0 path at /opt/gitlab/embedded/lib/ruby/2.7.0

## Defense

Defensive measures and detection strategies:

- Remove or avoid installing rubyluabridge gem in production
- Disable Lua extensions in WikiCloth configuration
- Monitor for unexpected .so file copies in Ruby lib directories
- Audit wiki renders for anomalous io.popen usage via logs

## Objectives

1. Enable Lua processing in WikiCloth for exploitation
2. Prepare server for sandbox bypass payloads
3. Confirm vulnerability setup without alerting

## Instructions

### Step 1: Install RVM

**Context**: Download and set up Ruby Version Manager to handle Ruby installations.

**Command** ([[commands/install-rvm]]):
```bash
curl -sSL https://get.rvm.io | bash
```

> Downloads and executes the RVM installer silently. Expected output includes installation progress and path additions to shell profile.

### Step 2: Source RVM Environment

**Context**: Load RVM into the current shell to use rvm commands.

**Command** ([[commands/source-rvm]]):
```bash
source /etc/profile.d/rvm.sh
```

> Initializes RVM environment variables. No output; verifies with `rvm --version` showing version info.

### Step 3: Install Ruby 2.7.4

**Context**: Install the Ruby version compatible with GitLab for building the gem.

**Command** ([[commands/rvm-install-ruby]]):
```bash
rvm install 2.7.4
```

> Compiles and installs Ruby. Expected output: progress bars and 'Installation of ruby-2.7.4 is complete'.

### Step 4: Clone rubyluabridge Repository

**Context**: Fetch source code for the Ruby-Lua bridge extension.

**Command** ([[commands/git-clone-rubyluabridge]]):
```bash
git clone https://github.com/neomantra/rubyluabridge
```

> Clones the repo into a local directory. Expected output: Cloning progress and 'done' message.

### Step 5: Install Build Dependencies

**Context**: Install Lua and Boost dev libraries required for compilation on Ubuntu.

**Command** ([[commands/apt-install-deps]]):
```bash
sudo apt install liblua5.1-0-dev libboost-dev
```

> Uses apt to fetch and install packages. Expected output: Package lists and 'done' for installations.

### Step 6: Configure Build

**Context**: Run the Ubuntu-specific extconf script to prepare compilation.

**Command** ([[commands/build-extconf]]):
```bash
./build/extconf_ubuntu.sh
```

> Configures the build environment. Expected output: Makefile generation messages.

### Step 7: Compile Extension

**Context**: Build the shared object file for Ruby-Lua integration.

**Command** ([[commands/make-build]]):
```bash
make
```

> Compiles C++ code into rubyluabridge.so. Expected output: Build logs ending in success.

### Step 8: Deploy to GitLab

**Context**: Copy the compiled extension to GitLab's embedded Ruby library.

**Command** ([[commands/cp-rubyluabridge-so]]):
```bash
sudo cp rubyluabridge.so /opt/gitlab/embedded/lib/ruby/2.7.0/rubyluabridge.so
```

> Places the .so file for loading during wiki rendering. Expected output: No error on copy.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Python]] Lua

### Sub-Techniques


## Commands Used

- [[commands/install-rvm]]
- [[commands/source-rvm]]
- [[commands/rvm-install-ruby]]
- [[commands/git-clone-rubyluabridge]]
- [[commands/apt-install-deps]]
- [[commands/build-extconf]]
- [[commands/make-build]]
- [[commands/cp-rubyluabridge-so]]

## Tools Used

- [[tools/rvm]]
- [[tools/git]]
- [[tools/apt]]

## Tags

- setup
- lua
- gem-install
