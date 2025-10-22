---
id: 83e9b659-b886-407d-a040-22aeb03738e2
name: VDSO Hijacking
type: sub-technique
mitre_id: T1055.014
mitre_url: null
created_at: '2023-04-06T00:31:26.606539+00:00'
updated_at: '2023-04-06T00:31:26.606539+00:00'
parent_technique: '[[Process Injection|T1055 - Process Injection]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
---

# VDSO Hijacking

**MITRE ID**: T1055.014

**Parent Technique**: [[Process Injection|T1055 - Process Injection]]

This is a sub-technique of T1055 - Process Injection.

## Summary

Adversaries may inject malicious code into processes via VDSO hijacking in order to evade process-based defenses as well as possibly elevate privileges. Virtual dynamic shared object (vdso) hijacking is a method of executing arbitrary code in the address space of a separate live process. 

VDSO hija

## Description

Adversaries may inject malicious code into processes via VDSO hijacking in order to evade process-based defenses as well as possibly elevate privileges. Virtual dynamic shared object (vdso) hijacking is a method of executing arbitrary code in the address space of a separate live process. 

VDSO hijacking involves redirecting calls to dynamically linked shared libraries. Memory protections may prevent writing executable code to a process via [Ptrace System Calls](https://attack.mitre.org/techniques/T1055/008). However, an adversary may hijack the syscall interface code stubs mapped into a process from the vdso shared object to execute syscalls to open and map a malicious shared object. This code can then be invoked by redirecting the execution flow of the process via patched memory address references stored in a process' global offset table (which store absolute addresses of mapped library functions).(Citation: ELF Injection May 2009)(Citation: Backtrace VDSO)(Citation: VDSO Aug 2005)(Citation: Syscall 2014)

Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via VDSO hijacking may also evade detection from security products since the execution is masked under a legitimate process.  

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]
