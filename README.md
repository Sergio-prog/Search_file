A program to search for any file on all your computers using different parameters

Example:

```python
search = Search(r"C:/Games")
print(search.search_by_suffix(".db"))
>> 'C:\\Games\\Adobe\\Adobe Premiere Pro 2023\\typesupport\\FntNames.db',
>> 'C:\\Games\\osu!\\collection.db'...
```