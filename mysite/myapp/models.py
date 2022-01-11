from django.db import models


class Question(models.Model):
    label = models.CharField(
        max_length=100
    )

    class Meta:
        # Hier kun je metadata definiere, bijv. naam van het model en wat het meervoud is
        # Dit zie je bijv. terug in de admin
        verbose_name = "Vraag"
        verbose_name_plural = "Vragen"
        # unique_together

    def __str__(self):
        # Als we een object printen hoe moet dat gerepresenteerd worden
        return self.label


class Answer(models.Model):
    # Normale tekst input
    label = models.CharField(
        max_length=100
    )
    # A relatie naar een ander model (tabel)
    question = models.ForeignKey(
        # De manier om aan te geven waar de relatie naar toe ligt -> "AppNaam.ModelNaam"
        "myapp.Question",
        # Als we de `Question` verwijderen, verwijderen we ook de antwoord optie
        on_delete=models.CASCADE,
        # Of er null values in de DB mogen
        null=True,
        # Of het formulier dat we baseren op dit model (in de admin bijv.) leeg mag blijven
        blank=True
    )

    class Meta:
        # Hier kun je metadata definiere, bijv. naam van het model en wat het meervoud is
        # Dit zie je bijv. terug in de admin
        verbose_name = "Antwoord"
        verbose_name_plural = "Antwoorden"
        # unique_together

    def __str__(self):
        # Als we een object printen hoe moet dat gerepresenteerd worden
        # Hier gebruiken we de f-string, handig voor het gebruik met variabelen
        return f"Antwoord '{self.label}' voor vraag {self.question.label}"
