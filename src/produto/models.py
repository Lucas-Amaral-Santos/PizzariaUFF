from django.db import models
from django.conf import settings

class Categoria(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200)

    class Meta:
        db_table = 'categoria'
        ordering = ('nome',)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=120, unique=True)
    imagem = models.CharField(max_length=120)
    quantidade = models.IntegerField(default=0)
    slug = models.SlugField(max_length=120, null=True)
    likes = models.IntegerField('likes', default=0)
    dislikes = models.IntegerField('dislikes', default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_cadastro = models.DateField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='produtos',
                             on_delete=models.DO_NOTHING,
                             null=True)

    def get_add_to_cart_url(self):
        return reverse('produto:cadastra_carrinho', args=[self.id, self.slug])

    class Meta:
        db_table = 'produto'
        ordering = ('nome',)

    def __str__(self):
        return self.nome

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def _str_(self):
        return f"{self.quantity} unidades de {self.item.nome}"

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def _str_(self):
        return self.user.username


class Foto(models.Model):
    nome = models.CharField('nome', max_length=200, blank=True)

    class Meta:
        db_table = 'foto'

    def __str__(self):
        return self.nome
