from odoo import fields, models, api

class CrmReport(models.TransientModel):
    _name = 'crm.won.lost.report'
    sales_person = fields.Many2one('res.users', string="Sales Person")
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date', default=fields.Date.today)

    def print_xls_report(self, cr, uid, ids, context=None):
        data = self.read(cr, uid, ids)[0]
        return {'type': 'ir.actions.report.xml',
                'report_name': 'crm_won_lost_report.report_crm_won_lost_report.xlsx',
                'datas': data
                }

    # def print_xls_report(self, cr, uid, ids, context=None):
    #     rec = self.browse(data)
    #     data = {}
    #     data['form'] = rec.read(['sales_person', 'start_date', 'end_date'])
    #     return self.env['report'].get_action(rec, 'crm_won_lost_report.report_crm_won_lost_report.xlsx', data=data

