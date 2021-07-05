from pprint import pprint

import scrapy
from scrapy.http import FormRequest

from dotenv import dotenv_values

config = dotenv_values(".env")


class InvoiceSpider(scrapy.Spider):
    name = "invoice"

    def start_requests(self):
        yield FormRequest(url='https://invoice.husky.io/sessions',
                          formdata={
                              "email": config["EMAIL"],
                              "password": config["PASSWORD"]},
                          callback=self.login_callback)

    def login_callback(self, response):

        self.logger.info("\n\n\nLogin done successfully!!!\n\n\n")
        invoice_number = response.css('input#invoice_number::attr(value)').get()
        invoice_from = response.css('input#invoice_from::attr(value)').get()
        invoice_from_address = response.css('textarea#invoice_from_address::text').get().strip()
        authenticity_token = response.css('input[name="authenticity_token"]::attr(value)').get()

        to = config["TO"]
        to_email = config["TO_EMAIL"]
        to_address = config["TO_ADDRESS"]

        formdata = {
            "utf8": "\u2713",
            "authenticity_token": authenticity_token,
            "invoice[number]": invoice_number,
            "invoice[from]": invoice_from,
            "invoice[from_address]": invoice_from_address,
            "invoice[to]": to,
            "invoice[to_email]": to_email,
            "invoice[to_address]": to_address,
            "invoice[services_attributes][0][description]": config["SERVICE_DESCRIPTION"],
            "invoice[services_attributes][0][currency]": config["SERVICE_CURRENCY"],
            "invoice[services_attributes][0][value]": config["SERVICE_VALUE"],
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
            self.logger.info('\n\n\nInvoice sent successfully!\n\n\n')
        else:
            self.logger.info('\n\n\nInvoice NOT sent! :\'(  \n\n\n')
