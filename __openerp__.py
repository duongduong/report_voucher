{
    'name' : 'PJ_Test',
    'version' : '1.0',
    'description' : "",
    'depends' : [ 'product', 'account','base', 'sale','account_voucher'
                 ],
    'data': ['_test_view.xml',
             'report/report_saleorder_inherit.xml',
             'report_acc_voucher.xml',
             'report/report_account_voucher_pdf.xml'],

    'auto_install': False,
}