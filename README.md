# JSON Translations to CSV

## Convert multiple json translation files to one csv

### Usage: JSON files to CSV
Add json files to `input` directory. Files should have simple object with key values for example:
```
{
    "translationKey1": "value1",
    "translationKey2": "value2"
}
```

Run `py scritp.py`
Results CSV file will be in `output` directory.

### Usage: CSV to JSON files
Add csv file named `data.csv` to `input` directory. CSV should be same format as output from JSONtoCSV script
Run `script-revert.py`
Results JSON files will be in `output` directory.
