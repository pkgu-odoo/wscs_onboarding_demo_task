from odoo import models, fields, api
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.model
    def create(self, vals):
        partner_id = vals.get('partner_id')
        if partner_id:
            partner = self.env['res.partner'].browse(partner_id)
            notify_user = partner.status_id.notify_user_id
            if  partner.status_id and partner.status_id.name in ['Verified - Grade 1', 'Verified - Grade 2']:
                status_record = self.env['vendor.status'].search([('name', '=', 'Active')], limit=1)
                partner.status_id = status_record

            elif partner.status_id.prevent_po_creation in ['no'] and partner.status_id and partner.status_id.name in ['Verified - Grade 1', 'Verified - Grade 2']:
                status_record = self.env['vendor.status'].search([('name', '=', 'Active')], limit=1)
                partner.status_id = status_record

            elif partner.status_id.prevent_po_creation in ['alert']:
                status_record = self.env['vendor.status'].search([('name', '=', 'Active')], limit=1)
                partner.status_id = status_record
                purchase_order = super().create(vals)
                if notify_user:
                    active_type_id = self.env.ref('mail.mail_activity_data_todo').id
                    purchase_order.activity_schedule(
                    activity_type_id=active_type_id,
                    summary=("Follow up on the newly created Purchase Order"),
                    note=("The supplier status has been changed to 'Active'. Please review the purchase order."),
                    user_id=notify_user.id,
                    )
                return purchase_order

            elif partner.status_id.prevent_po_creation in ['yes']:
                raise UserError("You cannot create a Purchase Order because purchase order is already created")
        return super().create(vals)
