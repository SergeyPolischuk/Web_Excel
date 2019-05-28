from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name
        # return "Статус заказа %s" % self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказов'


class Order(models.Model):
    id = models.TextField(primary_key=True, null=False, blank=False, editable=False)
    description = models.TextField(max_length=1024,
                                   verbose_name='Описание задачи',
                                   help_text='Осталось %s' %1024 + ' символа(-ов)')
    customer_name = models.CharField(max_length=32, null=False, verbose_name='Ваше имя', help_text='Введите ваше имя')
    customer_phone = models.CharField(max_length=12,
                                      blank=True,
                                      null=True,
                                      default=None,
                                      verbose_name='Ваш номер телефона',
                                      help_text='Введите ваш номер телефона')       # TODO: добавить маску ввода для номера телефона
    customer_email = models.EmailField(max_length=32, blank=True, null=True, default=None, verbose_name='Ваш Email', help_text='Введите ваш Email')

    # polischuksg@gmail.com
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False)
    date_updated = models.DateTimeField(auto_now_add=False, auto_now=True, editable=False)
    date_deadline = models.DateField(blank=True,
                                     null=True,
                                     default=None,
                                     verbose_name='Желаемый срок выполнения задачи')    # TODO: дописать валидацию даты

    # urgently = models.BooleanField(default=False, verbose_name='Срочно')   #срочность
    # status = models.ForeignKey('Status', on_delete=True, default='В обработке', editable=False)     #скрытое поле

    cost = models.PositiveIntegerField(blank=True,
                                       null=True,
                                       default=100,
                                       validators=[MinValueValidator(50)],
                                       verbose_name='Оценочная стоимость, USD',
                                       help_text='Введите оценочную стоимость или бюджет вашей задачи в USD')
    attachment = models.FileField(upload_to='file', blank=True, null=True, default=None, verbose_name='Выберите файл для загрузки')  # upload_to

    def __str__(self):
        return "Заказ %s %s" % (self.pk, self.date_deadline)

    class Meta:
        ordering = ["-date_created"]
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'




# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)