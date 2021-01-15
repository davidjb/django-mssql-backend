# Generated by Django 3.1.5 on 2021-01-18 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0007_test_remove_onetoone_field_part2'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestUnsupportableUniqueConstraint',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('_type', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TestSupportableUniqueConstraint',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('_type', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddConstraint(
            model_name='testsupportableuniqueconstraint',
            constraint=models.UniqueConstraint(
                condition=models.Q(
                    ('status', 'in_progress'),
                    ('status', 'needs_changes'),
                    ('status', 'published'),
                ),
                fields=('_type',),
                name='and_constraint',
            ),
        ),
        migrations.AddConstraint(
            model_name='testsupportableuniqueconstraint',
            constraint=models.UniqueConstraint(
                condition=models.Q(status__in=['in_progress', 'needs_changes']),
                fields=('_type',),
                name='in_constraint',
            ),
        ),
    ]
