---
id: 0af034da-0e3b-42ac-886c-07ee827e1247
name: PowerView Get Global Catalogs for the Current Forest
type: command
executor: powershell
data: Get-ForestGlobalCatalog
output: "PS C:\\> Get-ForestGlobalCatalog\n\n\nForest                     : TESLA.LOCAL\n\
  CurrentTime                : 7/1/2020 10:31:36 PM\nHighestCommittedUsn        :\
  \ 12888\nOSVersion                  : Windows Server 2019 Standard Evaluation\n\
  Roles                      : {SchemaRole, NamingRole, PdcRole, RidRole...}\nDomain\
  \                     : TESLA.LOCAL\nIPAddress                  : 10.10.2.5\nSiteName\
  \                   : Default-First-Site-Name\nSyncFromAllServersCallback :\nInboundConnections\
  \         : {6b0a9451-b145-48da-9e1e-a6a3800d89a6}\nOutboundConnections        :\
  \ {}\nName                       : DC-MAIN.TESLA.LOCAL\nPartitions             \
  \    : {DC=TESLA,DC=LOCAL, CN=Configuration,DC=TESLA,DC=LOCAL,\n               \
  \              CN=Schema,CN=Configuration,DC=TESLA,DC=LOCAL, DC=DomainDnsZones,DC=TESLA,DC=LOCAL...}\n\
  \nForest                     : TESLA.LOCAL\nCurrentTime                : 7/1/2020\
  \ 10:31:36 PM\nHighestCommittedUsn        : 13122\nOSVersion                  :\
  \ Windows Server 2019 Standard Evaluation\nRoles                      : {PdcRole,\
  \ RidRole, InfrastructureRole}\nDomain                     : DEV.TESLA.LOCAL\nIPAddress\
  \                  : 10.10.1.5\nSiteName                   : Default-First-Site-Name\n\
  SyncFromAllServersCallback :\nInboundConnections         : {ed57cdea-3117-48fa-a199-307becf29b05}\n\
  OutboundConnections        : {6b0a9451-b145-48da-9e1e-a6a3800d89a6}\nName      \
  \                 : DC-DEV.DEV.TESLA.LOCAL\nPartitions                 : {CN=Configuration,DC=TESLA,DC=LOCAL,\
  \ CN=Schema,CN=Configuration,DC=TESLA,DC=LOCAL,\n                             DC=ForestDnsZones,DC=TESLA,DC=LOCAL,\
  \ DC=DEV,DC=TESLA,DC=LOCAL...}"
created_at: '2020-07-01T22:54:44.508867+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# PowerView Get Global Catalogs for the Current Forest

```powershell
Get-ForestGlobalCatalog
```

## Expected Output

```
PS C:\> Get-ForestGlobalCatalog


Forest                     : TESLA.LOCAL
CurrentTime                : 7/1/2020 10:31:36 PM
HighestCommittedUsn        : 12888
OSVersion                  : Windows Server 2019 Standard Evaluation
Roles                      : {SchemaRole, NamingRole, PdcRole, RidRole...}
Domain                     : TESLA.LOCAL
IPAddress                  : 10.10.2.5
SiteName                   : Default-First-Site-Name
SyncFromAllServersCallback :
InboundConnections         : {6b0a9451-b145-48da-9e1e-a6a3800d89a6}
OutboundConnections        : {}
Name                       : DC-MAIN.TESLA.LOCAL
Partitions                 : {DC=TESLA,DC=LOCAL, CN=Configuration,DC=TESLA,DC=LOCAL,
                             CN=Schema,CN=Configuration,DC=TESLA,DC=LOCAL, DC=DomainDnsZones,DC=TESLA,DC=LOCAL...}

Forest                     : TESLA.LOCAL
CurrentTime                : 7/1/2020 10:31:36 PM
HighestCommittedUsn        : 13122
OSVersion                  : Windows Server 2019 Standard Evaluation
Roles                      : {PdcRole, RidRole, InfrastructureRole}
Domain                     : DEV.TESLA.LOCAL
IPAddress                  : 10.10.1.5
SiteName                   : Default-First-Site-Name
SyncFromAllServersCallback :
InboundConnections         : {ed57cdea-3117-48fa-a199-307becf29b05}
OutboundConnections        : {6b0a9451-b145-48da-9e1e-a6a3800d89a6}
Name                       : DC-DEV.DEV.TESLA.LOCAL
Partitions                 : {CN=Configuration,DC=TESLA,DC=LOCAL, CN=Schema,CN=Configuration,DC=TESLA,DC=LOCAL,
                             DC=ForestDnsZones,DC=TESLA,DC=LOCAL, DC=DEV,DC=TESLA,DC=LOCAL...}
```


