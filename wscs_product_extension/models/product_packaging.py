from odoo import fields, models


class ProductPackaging(models.Model):
    _inherit = 'product.packaging'

    width = fields.Integer(string='Width',required=True)
    length = fields.Integer(string='Length',required=True)
    height = fields.Integer(string='Height Volume(m³)',required=True)
    net_weight = fields.Float(string='Nett Weight',required=True)
    gross_weight = fields.Float(string='Gross Weight',required=True)
    volume = fields.Float(string='Case Volume (m³)', compute='_compute_volume')
    def _compute_volume(self):
        for rec in self:
            rec.volume = (rec.width * rec.length * rec.height)
