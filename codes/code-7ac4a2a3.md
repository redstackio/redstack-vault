---
id: 7ac4a2a3-471e-4cbf-94d0-d73790ac40e0
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:07.394248+00:00'
updated_at: '2023-04-10T20:26:01.513573+00:00'
---

# Code Snippet 7ac4a2a3

**Language**: ps1

```ps1
# Detect if current forest is PAM trust
Import ADModule
Get-ADTrust -Filter {(ForestTransitive -eq $True) -and (SIDFilteringQuarantined -eq $False)}

# Enumerate shadow security principals 
Get-ADObject -SearchBase ("CN=Shadow Principal Configuration,CN=Services," + (Get-ADRootDSE).configurationNamingContext) -Filter * -Properties * | select Name,member,msDS-ShadowPrincipalSid | fl

# Enumerate if current forest is managed by a bastion forest
# Trust_Attribute_PIM_Trust + Trust_Attribute_Treat_As_External
Get-ADTrust -Filter {(ForestTransitive -eq $True)} 
```


