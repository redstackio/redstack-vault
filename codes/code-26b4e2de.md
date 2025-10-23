---
id: 26b4e2de-1c57-47de-8542-89f7c20b93d9
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:16.551254+00:00'
updated_at: '2023-04-10T20:36:25.322657+00:00'
---

# Code Snippet 26b4e2de

**Language**: Powershell

```powershell
Beacon Remote Exploits
======================
jump [module] [target] [listener] 

    psexec	x86	Use a service to run a Service EXE artifact
    psexec64	x64	Use a service to run a Service EXE artifact
    psexec_psh	x86	Use a service to run a PowerShell one-liner
    winrm	x86	Run a PowerShell script via WinRM
    winrm64	x64	Run a PowerShell script via WinRM

Beacon Remote Execute Methods
=============================
remote-exec [module] [target] [command] 

    Methods                         Description
    -------                         -----------
    psexec                          Remote execute via Service Control Manager
    winrm                           Remote execute via WinRM (PowerShell)
    wmi                             Remote execute via WMI (PowerShell)

```


