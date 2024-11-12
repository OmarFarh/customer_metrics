# -*- coding: utf-8 -*-
# from odoo import http


# class CustomerMetrics(http.Controller):
#     @http.route('/customer_metrics/customer_metrics', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customer_metrics/customer_metrics/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('customer_metrics.listing', {
#             'root': '/customer_metrics/customer_metrics',
#             'objects': http.request.env['customer_metrics.customer_metrics'].search([]),
#         })

#     @http.route('/customer_metrics/customer_metrics/objects/<model("customer_metrics.customer_metrics"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customer_metrics.object', {
#             'object': obj
#         })

