import re

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ProductCategory(models.Model):
    _inherit = "product.category"

    external_url = fields.Char(
        string="External URL",
    )

    is_published = fields.Boolean(
        string="Published",
        default=True,
    )

    def _check_url(self, url):
        # Basic URL validation using a regex
        url_regex = r"^(https?://)?([a-z0-9.-]+)\.[a-z]{2,}(/.*)?$"
        return re.match(url_regex, url)

    @api.constrains("external_url")
    def _validate_url(self):
        for record in self:
            if record.external_url and not self._check_url(record.external_url):
                raise ValidationError(_("The URL provided is not valid."))
