---
id: 83f7bb3a-cb19-43c5-8d8f-fcf0d7ccbc46
name: Find Files by Name
type: command
executor: bash
data: find / -name $_STRING
output: "bob@a7ffb5e7e757:/$ find / -name \"*passw*\" 2>/dev/null\n/etc/cron.daily/passwd\
  \             \n/etc/pam.d/chpasswd                \n/etc/pam.d/common-password\
  \            \n/etc/pam.d/passwd                      \n/etc/passwd            \
  \              \n/etc/passwd-                          \n/etc/security/opasswd \
  \                  \n/usr/bin/gpasswd                    \n/usr/bin/passwd     \
  \                     \n/usr/lib/tmpfiles.d/passwd.conf   \n/usr/sbin/chgpasswd\
  \               \n/usr/sbin/chpasswd               \n/usr/sbin/update-passwd"
created_at: '2020-03-10T06:28:38.723242+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Find Files by Name

```bash
find / -name $_STRING
```

## Expected Output

```
bob@a7ffb5e7e757:/$ find / -name "*passw*" 2>/dev/null
/etc/cron.daily/passwd             
/etc/pam.d/chpasswd                
/etc/pam.d/common-password            
/etc/pam.d/passwd                      
/etc/passwd                          
/etc/passwd-                          
/etc/security/opasswd                   
/usr/bin/gpasswd                    
/usr/bin/passwd                          
/usr/lib/tmpfiles.d/passwd.conf   
/usr/sbin/chgpasswd               
/usr/sbin/chpasswd               
/usr/sbin/update-passwd
```


