---
id: b3099912-d659-43ac-b1ba-89cbeb4ab24c
name: Get-ADDomain Get Domain Information from Active Directory
type: command
executor: powershell
data: Get-ADDomain -Identity $_DOMAIN
output: "PS C:\\> Get-ADDomain -Identity dev.tesla.local\n\nAllowedDNSSuffixes   \
  \              : {}\nChildDomains                       : {}\nComputersContainer\
  \                 : CN=Computers,DC=DEV,DC=TESLA,DC=LOCAL\nDeletedObjectsContainer\
  \            : CN=Deleted Objects,DC=DEV,DC=TESLA,DC=LOCAL\nDistinguishedName  \
  \                : DC=DEV,DC=TESLA,DC=LOCAL\nDNSRoot                           \
  \ : DEV.TESLA.LOCAL\nDomainControllersContainer         : OU=Domain Controllers,DC=DEV,DC=TESLA,DC=LOCAL\n\
  DomainMode                         : Windows2016Domain\nDomainSID              \
  \            : S-1-5-21-1576920733-1301476157-954876328\nForeignSecurityPrincipalsContainer\
  \ : CN=ForeignSecurityPrincipals,DC=DEV,DC=TESLA,DC=LOCAL\nForest              \
  \               : TESLA.LOCAL\nInfrastructureMaster               : DC-DEV.DEV.TESLA.LOCAL\n\
  LastLogonReplicationInterval       : \nLinkedGroupPolicyObjects           : {CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=System,DC=DEV,DC=TESLA,D\n\
  \                                     C=LOCAL}\nLostAndFoundContainer          \
  \    : CN=LostAndFound,DC=DEV,DC=TESLA,DC=LOCAL\nManagedBy                     \
  \     : \nName                               : DEV\nNetBIOSName                \
  \        : DEV\nObjectClass                        : domainDNS\nObjectGUID     \
  \                    : 71b069dd-fd3a-42c9-a1ff-0167124f1acc\nParentDomain      \
  \                 : TESLA.LOCAL\nPDCEmulator                        : DC-DEV.DEV.TESLA.LOCAL\n\
  PublicKeyRequiredPasswordRolling   : True\nQuotasContainer                    :\
  \ CN=NTDS Quotas,DC=DEV,DC=TESLA,DC=LOCAL\nReadOnlyReplicaDirectoryServers    :\
  \ {}\nReplicaDirectoryServers            : {DC-DEV.DEV.TESLA.LOCAL}\nRIDMaster \
  \                         : DC-DEV.DEV.TESLA.LOCAL\nSubordinateReferences      \
  \        : {}\nSystemsContainer                   : CN=System,DC=DEV,DC=TESLA,DC=LOCAL\n\
  UsersContainer                     : CN=Users,DC=DEV,DC=TESLA,DC=LOCAL"
created_at: '2020-07-07T04:30:50.322379+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Get-ADDomain Get Domain Information from Active Directory

```powershell
Get-ADDomain -Identity $_DOMAIN
```

## Expected Output

```
PS C:\> Get-ADDomain -Identity dev.tesla.local

AllowedDNSSuffixes                 : {}
ChildDomains                       : {}
ComputersContainer                 : CN=Computers,DC=DEV,DC=TESLA,DC=LOCAL
DeletedObjectsContainer            : CN=Deleted Objects,DC=DEV,DC=TESLA,DC=LOCAL
DistinguishedName                  : DC=DEV,DC=TESLA,DC=LOCAL
DNSRoot                            : DEV.TESLA.LOCAL
DomainControllersContainer         : OU=Domain Controllers,DC=DEV,DC=TESLA,DC=LOCAL
DomainMode                         : Windows2016Domain
DomainSID                          : S-1-5-21-1576920733-1301476157-954876328
ForeignSecurityPrincipalsContainer : CN=ForeignSecurityPrincipals,DC=DEV,DC=TESLA,DC=LOCAL
Forest                             : TESLA.LOCAL
InfrastructureMaster               : DC-DEV.DEV.TESLA.LOCAL
LastLogonReplicationInterval       : 
LinkedGroupPolicyObjects           : {CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=System,DC=DEV,DC=TESLA,D
                                     C=LOCAL}
LostAndFoundContainer              : CN=LostAndFound,DC=DEV,DC=TESLA,DC=LOCAL
ManagedBy                          : 
Name                               : DEV
NetBIOSName                        : DEV
ObjectClass                        : domainDNS
ObjectGUID                         : 71b069dd-fd3a-42c9-a1ff-0167124f1acc
ParentDomain                       : TESLA.LOCAL
PDCEmulator                        : DC-DEV.DEV.TESLA.LOCAL
PublicKeyRequiredPasswordRolling   : True
QuotasContainer                    : CN=NTDS Quotas,DC=DEV,DC=TESLA,DC=LOCAL
ReadOnlyReplicaDirectoryServers    : {}
ReplicaDirectoryServers            : {DC-DEV.DEV.TESLA.LOCAL}
RIDMaster                          : DC-DEV.DEV.TESLA.LOCAL
SubordinateReferences              : {}
SystemsContainer                   : CN=System,DC=DEV,DC=TESLA,DC=LOCAL
UsersContainer                     : CN=Users,DC=DEV,DC=TESLA,DC=LOCAL
```


