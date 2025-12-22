---
id: 9d2a2822-f135-4206-a643-569178311445
name: Detect-.NET-Serialization-Attacks
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:59.065177+00:00'
updated_at: '2023-04-06T03:55:59.078007+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/File and Directory Discovery|T1083 - File and Directory
    Discovery]]
  - '[[techniques/Process Discovery|T1057 - Process Discovery]]'
  - '[[techniques/Software Discovery|T1518 - Software Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Detection]]'
  - '[[tags/.NET Serialization]]'
commands:
  - '[[commands/powershell-search-serialized-files]]'
  - '[[commands/sysmon-configure-dotnet-events]]'
platforms:
  - Windows
tools:
  - '[[tools/Sysmon]]'
validated: true
---

# Detect-.NET-Serialization-Attacks

## Summary

This procedure outlines how to detect potential .NET serialization attacks by monitoring for indicators such as the creation of serialized object files, usage of vulnerable serialization libraries, and suspicious network traffic containing serialized payloads. It enables defenders to identify and respond to attempts where attackers abuse .NET's serialization features to execute arbitrary code via crafted objects.

## Description

.NET serialization converts objects into byte streams for storage or transmission, but attackers can embed malicious code in these streams. When deserialized, this code executes, leading to remote code execution (RCE) or other compromises. This procedure focuses on defensive monitoring using system logs, file system scans, and network analysis to spot IOCs like files with extensions (.dat, .bin, .ser), references to libraries (BinaryFormatter, NetDataContractSerializer, DataContractSerializer), or base64-encoded serialized data in traffic. Applicable in enterprise Windows environments with .NET applications, it helps prevent data exfiltration or persistence by alerting on anomalous serialization activity.

## Requirements

1. Administrative access to Windows systems for log monitoring and tool installation.
2. Sysmon or equivalent EDR tool installed for event logging.
3. Network intrusion detection system (NIDS) like Snort or Suricata for traffic analysis.
4. Knowledge of .NET framework and common serialization abuse patterns.

## Defense

- Implement application whitelisting to restrict use of vulnerable serializers like BinaryFormatter.
- Enable .NET runtime monitoring and disable unsafe deserialization in code.
- Use network segmentation to isolate .NET applications and limit lateral movement.
- Regularly audit file systems and logs for IOCs, and train teams on serialization risks.

## Objectives

1. Identify creation or access of suspicious serialized files on the file system.
2. Detect processes loading .NET serialization libraries in anomalous contexts.
3. Alert on network traffic containing serialized payloads.
4. Respond to potential attacks before code execution or data compromise occurs.

## Instructions

### Step 1: Configure Sysmon for .NET Event Monitoring

**Context**: Sysmon logs process creations, file operations, and module loads related to .NET, allowing detection of serialization library usage or file creations. This step sets up monitoring for relevant events.

**Command** ([[commands/sysmon-configure-dotnet-events]]):
```xml
<Sysmon schemaversion="4.81">
  <EventFiltering>
    <RuleGroup name="" groupRelation="or">
      <ProcessCreate onmatch="include">
        <Image condition="contains">.NET</Image>
        <Module condition="contains">BinaryFormatter</Module>
      </ProcessCreate>
      <FileCreateTime onmatch="include">
        <TargetFilename condition="end with">.dat</TargetFilename>
        <TargetFilename condition="end with">.bin</TargetFilename>
        <TargetFilename condition="end with">.ser</TargetFilename>
      </FileCreateTime>
    </RuleGroup>
  </EventFiltering>
</Sysmon>
```

> Save this as sysmon-dotnet.xml and run `sysmon -i sysmon-dotnet.xml` to install the config. This captures events like process starts involving .NET serializers or file creations with suspicious extensions. Review logs in Event Viewer under Applications and Services Logs > Microsoft > Windows > Sysmon.

### Step 2: Search File System for Serialized Objects

**Context**: Attackers may drop or access serialized files; scanning for common extensions and content patterns (e.g., base64-encoded objects) reveals potential IOCs. Use this to proactively hunt for artifacts.

**Command** ([[commands/powershell-search-serialized-files]]):
```powershell
Get-ChildItem -Path C:\ -Recurse -Include *.dat,*.bin,*.ser -ErrorAction SilentlyContinue | Select-String -Pattern "AAEAAAD" | Select-Object Path, Filename, Line
```

> This PowerShell command recursively searches the C: drive for files with serialization extensions and looks for the .NET serialization header pattern (e.g., from [[codes/.NET-Serialized-Object-Example]]). Expected output includes paths to matching files. If found, analyze with a hex editor or deserializer tool to check for malicious payloads. Run periodically via scheduled tasks for ongoing detection.
