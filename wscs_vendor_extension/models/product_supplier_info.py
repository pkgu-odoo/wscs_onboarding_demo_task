# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductSupplierInfo(models.Model):
    _inherit = 'product.supplierinfo'

    qty_per_case = fields.Integer(string='Quantity per Case',default=0)
    cases_per_container = fields.Integer(string='Cases per Container',default=0)
    price_per_1000 = fields.Float(string='Price per 1000',default=0.0)
    incoterm = fields.Char(string='Incoterm')
