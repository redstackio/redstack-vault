---
id: 35182687-d3af-437e-a7ba-9f8294033bcc
name: List a Local Windows User's Info and Group Membership
type: command
executor: command_prompt
data: net user $_USER
output: "PS C:\\Users\\Bob > net user bob\nUser name                    Bob\nFull\
  \ Name\nComment\nUser's comment\nCountry/region code          000 (System Default)\n\
  Account active               Yes\nAccount expires              Never\n\nPassword\
  \ last set            3/10/2020 12:50:20 PM\nPassword expires             Never\n\
  Password changeable          3/10/2020 12:50:20 PM\nPassword required          \
  \  No\nUser may change password     Yes\n\nWorkstations allowed         All\nLogon\
  \ script\nUser profile\nHome directory\nLast logon                   3/10/2020 6:34:36\
  \ PM\n\nLogon hours allowed          All\n\nLocal Group Memberships      *Administrators\
  \       *docker-users\n                             *Hyper-V Administrator*Performance\
  \ Log Users\nGlobal Group memberships     *None\nThe command completed successfully."
created_at: '2020-03-20T20:55:40.966792+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# List a Local Windows User's Info and Group Membership

```command_prompt
net user $_USER
```

## Expected Output

```
PS C:\Users\Bob > net user bob
User name                    Bob
Full Name
Comment
User's comment
Country/region code          000 (System Default)
Account active               Yes
Account expires              Never

Password last set            3/10/2020 12:50:20 PM
Password expires             Never
Password changeable          3/10/2020 12:50:20 PM
Password required            No
User may change password     Yes

Workstations allowed         All
Logon script
User profile
Home directory
Last logon                   3/10/2020 6:34:36 PM

Logon hours allowed          All

Local Group Memberships      *Administrators       *docker-users
                             *Hyper-V Administrator*Performance Log Users
Global Group memberships     *None
The command completed successfully.
```


