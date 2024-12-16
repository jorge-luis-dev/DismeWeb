from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    external_url = fields.Char(
        string="External URL",
    )

    is_published = fields.Boolean(
        string="Published",
        default=True,
    )

    pdf_attachment = fields.Binary("PDF Attachment")
    pdf_attachment_name = fields.Char("PDF File Name")
