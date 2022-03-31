# [DE]
# :spoon: LöeffelspracheConverterPY :spoon:

Basic Converter von normaler Sprache[^1] bzw. Text[^1] in die sog. "Löffelsprache" auch "Löfflisch" genannt - mit Python. 
[^1]: Nur getestet mit Deutsch

Der code enthät ein Dictionary, welches beliebig geändert werden kann.
So können mit wenigen Änderungen auch die vielen Abwandlungen der Sprache eingepflegt werden.

### :scroll: Benötigt wird folgende Library: :scroll:
**[re] (Regular Expression Operations) aka regex**

Falls nicht vorhanden, kann diese über pip installiert werden:
> pip install regex

### :open_book: Das Dictionary ist wiefolgt aufgebaut: :open_book:
```
rep_dict = {'a': 'alewa',
            'e': 'elewe',
            'i': 'ilewi',
            'o': 'olewo',
            'u': 'ulewu',
            'ä': 'älewä',
            'ö': 'ölewö',
            'ü': 'ülewü',
            'ei': 'eilewei',
            'ie': 'ielewie',
            'au': 'aulewau'}
```           
Hier können abwandlungen der Sprache angelegt werden, oder auch zusätzliche Werte zur weiteren "Verschlüsselung" hinzugefügt werden.

# [EN]
# :spoon: SpoonSpeechConverterPY :spoon:

Basic converter from normal speech[^2] or text[^2] to the so called "Löffelsprache" also known as "Löfflisch" - with Python. 
[^2]: tested with german. even though this documentation is in english, i think this won't work with english. But if there's something simmilar in the english language please let me know how it works and commit your code to the project.

The code contains a dictionary, which you can edit to your needs.
This way you can easily make changes and implement dozens of varieties to the speech. (or maybe create your own one?)

### :scroll: Needed library: :scroll:
**[re] (Regular Expression Operations) aka regex**

If you don't have this in your python installation already, you can install it using pip:
> pip install regex

### :open_book: The dictionary is built like this: :open_book:
```
rep_dict = {'a': 'alewa',
            'e': 'elewe',
            'i': 'ilewi',
            'o': 'olewo',
            'u': 'ulewu',
            'ä': 'älewä',
            'ö': 'ölewö',
            'ü': 'ülewü',
            'ei': 'eilewei',
            'ie': 'ielewie',
            'au': 'aulewau'}
```           
Here you can create or change varieties of the speech, or you can also add additional letters for further "decryption".


_coded with :purple_heart: by_ **Fabian Rehme**
