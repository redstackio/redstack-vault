---
id: 5a180f5b-51ba-4a3b-b9f8-846246a6f60f
name: PowerSploit Cheatsheet
type: cheatsheet
verified: false
created_at: '2020-07-14T18:21:07.426653+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# PowerSploit Cheatsheet

# Description

PowerSploit is a collection of Microsoft PowerShell modules that can be used to aid penetration testers during all phases of an assessment. PowerSploit is comprised of multiple modules and scripts.



## PowerUp



**Command** ([[Performs multiple local host privilege escalation checks for common Windows misconfigurations.]]):

```bash
Invoke-AllChecks

```





[See cheat sheet for more commands](https://github.com/HarmJ0y/CheatSheets/blob/master/PowerUp.pdf)



## PowerView

Requires domain user privileges



**Command** ([[Find Administrative users logged in across the domain – default group = Domain Admins]]):

```bash
Invoke-UserHunter -Threads 15 -NoPing [-GroupName “Enterprise Admins”]
Invoke-UserHunter -Threads 20 -GroupName "Domain Admins" -SearchForest -CheckAccess

```







**Command** ([[Find User (Stealthy via Fileshares)]]):

```bash
Invoke-UserHunter -Stealth -Threads 5 -NoPing [-GroupName “Enterprise Admins”] [-UserName "svcAccount"]

```







**Command** ([[Get domain user info]]):

```bash
Get-NetUser [-UserName john] Get-NetUser -Domain | Select-Object objectsid,lockouttime,samaccounttype,accountexpires,objectclass,useraccountcontrol,@{Name='memberof';Expression={[string]::join(";",($_.memberof))}},info,distinguishedname,adspath,cn,pwdlastset,objectguid,whencreated,description,samaccountname,usnchanged,name| export-csv userprops_members.csv

```







**Command** ([[Find group names]]):

```bash
Get-NetGroup [-GroupName *admin*]

```







**Command** ([[Get group members]]):

```bash
Get-NetGroupMember [-GroupName “Domain Admins”]

```







**Command** ([[Find open shares – Noisy]]):

```bash
Invoke-ShareFinder -CheckShareAccess

```







**Command** ([[Find open (non-default i.e. C$) shares by LDAP source]]):

```bash
Invoke-ShareFinder -ComputerADSPath "LDAP://OU=Servers,OU=IT,DC=domain,DC=com" -CheckShareAccess -ExcludeStandard | Out-File -Encoding ascii c:\windows\temp\server_shares.txt Invoke-ShareFinder -ExcludePrint -ExcludeIPC -CheckShareAccess

```







**Command** ([[Find interesting files]]):

```powershell
powershell Invoke-FileFinder -ComputerName -share share_list.txt -terms ssn,pass,sensitive,secret,admin,login,unattend*.xml,web.config,account -Threads 20 | export-csv filefinder_shares.csv

```







**Command** ([[ Find machines on the domain the current user has local admin access to]]):

```bash
Find-LocalAdminAccess

```







**Command** ([[Get details of all domain computers and export to a CSV file for easy viewing]]):

```bash
Get-computerproperty -Domain -properties displayname,adspath,lastlogontimestamp,operatingsystem,operatingsystemversion,@{Name='memberof';Expression={[string]::join(";",($_.memberof))}}|export-csv computerprops.csv

```







**Command** ([[Get Computers with Unconstrained Delegation]]):

```bash
Get-NetComputer -Unconstrained |ft -a

```







**Command** ([[Get Users & Computers Trusted for Delegation]]):

```bash
Get-DomainUser -TrustedtoAuth -Properties distinguisedname,useraccountcontrol,msds-allowedtodelegateto|fl Get-DomainComputer -TrustedtoAuth -Properties distinguisedname,useraccountcontrol,msds-allowedtodelegateto|fl

```






