from odoo import fields, models


class ProductSupplierInfo(models.Model):
    _inherit = 'product.supplierinfo'

    qty_per_case = fields.Integer(string='Quantity per Case')
    cases_per_container = fields.Integer(string='Cases per Container')
    price_per_1000 = fields.Float(string='Price per 1000')
    incoterm = fields.Char(string='Incoterm')
