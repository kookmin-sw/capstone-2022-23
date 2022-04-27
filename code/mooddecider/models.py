from django.db import models
from model_utils.fields import StatusField
from model_utils import Choices


# class TimestampedModel(models.Model):
#     created_at = models.DateTimeField(
#         auto_now_add=True,
#         db_column="CRE_DT",
#         verbose_name="생성시간",
#         help_text="The value is automatically entered when the table is created.",
#     )
#     updated_at = models.DateTimeField(
#         auto_now=True,
#         db_column="UPD_DT",
#         verbose_name="갱신시간",
#         help_text="The value is automatically entered when the table is updated.",
#     )

#     class Meta:
#         abstract = True


# class Result(TimestampedModel):
#     STATUS = Choices("ongoing", "completion", "failure")
#     # user = models.ForeignKey(User, db_column='USER_ID', verbose_name='사용자ID', related_name='result', on_delete=models.CASCADE)
#     url = models.CharField(
#         db_column="URL",
#         max_length=50,
#         verbose_name="URL",
#         help_text="The value is the address of the page the user wants to analyze the mood(atmosphere).",
#     )
#     status = StatusField(
#         db_column="RESULT_ST",
#         verbose_name="분석상태",
#         help_text="The value is an analysis status value, which includes ongoing, failure, completion.",
#     )

#     class Meta:
#         db_table = "Result"
#         verbose_name = "result"
#         verbose_name_plural = "results"

#     def __str__(self):
#         return "url: %s의 분석 결과" % (self.url)

#     def get_absolute_url(self):
#         return reverse("result", kwargs={"pk": self.pk})


# class History(TimestampedModel):
#     STATUS = Choices("ongoing", "success", "failure")
#     # user = models.ForeignKey(User, db_column='USER_ID', verbose_name='사용자ID', related_name='result', on_delete=models.CASCADE)
#     url = models.CharField(
#         db_column="URL",
#         max_length=50,
#         verbose_name="URL",
#         help_text="The value is the address of the page the user wants to analyze the mood(atmosphere).",
#     )
#     status = StatusField(
#         db_column="RESULT_ST",
#         verbose_name="분석상태",
#         help_text="The value is an analysis status value, which includes ongoing, failure, success.",
#     )

#     class Meta:
#         db_table = "History"
#         verbose_name = "history"
#         verbose_name_plural = "history"
#         constraints = [
#             models.UniqueConstraint(
#                 fields=["user", "created_at"],
#                 name="unique history",
#                 # deferrable = constraints.Deferrable.DEFERRED,
#             )
#         ]

#     def __str__(self):
#         return "분석 결과리스트"

#     def get_absolute_url(self):
#         return reverse("history", kwargs={"pk": self.pk})
