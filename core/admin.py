from django.contrib import admin
from .models import Post, CompaniesLoans


class CompaniesAdmin(admin.ModelAdmin):
    fieldsets = (
                ('Main', {
                        'fields': (

                            'name',
                            ('min_amount', 'max_amount',),
                            ('min_duration', 'max_duration',),
                            'first_free',
                            'amount_first_free',
                            'age',
                            'verification',
                            'extension_period',
                            'order',
                            'miscs'
                        )
                    }
                 ),
                ('Example Loan Data', {
                        'fields': (
                            'example_amount',
                            'example_duration',
                            'example_fixed_interest_rate',
                            'example_total_amount_repay',
                            'example_total_installment_amount',
                            'example_capital_interest',
                            'example_provision',
                            'example_rrso',
                            'example_installment_amount',
                        )
                })
    )


admin.site.register(Post)
admin.site.register(CompaniesLoans, CompaniesAdmin)




