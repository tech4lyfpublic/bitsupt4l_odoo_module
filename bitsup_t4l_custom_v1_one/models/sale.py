# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    brand_id = fields.Many2one('brand.brand',string="Brand")


    @api.model
    def create(self, vals):
        sequence = self.env["ir.sequence"].next_by_code("sale.quotation")
        vals["name"] = sequence or "/"
        return super(SaleOrder, self).create(vals)


    def copy(self, default=None):
        self.ensure_one()
        if default is None:
            default = {}
        if self.origin and self.origin != "":
            default["origin"] = self.origin + ", " + self.name
        else:
            default["origin"] = self.name
        return super(SaleOrder, self).copy(default)

    def action_confirm(self):
        for order in self:
            # if self.name[:2] != "SQ":
            #     continue
            if order.state not in ("draft", "sent"):
                continue
            if order.origin and order.origin != "":
                quo = order.origin + ", " + order.name
            else:
                quo = order.name
            sequence = self.env["ir.sequence"].next_by_code("sale.order")
            order.write({"origin": quo, "name": sequence})
        return super().action_confirm()

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    brand_id = fields.Many2one('brand.brand', related="product_template_id.brand_id", string="Brand")

    # @api.depends('product_id')
    # def get_brand(self):
    #     for rec in self:
    #         product = self.env['product.template'].search([("id","=",rec.product_template_id)])
    #         rec.brand_id = product.brand_id

    # product_category_id = fields.Many2one(
    #     'product.category',
    #     string='Product Category',
    #     compute='_compute_product_category',
    #     store=True,
    # )
    #
    # @api.depends('product_id')
    # def _compute_product_category(self):
    #     for line in self:
    #         if line.product_id:
    #             line.product_category_id = line.product_id.categ_id
    #         else:
    #             line.product_category_id = False