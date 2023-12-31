

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('customer_email', models.EmailField(max_length=100)),
                ('service', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
