# -*- coding: utf-8 -*-
from odoo import fields, models, _


class ProductCategory(models.Model):
    _inherit = 'product.category'

    category_description = fields.Char(_("Category Description"))
