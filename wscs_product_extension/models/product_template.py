from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_status_id = fields.Many2one('product.status', string='Product Status')
    hs_code = fields.Char(string='HS Code')
    customer_reference = fields.Char(string='Customer Reference')
    product_palletspec_ids = fields.One2many('product.palletspec', 'product_template_id',nolabel=True)
    landed_cost = fields.Float(string='Landed Cost')
    margin = fields.Float(string='Margin')