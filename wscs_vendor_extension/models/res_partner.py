from odoo import fields, models, api
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    status_id = fields.Many2one('vendor.status', string='Vendor Status')
    product_category_ids = fields.Many2many('product.category', string='Product Categories')
    other_certification_id = fields.Many2one('gfsi.certification',string = 'Other Certification')
    gfsi_scheme_id = fields.Many2one('gfsi.scheme', string='GFSI Scheme')
    gfsi_grade_id = fields.Many2one('gfsi.gradezip', string='GFSI Grade')
    sedx_no = fields.Char('Sedex Member No.')

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

    @api.onchange('status_id')
    def onchange_status(self):
        if self.status_id:
            new_hierarchy = self.status_id.hierarchy
            current_hierarchy = self._origin.status_id.hierarchy
            new_user_list = self.status_id.status_change_ids

            if(new_hierarchy < current_hierarchy):
                raise ValidationError("You cannot downgrade to a status with a lower hierarchy level.")
            elif self.env.user not in new_user_list:
                raise ValidationError("user does not have permission to change status.")
