import odoo.tests.common as common


class TestProductCategoryCustom(common.TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        vals = {
            "name": "Category Test",
            "external_url": "www.odoo.com"
        }
        cls.category = cls.env["product.category"].create(vals)

    def test_category(self):
        new_category = self.category.copy()

        self.assertEqual(
            False,
            new_category.is_published,
        )
