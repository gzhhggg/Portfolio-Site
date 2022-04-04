from django.db import models

class Profile(models.Model):
    title = models.CharField('タイトル', max_length=100, null=True, blank=True)
    subtitle = models.CharField('サブタイトル', max_length=100, null=True, blank=True)
    name = models.CharField('名前', max_length=100)
    job = models.TextField('仕事')
    introduction = models.TextField('自己紹介')
    github = models.CharField('github', max_length=100, null=True, blank=True)
    twitter = models.CharField('twitter', max_length=100, null=True, blank=True)
    linkedin = models.CharField('linkedin', max_length=100, null=True, blank=True)
    facebook = models.CharField('facebook', max_length=100, null=True, blank=True)
    instagram = models.CharField('instagram', max_length=100, null=True, blank=True)
    topimage = models.ImageField(upload_to='images', verbose_name='トップ画像')
    subimage = models.ImageField(upload_to='images', verbose_name='サブ画像')

    def __str__(self):
        return self.name

class Work(models.Model):
    title = models.CharField('タイトル', max_length=100)
    image = models.ImageField(upload_to='images', verbose_name='イメージ画像')
    thumbnail = models.ImageField(upload_to='images', verbose_name='サムネイル', null=True, blank=True)
    language = models.CharField('言語', max_length=100,  null=True, blank=True)
    os = models.CharField('OS',max_length=100, null=True, blank=True)
    database = models.CharField('database',max_length=100, null=True, blank=True)
    framework = models.CharField('framework',max_length=100, null=True, blank=True)
    cloud = models.CharField('cloud',max_length=100, null=True, blank=True)
    url = models.CharField('URL', max_length=100, null=True, blank=True)
    deploy = models.CharField('deploy', max_length=100, null=True, blank=True)
    created = models.DateField('作成日時')
    description = models.TextField('説明')
    point = models.TextField('ポイント')

    def __str__(self):
        return self.title

class Experience(models.Model):
    occupation = models.CharField('職種', max_length=100)
    company = models.CharField('会社', max_length=100)
    description = models.TextField('説明')
    place = models.CharField('場所', max_length=100)
    period = models.CharField('期間', max_length=100)

    def __str__(self):
        return self.occupation


class Education(models.Model):
    course = models.CharField('コース', max_length=100)
    school = models.CharField('学校', max_length=100)
    place = models.CharField('場所', max_length=100)
    period = models.CharField('期間', max_length=100)

    def __str__(self):
        return self.course

class OS(models.Model):
    name = models.CharField('OS', max_length=100)
    level = models.CharField('レベル', max_length=100)
    percentage = models.IntegerField('パーセンテージ')

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField('言語', max_length=100)
    level = models.CharField('レベル', max_length=100)
    percentage = models.IntegerField('パーセンテージ')

    def __str__(self):
        return self.name

class Database(models.Model):
    name = models.CharField('データベース', max_length=100)
    level = models.CharField('レベル', max_length=100)
    percentage = models.IntegerField('パーセンテージ')

    def __str__(self):
        return self.name

class Framework(models.Model):
    name = models.CharField('フレームワーク', max_length=100)
    level = models.CharField('レベル', max_length=100)
    percentage = models.IntegerField('パーセンテージ')

    def __str__(self):
        return self.name

class Cloud(models.Model):
    name = models.CharField('クラウドサービス', max_length=100)
    level = models.CharField('レベル', max_length=100)
    percentage = models.IntegerField('パーセンテージ')

    def __str__(self):
        return self.name