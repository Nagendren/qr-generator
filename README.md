# qr-generator
Create a desktop app for  QR generator

## Dependencies

- terraform basic
- terraform Advance
- terraform with AWS

```sh
pip install pyqrcode
pip install pillow
pip install pypng
```
> If you commit your aws secrets by mistake,
> AWS has micro level of monitoring where it will detect the commit with secerts and access will be restrcited for the particular IAM user.
> You need to rotate the keys or create new users for future use. 
> Thanks to AWS for this detailed monitoring
