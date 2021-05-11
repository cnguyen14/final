
from django.db import migrations

GROUPS = [
    {
        'name': 'ci_manager',
    },
    {
        'name': 'ci_shipper',
    },
    {
        'name': 'ci_customer',
    },
]


def add_group_data(apps, schema_editor):
    group_model_class = apps.get_model('auth', 'Group')
    for group in GROUPS:
        group_object = group_model_class.objects.create(
            name=group['name'],
        )


def remove_group_data(apps, schema_editor):
    group_model_class = apps.get_model('auth', 'Group')
    for group in GROUPS:
        group_object = group_model_class.objects.get(
            name=group['name']
        )
        group_object.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [

        migrations.RunPython(
            add_group_data,
            remove_group_data
        )

    ]