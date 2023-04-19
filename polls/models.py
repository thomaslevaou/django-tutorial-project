from django.db import models

"""
En Django, les modèles représentent l'organisation en base de données, avec éventuellement quelques métadonnées supplémentaires.
Le modèle Django est censé être la seule et définitive source d'information sur la donnée. Django suit le principe du DRY (Don't Repeat Yourself),
et donc va éviter toute redondance (comme j'ai souvent eu l'habitude de voir en SQL).

En Django, les migrations dépendent complètement des modèles (alors que ce n'est pas le cas en Ruby on Rails par exemple).

Tous les modèles Django héritent de la classe `models.Model`.

Les déclarations de modèle ci-dessous suffisent à Django pour pouvoir faire ensuite des CREATE TABLE, et créer une API de connexion à la base de données pour
que les modifications des modèles ci-dessous se synchronisent avec les tables en base.
"""

class Question(models.Model):
    question_text = models.CharField(max_length=200)

    # Si on précise une string en premier caractère du champ du modèle, alors ce sera le nom du champ de manière "plus humainement lisible"
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    # Comme en Symfony, on peut faire du ManyToOne, ManyToMany et du OneToOne en Django
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
