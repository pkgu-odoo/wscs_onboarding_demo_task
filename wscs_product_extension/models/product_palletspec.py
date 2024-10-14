from odoo import models, fields, api

class ProductPalletSpec(models.Model):
    _name = 'product.palletspec'
    _description = 'Product Pallet Specification'

    name = fields.Char(string='Pallet Type')
    product_template_id = fields.Many2one('product.template', string='Product', required=True)
    company_id = fields.Many2one('res.company', string='Company')
    cases_per_layer = fields.Float(string='Cases perLayer', required=True)
    layers_per_pallet = fields.Float(string='Layers per Pallet', required=True)
    qty = fields.Float(string='Pallet Quantity', compute='_compute_qty')
    product_uom_id = fields.Many2one('uom.uom', string='Unit of Measure')
    width = fields.Integer(string='Width', required=True)
    length = fields.Integer(string='Length', required=True)
    height = fields.Integer(string='Height', required=True)
    weight = fields.Float(string=' Nett Weight')
    volume = fields.Float(string='Pallet Volume', compute='_compute_volume')
    units = fields.Integer(string='Pieces per Pallet', compute='_compute_units')

    @api.depends('cases_per_layer', 'layers_per_pallet')
    def _compute_qty(self):
        for rec in self:
            rec.qty = rec.cases_per_layer * rec.layers_per_pallet

    @api.depends('width', 'length', 'height')
    def _compute_volume(self):
        for rec in self:
            rec.volume = (rec.width) * (rec.length) * (rec.height)

    @api.depends('cases_per_layer', 'layers_per_pallet', 'qty')
    def _compute_units(self):
        for rec in self:
            rec.units = rec.cases_per_layer * rec.layers_per_pallet * rec.qty
