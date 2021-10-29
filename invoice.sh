#!/bin/bash -e

pipenv install --dev
cd auto_invoice
pipenv run scrapy crawl invoice
cd -
