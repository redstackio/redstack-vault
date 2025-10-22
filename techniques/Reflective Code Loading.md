---
id: d561ba0f-62d5-4d58-a439-0eb20a383245
name: Reflective Code Loading
type: technique
mitre_id: T1620
mitre_url: null
created_at: '2023-04-06T00:31:26.044891+00:00'
updated_at: '2023-04-06T00:31:27.809261+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Reflective Code Loading

**MITRE ID**: T1620

## Description

Adversaries may reflectively load code into a process in order to conceal the execution of malicious payloads. Reflective loading involves allocating then executing payloads directly within the memory of the process, vice creating a thread or process backed by a file path on disk. Reflectively loaded payloads may be compiled binaries, anonymous files (only present in RAM), or just snubs of fileless executable code (ex: position-independent shellcode).(Citation: Introducing Donut)(Citation: S1 Custom Shellcode Tool)(Citation: Stuart ELF Memory)(Citation: 00sec Droppers)(Citation: Mandiant BYOL)

Reflective code injection is very similar to [Process Injection](https://attack.mitre.org/techniques/T1055) except that the “injection” loads code into the processes’ own memory instead of that of a separate process. Reflective loading may evade process-based detections since the execution of the arbitrary code may be masked within a legitimate or otherwise benign process. Reflectively loading payloads directly into memory may also avoid creating files or other artifacts on disk, while also enabling malware to keep these payloads encrypted (or otherwise obfuscated) until execution.(Citation: Stuart ELF Memory)(Citation: 00sec Droppers)(Citation: Intezer ACBackdoor)(Citation: S1 Old Rat New Tricks)

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
