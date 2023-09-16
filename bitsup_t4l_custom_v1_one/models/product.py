# -*- coding: utf-8 -*-

from odoo import models, fields, api



class BrandBrand(models.Model):
    _name = "brand.brand"


    name = fields.Char(string="Name",required=True)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    brand_id = fields.Many2one('brand.brand', string="Brand Name")



