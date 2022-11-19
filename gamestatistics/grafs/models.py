from django.db import models
"""
Таблица версии, таблица юзеры, таблица ивенты, потом таблица сессии еще добавится

Юзер основа, у юзера лежат ссылки на массивы ивентов и сессий
"""

class Event(models.Model):
    sub_id = models.IntegerField()
    platform = models.CharField(max_length=255, blank=True, null=True)
    deviceType = models.CharField(max_length=255, blank=True, null=True)
    eventName = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=255, blank=True, null=True)
    referrer = models.CharField(max_length=255, blank=True, null=True)
    localTime = models.TimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    loadTime = models.CharField(max_length=255, blank=True, null=True)
    timeFromStart = models.IntegerField( blank=True, null=True)


    def __str__(self):
        return f'{self.sub_id}  название ивента {self.eventName}'


class Version(models.Model):
    sub_id = models.IntegerField()
    versionIdentifier = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    startTime = models.TimeField( blank=True, null=True)
    startDate = models.DateField( blank=True, null=True)
    startDateLong = models.IntegerField( blank=True, null=True)
    endTime = models.TimeField( blank=True, null=True)
    endDate = models.DateField( blank=True, null=True)
    endDateLong = models.IntegerField( blank=True, null=True)

    def __str__(self):
        return f'{self.sub_id}  версия {self.versionIdentifier}'

# class Session(models.Model):


class SubUser(models.Model):
    sub_id = models.IntegerField()
    platformUserId = models.IntegerField()
    sessionCounter = models.IntegerField( blank=True, null=True)
    playTime = models.IntegerField( blank=True, null=True)
    active = models.BooleanField(default=False, blank=True, null=True)
    lastActivity = models.IntegerField( blank=True, null=True)
    referer = models.CharField(max_length=255, blank=True, null=True)
    registrationDate = models.DateField( blank=True, null=True)
    adsCounter = models.IntegerField( blank=True, null=True)
    platform = models.CharField(max_length=255, blank=True, null=True)
    deviseType = models.CharField(max_length=255, blank=True, null=True)
    event = models.ManyToManyField(Event)
    # session = models.ForeignKey(Session, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.sub_id}  платформа {self.platformUserId}'




