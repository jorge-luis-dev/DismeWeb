from odoo.http import request, route

from odoo.addons.website.controllers.main import Home


class Category(Home):
    @route(
        "/hola/odoo/v1/products/category/<int:category_id>", auth="public", website=True
    )
    def products_category(self, category_id, **kwargs):
        result = (
            request.env["product.category"]
            .sudo()
            .search_read(
                [("id", "=", category_id), ("is_published", "=", True)],
                ["name"],
                limit=1,
            )
        )

        if result:
            category_name = f"Productos de {result[0]["name"]}"

            Product = request.env["product.template"]
            products = Product.sudo().search([("categ_id", "=", category_id)])
        else:
            return request.render("web_portal.404", status=404)

        return request.render(
            "web_portal.products_category_web_portal",
            {
                "products": products,
                "categorie_name": category_name,
            },
        )
