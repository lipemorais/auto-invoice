from builtins import breakpoint
from pprint import pprint

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

        self.logger.info("\n\n\nLogin done successfully!!!\n\n\n")
        invoice_number = response.css('input#invoice_number::attr(value)').get()
        invoice_from = response.css('input#invoice_from::attr(value)').get()
        invoice_from_address = response.css('textarea#invoice_from_address::text').get().strip()
        authenticity_token = response.css('input[name="authenticity_token"]::attr(value)').get()

        to = "Consumers Unified, LLC"
        to_email = "felipejpa15@gmail.com"
        to_address = "297 Kingsbury Grade, Suite 1025, Mailbox 4470 Stateline, NV 89449-4470"

        formdata = {
            "utf8": "\u2713",
            "authenticity_token": authenticity_token,
            "invoice[number]": invoice_number,
            "invoice[from]": invoice_from,
            "invoice[from_address]": invoice_from_address,
            "invoice[to]": to,
            "invoice[to_email]": to_email,
            "invoice[to_address]": to_address,
            "invoice[services_attributes][0][description]": "Software development",
            "invoice[services_attributes][0][currency]": "USD",
            "invoice[services_attributes][0][value]": "31250.00",
        }

        self.logger.info("Information sent to generate invoice: \n")
        pprint(formdata)

        yield FormRequest(
            url='https://invoice.husky.io/invoices',
            formdata=formdata,
            callback=self.invoice_sent_callback,
            dont_filter=True,
        )

    def invoice_sent_callback(self, response):
        if response.status == 200:
            self.logger.info('Invoice sent successfully!')
        else:
            self.logger.info('Invoice NOT sent! :\'(')
