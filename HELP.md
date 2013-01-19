Basic steps to add support for a particular service:

1. Add information to
    [README](https://github.com/rigoneri/syte/blob/master/README.md)
2. Add setting to turn service on/off
    in [syte_settings.py](https://github.com/rigoneri/syte/blob/master/syte/syte_settings.py)
3. Add above setting to site_pages context processor in
    [context_processor.py](https://github.com/rigoneri/syte/blob/master/syte/context_processor.py)
4. Add a new django view for the particular service to get info and return json.
 	- For example [twitter.py](https://github.com/rigoneri/syte/blob/master/syte/views/twitter.py) or [dribbble.py](https://github.com/rigoneri/syte/blob/master/syte/views/dribbble.py)
5. Add above view to [urls.py](https://github.com/rigoneri/syte/blob/master/syte/urls.py)
6. Write js file/function to query django view and add to
    [js components](https://github.com/rigoneri/syte/tree/master/syte/static/js/components)
7. Add hook/call to main javascript integration point
   [links.js](https://github.com/rigoneri/syte/tree/master/syte/static/js/components/links.js)
8. Add above js to list of js to
    [compress.py](https://github.com/rigoneri/syte/blob/master/syte/compress.py)
9. Add link for service to
    [base view template](https://github.com/rigoneri/syte/blob/master/syte/templates/base.html)
10. Add html template to
    [templates directory](https://github.com/rigoneri/syte/tree/master/syte/static/templates) to be rendered js file/function that queries django view for service.
