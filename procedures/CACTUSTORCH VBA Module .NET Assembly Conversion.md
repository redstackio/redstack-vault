---
id: f6f9be91-4678-4be3-8bf4-0d5dd6ccdae1
name: CACTUSTORCH VBA Module .NET Assembly Conversion
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.675333+00:00'
updated_at: '2023-04-10T20:36:52.271840+00:00'
tags:
- '[[DOCM - CACTUSTORCH VBA Module]]'
- '[[Office - Attacks]]'
commands:
- '[[DotNetToJScript.exe]]'
---

# CACTUSTORCH VBA Module .NET Assembly Conversion

## Summary

The CACTUSTORCH VBA Module is a tool used by threat actors to execute commands on a victim machine. By converting a .NET assembly to JScript, an attacker can evade detection and execute malicious code. This technique is commonly used in targeted attacks and can be difficult to detect due to the use

## Description

# Description

The CACTUSTORCH VBA Module is a tool used by threat actors to execute commands on a victim machine. By converting a .NET assembly to JScript, an attacker can evade detection and execute malicious code. This technique is commonly used in targeted attacks and can be difficult to detect due to the use of legitimate tools.

From a technical standpoint, this technique involves converting a .NET assembly to JScript using the 'Ildasm.exe' and 'jsc.exe' tools. This creates a JScript file that contains the malicious code, which can then be executed on the victim machine. The business value of this technique is that it allows an attacker to gain access to sensitive data or systems, which can be used for financial gain or espionage purposes.

 

## Requirements

1. Access to the CACTUSTORCH VBA Module

1. Access to the 'Ildasm.exe' and 'jsc.exe' tools

 

## Defense

1. Implement strict application whitelisting policies to prevent the execution of unauthorized scripts

1. Regularly monitor and analyze network traffic for any anomalous activity

1. Ensure that all software and systems are up-to-date with the latest security patches

 

## Objectives

1. Execute commands on a victim machine

1. Evade detection

 

# Instructions

1. To convert a .NET assembly to JScript, use the DotNetToJScript.exe tool and provide the path to the assembly file. Use the -l option to specify the language of the output file (in this case, vba). Use the -o option to specify the output file name and location. Use the -c option to specify the name of the class that contains the Main method to be executed.

 



**Code**: [[DotNetToJScript.exeExampleAssembly.dll -l vba -o t]]



> The DotNetToJScript.exe tool allows you to convert a .NET assembly to JScript code. This can be useful for running .NET code on systems that do not have the .NET Framework installed. The -l option specifies the output language, which can be one of vba, jscript, or cscript. The -o option specifies the output file name and location. The -c option specifies the name of the class that contains the Main method to be executed. Note that the output JScript code may not be an exact representation of the original .NET code, and may require additional modifications to work correctly.



**Command** ([[DotNetToJScript.exe]]):

```bash
DotNetToJScript.exeExampleAssembly.dll -l vba -o test.vba -c cactusTorch
```



## Commands Used

- [[DotNetToJScript.exe]]

## Tags

- [[DOCM - CACTUSTORCH VBA Module]]
- [[Office - Attacks]]


