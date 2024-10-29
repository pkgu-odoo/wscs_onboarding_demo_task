# -*- coding: utf-8 -*-
from odoo import fields, models,api


class VendorStatus(models.Model):
    _name = 'vendor.status'
    _description = 'Vendor Status'
    _order = 'sequence'

    name = fields.Char('Vendor Status', required=True)
    sequence = fields.Integer(string='Sequence')
    status_change_ids = fields.Many2many('res.users',string='Status Change')
    prevent_po_creation = fields.Selection([
        ('no','No'),
        ('yes','Yes'),
        ('alert','Alert')],
        string='Prevent PO Creation')
    notify_user_id = fields.Many2one('res.users',string='Notify User')
    category_ids = fields.Many2many('product.category',string='Categories')
    is_active = fields.Boolean(string='Is_active')
