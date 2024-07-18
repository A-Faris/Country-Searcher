# Country Searcher

This is a terminal-based country searcher.

fetchData() function searches for the country that is entered, extracts the useful information and displays it to the searcher.
It extracts as much useful information as possible including the name, currency and flag emoji.
If more than one country is returned (e.g. if you search United it will return United Kingdom and United States of America) then the first one is returned.

Handle Errors.
If the server returns with anything apart from 200 then an appropriate error message is shown.
e.g. If the server returns 404, an error message about the content not being found is shown. If the server shows 500, an error message explaining the error happened on the server is shown.