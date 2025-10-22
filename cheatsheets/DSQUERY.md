---
id: 05f723e0-91a5-484a-9ed6-12fca0afbcf3
name: DSQUERY
type: cheatsheet
verified: false
created_at: '2020-07-14T18:21:12.441455+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# DSQUERY

# Description

Queries the directory by using search criteria that you specify. Each of the **dsquery** commands finds objects of a specific object type, with the exception of **dsquery ***, which can query for any type of object. It is available if Active Directory Domain Services (AD DS) server role is installed.

Applies To: Windows Server 2003, Windows Server 2008, Windows Server 2003 R2, Windows Server 2008 R2, Windows Server 2012, Windows Server 2003 with SP1, Windows 8

**Command** ([[Get attributes for all Windows hosts in the Domain]]):

```bash
dsquery * -filter "(&(objectclass=computer) (objectcategory=computer) (operatingSystem=Windows*))" -limit 0 |dsget computer -dn -samid -desc -loc >c:\windows\temp\computers.log

```

**Command** ([[Get attributes for computers in a specific OU]]):

```bash
dsquery computer <OU=PUT OU HERE> -limit 0 |dsget computer -dn -samid -desc -l >c:\windows\temp\out.log

```

**Command** ([[Get attributes for users in the specified OU]]):

```bash
dsquery user <OU=PUT OU HERE> -limit 0 |dsget user -dn -samid -display -desc -office -tel -email -title -hmdir -profile -loscr -mustchpwd -canchpwd -pwdneverexpires -disabled

```

**Command** ([[Get DC]]):

```bash
dsquery server -forest

```

**Command** ([[Get DC]]):

```bash
dsquery server -o rdn -forest

```

**Command** ([[Get Domain Functional Level]]):

```bash
dsquery * "DC=corp,DC=test,DC=com" -scope base -attr msDS-Behavior-Version ntMixedDomain

```

**Command** ([[Get Forest Functional Level]]):

```bash
dsquery * "CN=Partitions,CN=Configuration,DC=corp,DC=test,DC=com" -scope base -attr msDS-Behavior-Version ntMixedDomain

```
