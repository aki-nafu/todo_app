from django.db import models

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    u_id = models.IntegerField(default=1)

    # 変更
    def __str__(self):
        return self.item + ' | ' + str(self.completed) + ' | ' + str(self.u_id)