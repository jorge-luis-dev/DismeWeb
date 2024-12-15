def post_init_hook(env):
    all_companies = env["res.company"].search([])
    country_code = "EC"
    country = env["res.country"].search([("code", "=", country_code)])

    for company in all_companies:
        company.sudo().write({"country_id": country.id})
