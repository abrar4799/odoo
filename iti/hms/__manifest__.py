{
    'name': "iti_hms",
    'summary': "summary about hms"
    ,
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'security/security.xml',
        'security/ir.model.csv',
        'views/PatientView.xml',
        'views/DeptView.xml',
        'views/DocView.xml',
        'views/CustView.xml',
        'views/LogHistory.xml',


    ],
    'depends': ['crm'] ,
}