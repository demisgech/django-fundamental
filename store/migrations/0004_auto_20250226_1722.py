# Generated by Django 5.1.6 on 2025-02-26 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_add_slug_to_product'),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT INTO store_collection(title)              
            VALUES('collection1')
            """,
            """
            DELETE FROM store_collection 
            WHERE title ='collection1'
            """)
    ]
