---
id: 91c0db01-9526-4239-82e3-7bacfabd0711
name: Regsvcs/Regasm
type: technique
mitre_id: T1121
mitre_url: null
created_at: '2019-08-28T21:17:33.159591+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
procedures:
- '[[Windows - Regasm / Regsvc Payload Execution]]'
---

# Regsvcs/Regasm

**MITRE ID**: T1121

## Description

Regsvcs and Regasm are Windows command-line utilities that are used to register .NET Component Object Model (COM) assemblies. Both are digitally signed by Microsoft. [1] [2]Adversaries can use Regsvcs and Regasm to proxy execution of code through a trusted Windows utility. Both utilities may be used to bypass process whitelisting through use of attributes within the binary to specify code that should be run before registration or unregistration: [ComRegisterFunction] or [ComUnregisterFunction] respectively. The code with the registration and unregistration attributes will be executed even if the process is run under insufficient privileges and fails to execute. [3]

# Detection

Use process monitoring to monitor the execution and arguments of Regsvcs.exe and Regasm.exe. Compare recent invocations of Regsvcs.exe and Regasm.exe with prior history of known good arguments and executed binaries to determine anomalous and potentially adversarial activity. Command arguments used before and after Regsvcs.exe or Regasm.exe invocation may also be useful in determining the origin and purpose of the binary being executed.

# Mitigation

Regsvcs and Regasm may not be necessary within a given environment. Block execution of Regsvcs.exe and Regasm.exe if they are not required for a given system or network to prevent potential misuse by adversaries.

# Footnotes

[1] Microsoft. (n.d.). Regsvcs.exe (.NET Services Installation Tool). Retrieved July 1, 2016.

[2] Microsoft. (n.d.). Regasm.exe (Assembly Registration Tool). Retrieved July 1, 2016.

[3] Smith, C. (2016, August 17). Includes 5 Known Application Whitelisting/ Application Control Bypass Techniques in One File. Retrieved June 30, 2017.

## Defense

Regsvcs and Regasm may not be necessary within a given environment. Block execution of Regsvcs.exe and Regasm.exe if they are not required for a given system or network to prevent potential misuse by adversaries.

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

## Related Procedures (1)

- [[Windows - Regasm / Regsvc Payload Execution]]
