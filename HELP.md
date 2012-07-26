Basic steps to add support for a particular service:

1. Add information to
    [README](https://github.com/rigoneri/syte/blob/master/README.md)
2. Add setting to turn service on/off
    in [syte_settings.py](https://github.com/rigoneri/syte/blob/master/syte/syte_settings.py)
3. Add above setting to site_pages context processor in
    [context_processor.py](https://github.com/rigoneri/syte/blob/master/syte/context_processor.py)
4. Add django view in
    [views.py](https://github.com/rigoneri/syte/blob/master/syte/views.py)
    to get info and return json
5. Add above view to [urls.py](https://github.com/rigoneri/syte/blob/master/syte/urls.py)
6. Add js file/function to query django view
    [js components](https://github.com/rigoneri/syte/tree/master/syte/static/js/components)
7. Add above js to list of js to
    [compress.py](https://github.com/rigoneri/syte/blob/master/syte/compress.py)
8. Add link for service to
    [base view template](https://github.com/rigoneri/syte/blob/master/syte/templates/base.html)
9. Add html template to
    [templates directory](https://github.com/rigoneri/syte/tree/master/syte/static/templates) to be rendered js file/function that queries django view for service.
