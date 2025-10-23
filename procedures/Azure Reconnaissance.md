---
id: c0079203-1ded-4fba-b335-0ce2e6e27014
name: Azure Reconnaissance
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:14.651569+00:00'
updated_at: '2023-04-10T20:19:39.791087+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Reconnaissance|TA0043 - Reconnaissance]]'
techniques:
- '[[Active Scanning|T1595 - Active Scanning]]'
- '[[Domain Generation Algorithms|T1483 - Domain Generation Algorithms]]'
- '[[Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
- '[[Search Open Technical Databases|T1596 - Search Open Technical Databases]]'
tags:
- '[[Azure Recon Tools]]'
- '[[Cloud - Azure]]'
commands:
- '[[Activate pipenv virtual environment]]'
- '[[Activate virtual environment]]'
- '[[Activate virtual environment]]'
- '[[Authenticate with RoadRecon API]]'
- '[[Create Backdoor]]'
- '[[Execute Backdoor]]'
- '[[Execute Command]]'
- '[[Execute MSBuild]]'
- '[[Export to CSV, JSON, XML, EXCEL with Certificate Credentials]]'
- '[[Export to CSV, JSON, XML, EXCEL with Certificate Credentials and Password]]'
- '[[Export to PRINT]]'
- '[[Gather data from RoadRecon API]]'
- '[[Get All Secrets]]'
- '[[Get Available VM Disks]]'
- '[[Get Azure AD Users]]'
- '[[Get Resources]]'
- '[[Launch RoadRecon GUI]]'
- '[[Login to Azure]]'
- '[[Navigate to the frontend directory]]'
- '[[Resolve TenantID for a specific username]]'
- '[[Set Role]]'
- '[[Set Subscription]]'
- '[[Start the backend server]]'
- '[[Start the collector]]'
- '[[Start the frontend server]]'
- '[[Unblock files]]'
---

# Azure Reconnaissance

## Summary

Azure Reconnaissance is a set of tools and techniques used to gather information about an organization's Azure environment. This information can be used by attackers to identify potential targets, map out the network, and gain a better understanding of the environment's security posture. The Azure 

## Description

# Description

Azure Reconnaissance is a set of tools and techniques used to gather information about an organization's Azure environment. This information can be used by attackers to identify potential targets, map out the network, and gain a better understanding of the environment's security posture. The Azure Reconnaissance procedure involves using various tools to scan the environment, identify vulnerabilities, and gather information about users, domains, and other resources. This information can then be used to plan and execute further attacks against the organization.

From a technical perspective, Azure Reconnaissance involves using tools such as BloodHound Attack Research Kit (BARK), ROADTool, Azure StormSpotter, Azucar, and PowerZure to gather information about the Azure environment. These tools can be used to identify Azure AD users, enumerate cloud resources, and map out the network topology. The business value of Azure Reconnaissance lies in its ability to identify potential security weaknesses in the organization's Azure environment, allowing them to take proactive measures to improve their security posture.

 

## Requirements

1. Access to the organization's Azure environment.

1. Credentials with sufficient privileges to perform the necessary scans and gather information.

1. Tools such as BloodHound Attack Research Kit (BARK), ROADTool, Azure StormSpotter, Azucar, and PowerZure.

 

## Defense

1. Ensure that all Azure resources are properly configured and secured.

1. Implement strong access controls and authentication mechanisms to prevent unauthorized access to the Azure environment.

1. Regularly monitor the Azure environment for suspicious activity and potential security weaknesses.

 

## Objectives

1. Identify potential targets within an organization's Azure environment.

1. Map out the network topology of the Azure environment.

1. Gather information about users, domains, and other resources in the Azure environment.

 

# Instructions

1. To retrieve all Azure AD users using BARK, run the following commands:

 



**Code**: [[. .\BARK.ps1
$MyRefreshTokenRequest = Get-AZRefres]]



> This command will import the BARK PowerShell module and retrieve a refresh token for the specified Azure AD tenant. It will then use the refresh token to obtain an access token for Microsoft Graph API. Finally, it will retrieve all Azure AD users using the obtained access token and display a progress bar.



**Command** ([[Get Azure AD Users]]):

```bash
. .\BARK.ps1
$MyRefreshTokenRequest = Get-AZRefreshTokenWithUsernamePassword -username "user@contoso.onmicrosoft.com" -password "MyVeryCoolPassword" -TenantID "contoso.onmicrosoft.com"
$MyMSGraphToken = Get-MSGraphTokenWithRefreshToken -RefreshToken $MyRefreshTokenRequest.refresh_token -TenantID "contoso.onmicrosoft.com"
$MyAADUsers = Get-AllAzureADUsers -Token $MyMSGraphToken.access_token -ShowProgress
```



2. This JSON object contains details of the commands for the ROADTool framework. The commands are as follows:
1. `roadrecon auth`: This command is used to authenticate to Azure Active Directory. The command takes in several arguments such as `-u` for username, `-p` for password, `-t` for tenant, `-c` for client, `--as-app`, `--device-code`, `--access-token`, `--refresh-token`, `-f` for tokenfile, and `--tokens-stdout`.
2. `roadrecon gather`: This command is used to gather information from Azure Active Directory. The command takes in several arguments such as `-d` for database, `-f` for tokenfile, `--tokens-stdin`, and `--mfa`.
3. `roadrecon gui`: This command is used to launch the GUI of the ROADTool framework.

 



**Code**: [[pipenv shell
roadrecon auth [-h] [-u USERNAME] [-p]]



> The `roadrecon auth` command is used to authenticate to Azure Active Directory. This command takes in several arguments such as `-u` for username, `-p` for password, `-t` for tenant, `-c` for client, `--as-app`, `--device-code`, `--access-token`, `--refresh-token`, `-f` for tokenfile, and `--tokens-stdout`. The `-u` argument is used to specify the username of the user that needs to be authenticated. The `-p` argument is used to specify the password for the user. The `-t` argument is used to specify the tenant name. The `-c` argument is used to specify the client ID. The `--as-app` argument is used to authenticate as an application. The `--device-code` argument is used to authenticate using device code. The `--access-token` argument is used to specify the access token. The `--refresh-token` argument is used to specify the refresh token. The `-f` argument is used to specify the token file. The `--tokens-stdout` argument is used to output the tokens to stdout.

The `roadrecon gather` command is used to gather information from Azure Active Directory. This command takes in several arguments such as `-d` for database, `-f` for tokenfile, `--tokens-stdin`, and `--mfa`. The `-d` argument is used to specify the database name. The `-f` argument is used to specify the token file. The `--tokens-stdin` argument is used to read tokens from stdin. The `--mfa` argument is used to enable multifactor authentication.

The `roadrecon gui` command is used to launch the GUI of the ROADTool framework.



**Command** ([[Activate pipenv virtual environment]]):

```bash
pipenv shell
```





**Command** ([[Authenticate with RoadRecon API]]):

```bash
roadrecon auth -u test@<TENANT NAME>.onmicrosoft.com -p <PASSWORD>
```





**Command** ([[Gather data from RoadRecon API]]):

```bash
roadrecon gather
```





**Command** ([[Launch RoadRecon GUI]]):

```bash
roadrecon gui
```



3. Follow the below commands to start the StormSpotter tool:

 



**Code**: [[# session 1 - backend
- Activate virtual environme]]



> - In session 1, activate the virtual environment and start the backend server.
- In session 2, navigate to the frontend directory and start the frontend server.
- In session 3, activate the virtual environment, login to Azure and start the collector.
- Access the StormSpotter tool on http://localhost:9091 with the provided credentials.



**Command** ([[Activate virtual environment]]):

```bash
pipenv shell
```





**Command** ([[Start the backend server]]):

```bash
python ssbackend.pyz
```





**Command** ([[Navigate to the frontend directory]]):

```bash
cd C:\Tools\stormspotter\frontend\dist\spa\
```





**Command** ([[Start the frontend server]]):

```bash
quasar.cmd serve -p 9091 --history
```





**Command** ([[Activate virtual environment]]):

```bash
pipenv shell
```





**Command** ([[Login to Azure]]):

```bash
az login -u test@<TENANT NAME>.onmicrosoft.com -p <PASSWORD>
```





**Command** ([[Start the collector]]):

```bash
python C:\Tools\stormspotter\stormcollector\sscollector.pyz cli
```



4. To execute the Azucar command, follow the below instructions:
1. Ensure that you are using an account with at least read-permission on the assets you want to access.
2. Run the command `Get-ChildItem -Recurse c:\Azucar_V10 | Unblock-File`.
3. Run the command `.\Azucar.ps1 -AuthMode UseCachedCredentials -Verbose -WriteLog -Debug -ExportTo PRINT` to export the data to PRINT.
4. Run the command `.\Azucar.ps1 -ExportTo CSV,JSON,XML,EXCEL -AuthMode Certificate_Credentials -Certificate C:\AzucarTest\server.pfx -ApplicationId 00000000-0000-0000-0000-000000000000 -TenantID 00000000-0000-0000-0000-000000000000` to export the data to CSV, JSON, XML, or EXCEL. Ensure that you replace the certificate and application ID with your own.
5. Run the command `.\Azucar.ps1 -ExportTo CSV,JSON,XML,EXCEL -AuthMode Certificate_Credentials -Certificate C:\AzucarTest\server.pfx -CertFilePassword MySuperP@ssw0rd! -ApplicationId 00000000-0000-0000-0000-000000000000 -TenantID 00000000-0000-0000-0000-000000000000` to export the data to CSV, JSON, XML, or EXCEL. Ensure that you replace the certificate, certificate file password, and application ID with your own.
6. To resolve the TenantID for a specific username, run the command `.\Azucar.ps1 -ResolveTenantUserName user@company.com`.

 



**Code**: [[# You should use an account with at least read-per]]



> The Azucar command is a PowerShell script that automatically gathers a variety of configuration data and analyses all data relating to a particular subscription in order to determine security risks. The command has various arguments, which are:
- `AuthMode`: Specifies the authentication mode to use. This argument has two possible values: `UseCachedCredentials` and `Certificate_Credentials`.
- `Verbose`: Specifies whether to enable verbose output.
- `WriteLog`: Specifies whether to write the output to a log file.
- `Debug`: Specifies whether to enable debug output.
- `ExportTo`: Specifies the format in which to export the data. This argument has four possible values: `PRINT`, `CSV`, `JSON`, `XML`, and `EXCEL`.
- `Certificate`: Specifies the path to the certificate file to use for authentication.
- `CertFilePassword`: Specifies the password for the certificate file.
- `ApplicationId`: Specifies the ID of the application to use for authentication.
- `TenantID`: Specifies the ID of the tenant to use for authentication.
- `ResolveTenantUserName`: Resolves the TenantID for a specific username.



**Command** ([[Unblock files]]):

```bash
Get-ChildItem -Recurse c:\Azucar_V10 | Unblock-File
```





**Command** ([[Export to PRINT]]):

```bash
.\Azucar.ps1 -AuthMode UseCachedCredentials -Verbose -WriteLog -Debug -ExportTo PRINT
```





**Command** ([[Export to CSV, JSON, XML, EXCEL with Certificate Credentials]]):

```bash
.\Azucar.ps1 -ExportTo CSV,JSON,XML,EXCEL -AuthMode Certificate_Credentials -Certificate C:\AzucarTest\server.pfx -ApplicationId 00000000-0000-0000-0000-000000000000 -TenantID 00000000-0000-0000-0000-000000000000
```





**Command** ([[Export to CSV, JSON, XML, EXCEL with Certificate Credentials and Password]]):

```bash
.\Azucar.ps1 -ExportTo CSV,JSON,XML,EXCEL -AuthMode Certificate_Credentials -Certificate C:\AzucarTest\server.pfx -CertFilePassword MySuperP@ssw0rd! -ApplicationId 00000000-0000-0000-0000-000000000000 -TenantID 00000000-0000-0000-0000-000000000000
```





**Command** ([[Resolve TenantID for a specific username]]):

```bash
.\Azucar.ps1 -ResolveTenantUserName user@company.com
```



5. To use this tool, first run the `git submodule init` and `git submodule update` commands. Then, import the AzureRM and AzuriteExplorer modules using the `Import-Module` command. Finally, review your Azure subscriptions using the `Review-AzureRmSubscription` and `Review-CustomAzureRmSubscription` commands.

 



**Code**: [[git submodule init
git submodule update
PS> Import]]



> This tool is designed to help security professionals perform enumeration and reconnaissance activities in the Microsoft Azure cloud. The `git submodule init` and `git submodule update` commands are used to download the necessary dependencies. The `Import-Module` commands are used to load the required PowerShell modules. Finally, the `Review-AzureRmSubscription` and `Review-CustomAzureRmSubscription` commands are used to review your Azure subscriptions and gather information about the resources in those subscriptions.

6. To gather information about Azure domains, import the MicroBurst module and the Get-AzureDomainInfo script. Then, use the Get-AzureDomainInfo command with the desired options.

 



**Code**: [[PS C:> Import-Module .\MicroBurst.psm1
PS C:> Impo]]



> The Get-AzureDomainInfo command is used to gather information about Azure domains. The -folder option specifies the folder where the output files will be saved. The -Verbose option provides detailed information about the execution of the command. This command can be used to discover Azure services, audit weak configurations, and perform post-exploitation actions such as credential dumping.

7. The PowerZure Azure Security Assessment Commands allow users to perform various security assessment tasks on their Azure environment. The commands are divided into several categories based on the user's role in the environment - Reader, Contributor, Owner, and Administrator. Each category has a set of commands that can be used to perform specific tasks. For example, the Contributor category has commands like Execute-Command and Execute-MSBuild that allow users to execute commands and build scripts on a virtual machine in the Azure environment. Similarly, the Owner category has a Set-Role command that allows users to set a role for a specific user on a resource in the Azure environment.

 



**Code**: [[# Require az module !
$ ipmo .\PowerZure
$ Set-Sub]]



> The PowerZure Azure Security Assessment Commands are written in PowerShell and require the az module to be installed. The commands are divided into several categories based on the user's role in the environment - Reader, Contributor, Owner, and Administrator. Each category has a set of commands that can be used to perform specific tasks. The Reader category has commands like Get-Runbook, Get-AllUsers, Get-Apps, Get-Resources, Get-WebApps, and Get-WebAppDetails that allow users to retrieve information about the resources in the Azure environment. The Contributor category has commands like Execute-Command and Execute-MSBuild that allow users to execute commands and build scripts on a virtual machine in the Azure environment. The category also has commands like Get-AllSecrets, Get-AvailableVMDisks, and Get-VMDisk that allow users to retrieve information about the secrets, disks, and virtual machines in the Azure environment. The Owner category has a Set-Role command that allows users to set a role for a specific user on a resource in the Azure environment. The Administrator category has commands like Create-Backdoor and Execute-Backdoor that allow users to create and execute backdoors on a virtual machine in the Azure environment.



**Command** ([[Set Subscription]]):

```bash
$ Set-Subscription -Id [idgoeshere]
```





**Command** ([[Get Resources]]):

```bash
$ Get-Resources
```





**Command** ([[Execute Command]]):

```bash
$ Execute-Command -OS Windows -VM Win10Test -ResourceGroup Test-RG -Command "whoami"
```





**Command** ([[Execute MSBuild]]):

```bash
$ Execute-MSBuild -VM Win10Test  -ResourceGroup Test-RG -File "build.xml"
```





**Command** ([[Get All Secrets]]):

```bash
$ Get-AllSecrets # AllAppSecrets, AllKeyVaultContents
```





**Command** ([[Get Available VM Disks]]):

```bash
$ Get-AvailableVMDisks, Get-VMDisk # Download a virtual machine's disk
```





**Command** ([[Set Role]]):

```bash
$ Set-Role -Role Contributor -User test@contoso.com -Resource Win10VMTest
```





**Command** ([[Create Backdoor]]):

```bash
$ Create-Backdoor
```





**Command** ([[Execute Backdoor]]):

```bash
$ Execute-Backdoor
```



## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Discovery|TA0007 - Discovery]]
- [[Reconnaissance|TA0043 - Reconnaissance]]

### Techniques

- [[Active Scanning|T1595 - Active Scanning]]
- [[Domain Generation Algorithms|T1483 - Domain Generation Algorithms]]
- [[Domain Trust Discovery|T1482 - Domain Trust Discovery]]
- [[Search Open Technical Databases|T1596 - Search Open Technical Databases]]

## Commands Used

- [[Activate pipenv virtual environment]]
- [[Activate virtual environment]]
- [[Activate virtual environment]]
- [[Authenticate with RoadRecon API]]
- [[Create Backdoor]]
- [[Execute Backdoor]]
- [[Execute Command]]
- [[Execute MSBuild]]
- [[Export to CSV, JSON, XML, EXCEL with Certificate Credentials]]
- [[Export to CSV, JSON, XML, EXCEL with Certificate Credentials and Password]]
- [[Export to PRINT]]
- [[Gather data from RoadRecon API]]
- [[Get All Secrets]]
- [[Get Available VM Disks]]
- [[Get Azure AD Users]]
- [[Get Resources]]
- [[Launch RoadRecon GUI]]
- [[Login to Azure]]
- [[Navigate to the frontend directory]]
- [[Resolve TenantID for a specific username]]
- *...and 6 more*

## Tags

- [[Azure Recon Tools]]
- [[Cloud - Azure]]


