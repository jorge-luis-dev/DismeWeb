{
    "name": "Disme Website",
    "summary": "Website for Disme",
    "version": "18.0.1.0.0",
    "license": "AGPL-3",
    "author": "Jorge Luis,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-ecuador",
    "category": "website",
    "depends": [
        "stock",
        "l10n_ec",
        "portal",
        "product_categ_image",
        "product_category_custom",
    ],
    "data": [
        # 'security/ir.model.access.csv',
        "views/home_web_portal.xml",
        "views/product_by_category.xml",
        "views/404.xml",
    ],
    "installable": True,
    "post_init_hook": "post_init_hook",
}
