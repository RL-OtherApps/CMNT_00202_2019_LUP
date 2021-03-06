# © 2020 Comunitea - Javier Colmenero <javier@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Cost Sheet Lupeon',
    'version': '12.0.0.0',
    'author': 'Custom ',
    "category": "Sales",
    'license': 'AGPL-3',
    'depends': [
        'sale',
        'stock_picking_report_valued',
        'project',
        'mrp',
        'hr'
    ],
    'contributors': [
        "Comunitea ",
        "Javier Colmenero <javier@comunitea.com>"
    ],
    "data": [
        'security/ir.model.access.csv',
        'security/sheet_security.xml',
        'data/sheet_data.xml',
        'views/sale_view.xml',
        'views/cost_sheet_view.xml',
        'views/applicable_legislation_view.xml',
        'views/part_feature_view.xml',
        'views/oppi_type_view.xml',
        'views/printer_machine.xml',
        'views/product_view.xml',
        'views/design_software_view.xml',
        'views/project_view.xml',
        'views/mrp_production_view.xml',
    ],
    "installable": True,
    'application': False,
}
