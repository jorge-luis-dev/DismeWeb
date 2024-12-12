from odoo.http import request, route

from odoo.addons.website.controllers.main import Home


class Main(Home):
    @route("/", auth="public", website=True)
    def index(self, **kwargs):
        super().index(**kwargs)

        Category = request.env["product.category"]
        categories = Category.sudo().search([("is_published", "=", True)])

        res = request.render(
            "web_portal.home_web_portal",
            {"categories": categories},
        )

        return res

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
            categorie_name = f"Productos de {result[0]["name"]}"

            Product = request.env["product.template"]
            products = Product.sudo().search([("categ_id", "=", category_id)])
        else:
            categorie_name = "Productos no encontrados"
            products = False

        return request.render(
            "web_portal.products_category_web_portal",
            {
                "products": products,
                "categorie_name": categorie_name,
            },
        )
