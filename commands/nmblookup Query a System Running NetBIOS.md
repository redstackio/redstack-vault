---
id: ba42ac59-49d3-4ac1-a6c3-5a77fd15e1b8
name: nmblookup Query a System Running NetBIOS
type: command
executor: ''
data: nmblookup -A $_TARGET_IP
output: "root@kali:~# nmblookup -A 10.10.10.10\nLooking up status of 10.10.10.10\n\
  \        BOB-PC          <00> -         B <ACTIVE> \n        WORKGROUP       <00>\
  \ - <GROUP> B <ACTIVE> \n        BOB-PC          <20> -         B <ACTIVE> \n  \
  \      WORKGROUP       <1e> - <GROUP> B <ACTIVE> \n        WORKGROUP       <1d>\
  \ -         B <ACTIVE> \n        ..__MSBROWSE__. <01> - <GROUP> B <ACTIVE> \n\n\
  \        MAC Address = 00-0C-29-72-EB-B4"
created_at: '2019-09-23T17:52:33.509806+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# nmblookup Query a System Running NetBIOS

```bash
nmblookup -A $_TARGET_IP
```

## Expected Output

```
root@kali:~# nmblookup -A 10.10.10.10
Looking up status of 10.10.10.10
        BOB-PC          <00> -         B <ACTIVE> 
        WORKGROUP       <00> - <GROUP> B <ACTIVE> 
        BOB-PC          <20> -         B <ACTIVE> 
        WORKGROUP       <1e> - <GROUP> B <ACTIVE> 
        WORKGROUP       <1d> -         B <ACTIVE> 
        ..__MSBROWSE__. <01> - <GROUP> B <ACTIVE> 

        MAC Address = 00-0C-29-72-EB-B4
```
