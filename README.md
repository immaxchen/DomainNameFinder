# DomainNameFinder
A python tool for finding available domain names with given text combination

Need to have whois installed on your computer

Feel free to edit the text files for word list

# Example

find available domain names with pattern: (one-letter)muffin.com

```python
from DomainNameFinder import *

checknames(letters, ['muffin'])
```
