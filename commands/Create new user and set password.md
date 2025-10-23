---
id: b448dae6-aa7e-4a8c-8f42-49c98eea1e01
name: Create new user and set password
type: command
executor: bash
data: 'sudo useradd -ou 0 -g 0 john

  sudo passwd john

  echo "linuxpassword" | passwd --stdin john'
output: null
created_at: '2023-04-06T03:56:17.905762+00:00'
updated_at: '2023-04-10T20:34:13.315723+00:00'
---

# Create new user and set password

```bash
sudo useradd -ou 0 -g 0 john
sudo passwd john
echo "linuxpassword" | passwd --stdin john
```


