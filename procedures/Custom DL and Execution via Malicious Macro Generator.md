---
id: 2ef052ce-571d-4800-949d-b2dbf0dc3976
name: Custom DL and Execution via Malicious Macro Generator
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.701408+00:00'
updated_at: '2023-04-10T20:36:49.656337+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Drive-by Compromise|T1189 - Drive-by Compromise]]'
- '[[Scripting|T1064 - Scripting]]'
- '[[User Execution|T1204 - User Execution]]'
tags:
- '[[DOCM - MMG with Custom DL + Exec]]'
- '[[Office - Attacks]]'
commands:
- '[[Clone repository from GitHub]]'
- '[[Configure payload settings]]'
- '[[Generate malicious VBA macro]]'
---

# Custom DL and Execution via Malicious Macro Generator

## Summary

This procedure involves the creation of a malicious macro generator that will download and execute a custom payload from a remote server. Once the macro is executed, the payload will be downloaded and executed on the victim's machine. This technique is commonly used for initial access and can be us

## Description

# Description

This procedure involves the creation of a malicious macro generator that will download and execute a custom payload from a remote server. Once the macro is executed, the payload will be downloaded and executed on the victim's machine. This technique is commonly used for initial access and can be used to gain a foothold in the target environment. 

To execute this procedure, the attacker will create a macro that will download and execute a payload from a remote server. The macro can be included in a legitimate-looking document that will be sent to the victim via email or other means. Once the victim opens the document and enables macros, the payload will be downloaded and executed on the victim's machine. This technique is effective because it leverages the trust that users have in documents and the ease of social engineering to get them to enable macros. 

The business value of this procedure is that it can be used to gain a foothold in a target environment and can be used to steal sensitive information or to launch further attacks.

## Requirements

1. Access to a remote server to host the payload

1. Ability to create a malicious macro generator

1. Ability to social engineer the victim into enabling macros

## Defense

1. Disable macros by default in Microsoft Office

1. Educate users on the dangers of enabling macros from unknown sources

1. Implement application whitelisting to prevent the execution of unknown macros

## Objectives

1. Gain initial access to the target environment

1. Download and execute a custom payload

# Instructions

1. Follow the steps below to generate a malicious macro using Malicious Macro Generator:
1. Clone the MaliciousMacroGenerator repository from GitHub using the command 'git clone https://github.com/Mr-Un1k0d3r/MaliciousMacroGenerator'
2. Navigate to the cloned directory and run the command 'python MMG.py configs/generic-cmd.json malicious.vba'
3. A malicious macro will be generated and saved as malicious.vba in the current directory.

**Code**: [[git clone https://github.com/Mr-Un1k0d3r/Malicious]]

> The generated macro is designed to execute a generic command payload with no evasion technique. The payload will execute the command 'cmd.exe /c C:\\Users\\Public\\beacon.exe' on the target system.

**Command** ([[Clone repository from GitHub]]):

```bash
git clone https://github.com/Mr-Un1k0d3r/MaliciousMacroGenerator
```

**Command** ([[Generate malicious VBA macro]]):

```bash
python MMG.py configs/generic-cmd.json malicious.vba
```

**Command** ([[Configure payload settings]]):

```bash
{
    "description": "Generic command exec payload\nEvasion technique set to none",
    "template": "templates/payloads/generic-cmd-template.vba",
    "varcount": 152,
    "encodingoffset": 5,
    "chunksize": 180,
    "encodedvars": 	{},
    "vars": 	[],
    "evasion": 	["encoder"],
    "payload": "cmd.exe /c C:\\Users\\Public\\beacon.exe"
}
```

2. The code above contains a function named 'DownloadFileA' which takes two arguments: URL and DownloadPath. The function downloads a file from the given URL and saves it to the specified download path. If the download is successful, the function returns True, otherwise it returns False. The code also contains two subroutines named 'AutoOpen' and 'Auto_Open' which are executed automatically when the Excel file is opened. These subroutines call the 'DownloadFileA' function to download a file from the specified URL and save it to the specified path.

**Code**: [[Private Declare PtrSafe Function URLDownloadToFile]]

> This code can be used to download a file from a remote server and save it to a local path. The 'DownloadFileA' function can be called with the URL of the file to be downloaded and the local path where the file should be saved. The function checks if the parent folder of the download path exists, and if it does not, the function exits without downloading the file. If the download is successful, the function returns True, otherwise it returns False. The 'AutoOpen' and 'Auto_Open' subroutines are executed automatically when the Excel file is opened, and they call the 'DownloadFileA' function with the URL and download path specified in the code.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Drive-by Compromise|T1189 - Drive-by Compromise]]
- [[Scripting|T1064 - Scripting]]
- [[User Execution|T1204 - User Execution]]

## Commands Used

- [[Clone repository from GitHub]]
- [[Configure payload settings]]
- [[Generate malicious VBA macro]]

## Tags

- [[DOCM - MMG with Custom DL + Exec]]
- [[Office - Attacks]]
