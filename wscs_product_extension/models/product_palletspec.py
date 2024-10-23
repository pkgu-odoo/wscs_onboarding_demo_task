# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ProductPalletSpec(models.Model):
    _name = 'product.palletspec'
    _description = 'Product Pallet Specification'

    name = fields.Char(string='Pallet Type',required=True)
    product_template_id = fields.Many2one('product.template', string='Product', required=True)
    company_id = fields.Many2one('res.company', string='Company')
    cases_per_layer = fields.Float(string='Cases perLayer')
    layers_per_pallet = fields.Float(string='Layers per Pallet')
    wscs_qty = fields.Float(string='Pallet Quantity', compute='_compute_qty',store=True)
    product_uom_id = fields.Many2one('uom.uom', string='Unit of Measure')
    cases_per_width = fields.Integer(string='Width')
    cases_per_length = fields.Integer(string='Length')
    cases_per_height = fields.Integer(string='Height')
    cases_per_weight = fields.Float(string=' Nett Weight')
    cases_per_volume = fields.Float(string='Pallet Volume', compute='_compute_volume',store=True)
    cases_per_units = fields.Integer(string='Pieces per Pallet', compute='_compute_units',store=True)

    @api.depends('cases_per_layer', 'layers_per_pallet')
    def _compute_qty(self):
        for rec in self:
            rec.wscs_qty = rec.cases_per_layer * rec.layers_per_pallet

    @api.depends('cases_per_width', 'cases_per_length', 'cases_per_height')
    def _compute_volume(self):
        for rec in self:
            rec.cases_per_volume = (rec.cases_per_width/1000) * (rec.cases_per_length/1000) * (rec.cases_per_height/1000)

    @api.depends('cases_per_layer', 'layers_per_pallet', 'wscs_qty')
    def _compute_units(self):
        for rec in self:
            rec.cases_per_units = rec.cases_per_layer * rec.layers_per_pallet * rec.wscs_qty
