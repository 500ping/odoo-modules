from odoo import models, fields, _


class MPSPlanWizard(models.TransientModel):
    _name = 'select.mps.plan'

    plan_id = fields.Many2one('mps.plan', srting=_('Select Plan'))

    def select_plan(self):
        for product in self.plan_id.plan_line_ids.product_id:
            print(product.name)