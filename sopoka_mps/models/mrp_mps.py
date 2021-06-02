from odoo import models, fields, api, _
from odoo.tools.date_utils import add, subtract
from odoo.tools.float_utils import float_round
from odoo.exceptions import ValidationError

from math import log10
from collections import defaultdict


class MrpProductionSchedule(models.Model):
    _inherit = "mrp.production.schedule"

    plan_id = fields.Many2one('mps.plan', string=_('Plan'))




