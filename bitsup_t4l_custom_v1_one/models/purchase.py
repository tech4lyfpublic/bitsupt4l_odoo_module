from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    bom_id = fields.Many2one('mrp.bom', string='Bill of Materials')

    @api.onchange('bom_id')
    def onchange_bom_id(self):
        if self.bom_id:
            # Clear existing order lines
            #self.order_line = [(5, 0, 0)]

            # Create order lines based on the selected BOM
            bom = self.bom_id
            order_lines = []
            for line in bom.bom_line_ids:
                order_lines.append((0, 0, {
                    'product_id': line.product_id.id,
                    'name': line.product_id.description_purchase,
                    'product_qty': line.product_qty,
                    'product_uom': line.product_uom_id.id,
                    'price_unit': line.product_id.standard_price,  # You can set the price as needed
                }))
            self.order_line = order_lines


# class PurchaseOrderLine(models.Model):
#     _inherit = 'purchase.order.line'
#
#     # Add any additional fields you need for your purchase order lines
#
#     @api.onchange('product_id', 'product_qty', 'product_uom')
#     def onchange_product_id(self):
#         if self.product_id:
#             # Ensure that the order_id field is set to the parent purchase order
#             self.order_id = self.order_id
