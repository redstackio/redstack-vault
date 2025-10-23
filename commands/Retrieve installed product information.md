---
id: ab729622-403c-40d1-b98b-7b7851aed442
name: Retrieve installed product information
type: command
executor: bash
data: select prod_release,installed_prod_fullname from table(sysproc.env_get_prod_info())
  as productinfo
output: null
created_at: '2023-04-06T03:56:32.535829+00:00'
updated_at: '2023-04-10T20:21:57.272196+00:00'
---

# Retrieve installed product information

```bash
select prod_release,installed_prod_fullname from table(sysproc.env_get_prod_info()) as productinfo
```


