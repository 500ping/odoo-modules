odoo.define('sopoka_mps.ClientActionInherit', function (require) {
    'use strict';

    var ClientAction = require('mrp_mps.ClientAction');

    return ClientAction.include({
        events: _.extend({}, ClientAction.prototype.events, {
            'click .o_mrp_mps_select_plan': '_onClickSelectPlan',
        }),

        _onClickSelectPlan: function (ev) {
            ev.stopPropagation();
            this._selectPlan();
        },

        _selectPlan: function (dateIndex, productionScheduleId) {
            var self = this;
            console.log('123');
            this.mutex.exec(function () {
                return self.do_action('sopoka_mps.select_mps_plan_wizard', {});
            });
        },
    });
});