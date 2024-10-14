from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_status_id = fields.Many2one('product.status', string='Product Status')
    hs_code = fields.Char(string='HS Code')
    customer_reference = fields.Char(string='Customer Reference')
    product_palletspec_ids = fields.One2many('product.palletspec', 'product_template_id')
    landed_cost = fields.Float(string='Landed Cost')
    margin = fields.Float(string='Margin')

    @api.onchange('product_status_id')
    def onchange_status(self):
        if self.product_status_id:
            new_hierarchy = self.product_status_id.hierarchy
            current_hierarchy = self._origin.product_status_id.hierarchy
            new_user_list = self.product_status_id.status_change_up_id.users
            if(new_hierarchy < current_hierarchy):
                raise ValidationError("You cannot downgrade to a status with a lower hierarchy level.")
            elif self.env.user not in new_user_list:
                raise ValidationError("user does not have permission to change status.")
