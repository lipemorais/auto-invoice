import urllib.parse

from builtins import breakpoint

import scrapy
from scrapy.http import FormRequest


class InvoiceSpider(scrapy.Spider):
    name = "invoice"

    def start_requests(self):
        yield FormRequest(url='https://invoice.husky.io/sessions',
                          formdata={
                              "email": "felipejpa15@gmail.com",
                              "password": "=n6dBBAaoa9fd_y<^CgoE?T[.a}Sx)$bkt53c]3\\"},
                          callback=self.login_callback)

    def login_callback(self, response):
        invoice_number = response.css('input#invoice_number::attr(value)').get()
        invoice_from = response.css('input#invoice_from::attr(value)').get()
        invoice_from_address = response.css('textarea#invoice_from_address::text').get().strip()
        authenticity_token = response.css('input[name="authenticity_token"]::attr(value)').get()

        to = "Consumers Unified, LLC"
        to_email = "felipejpa15@gmail.com"
        to_address = "297 Kingsbury Grade, Suite 1025, Mailbox 4470 Stateline, NV 89449-4470"

        services_attributes = [{"description": "Software development",
                                "currency": "USD",
                                "value": "31250.00"}]

        invoice = {"number": invoice_number,
                   "from": invoice_from,
                   "from_address": invoice_from_address,
                   "to": to,
                   "to_email": to_email,
                   "to_address": to_address,
                   "services_attributes": services_attributes}

        # headers = {
        #     "Host": "invoice.husky.io",
        #     "Connection": "keep-alive",
        #     'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        #     'sec-ch-ua-mobile': '?0',
        #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        #     "Origin": "https://invoice.husky.io",
        #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        #     "Content-Type": "application/x-www-form-urlencoded",
        #     'Cache-Control': 'max-age=0',
        #     'Upgrade-Insecure-Requests': '1',
        #     'Accept-Language': 'en-US,en;q=0.9',
        #     'Referer': 'https://invoice.husky.io/',
        #     'Sec-Fetch-Dest': 'document',
        #     'Sec-Fetch-User': '?1',
        #     'Sec-Fetch-Mode': 'navigate',
        #     'Sec-Fetch-Site': 'same-origin',
        #     'Cookie': '_husky_invoice_generator_session=QXV6b29vSEg0WDU1SHVDUDZhODlWOHd0WmhlNkRQR21DRG5uVENSdnp5SnRLMGpmVzFTODVzSnFkMTlXSFR1dDdyK2dMWjhKengyVFdVUkFkYWN6QVdVV2JjRm1QK21uTFFwejUrVEVVMDBuaEhlNlA1L3lHYmxxK0puVlUrZ0UrZG9RaFBiaGowc3RHVkhSYnpIUFVNa3RxWkVuVzVhMlVsdExWK3NJK29HdHAxRVRyUFZ0MzVqTGt4MVN1K3hGNHZ5QmpwejlJNmtNb2ZaNmpCSjgwNkN0VmM3cmNMK1VhdXFKUHZXdjY5ZHF2SEljS0FwcVJyZ3RIUjg2NGkyKy0tMkVtTTh4MGErOS9TMGh4eGFkS2IvUT09--e9887d45e293749c81f34a164c699c834685a55d'
        # }

        yield FormRequest(url='https://invoice.husky.io/invoices', formdata={"utf8": "\u2713","invoice": invoice, "authenticity_token": authenticity_token, "commit": "Enviar invoice"},callback=self.invoice_sent_callback)

    def invoice_sent_callback(self, response):
        breakpoint()
        if response.status == 200:
            self.logger.info('Invoice sent!')
        else:
            self.logger.info('Invoice NOT sent! :\'(')
