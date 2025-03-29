from django.db import models


# Create your models here.
class NLOnlineAntrag(models.Model):
    application_date = models.DateTimeField(auto_now_add=True)
    street = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    phone = models.CharField(max_length=100)

    field_of_study = models.CharField(max_length=100)
    application_date_bafoeg = models.DateField(blank=True)

    account_holder = models.CharField(max_length=100)
    iban = models.CharField(max_length=100)
    bic = models.CharField(max_length=100)

    signed_form = models.FileField(upload_to='signed_forms/')
    health_insurance_certificate = models.FileField(upload_to='health_insurance_certificates/')
    enrollment_certificate = models.FileField(upload_to='enrollment_certificates/')
    bank_statements = models.FileField(upload_to='bank_statements/')
    identity_document = models.FileField(upload_to='identity_documents/')
    other_documents = models.FileField(upload_to='other_documents/', blank=True)


class Applicant(models.Model):
    application = models.ForeignKey(NLOnlineAntrag, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    email = models.EmailField(max_length=100)
    stud_email = models.EmailField(max_length=100)


class EarningsExpenses(models.Model):
    application = models.ForeignKey(NLOnlineAntrag, on_delete=models.CASCADE, related_name='earnings_expenses')

    earning_month = models.DateField()

    earnings_from_parents = models.DecimalField(max_digits=10, decimal_places=2)
    earnings_from_grants = models.DecimalField(max_digits=10, decimal_places=2)
    earnings_from_job = models.DecimalField(max_digits=10, decimal_places=2)
    earnings_from_credit = models.DecimalField(max_digits=10, decimal_places=2)
    other_earnings = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    other_earnings_description = models.CharField(max_length=100, blank=True)

    # expenses_for_rent = models.DecimalField(max_digits=10, decimal_places=2)
    # expenses_for_food = models.DecimalField(max_digits=10, decimal_places=2)
    # expenses_for_health_insurance = models.DecimalField(max_digits=10, decimal_places=2)
