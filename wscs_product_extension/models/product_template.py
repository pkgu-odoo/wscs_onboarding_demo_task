# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, AccessError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_status_id = fields.Many2one('product.status', string='Product Status',default= lambda self: self.env['product.status'].search([],limit=1))
    customer_reference = fields.Char(string='Customer Reference')
    product_palletspec_ids = fields.One2many('product.palletspec', 'product_template_id')
    landed_cost = fields.Float(string='Landed Cost',default=0.0)
    wscs_margin = fields.Float(string='Margin',compute='_compute_margin_percentage',store=True)

    wscs_status_active = fields.Boolean(string='Active')
    wscs_status_pricing = fields.Boolean(string='Pricing')
    wscs_status_dormant = fields.Boolean(string='Dormant')
    wscs_status_npd = fields.Boolean(string='NPD')
    wscs_status_archived = fields.Boolean(string='Archived')

    @api.depends('landed_cost', 'list_price', 'standard_price')
    def _compute_margin_percentage(self):
        for rec in self:
            if rec.list_price:
                rec.wscs_margin = ((rec.list_price - (rec.standard_price + rec.landed_cost)) / rec.list_price)
            else:
                rec.wscs_margin = 0

    @api.model
    def write(self, vals):
        current_hierarchy = self.product_status_id.sequence if self.product_status_id else 0
        if 'product_status_id' in vals:
            new_status = self.env['product.status'].browse(vals['product_status_id'])
            new_hierarchy = new_status.sequence
            new_user_list = new_status.status_change_up_id.users
            if new_hierarchy < current_hierarchy:
                raise ValidationError(_("You cannot downgrade to a status with a lower hierarchy level."))
            elif self.env.user not in new_user_list:
                raise AccessError(_("User does not have permission to change status."))
        return super().write(vals)
