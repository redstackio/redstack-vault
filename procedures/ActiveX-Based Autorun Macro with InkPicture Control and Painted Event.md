---
id: 0df27b77-592c-4f56-a5d3-d4394d2569d5
name: ActiveX-Based Autorun Macro with InkPicture Control and Painted Event
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:23.734272+00:00'
updated_at: '2023-04-10T20:36:57.996707+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Scripting|T1064 - Scripting]]'
- '[[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]'
tags:
- '[[DOCM - ActiveX-based (InkPicture control, Painted event) Autorun macro]]'
- '[[Office - Attacks]]'
commands:
- '[[Add Microsoft InkPicture Control]]'
---

# ActiveX-Based Autorun Macro with InkPicture Control and Painted Event

## Summary

This procedure involves an ActiveX-based autorun macro that utilizes the InkPicture control and Painted event to download and execute a file using PowerShell. The macro is embedded in a Microsoft Office document with a .docm extension. The InkPicture control allows the attacker to draw or write on 

## Description

# Description

This procedure involves an ActiveX-based autorun macro that utilizes the InkPicture control and Painted event to download and execute a file using PowerShell. The macro is embedded in a Microsoft Office document with a .docm extension. The InkPicture control allows the attacker to draw or write on the document and the Painted event is triggered when the user finishes drawing or writing. This event is exploited to download and execute a malicious PowerShell script from a remote location.

This technique can be used by attackers to bypass security controls and gain a foothold in the target's network. The use of ActiveX controls and PowerShell scripts can make detection and mitigation difficult for defenders.

 

## Requirements

1. The victim must open the malicious Office document with the embedded macro

1. The victim's system must have ActiveX controls enabled

1. The attacker must have a remote location to host the malicious PowerShell script

 

## Defense

1. Disable or restrict the use of ActiveX controls in the organization

1. Implement security controls to detect and block malicious PowerShell scripts

1. Train users to be cautious when opening Office documents from unknown or suspicious sources

 

## Objectives

1. Download and execute a malicious PowerShell script on the victim's system

1. Bypass security controls and gain a foothold in the target's network

 

# Instructions

1. To add the Microsoft InkPicture Control to the Ribbon, follow these steps:
1. Open the document where you want to add the control.
2. Click on the 'Insert' tab in the Ribbon.
3. Click on the 'More Controls' option and select 'Microsoft InkPicture Control' from the list of controls.
4. The control will now be added to the Ribbon.

 



**Code**: [[-> Insert -> More Controls -> Microsoft InkPicture]]



> The Microsoft InkPicture Control is a control that allows users to draw or write on the document using a pen or stylus. This control is useful for applications that require user input or annotations on the document.



**Command** ([[Add Microsoft InkPicture Control]]):

```bash
-> Insert -> More Controls -> Microsoft InkPicture Control
```



2. To download and execute a file using PowerShell, follow these steps:
1. Replace '<host>' with the URL of the file you want to download.
2. Save the code to a file with a '.vbs' extension.
3. Run the file to download and execute the file.

 



**Code**: [[Private Sub InkPicture1_Painted(ByVal hDC As Long,]]



> This command uses a Visual Basic script to download and execute a file from a specified URL using PowerShell. The script creates a new instance of the .NET WebClient class and uses it to download the file to the local system. It then uses the Start-Process cmdlet to execute the downloaded file. This command can be used to automate the download and execution of files from a remote server.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Scripting|T1064 - Scripting]]
- [[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]

## Commands Used

- [[Add Microsoft InkPicture Control]]

## Tags

- [[DOCM - ActiveX-based (InkPicture control, Painted event) Autorun macro]]
- [[Office - Attacks]]


