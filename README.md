# TI-nspire CX II-T CRC Encoder und Decoder

Dieses Repository enthält Python-Skripte zur Durchführung der CRC (Cyclic Redundancy Check)-Kodierung und -Dekodierung, optimiert für den TI-nspire CX II-T Taschenrechner.

## CRC Encoder

`crcEncoder.py` führt eine CRC-Kodierung auf binären Daten durch. Es dividiert die Daten durch ein Generatorpolynom und fügt die resultierende CRC-Prüfsumme an die Originaldaten an.

## Detaillierte Ausgabe der Berechnung

Das Skript `crcEncoder.py` gibt nicht nur den Transmitted Value aus, sondern zeigt auch den gesamten Lösungsweg der binären Polynomdivision. Dies umfasst jeden Schritt der Division, die XOR-Operationen und den berechneten Rest. Diese detaillierte Ausgabe hilft dabei, den Prozess der CRC-Kodierung besser zu verstehen und zu verfolgen.

### Anpassung

- Ändern Sie `val1` für die zu kodierenden Daten.
- Ändern Sie `val2` für das Generatorpolynom.

### Beispiel

```python
val1 = "011000100101" # Ihre Daten
val2 = "10011"       # Ihr Generatorpolynom
```

## CRC Decoder

`crcDecoder.py`  wird verwendet, um die Integrität der empfangenen Daten zu überprüfen.

## Nutzung auf TI-nspire CX CAS

1. Laden Sie die `.py`-Dateien und `.tns`-Dateien aus dem Repository herunter.
2. Übertragen Sie diese Dateien mithilfe der TI-nspire CX CAS Student Software auf Ihren Taschenrechner.
3. Öffnen Sie die Dateien auf dem Taschenrechner, um die Skripte auszuführen.

Für weitere Details zur Nutzung und Anpassung der Skripte, siehe die Kommentare im Code.