from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'
#NUevo campo
    picking_total = fields.Monetary(
        string="Total Despacho",
        currency_field='currency_id',
        compute='_compute_picking_total',
        store=False
    )
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        related='company_id.currency_id',
        readonly=True
    )
    
    dispatcher_partner_id = fields.Many2one(
        'res.partner',
        string='Despachador',
        help='El empleado que despacha el pedido',
        domain=[('dispatcher', '=', True)]
    )
    
    def _compute_picking_total(self):
        for picking in self:
            total = 0.0
            for move in picking.move_ids:
                if move.product_id and move.product_uom_qty and move.product_id.lst_price:
                    total += move.product_uom_qty * move.product_id.lst_price
            picking.picking_total = total