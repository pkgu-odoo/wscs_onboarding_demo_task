# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductPackaging(models.Model):
    _inherit = 'product.packaging'

    wscs_width = fields.Integer(string='Width',default=0)
    wscs_length = fields.Integer(string='Length',default=0)
    wscs_height = fields.Integer(string='Height Volume(m³)',default=0)
    wscs_net_weight = fields.Float(string='Nett Weight',default=0.0)
    wscs_gross_weight = fields.Float(string='Gross Weight',default=0.0)
    wscs_volume = fields.Float(string='Case Volume (³)', compute='_compute_volume', store=True)

    @api.depends('wscs_width', 'wscs_length', 'wscs_height')
    def _compute_volume(self):
        for rec in self:
            rec.wscs_volume = (rec.wscs_width/1000 * rec.wscs_length/1000 * rec.wscs_height/1000)
