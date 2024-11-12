from re import search

from odoo import models, fields, api


class CustomerMetrics(models.Model):
    _name = 'res.partner.customer.metrics'
    _description = 'customer_metrics.customer_metrics'

    customer_id = fields.Many2one(comodel_name='res.partner', string='Customer')
    total_sales = fields.Float(compute='_compute_total_sales' , readonly= True)
    order_count = fields.Integer(compute='_compute_total_sales' , readonly= True)

    @api.depends('customer_id')
    def _compute_total_sales(self):

        for rec in self:

            orders = self.env['sale.order'].search([('partner_id', '=' , rec.customer_id.id)]).mapped('amount_total')
            rec.order_count = len(orders)
            rec.total_sales = sum(orders)


    def get_top_customers(self , *args, **kwargs):

        top_customers = self.env['sale.order'].read_group([('state', '=', 'sale')],
            fields=['partner_id', 'amount_total'],
            groupby=['partner_id'],
            orderby='amount_total desc',
            limit=5,)

        result = []

        for customer in top_customers:
            count_orders = self.env['sale.order'].search_count([('partner_id' , '=' , customer['partner_id'][0])])
            result.append({"name": customer['partner_id'][1] , "amount_total": customer['amount_total'] , "count_order": count_orders})

        return result