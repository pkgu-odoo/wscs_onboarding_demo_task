# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ProductTemplate(models.Model):
    _name = 'product.status'
    _description = 'Product Status'
    _order = 'sequence'

    name = fields.Char('Status', required=True)
    sequence = fields.Integer(string='Sequence',default=10)
    status_change_up_id = fields.Many2one('res.groups', string='Group Name - Status Change Up')
    status_change_down_id = fields.Many2one('res.groups', string='Group Name - Status Change Down')
