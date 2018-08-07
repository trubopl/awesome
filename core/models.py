from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

from ckeditor_uploader.fields import RichTextUploadingField


class CompaniesLoans(models.Model):
    name = models.CharField(max_length=100)
    min_amount = models.IntegerField()
    max_amount = models.IntegerField()
    min_duration = models.IntegerField()
    max_duration = models.IntegerField()
    first_free = models.BooleanField()
    amount_first_free = models.IntegerField()
    age = models.CharField(max_length=100)
    verification = models.CharField(max_length=100)
    extension_period = models.BooleanField()
    order = models.IntegerField()
    miscs = models.CharField(max_length=250, blank=True)


    # <-- Fields for representative example -->
    example_amount = models.IntegerField()
    example_duration = models.IntegerField()
    example_fixed_interest_rate = models.IntegerField()
    example_total_amount_repay = models.IntegerField()
    example_total_installment_amount = models.IntegerField()
    example_capital_interest = models.IntegerField()
    example_provision = models.IntegerField()
    example_rrso = models.IntegerField()
    example_installment_amount = models.IntegerField()

    def __str__(self):
        return self.name


class CompaniesInstallment(models.Model):
    inst_name = models.CharField(max_length=100)
    inst_min_amount = models.IntegerField()
    inst_max_amount = models.IntegerField()
    inst_min_duration = models.IntegerField()
    inst_max_duration = models.IntegerField()
    inst_first_free = models.BooleanField()
    inst_amount_first_free = models.IntegerField()
    inst_age = models.CharField(max_length=100)
    inst_verification = models.CharField(max_length=100)
    inst_extension_period = models.BooleanField()
    inst_order = models.IntegerField()
    inst_miscs = models.CharField(max_length=250, blank=True)

    # <-- Fields for representative example -->
    inst_example_amount = models.IntegerField()
    inst_example_duration = models.IntegerField()
    inst_example_fixed_interest_rate = models.IntegerField()
    inst_example_total_amount_repay = models.IntegerField()
    inst_example_total_installment_amount = models.IntegerField()
    inst_example_capital_interest = models.IntegerField()
    inst_example_provision = models.IntegerField()
    inst_example_rrso = models.IntegerField()
    inst_example_installment_amount = models.IntegerField()

    def __str__(self):
        return self.name


class CompaniesCredit(models.Model):
    name = models.CharField(max_length=100)
    min_amount = models.IntegerField()
    max_amount = models.IntegerField()
    min_days = models.IntegerField()
    max_days = models.IntegerField()
    miscs = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=255, null=False)
    published_date = models.DateTimeField(default=timezone.now(), blank=True, null=True)
    description = RichTextUploadingField(null=False)
    meta_title = models.CharField(max_length=158, null=False)
    meta_description = models.CharField(max_length=320, null=False)
    slug = models.SlugField(default='', null=False)

#<--- Validations turned off until Edit button exists -->

    #def validate_title(self):
        #title_exists = Post.objects.filter(title=self.title).exists()

        #if title_exists:
            #raise ValidationError('Title already exists ! ')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        #self.validate_title()
        super(Post, self).save(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/blog/' + self.slug

