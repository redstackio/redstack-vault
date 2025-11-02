---
id: 1c1d443d-30d4-4718-a3be-c11067f74f7e
name: Query a System for Installed Patches
type: command
executor: command_prompt
data: wmic qfe get Caption,Description,HotFixID,InstalledOn
output: 'C:\>wmic qfe get Caption,Description,HotFixID,InstalledOn

  Caption                                     Description      HotFixID   InstalledOn

  http://support.microsoft.com/?kbid=4515871  Update           KB4515871  10/5/2019

  http://support.microsoft.com/?kbid=4503308  Security Update  KB4503308  7/9/2019

  http://support.microsoft.com/?kbid=4506472  Update           KB4506472  7/9/2019

  http://support.microsoft.com/?kbid=4509096  Security Update  KB4509096  7/9/2019

  http://support.microsoft.com/?kbid=4515383  Security Update  KB4515383  10/5/2019

  http://support.microsoft.com/?kbid=4516115  Security Update  KB4516115  10/5/2019

  http://support.microsoft.com/?kbid=4520390  Security Update  KB4520390  10/5/2019

  http://support.microsoft.com/?kbid=4521863  Security Update  KB4521863  10/14/2019

  http://support.microsoft.com/?kbid=4517389  Update           KB4517389  10/21/2019'
created_at: '2020-01-24T21:45:44.859843+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[wmic]]'
---

# Query a System for Installed Patches

```command_prompt
wmic qfe get Caption,Description,HotFixID,InstalledOn
```

## Expected Output

```
C:\>wmic qfe get Caption,Description,HotFixID,InstalledOn
Caption                                     Description      HotFixID   InstalledOn
http://support.microsoft.com/?kbid=4515871  Update           KB4515871  10/5/2019
http://support.microsoft.com/?kbid=4503308  Security Update  KB4503308  7/9/2019
http://support.microsoft.com/?kbid=4506472  Update           KB4506472  7/9/2019
http://support.microsoft.com/?kbid=4509096  Security Update  KB4509096  7/9/2019
http://support.microsoft.com/?kbid=4515383  Security Update  KB4515383  10/5/2019
http://support.microsoft.com/?kbid=4516115  Security Update  KB4516115  10/5/2019
http://support.microsoft.com/?kbid=4520390  Security Update  KB4520390  10/5/2019
http://support.microsoft.com/?kbid=4521863  Security Update  KB4521863  10/14/2019
http://support.microsoft.com/?kbid=4517389  Update           KB4517389  10/21/2019
```


