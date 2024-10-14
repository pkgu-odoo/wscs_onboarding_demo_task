from odoo import models, fields


class ProductTemplate(models.Model):
    _name = 'product.status'
    _description = 'Product Status'

    name = fields.Char('Status')
    hierarchy = fields.Integer('Sequence')
    status_change_up_id = fields.Many2one('res.groups', string='Group Name - Status Change Up')
    status_change_down_id = fields.Many2one('res.groups', string='Group Name - Status Change Down')
