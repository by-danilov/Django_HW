from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    help = 'Создает группу "Модератор продуктов" с нужными правами.'

    def handle(self, *args, **options):
        MODERATOR_GROUP_NAME = 'Модератор продуктов'
        moderator_group, created = Group.objects.get_or_create(name=MODERATOR_GROUP_NAME)

        content_type = ContentType.objects.get_for_model(Product)

        required_permissions = [
            'can_unpublish_product',
            'delete_product',
        ]


        for codename in required_permissions:
            try:
                permission = Permission.objects.get(
                    codename=codename,
                    content_type=content_type,
                )
                moderator_group.permissions.add(permission)
                self.stdout.write(self.style.SUCCESS(f' - Добавлено право: {codename}'))
            except Permission.DoesNotExist:
                self.stdout.write(self.style.ERROR(f' - ОШИБКА: Право {codename} не найдено. Проверьте миграции.'))

        self.stdout.write(self.style.SUCCESS(
            f'\nГруппа "{MODERATOR_GROUP_NAME}" успешно настроена.'
        ))
