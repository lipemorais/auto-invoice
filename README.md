# auto-invoice

The objective of this project is easily generate an invoice on [husky.io](husky.io)

## Setup
To set up the project you need to make a copy of `auto_invoice/.env.example`
```bash
cp auto_invoice/.env.example auto_invoice/.env
```

So you can fill the sensitive data in `auto_invoice/.env`

Once you are done with filling the data you can run

`make invoice`

You should look for 2 important logs:
1. `Login done successfully!!!` so you know that your login on husky was successful
2. `Invoice sent successfully!` so you know that your invoice was sent for your e-mail 
