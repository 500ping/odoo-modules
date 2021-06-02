from odoo import models, fields, api, _


class MrpProductionPlan(models.Model):
    _name = "mps.plan"
    _description = "Plan For MPS"

    name = fields.Char(string=_('Plan Name'))
    date_start = fields.Date(string=_('Date Start'), default=fields.Date.today)
    date_stop = fields.Date(string=_('Date Stop'))
    date_stop = fields.Date(string=_('Date Stop'))
    plan_line_ids = fields.One2many('mps.plan.line', 'plan_id', string=_('Plan Lines'))


class MrpProductionPlanLine(models.Model):
    _name = "mps.plan.line"
    _description = "Plan Details For MPS"

    name = fields.Char(string=_('Ref'))
    product_id = fields.Many2one('product.product', string=_('Product'))
    qty_todo = fields.Float(string=_('Quantity'))
    plan_id = fields.Many2one('mps.plan', string=_('MPS Plan Id'))