from odoo import fields, models, _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    external_url = fields.Char(
        string="External URL",
    )

    is_published = fields.Boolean(
        string="Published",
        default=False,
    )