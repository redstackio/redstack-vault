---
id: 52dd3515-183f-40d7-80bb-8591eca5b5cd
name: Dynamic-link Library Injection
type: sub-technique
mitre_id: T1055.001
mitre_url: null
created_at: '2023-04-06T00:31:27.185617+00:00'
updated_at: '2023-04-06T00:31:27.185617+00:00'
parent_technique: '[[Process Injection|T1055 - Process Injection]]'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[MSSQL Server Extended Stored Procedure DLL Injection]]'
- '[[Windows - Run Programs with Different Permissions using Runas Command]]'
---

# Dynamic-link Library Injection

**MITRE ID**: T1055.001

**Parent Technique**: [[Process Injection|T1055 - Process Injection]]

This is a sub-technique of T1055 - Process Injection.

## Summary

Adversaries may inject dynamic-link libraries (DLLs) into processes in order to evade process-based defenses as well as possibly elevate privileges. DLL injection is a method of executing arbitrary code in the address space of a separate live process.  

DLL injection is commonly performed by writin

## Description

Adversaries may inject dynamic-link libraries (DLLs) into processes in order to evade process-based defenses as well as possibly elevate privileges. DLL injection is a method of executing arbitrary code in the address space of a separate live process.  

DLL injection is commonly performed by writing the path to a DLL in the virtual address space of the target process before loading the DLL by invoking a new thread. The write can be performed with native Windows API calls such as <code>VirtualAllocEx</code> and <code>WriteProcessMemory</code>, then invoked with <code>CreateRemoteThread</code> (which calls the <code>LoadLibrary</code> API responsible for loading the DLL). (Citation: Elastic Process Injection July 2017) 

Variations of this method such as reflective DLL injection (writing a self-mapping DLL into a process) and memory module (map DLL when writing into process) overcome the address relocation issue as well as the additional APIs to invoke execution (since these methods load and execute the files in memory by manually preforming the function of <code>LoadLibrary</code>).(Citation: Elastic HuntingNMemory June 2017)(Citation: Elastic Process Injection July 2017) 

Another variation of this method, often referred to as Module Stomping/Overloading or DLL Hollowing, may be leveraged to conceal injected code within a process. This method involves loading a legitimate DLL into a remote process then manually overwriting the module's <code>AddressOfEntryPoint</code> before starting a new thread in the target process.(Citation: Module Stomping for Shellcode Injection) This variation allows attackers to hide malicious injected code by potentially backing its execution with a legitimate DLL file on disk.(Citation: Hiding Malicious Code with Module Stomping) 

Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via DLL injection may also evade detection from security products since the execution is masked under a legitimate process. 

## Tactics

This sub-technique is used in the following tactics:

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures

There are 2 procedures using this sub-technique:

- [[MSSQL Server Extended Stored Procedure DLL Injection]]
- [[Windows - Run Programs with Different Permissions using Runas Command]]
