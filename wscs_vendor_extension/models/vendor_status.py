# -*- coding: utf-8 -*-
from odoo import fields, models,api


class VendorStatus(models.Model):
    _name = 'vendor.status'
    _description = 'Vendor Status'
    _order = 'sequence'

    name = fields.Char('Vendor Status', required=True)
    sequence = fields.Integer(string='Sequence')
    wscs_vendor_hierarchy = fields.Integer(string='Hierarchy', compute='_compute_wscs_vendor_hierarchy', store=True)
    status_change_ids = fields.Many2many('res.users',string='Status Change')
    prevent_po_creation = fields.Selection([
        ('no','No'),
        ('yes','Yes'),
        ('alert','Alert')],
        string='Prevent PO Creation')
    notify_user_id = fields.Many2one('res.users',string='Notify User')
    category_ids = fields.Many2many('product.category',string='Categories')
    
    @api.depends('sequence')
    def _compute_wscs_vendor_hierarchy(self):
        for record in self:
            record.wscs_vendor_hierarchy = record.sequence

    def create(self, vals):
        top_sequence_record = self.search([], limit=1, order='sequence desc')
        if top_sequence_record:
            vals['sequence'] = top_sequence_record.sequence + 1
        else:
            vals['sequence'] = 1
        return super().create(vals)
