---
id: 6df7d997-8b79-405f-8d3c-6aa17758050b
type: procedure
verified: true
submitted: true
created_at: '2020-03-04T05:01:54.843816+00:00'
updated_at: '2023-05-25T19:47:41.193609+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/Security Software Discovery|T1063 - Security Software
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/applocker]]'
  - '[[tags/Enumeration]]'
commands:
  - '[[commands/powershell-get-applocker-policy-xml]]'
  - '[[commands/xmllint-format-xml-file]]'
platforms:
  - Windows
tools: []
validated: true
---

# Enumerate-AppLocker-Rules

## Summary

This procedure retrieves and analyzes AppLocker policy rules on a Windows system, which control the execution of applications, scripts, and other files. It allows attackers or security testers to understand restrictions in place, identify allowed paths or publishers, and potentially find bypass opportunities during red team engagements or penetration testing.

## Description

AppLocker is a Windows security feature that enforces application control policies to permit or deny the execution of files based on attributes like path, publisher, file hash, or extension. Rules can apply to executables (.exe), scripts (.ps1, .bat, etc.), Windows Installer packages (.msi), packaged apps, and DLLs (.dll). If AppLocker is configured in audit or enforce mode, unprivileged users can often query the effective policy to enumerate these rules. This procedure exports the policy in XML format for easy parsing and review, optionally formatting it for readability. It is useful in discovery phases to map out the environment's defenses and plan subsequent actions like testing restricted executions.

## Requirements

1. Access to a Windows system with PowerShell 3.0 or later (AppLocker module is built-in on Windows 7+ Enterprise editions or Server 2008 R2+).
2. Local or remote execution privileges (typically low-privilege user is sufficient, as policy viewing doesn't require admin rights unless restricted).
3. For the optional formatting step: A Linux/Unix-like system (e.g., Kali Linux) with xmllint installed, and the XML output transferred from the Windows host.
4. Network access if executing remotely via tools like WinRM or PSEXEC.

## Defense

Defensive measures and detection strategies:

- Enable advanced auditing for PowerShell execution to log module imports and command invocations (Group Policy: Computer Configuration > Policies > Windows Settings > Security Settings > Advanced Audit Policy Configuration > Detailed Tracking > Audit Process Creation).
- Restrict AppLocker policy visibility using Group Policy to prevent non-admin users from querying policies (though this is uncommon).
- Monitor for anomalous PowerShell usage, such as Import-Module AppLocker without legitimate context, using EDR tools like Sysmon or Windows Defender ATP.
- For XML transfer and processing: Network monitoring for unusual file transfers from Windows endpoints to Linux hosts.

## Objectives

1. Export the effective AppLocker policy to identify enforcement modes and rule details for each file type.
2. Analyze rules to determine allowed/denied executions, aiding in evasion planning.
3. Optionally format the output for human-readable review to spot misconfigurations quickly.

## Instructions

### Step 1: Export AppLocker Policy in XML Format

**Context**: This step uses PowerShell to import the AppLocker module and retrieve the effective policy in XML, which includes all rule collections for executables, scripts, DLLs, etc. The XML output reveals enforcement modes (Enabled, Audit, Disabled) and specific rules, helping assess the policy's restrictiveness without needing administrative privileges.

**Command** ([[commands/powershell-get-applocker-policy-xml]]):

```powershell
powershell -nop -c "Import-Module AppLocker; Get-AppLockerPolicy -Effective -Xml"
```

> This command bypasses profile loading (-nop) for stealth and outputs the policy directly. If the system lacks the AppLocker module (e.g., non-Enterprise edition), it will error out, indicating no policy is present. Save the output to a file for analysis: `... | Out-File -Encoding UTF8 applocker.xml`. Non-XML output can be obtained by omitting -Xml, but XML is preferred for parsing.

### Step 2: Format XML Output for Readability (Optional)

**Context**: If the raw XML is lengthy or unformatted, transfer it to a Linux host and use xmllint to pretty-print it. This makes it easier to review rule details like file paths, SIDs, and actions (Allow/Deny), revealing potential bypasses such as overly permissive default rules.

**Command** ([[commands/xmllint-format-xml-file]]):

```bash
xmllint --format - < $_FILE.xml
```

> Pipe the XML file into xmllint for indentation and structure. Replace $_FILE.xml with the actual filename (e.g., applocker.xml). This step assumes the file has been copied from Windows (e.g., via SMB or SCP). Review the formatted output for sections like <RuleCollection Type="Exe"> to identify enforceable rules.
