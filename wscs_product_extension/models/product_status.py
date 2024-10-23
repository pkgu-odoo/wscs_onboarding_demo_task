# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ProductTemplate(models.Model):
    _name = 'product.status'
    _description = 'Product Status'
    _order = 'sequence'

    name = fields.Char('Status', required=True)
    sequence = fields.Integer(string='Sequence')
    wscs_hierarchy = fields.Integer(string='Hierarchy', compute='_compute_wscs_hierarchy', store=True)
    status_change_up_id = fields.Many2one('res.groups', string='Group Name - Status Change Up')
    status_change_down_id = fields.Many2one('res.groups', string='Group Name - Status Change Down')

    @api.depends('sequence')
    def _compute_wscs_hierarchy(self):
        for record in self:
            record.wscs_hierarchy = record.sequence

    def create(self, vals):
        top_sequence_record = self.search([], limit=1, order='sequence desc')
        if top_sequence_record:
            vals['sequence'] = top_sequence_record.sequence + 1
        else:
            vals['sequence'] = 1
        return super().create(vals)
