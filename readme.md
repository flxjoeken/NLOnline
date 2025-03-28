# NLOnline

> [!NOTE]
> Hier entsteht eine Webanwendung um Notlagenzuschuss-Anträge an die Verfasste Studierendenschaft der 
> Universität Heidelberg digital stellen zu können. 

## Einrichtung einer Entwicklungsumgebung

```shell
pip install -r 'requirements.txt'

# Bei Bedarf Datenbankmigrationen aktualisieren
python manage.py makemigrations

# Migrationen durchführen
python manage.py migrate

# Server starten
python manage.py runserver
```

## TODOs

- [ ] Eigene Datenbank-tabelle für Antragsteller in `models.py` anlegen
- [ ] Den Antragsteller, beim Antragsformular anlegen

- [ ] Sonstiges in Ein- und Ausgaben ausführen
- [ ] Aktiv Monate angeben bei den ein-und ausgaben
- 
