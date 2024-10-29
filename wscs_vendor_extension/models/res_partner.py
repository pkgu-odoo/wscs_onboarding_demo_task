# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
from odoo.exceptions import ValidationError, AccessError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    status_id = fields.Many2one('vendor.status', string='Vendor Status',default= lambda self: self.env['vendor.status'].search([],limit=1))
    product_category_ids = fields.Many2many('product.category', string='Product Categories')
    other_certification_id = fields.Many2one('gfsi.certification',string = 'Other Certification')
    gfsi_scheme_id = fields.Many2one('gfsi.scheme', string='GFSI Scheme')
    gfsi_grade_id = fields.Many2one('gfsi.gradezip', string='GFSI Grade')
    sedx_no = fields.Char('Sedex Member partner_idNo.')

    sedex_registered = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No')
    ])
    ethical_audit = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No')
    ])
    gfsi_cretification = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No')
    ])
    fsc_certified = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No')
    ])
    pefc_certified = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No')
    ])

    status_active = fields.Boolean(string='Active')
    status_Prospective = fields.Boolean(string='Prospective')
    status_evalution = fields.Boolean(string='Evalution')
    status_rejected = fields.Boolean(string='Rejected')
    status_grade2 = fields.Boolean(string='Verified-Grade 2')
    status_grade1 = fields.Boolean(string='Verified-Grade 1')
    status_onhold = fields.Boolean(string='Active On Hold')
    status_disqualified = fields.Boolean(string='Disqualified')

    @api.model
    def write(self, vals):
        current_hierarchy = self.status_id.sequence if self.status_id else 0
        if 'status_id' in vals:
            new_status = self.env['vendor.status'].browse(vals['status_id'])
            new_hierarchy = new_status.sequence
            new_user_list = new_status.status_change_ids
            if new_hierarchy < current_hierarchy:
                raise ValidationError(_("You cannot downgrade to a status with a lower hierarchy level."))
            elif self.env.user not in new_user_list:
                raise AccessError(_("User does not have permission to change status."))
        return super().write(vals)
