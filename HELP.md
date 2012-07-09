Basic steps to add support for a particular service:

    1. Add information to README
    2. Add setting to turn service on/off (syte/syte_settings.py)
    3. Add above setting to site_pages context processor (syte/context_processor.py)
    4. Add django view to get info and return json (syte/views.py)
    5. Add js to query django view
    6. Add above js to list of js to compress (syte/compress.py)
    7. Add link for service to base view (syte/templates/base.html)
    8. Add html template in static/templates/ to be rendered from js
