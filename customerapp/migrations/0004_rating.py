

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0003_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('customer_email', models.EmailField(max_length=100)),
                ('rating', models.BigIntegerField()),
                ('review', models.CharField(max_length=100)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
            ],
        ),
    ]
