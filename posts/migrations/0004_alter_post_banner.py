
# Generated by Django 5.0.7 on 2024-07-30 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_post_image_url_post_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, default='fallback.png', upload_to=''),
        ),
    ]

# Generated by Django 5.0.7 on 2024-07-30 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_post_image_url_post_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, default='fallback.png', upload_to=''),
        ),
    ]

