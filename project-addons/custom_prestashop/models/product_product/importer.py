# © 2020 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo.addons.component.core import Component
from odoo.addons.connector.components.mapper import mapping


class ProductCombinationMapper(Component):
    _inherit = "prestashop.product.combination.mapper"

    @mapping
    def from_main_template(self, record):
        main_template = self.get_main_template_binding(record)
        result = super().from_main_template(record)
        if (
            main_template
            and main_template.odoo_id["type"] == "virtual"
        ):
            result["type"] = "service"
        else:
            result["type"] = "product"
        return result

    @mapping
    def weight(self, record):
        combination_weight = float(record.get('weight', '0.0'))
        main_weight = self.binder_for('prestashop.product.template').to_internal(record['id_product']).weight
        weight = main_weight + combination_weight
        return {'weight': weight}
