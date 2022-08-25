from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='Фото'),
        ),
    ]