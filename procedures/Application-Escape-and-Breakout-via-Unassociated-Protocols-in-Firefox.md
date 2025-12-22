---
id: c25ae809-f867-40df-a215-1b289cba3048
name: Application-Escape-and-Breakout-via-Unassociated-Protocols-in-Firefox
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:17.510672+00:00'
updated_at: '2023-04-06T03:56:17.525269+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Abuse Elevation Control Mechanism|T1548 - Abuse Elevation
    Control Mechanism]]
  - >-
    [[techniques/Exploitation for Client Execution|T1203 - Exploitation for
    Client Execution]]
sub_techniques:
  - >-
    [[sub-techniques/Bypass User Account Control|T1548.002 - Bypass User Account
    Control]]
tags:
  - '[[tags/Application Escape and Breakout]]'
  - '[[tags/Firefox]]'
  - '[[tags/Unassociated Protocols]]'
commands:
  - '[[commands/firefox-create-test-profile]]'
  - '[[commands/firefox-open-irc-with-test-profile]]'
platforms:
  - Windows
tools:
  - '[[tools/Firefox]]'
validated: true
---

# Application-Escape-and-Breakout-via-Unassociated-Protocols-in-Firefox

## Summary

Application escape and breakout via unassociated protocols in Firefox is a technique used by attackers to bypass browser sandbox restrictions and security mechanisms by leveraging protocol handlers for unassociated schemes like IRC. This involves creating a custom Firefox profile and launching the browser to a protocol URL that may invoke external applications or allow code execution outside the controlled environment, potentially evading defenses like User Account Control (UAC).

## Description

This procedure targets Firefox on Windows systems where an attacker has initial command execution access. By directing the browser to an unassociated protocol (e.g., irc://), the browser may attempt to handle it externally, such as prompting for a handler or launching a default application, enabling sandbox escape. A custom profile isolates the attack, allowing configuration of extensions or settings that facilitate privilege escalation or payload delivery. This aligns with exploiting client-side execution flaws to achieve broader system access, such as running arbitrary code with elevated privileges. The technique is useful in scenarios where the attacker is confined to a low-privilege context and needs to breakout for lateral movement or persistence.

## Requirements

1. Local shell access on a Windows target with Firefox installed (version 50+ recommended for profile management).
2. User-level permissions sufficient to create directories and execute browser binaries.
3. No administrative privileges required initially, but the breakout may aim to achieve elevation.

## Defense

- Apply the latest security patches to Firefox and the underlying OS to address protocol handling vulnerabilities.
- Configure group policies or browser settings to block or prompt for external protocol requests (e.g., via about:config settings like network.protocol-handler.external.irc).
- Implement application whitelisting (e.g., AppLocker or WDAC) to restrict external application launches from browsers.
- Monitor for anomalous browser process spawns and profile creations using EDR tools.

## Objectives

1. Escape the Firefox sandbox to execute code in an external context.
2. Bypass elevation controls like UAC to gain higher privileges.
3. Establish a foothold for further post-exploitation activities, such as persistence or data exfiltration.

## Instructions

### Step 1: Create Custom Firefox Profile

**Context**: A dedicated profile ensures isolation and allows custom configurations (e.g., disabled security features or malicious extensions) without impacting the default user profile. This step prepares the environment for the protocol-based breakout.

**Command** ([[commands/firefox-create-test-profile]]):
```bash
firefox -CreateProfile "Test" .\\test_profile
```

> This command creates a new profile directory. The profile name "Test" will be used in subsequent steps, and the path specifies where the profile files are stored. Run this from a shell with access to the Firefox executable. Why: Custom profiles can be pre-configured offline to weaken sandboxing or load payloads.

**Expected Output**: Firefox launches briefly and closes, creating a 'test_profile' directory containing profiles.ini and other files. Success is confirmed by listing the directory: `dir test_profile` shows the profile structure.

### Step 2: Launch Firefox with Profile and Target Unassociated Protocol

**Context**: Directing Firefox to an unassociated protocol like irc:// with the custom profile triggers handler resolution, which can lead to external application invocation if a handler is registered or prompt for one, enabling the escape from browser constraints.

**Command** ([[commands/firefox-open-irc-with-test-profile]]):
```bash
firefox irc://127.0.0.1 -P "Test"
```

> The -P flag specifies the profile, and irc:// is an example unassociated protocol (adjust to target-specific schemes like custom URIs). This may launch an external IRC client or allow file/protocol association exploits. Why: Unassociated protocols often bypass browser security as they defer handling to the OS.

**Expected Output**: Firefox opens using the Test profile and navigates to the URL, potentially displaying a prompt for protocol handling or spawning an external process (e.g., default IRC app). Check task manager for new processes spawned from firefox.exe.

### Step 3: Verify Breakout and Privilege Escalation

**Context**: Confirm the protocol invocation resulted in sandbox escape by monitoring for external execution and checking if elevated access was gained, such as through a launched handler with UAC bypass.

**Instructions**: After execution, use tasklist or Process Explorer to inspect child processes of Firefox. If a payload was associated with the protocol (e.g., via registry hijack), test for elevated shell access by attempting a privileged command like `whoami /priv`. Decision point: If no external launch occurs, register a custom handler in the profile's prefs.js to force execution.

**Expected Output**: Evidence of external process (e.g., cmd.exe or custom payload) running outside Firefox sandbox, possibly with SeDebugPrivilege enabled. Success if whoami shows elevated token.

**Success Indicators**:
- New processes spawned independently of Firefox.
- Protocol prompt or handler execution without browser errors.
- Elevated privileges confirmed via token inspection.
