# Remove Jira Issue Links from issue-key
<small>
Author: Suman Dinda<br>
Website: suman-dinda.github.io
</small>


## Steps

* Get issue-keys from csv file and fetch the issuelink key id using the jira get api key
```
/rest/api/2/issue/{issue-key}
```
* Delete the issue link from the rest api with DELETE request

```
/rest/api/2/issueLink/{linkId}
```

## Install Dependencies if any error manually

```
pip install requests HTTPBasicAuth getpass logging
```

## Requirements
- Python 3+ Interpreter

## Run Program

```
python index.py
```
## Notes

- Code is under testing, the current index.py supports deletion of outward links with outware name 'Implments'
- Make appropriate changes as required in line no: 47 for other link types

Good Day !!