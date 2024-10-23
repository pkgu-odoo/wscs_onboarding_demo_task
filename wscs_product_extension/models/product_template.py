# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_status_id = fields.Many2one(
        'product.status', 
        string='Product Status',
        default=lambda self: self.env['product.status'].search([('name', '=', 'Active')], limit=1)
        )
    customer_reference = fields.Char(string='Customer Reference')
    product_palletspec_ids = fields.One2many('product.palletspec', 'product_template_id')
    landed_cost = fields.Float(string='Landed Cost')
    margin = fields.Float(string='Margin')

    def write(self, vals):
        current_hierarchy = self.product_status_id.wscs_hierarchy if self.product_status_id else 0
        if 'product_status_id' in vals:
            new_status = self.env['product.status'].browse(vals['product_status_id'])
            new_hierarchy = new_status.wscs_hierarchy
            new_user_list = new_status.status_change_up_id.users
            if new_hierarchy < current_hierarchy:
                raise ValidationError(_("You cannot downgrade to a status with a lower hierarchy level."))
            elif self.env.user not in new_user_list:
                raise ValidationError(_("User does not have permission to change status."))
        return super().write(vals)
